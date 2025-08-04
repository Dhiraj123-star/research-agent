# agents.py - Agent Definitions and Tool Functions

import os
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv

# Import models
from models import (
    ResearchResult, 
    CodeAnalysis, 
    CreativeContent, 
    TaskSummary, 
    MultiAgentContext,
    format_research_result,
    format_creative_result
)

# Load environment variables
load_dotenv()

# =============================================================================
# INITIALIZE GEMINI MODEL
# =============================================================================

def get_gemini_model():
    """Get configured Gemini model"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY in your .env file")
    return GeminiModel("gemini-2.0-flash-exp")

# =============================================================================
# SPECIALIZED AGENTS
# =============================================================================

# Research Agent
research_agent = Agent(
    model=get_gemini_model(),
    output_type=ResearchResult,
    system_prompt="""You are a RESEARCH SPECIALIST AI agent. Your expertise includes:

🔍 RESEARCH CAPABILITIES:
- Comprehensive topic analysis and investigation
- Identifying key insights and patterns
- Evaluating information reliability and confidence
- Suggesting additional research sources
- Synthesizing complex information into clear summaries

📋 YOUR TASKS:
1. Thoroughly research the given topic
2. Provide clear, accurate summaries
3. Extract 3-5 most important findings
4. Assess confidence level honestly
5. Recommend sources for verification

🎯 FOCUS: Be objective, thorough, and indicate when information needs verification.""",
)

# Code Analysis Agent
code_agent = Agent(
    model=get_gemini_model(),
    output_type=CodeAnalysis,
    system_prompt="""You are a SENIOR SOFTWARE ENGINEER AI agent specializing in code analysis. Your expertise:

💻 CODE ANALYSIS SKILLS:
- Multi-language code review and assessment
- Security vulnerability detection
- Performance optimization recommendations
- Code complexity evaluation (1-10 scale)
- Best practices and design pattern suggestions

🔧 YOUR TASKS:
1. Identify programming language and frameworks
2. Analyze code complexity and structure
3. Find bugs, issues, and vulnerabilities
4. Provide actionable improvement suggestions
5. Highlight security concerns

🎯 FOCUS: Prioritize security, performance, maintainability, and code quality.""",
)

# Creative Content Agent
creative_agent = Agent(
    model=get_gemini_model(),
    output_type=CreativeContent,
    system_prompt="""You are a CREATIVE WRITING AI agent with expertise in content creation. Your skills:

✍️ CREATIVE CAPABILITIES:
- Blog posts, articles, and marketing copy
- Email templates and business communications
- Social media content and captions
- Technical documentation and guides
- Storytelling and narrative writing

📝 YOUR TASKS:
1. Create engaging, original content
2. Match tone and style to target audience
3. Optimize for readability and engagement
4. Ensure proper structure and flow
5. Provide appropriate titles and formatting

🎯 FOCUS: Create high-quality, engaging content that serves the intended purpose.""",
)

# Coordinator Agent (Main orchestrator)
coordinator_agent = Agent(
    model=get_gemini_model(),
    system_prompt="""You are the COORDINATOR AI agent managing a team of specialists:

🤖 YOUR TEAM:
- Research Agent: Handles research and information gathering
- Code Agent: Analyzes and reviews code
- Creative Agent: Creates written content and copy

🎯 YOUR ROLE:
1. Understand user requests and determine the best approach
2. Decide which specialized agents to involve
3. Coordinate between agents when needed
4. Synthesize results from multiple agents
5. Provide comprehensive responses

📋 COORDINATION RULES:
- For research topics → Use Research Agent
- For code analysis → Use Code Agent  
- For content creation → Use Creative Agent
- For complex tasks → Use multiple agents
- Always provide helpful, coordinated responses

You have access to tools to delegate tasks to your specialist agents.""",
)

# =============================================================================
# TOOL FUNCTIONS FOR AGENT COORDINATION
# =============================================================================

@coordinator_agent.tool
async def delegate_research(ctx: RunContext[MultiAgentContext], topic: str) -> ResearchResult:
    """Delegate research tasks to the research agent"""
    ctx.deps.add_conversation("system", f"Delegating research: {topic}", "coordinator")
    
    result = await research_agent.run(f"Research this topic: {topic}", deps=ctx.deps)
    research_data = result.output
    
    # Store result and create task summary
    ctx.deps.store_agent_result("research_agent", research_data)
    task_summary = TaskSummary(
        task_type="research",
        agents_used=["research_agent"],
        status="completed",
        result_summary=f"Researched: {research_data.topic} (Confidence: {research_data.confidence_level})"
    )
    ctx.deps.add_task_result(task_summary)
    
    return research_data

@coordinator_agent.tool
async def delegate_code_analysis(ctx: RunContext[MultiAgentContext], code: str, language: str = "auto-detect") -> CodeAnalysis:
    """Delegate code analysis to the code agent"""
    ctx.deps.add_conversation("system", f"Delegating code analysis for {language}", "coordinator")
    
    result = await code_agent.run(f"Analyze this {language} code:\n\n```\n{code}\n```", deps=ctx.deps)
    code_data = result.output
    
    # Store result and create task summary
    ctx.deps.store_agent_result("code_agent", code_data)
    task_summary = TaskSummary(
        task_type="code_analysis",
        agents_used=["code_agent"],
        status="completed",
        result_summary=f"Analyzed {code_data.language} code (Complexity: {code_data.complexity_score}/10)"
    )
    ctx.deps.add_task_result(task_summary)
    
    return code_data

@coordinator_agent.tool
async def delegate_content_creation(ctx: RunContext[MultiAgentContext], content_request: str, 
                                  content_type: str = "article", audience: str = "general", 
                                  tone: str = "professional") -> CreativeContent:
    """Delegate creative content creation to the creative agent"""
    ctx.deps.add_conversation("system", f"Delegating content creation: {content_type}", "coordinator")
    
    prompt = f"Create {content_type} content about: {content_request}. Target audience: {audience}. Tone: {tone}"
    result = await creative_agent.run(prompt, deps=ctx.deps)
    creative_data = result.output
    
    # Store result and create task summary
    ctx.deps.store_agent_result("creative_agent", creative_data)
    task_summary = TaskSummary(
        task_type="content_creation",
        agents_used=["creative_agent"],
        status="completed",
        result_summary=f"Created {creative_data.content_type}: {creative_data.title} ({creative_data.word_count} words)"
    )
    ctx.deps.add_task_result(task_summary)
    
    return creative_data

@coordinator_agent.tool
async def get_task_history(ctx: RunContext[MultiAgentContext]) -> str:
    """Get summary of completed tasks"""
    if not ctx.deps.task_history:
        return "No tasks completed yet in this session."
    
    summary = f"📊 Session {ctx.deps.session_id} - {len(ctx.deps.task_history)} tasks completed:\n\n"
    for i, task in enumerate(ctx.deps.task_history[-5:], 1):  # Last 5 tasks
        summary += f"{i}. {task.task_type.upper()}: {task.result_summary}\n"
        summary += f"   Agents: {', '.join(task.agents_used)} | Status: {task.status}\n\n"
    
    return summary

@coordinator_agent.tool
async def complex_research_analysis(ctx: RunContext[MultiAgentContext], topic: str) -> str:
    """Perform complex analysis using multiple agents"""
    ctx.deps.add_conversation("system", f"Starting complex analysis: {topic}", "coordinator")
    
    # First, research the topic
    research_result = await delegate_research(ctx, topic)
    
    # Then create a summary report
    report_request = f"Create a comprehensive report based on this research: {research_result.summary}. Include the key points: {', '.join(research_result.key_points)}"
    content_result = await delegate_content_creation(ctx, report_request, "report", "professional", "analytical")
    
    # Create combined task summary
    task_summary = TaskSummary(
        task_type="complex_analysis",
        agents_used=["research_agent", "creative_agent"],
        status="completed",
        result_summary=f"Complex analysis of '{topic}' with research and report generation"
    )
    ctx.deps.add_task_result(task_summary)
    
    return f"🔍 RESEARCH COMPLETED\n{format_research_result(research_result)}\n\n📄 ANALYSIS REPORT\n{format_creative_result(content_result)}"

# =============================================================================
# EXPORT ALL AGENTS
# =============================================================================

__all__ = [
    'research_agent',
    'code_agent', 
    'creative_agent',
    'coordinator_agent',
    'get_gemini_model'
]