# Simple Research Agent using Pydantic AI and Gemini


import os
import asyncio
from typing import List
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =============================================================================
# PYDANTIC MODEL FOR STRUCTURED RESEARCH RESULTS
# =============================================================================

class ResearchResult(BaseModel):
    """Structured model for research results"""
    topic: str = Field(..., description="The research topic")
    summary: str = Field(..., description="Brief summary of findings")
    key_points: List[str] = Field(..., description="3-5 key findings", min_items=3, max_items=5)
    confidence_level: str = Field(..., description="High, Medium, or Low confidence")
    sources_needed: List[str] = Field(default_factory=list, description="Recommended sources to verify")

# =============================================================================
# INITIALIZE GEMINI MODEL
# =============================================================================

def get_gemini_model():
    """Get configured Gemini model"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY in your .env file")
    
    #Simple model name approach (uses environment variable automatically)
    return GeminiModel("gemini-2.0-flash-exp")
    

# =============================================================================
# CREATE RESEARCH AGENT
# =============================================================================

research_agent = Agent(
    model=get_gemini_model(),
    output_type=ResearchResult,
    system_prompt="""You are a research specialist AI. Your job is to:

1. Research the given topic thoroughly
2. Provide a clear, concise summary
3. Extract 3-5 key findings or insights
4. Assess your confidence level in the findings
5. Suggest additional sources if needed

Always be accurate, objective, and indicate when information needs verification.
Focus on the most important and relevant information for the topic.""",
)

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================

async def research_topic(topic: str) -> ResearchResult:
    """Research a topic and return structured results"""
    try:
        print(f"🔍 Researching: {topic}")
        print("⏳ Please wait...")
        
        result = await research_agent.run(f"Research this topic: {topic}")
        return result.output
        
    except Exception as e:
        print(f"❌ Error during research: {e}")
        return None

def display_results(result: ResearchResult):
    """Display research results in a nice format"""
    if not result:
        print("❌ No results to display")
        return
    
    print("\n" + "="*60)
    print(f"📊 RESEARCH RESULTS: {result.topic}")
    print("="*60)
    
    print(f"\n📝 Summary:")
    print(f"   {result.summary}")
    
    print(f"\n🔑 Key Points:")
    for i, point in enumerate(result.key_points, 1):
        print(f"   {i}. {point}")
    
    print(f"\n📈 Confidence Level: {result.confidence_level}")
    
    if result.sources_needed:
        print(f"\n📚 Recommended Sources:")
        for source in result.sources_needed:
            print(f"   • {source}")
    
    print("="*60 + "\n")

async def interactive_mode():
    """Run interactive research session"""
    print("🤖 Simple Research Agent Started!")
    print("Type your research topics or 'quit' to exit")
    print("-" * 40)
    
    while True:
        try:
            topic = input("\n🔍 What would you like to research? ").strip()
            
            if topic.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not topic:
                print("Please enter a topic to research.")
                continue
            
            # Research the topic
            result = await research_topic(topic)
            
            # Display results
            display_results(result)
            
        except KeyboardInterrupt:
            print("\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

async def main():
    """Main function"""
    print("🚀 Initializing Research Agent...")
    
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found!")
        print("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
        return
    
    try:
        # Test the agent with a sample query
        print("\n🧪 Testing agent with sample query...")
        sample_result = await research_topic("artificial intelligence trends 2025")
        if sample_result:
            print("✅ Agent test successful!")
            display_results(sample_result)
        
        # Start interactive mode
        await interactive_mode()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    asyncio.run(main())