# multi_agent.py - Modularized Multi-Agent System

import os
import asyncio
from pydantic_ai import RunContext
from dotenv import load_dotenv

# Import models and agents
from models import MultiAgentContext
from agents import coordinator_agent, get_task_history

# Load environment variables
load_dotenv()

# =============================================================================
# MAIN MULTI-AGENT SYSTEM CLASS
# =============================================================================

class MultiAgentSystem:
    """Main orchestrator for the multi-agent system"""
    
    def __init__(self):
        self.context = MultiAgentContext()
        self.is_running = False
    
    async def process_request(self, user_input: str) -> str:
        """Process user request through the coordinator agent"""
        try:
            # Add user message to context
            self.context.add_conversation("user", user_input, "user")
            
            # Get coordinator's response
            result = await coordinator_agent.run(user_input, deps=self.context)
            
            # Format and return response
            if hasattr(result, 'output'):
                response = str(result.output)
            else:
                response = str(result)
            
            self.context.add_conversation("assistant", response, "coordinator")
            return response
            
        except Exception as e:
            error_msg = f"❌ Error processing request: {str(e)}"
            self.context.add_conversation("system", error_msg, "error")
            return error_msg
    
    async def run_interactive_session(self):
        """Run interactive multi-agent session"""
        print("🤖 MULTI-AGENT SYSTEM STARTED!")
        print("=" * 50)
        print("Available agents:")
        print("  🔍 Research Agent - Topic research and analysis")
        print("  💻 Code Agent - Code analysis and review")
        print("  ✍️  Creative Agent - Content creation and writing")
        print("  🎭 Coordinator - Orchestrates all agents")
        print()
        print("Commands:")
        print("  • Type any request and agents will coordinate automatically")
        print("  • 'history' - View task history")
        print("  • 'quit' or 'exit' - Stop the system")
        print("=" * 50)
        
        self.is_running = True
        
        while self.is_running:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                    print("👋 Multi-Agent System shutting down. Goodbye!")
                    break
                
                if user_input.lower() == 'history':
                    history = await get_task_history(RunContext(self.context))
                    print(f"\n{history}")
                    continue
                
                if not user_input:
                    continue
                
                print("\n🤖 Coordinating agents...")
                response = await self.process_request(user_input)
                print(f"\n📋 Response:\n{response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    def stop(self):
        """Stop the multi-agent system"""
        self.is_running = False

# =============================================================================
# EXAMPLE FUNCTIONS
# =============================================================================

async def run_multi_agent_examples():
    """Run example interactions to demonstrate multi-agent capabilities"""
    system = MultiAgentSystem()
    
    print("🧪 MULTI-AGENT EXAMPLES")
    print("=" * 30)
    
    examples = [
        "Research quantum computing trends",
        "Analyze this Python code: def factorial(n): return 1 if n <= 1 else n * factorial(n-1)",
        "Write a professional email about project updates",
        "Do a complex analysis on artificial intelligence impact on healthcare"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. Example: {example}")
        print("-" * 40)
        response = await system.process_request(example)
        print(f"Response: {response[:200]}...")
        print()
    
    print("✅ Examples completed!")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

async def main():
    """Main execution function"""
    print("🚀 Initializing Multi-Agent System...")
    
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found!")
        print("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
        return
    
    try:
        print("🔧 Testing agent coordination...")
        
        # Quick test
        system = MultiAgentSystem()
        test_response = await system.process_request("Hello, can you help me research Python programming?")
        
        if test_response and not test_response.startswith("❌"):
            print("✅ Multi-agent system ready!")
            
            # Ask user if they want examples
            print("\n🧪 Run examples first? (y/n): ", end="")
            if input().lower().startswith('y'):
                await run_multi_agent_examples()
            
            # Start interactive session
            await system.run_interactive_session()
        else:
            print("❌ System test failed. Please check your setup.")
        
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    asyncio.run(main())