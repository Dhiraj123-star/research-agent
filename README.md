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

## 🔄 CI/CD Pipeline & Automated Deployment

This project features a comprehensive CI/CD pipeline that automatically:

### 🔧 Continuous Integration
- **Automated Testing**: Runs on every push and pull request
  - Python linting with flake8
  - Import validation and basic functionality tests
  - Context management testing
- **Multi-Platform Docker Builds**: Supports linux/amd64 and linux/arm64
- **Integration Testing**: Validates Docker containers work correctly
- **Docker Compose Validation**: Ensures deployment configurations are valid

### 🚀 Continuous Deployment
- **Automated Docker Hub Publishing**: Images pushed to `dhiraj918106/multi-agent-ai`
- **Multi-Tag Strategy**: 
  - `latest` for main branch
  - Version tags for releases (e.g., `v1.0.0`)
  - Branch-specific tags for development
  - SHA-based tags for commit tracking
- **GitHub Releases**: Automatic release creation for version tags
- **Build Caching**: Optimized builds using GitHub Actions cache

### 📦 Available Docker Images

**Production Images** (automatically built and tested):
```bash
# Latest stable version
docker pull dhiraj918106/multi-agent-ai:latest

# Specific version
docker pull dhiraj918106/multi-agent-ai:v1.0.0

# Development branch
docker pull dhiraj918106/multi-agent-ai:develop
```

### 🔍 Quality Assurance
- **Automated Testing Pipeline**: All code changes are tested before deployment
- **Integration Testing**: Docker containers validated with actual functionality
- **Code Quality Checks**: Linting and style validation
- **Multi-Platform Support**: Ensures compatibility across different architectures

## 🚀 Quick Start

### Option A: Pre-built Docker Images (Recommended)

#### 1. Get Gemini API Key
- Go to [Google AI Studio](https://aistudio.google.com/apikey)
- Sign in with your Google account
- Click "Create API Key"
- Copy your API key

#### 2. Create Environment File
```bash
echo "GEMINI_API_KEY=your_actual_gemini_api_key_here" > .env
```

#### 3. Run Pre-built Images

**Multi-Agent System (Latest)**
```bash
# Run latest stable version
docker run -it --env-file .env dhiraj918106/multi-agent-ai:latest python multi_agent.py

# Run specific version
docker run -it --env-file .env dhiraj918106/multi-agent-ai:v1.0.0 python multi_agent.py
```

**Simple Research Agent**
```bash
# Run simple research agent
docker run -it --env-file .env dhiraj918106/multi-agent-ai:latest python main.py
```

### Option B: Local Docker Build

#### 1. Clone and Build
```bash
git clone <your-repo-url>
cd multi-agent-system
echo "GEMINI_API_KEY=your_actual_gemini_api_key_here" > .env
```

#### 2. Run with Docker Compose

**Multi-Agent System (Default)**
```bash
# Build and run
docker-compose up --build multi-agent

# Run in background
docker-compose up -d --build multi-agent
```

**Simple Research Agent**
```bash
# Run simple research agent
docker-compose --profile simple up --build research-agent
```

### Option C: Local Python Installation

#### 1. Install Dependencies
```bash
pip install pydantic-ai python-dotenv
```

#### 2. Create Environment File
Create a `.env` file in your project directory:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

#### 3. Choose Your Interface

**Simple Research Agent**
```bash
python main.py
```

**Multi-Agent System**
```bash
python multi_agent.py
```

## 🔄 Development & Deployment Workflow

### 🌟 For Contributors

**Development Process**:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to your branch
5. Create a pull request
6. **Automated CI/CD will**:
   - Run all tests
   - Build and validate Docker images
   - Perform integration testing
   - Provide feedback on your PR

**Release Process**:
1. Create a version tag (e.g., `v1.0.0`)
2. Push the tag to GitHub
3. **Automated deployment will**:
   - Build and push Docker images
   - Create a GitHub release
   - Update Docker Hub descriptions
   - Notify on completion

### 🏗️ CI/CD Pipeline Details

**Triggers**:
- Push to `main` or `develop` branches
- Pull requests to `main`
- Version tags (`v*`)

**Pipeline Stages**:
1. **Testing** - Code validation and functionality tests
2. **Building** - Multi-platform Docker image creation
3. **Integration Testing** - Container functionality validation
4. **Deployment** - Automated releases for version tags
5. **Notifications** - Success/failure notifications

**Quality Gates**:
- All tests must pass
- Docker builds must succeed
- Integration tests must validate
- Code must pass linting checks

## 💡 How to Use

### 🔍 Simple Research Agent (main.py)

1. **Start the agent** - Run using any of the quick start methods above
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

1. **Start the system** - Run using any of the quick start methods above
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

### 🐳 Docker & Deployment Features
- **Pre-built Images**: Ready-to-use Docker images on Docker Hub
- **Multi-Platform Support**: Works on AMD64 and ARM64 architectures
- **Automated Updates**: New versions automatically built and published
- **Security**: Non-root user, proper permissions
- **Health Monitoring**: Built-in health checks
- **Development Ready**: Volume mounting for code changes

## 🔧 Requirements

### Using Pre-built Docker Images (Easiest)
- Docker installed
- Valid Gemini API key
- Internet connection

### Local Docker Build
- Docker and Docker Compose
- Git (to clone repository)
- Valid Gemini API key

### Local Python Installation
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

## 📂 Project Structure

```
multi-agent-system/
├── main.py              # Simple research agent (original functionality)
├── models.py            # Pydantic models and data structures
├── agents.py            # Agent definitions and coordination tools
├── multi_agent.py       # Main orchestrator and interactive interface
├── Dockerfile           # Docker container configuration
├── docker-compose.yml   # Multi-service orchestration
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # CI/CD pipeline configuration
├── .dockerignore        # Docker build optimization
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
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

### Use Pre-built Docker Images when:
- You want the fastest setup experience
- You don't need to modify the source code
- You want guaranteed working versions
- You're deploying to production

### Use Local Docker Build when:
- You're developing or customizing the system
- You want to build from specific branches
- You need to test local changes

## 🐳 Docker Commands Quick Reference

### Pre-built Images
```bash
# Multi-Agent System (latest)
docker run -it --env-file .env dhiraj918106/multi-agent-ai:latest python multi_agent.py

# Simple Research Agent (latest)
docker run -it --env-file .env dhiraj918106/multi-agent-ai:latest python main.py

# Specific version
docker run -it --env-file .env dhiraj918106/multi-agent-ai:v1.0.0 python multi_agent.py

# Pull latest updates
docker pull dhiraj918106/multi-agent-ai:latest
```

### Local Docker Compose
```bash
# Multi-Agent System
docker-compose up --build multi-agent

# Simple Research Agent  
docker-compose --profile simple up --build research-agent

# Access running container
docker exec -it multi-agent-system python main.py

# View logs
docker-compose logs multi-agent

# Stop services
docker-compose down
```

## 🔄 Version Management

### Available Tags
- `latest` - Most recent stable version
- `v1.0.0`, `v1.1.0`, etc. - Specific releases
- `main-<sha>` - Latest commits from main branch
- `develop-<sha>` - Latest commits from develop branch

### Checking Versions
```bash
# List available tags
docker images dhiraj918106/multi-agent-ai

# Check image creation date
docker inspect dhiraj918106/multi-agent-ai:latest | grep Created
```

## ⚠️ Important Notes

- Keep your API key secure and never share it
- The agents use AI knowledge which may need verification for recent events
- Results are AI-generated and should be fact-checked for critical use cases
- Code analysis suggestions should be reviewed by experienced developers
- Creative content should be reviewed for accuracy and appropriateness
- Docker containers run with non-root user for security
- Pre-built images are automatically tested and validated through CI/CD

## 🆘 Troubleshooting

### General Issues
**API Key Error**: Make sure your `.env` file contains the correct API key  
**Import Error**: Use pre-built Docker images or install packages with `pip install pydantic-ai python-dotenv`  
**Connection Error**: Check your internet connection and API key validity  
**Agent Coordination Issues**: Restart the system if agents seem unresponsive  

### Docker Issues
**Image Pull Error**: Check internet connection and Docker Hub availability  
**Container Won't Start**: Check if API key is set in `.env` file  
**Permission Denied**: Ensure `.env` file exists and is readable  
**Interactive Mode Not Working**: Use `-it` flags with `docker run`  

### Version Issues
**Old Version Running**: Pull latest image with `docker pull dhiraj918106/multi-agent-ai:latest`  
**Tag Not Found**: Check available tags on Docker Hub  
**Build Conflicts**: Remove local images and use pre-built ones  

### Quick Fixes
```bash
# Use latest pre-built image
docker pull dhiraj918106/multi-agent-ai:latest

# Check what's running
docker ps

# View container logs
docker logs <container-name>

# Clean up old images
docker image prune

# Check available versions
docker images dhiraj918106/multi-agent-ai
```

## 🔄 Running Examples

The multi-agent system includes built-in examples. When you start it with any of the methods above, you'll be prompted to run demonstrations of each agent type before starting your interactive session.

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

### CI/CD Pipeline
- All pull requests trigger automated testing
- Successful merges to main/develop trigger Docker builds
- Version tags trigger automated releases
- All builds are tested on multiple platforms

### Release Process
1. Update version numbers
2. Create and push a version tag
3. CI/CD automatically creates release with Docker images
4. Updated images available within minutes

---

*Simple research assistance AND comprehensive multi-agent AI coordination with automated CI/CD deployment. Choose the interface that fits your needs. Pre-built Docker images available for instant setup! Powered by Pydantic AI and Google Gemini*