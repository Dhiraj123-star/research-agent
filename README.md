# Multi-Agent AI System

A comprehensive AI system built with Pydantic AI and Google Gemini that provides both simple research functionality and advanced multi-agent coordination for research, code analysis, and creative content creation.

## 🚀 Two Ways to Use

### Option 1: Simple Research Agent
Perfect for quick research tasks with a lightweight interface.

### Option 2: Multi-Agent System  
Advanced coordination between specialized agents for complex tasks.

## 🤖 Available Agents

- **🔍 Research Agent** - Topic research and comprehensive analysis
- **💻 Code Agent** - Code analysis, review, and security assessment
- **✍️ Creative Agent** - Content creation and professional writing
- **🎭 Coordinator Agent** - Orchestrates and coordinates all specialized agents

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install pydantic-ai python-dotenv
```

### 2. Get Gemini API Key
- Go to [Google AI Studio](https://aistudio.google.com/apikey)
- Sign in with your Google account
- Click "Create API Key"
- Copy your API key

### 3. Create Environment File
Create a `.env` file in your project directory:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 4. Choose Your Interface

#### Simple Research Agent
```bash
python main.py
```

#### Multi-Agent System
```bash
python multi_agent.py
```

## 💡 How to Use

### 🔍 Simple Research Agent (main.py)

1. **Start the agent** - Run `python main.py`
2. **Enter research topics** when prompted
3. **Get structured results** with:
   - Summary of findings
   - 3-5 key points
   - Confidence level assessment
   - Recommended sources for verification
4. **Type commands**:
   - Any research topic to get results
   - `quit`, `exit`, or `q` to stop

### 🤖 Multi-Agent System (multi_agent.py)

1. **Start the system** - Run `python multi_agent.py`
2. **Enter any request** - The coordinator will automatically determine which agents to use
3. **Get specialized results** based on your request type:
   - Research topics get comprehensive analysis
   - Code snippets get detailed review and suggestions
   - Content requests get professionally written material
   - Complex tasks use multiple agents working together
4. **Use commands**:
   - Any research topic, code, or content request
   - `history` - View completed task history
   - `quit`, `exit`, or `q` to stop

## ✨ Features

### 🔍 Research Capabilities (Both Interfaces)
- **Structured Output**: Results in organized format with key findings
- **Interactive Chat**: Simple command-line interface
- **Error Handling**: Graceful error management and recovery
- **Confidence Assessment**: AI evaluates its own confidence level
- **Source Recommendations**: Suggests additional sources to verify findings

### 💻 Code Analysis Features (Multi-Agent Only)
- **Multi-language Support**: Analyzes code in various programming languages
- **Complexity Scoring**: Rates code complexity on 1-10 scale
- **Security Review**: Identifies potential security vulnerabilities
- **Improvement Suggestions**: Provides actionable optimization recommendations

### ✍️ Creative Content Generation (Multi-Agent Only)
- **Multiple Content Types**: Articles, emails, reports, social media content
- **Audience Targeting**: Tailored content for specific audiences
- **Tone Adaptation**: Professional, casual, technical, or creative tones
- **Word Count Tracking**: Automatic content length measurement

### 🎭 Advanced Coordination (Multi-Agent Only)
- **Multi-Agent Collaboration**: Complex tasks using multiple specialists
- **Task History**: Track and review completed work
- **Session Management**: Persistent context within sessions
- **Error Handling**: Graceful error management and recovery

## 🔧 Requirements

- Python 3.8 or higher
- Internet connection for API calls
- Valid Gemini API key

## 🎯 Example Usage

### Simple Research Agent Example
```
🔍 What would you like to research? renewable energy trends

🔍 Researching: renewable energy trends
⏳ Please wait...

📊 RESEARCH RESULTS: renewable energy trends
📝 Summary: Global renewable energy capacity continues to grow...
🔑 Key Points:
   1. Solar power costs decreased by 50% in the last 5 years
   2. Wind energy now accounts for 15% of global electricity
   3. Battery storage technology improving rapidly
📈 Confidence Level: High
```

### Multi-Agent System Examples

#### Research Example
```
💬 You: research quantum computing trends

🤖 Coordinating agents...

📋 Response:
🔍 RESEARCH COMPLETED
📊 Topic: quantum computing trends
📝 Summary: Quantum computing is experiencing rapid advancement...
🔑 Key Points:
   1. IBM and Google leading in quantum processor development
   2. Quantum advantage demonstrated in specific algorithms
   3. Investment in quantum startups increased 300% in 2024
📈 Confidence Level: High
```

#### Code Analysis Example
```
💬 You: analyze this Python code: def factorial(n): return 1 if n <= 1 else n * factorial(n-1)

🤖 Coordinating agents...

📋 Response:
💻 Language: Python
📊 Complexity Score: 3/10
💡 Suggestions:
   • Add input validation for negative numbers
   • Consider iterative approach for better performance
   • Add type hints for better code documentation
```

#### Creative Content Example
```
💬 You: write a professional email about project updates

🤖 Coordinating agents...

📋 Response:
✍️ Content Type: email
📝 Title: Project Status Update - Weekly Summary
🎯 Audience: professional | Tone: professional
📊 Word Count: 150
📄 Content:
Subject: Weekly Project Update - [Project Name]

Dear Team,

I hope this email finds you well. I wanted to provide you with a comprehensive update...
```

#### Complex Analysis Example
```
💬 You: do a complex analysis on artificial intelligence impact on healthcare

🤖 Coordinating agents...

📋 Response:
🔍 RESEARCH COMPLETED
📊 Topic: artificial intelligence impact on healthcare
📝 Summary: AI is revolutionizing healthcare through diagnostic improvements...

📄 ANALYSIS REPORT
✍️ Content Type: report
📝 Title: Comprehensive Analysis: AI's Transformative Impact on Healthcare
[Full detailed report with research findings integrated...]
```

## 📂 Project Structure

```
multi-agent-system/
├── main.py           # Simple research agent (original functionality)
├── models.py         # Pydantic models and data structures
├── agents.py         # Agent definitions and coordination tools
├── multi_agent.py    # Main orchestrator and interactive interface
├── .env             # Environment variables (create this)
└── README.md        # This file
```

## 🎯 Which Interface to Choose?

### Use Simple Research Agent (`main.py`) when:
- You only need research functionality
- You want a lightweight, fast interface
- You prefer simplicity over advanced features
- You're doing quick fact-finding or topic exploration

### Use Multi-Agent System (`multi_agent.py`) when:
- You need code analysis or creative writing
- You want task coordination and history tracking
- You're working on complex projects requiring multiple skills
- You want the full power of specialized AI agents

## ⚠️ Important Notes

- Keep your API key secure and never share it
- The agents use AI knowledge which may need verification for recent events
- Results are AI-generated and should be fact-checked for critical use cases
- Code analysis suggestions should be reviewed by experienced developers
- Creative content should be reviewed for accuracy and appropriateness

## 🆘 Troubleshooting

**API Key Error**: Make sure your `.env` file contains the correct API key  
**Import Error**: Install required packages with `pip install pydantic-ai python-dotenv`  
**Connection Error**: Check your internet connection and API key validity  
**Agent Coordination Issues**: Restart the system if agents seem unresponsive  
**File Not Found**: Make sure you're running the correct file (`main.py` vs `multi_agent.py`)

## 🔄 Running Examples

The multi-agent system includes built-in examples. When you start it with `python multi_agent.py`, you'll be prompted to run demonstrations of each agent type before starting your interactive session.

---

*Simple research assistance AND comprehensive multi-agent AI coordination - Choose the interface that fits your needs. Powered by Pydantic AI and Google Gemini*