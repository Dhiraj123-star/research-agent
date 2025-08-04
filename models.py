# models.py - Pydantic Models for Multi-Agent System

from typing import List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

# =============================================================================
# PYDANTIC MODELS FOR DIFFERENT AGENT OUTPUTS
# =============================================================================

class ResearchResult(BaseModel):
    """Research agent output model"""
    topic: str = Field(..., description="The research topic")
    summary: str = Field(..., description="Brief summary of findings")
    key_points: List[str] = Field(..., description="3-5 key findings", min_items=3, max_items=5)
    confidence_level: str = Field(..., description="High, Medium, or Low confidence")
    sources_needed: List[str] = Field(default_factory=list, description="Recommended sources")

class CodeAnalysis(BaseModel):
    """Code analysis agent output model"""
    language: str = Field(..., description="Programming language detected")
    complexity_score: int = Field(..., ge=1, le=10, description="Code complexity (1-10)")
    issues_found: List[str] = Field(default_factory=list, description="Issues identified")
    suggestions: List[str] = Field(default_factory=list, description="Improvement suggestions")
    security_concerns: List[str] = Field(default_factory=list, description="Security issues")

class CreativeContent(BaseModel):
    """Creative content agent output model"""
    content_type: str = Field(..., description="Type of content created")
    title: str = Field(..., description="Content title")
    content: str = Field(..., description="The actual content")
    target_audience: str = Field(..., description="Intended audience")
    tone: str = Field(..., description="Writing tone used")
    word_count: int = Field(..., description="Word count")

class TaskSummary(BaseModel):
    """Task coordination output model"""
    task_type: str = Field(..., description="Type of task performed")
    agents_used: List[str] = Field(..., description="Agents involved")
    status: str = Field(..., description="Task completion status")
    result_summary: str = Field(..., description="Brief summary of results")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

# =============================================================================
# AGENT CONTEXT FOR COORDINATION
# =============================================================================

class MultiAgentContext:
    """Context class to manage multi-agent coordination"""
    
    def __init__(self):
        self.conversation_history: List[Dict[str, Any]] = []
        self.task_history: List[TaskSummary] = []
        self.agent_results: Dict[str, Any] = {}
        self.session_id: str = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def add_conversation(self, role: str, content: str, agent_name: str = "system"):
        """Add conversation entry"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "agent": agent_name,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_task_result(self, task_summary: TaskSummary):
        """Add completed task to history"""
        self.task_history.append(task_summary)
    
    def store_agent_result(self, agent_name: str, result: Any):
        """Store result from specific agent"""
        self.agent_results[agent_name] = result
    
    def get_recent_context(self, limit: int = 5) -> str:
        """Get recent conversation context"""
        recent = self.conversation_history[-limit:] if self.conversation_history else []
        return "\n".join([f"[{entry['agent']}] {entry['role']}: {entry['content']}" for entry in recent])

# =============================================================================
# RESULT FORMATTING FUNCTIONS
# =============================================================================

def format_research_result(result: ResearchResult) -> str:
    """Format research results for display"""
    output = f"📊 Topic: {result.topic}\n"
    output += f"📝 Summary: {result.summary}\n"
    output += f"🔑 Key Points:\n"
    for i, point in enumerate(result.key_points, 1):
        output += f"   {i}. {point}\n"
    output += f"📈 Confidence: {result.confidence_level}\n"
    if result.sources_needed:
        output += f"📚 Recommended Sources: {', '.join(result.sources_needed)}\n"
    return output

def format_code_result(result: CodeAnalysis) -> str:
    """Format code analysis results for display"""
    output = f"💻 Language: {result.language}\n"
    output += f"📊 Complexity Score: {result.complexity_score}/10\n"
    if result.issues_found:
        output += f"⚠️  Issues Found:\n"
        for issue in result.issues_found:
            output += f"   • {issue}\n"
    if result.suggestions:
        output += f"💡 Suggestions:\n"
        for suggestion in result.suggestions:
            output += f"   • {suggestion}\n"
    if result.security_concerns:
        output += f"🔒 Security Concerns:\n"
        for concern in result.security_concerns:
            output += f"   • {concern}\n"
    return output

def format_creative_result(result: CreativeContent) -> str:
    """Format creative content results for display"""
    output = f"✍️  Content Type: {result.content_type}\n"
    output += f"📝 Title: {result.title}\n"
    output += f"🎯 Audience: {result.target_audience} | Tone: {result.tone}\n"
    output += f"📊 Word Count: {result.word_count}\n"
    output += f"📄 Content:\n{result.content}\n"
    return output