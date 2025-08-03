# Simple Research Agent

A simple AI research agent built with Pydantic AI and Google Gemini that provides structured research results.

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

### 4. Run the Agent
```bash
python main.py
```

## 💡 How to Use

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

## ✨ Features

- **Structured Output**: Results in organized format with key findings
- **Interactive Chat**: Simple command-line interface
- **Error Handling**: Graceful error management and recovery
- **Confidence Assessment**: AI evaluates its own confidence level
- **Source Recommendations**: Suggests additional sources to verify findings

## 🔧 Requirements

- Python 3.8 or higher
- Internet connection for API calls
- Valid Gemini API key

## 🎯 Example Usage

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

## ⚠️ Important Notes

- Keep your API key secure and never share it
- The agent uses your knowledge cutoff and may need source verification for recent events
- Results are AI-generated and should be fact-checked for critical use cases

## 🆘 Troubleshooting

**API Key Error**: Make sure your `.env` file contains the correct API key  
**Import Error**: Install required packages with `pip install pydantic-ai python-dotenv`  
**Connection Error**: Check your internet connection and API key validity

---

*Simple, focused research assistance powered by Pydantic AI and Google Gemini*