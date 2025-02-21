（由于技术原因，联网搜索暂不可用）

Here’s a new `README.md` for your project, inspired by the article and tailored for a financial analysis multi-agent system using CrewAI and Ollama models. It includes emojis for better readability and engagement:

---

# 🚀 Financial Analysis Multi-Agent System with CrewAI & Ollama

Welcome to the **Financial Analysis Multi-Agent System**! This project leverages the power of **CrewAI** and **Ollama** to create a collaborative team of AI agents that automate and enhance financial analysis tasks. Whether you're analyzing stock performance, assessing risks, or generating investment strategies, this system provides a comprehensive solution powered by open-source LLMs. 💼📈

---

## 🌟 Key Features

- **Multi-Agent Collaboration**: Specialized agents work together to perform complex financial analysis tasks. 🤝
- **Open-Source LLMs**: Powered by Ollama's local LLMs (e.g., LLaMA 3, Mistral, Phi-3). 🦙
- **Modular Design**: Easily customize agents, tasks, and tools to fit your needs. 🧩
- **Automated Reporting**: Generate detailed reports in Markdown or JSON format. 📄
- **Real-Time Data Integration**: Fetch and analyze live financial data using APIs like Yahoo Finance. 📊
- **Risk Assessment**: Quantify risks using advanced metrics like Beta, Sharpe Ratio, and Value at Risk (VaR). 📉
- **Sentiment Analysis**: Gauge market sentiment from news and social media. 🗞️

---

## 🛠️ Tech Stack

- **Framework**: [CrewAI](https://crewai.com)
- **LLMs**: [Ollama](https://ollama.ai) (LLaMA 3, Mistral, Phi-3)
- **Data Sources**: Yahoo Finance (`yfinance`), News APIs
- **Visualization**: Plotly, Streamlit
- **Language**: Python 3.10+

---

## 🚀 Quick Start

### 1. **Set Up Ollama**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
ollama serve &

# Download a model (e.g., LLaMA 3)
ollama pull llama3
```

### 2. **Clone the Repository**
```bash
git clone https://github.com/your-username/financial-analysis-agent.git
cd financial-analysis-agent
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Run the System**
```bash
# Start the Streamlit app
streamlit run main.py
```

---

## 🧩 Project Structure

```
financial-analysis-agent/
├── agents/               # Agent definitions
│   └── financial_agents.py
├── tools/                # Analysis tools
│   ├── competitor_analysis.py
│   ├── risk_assessment_tool.py
│   └── sentiment_analysis_tool.py
├── tasks/                # Task workflows
│   └── analysis_tasks.py
├── config/               # Configuration files
│   ├── agents.yaml
│   └── tasks.yaml
├── data/                 # Sample datasets
├── outputs/              # Generated reports
├── main.py               # Streamlit app entry point
├── requirements.txt      # Dependencies
└── README.md             # You are here! 😊
```

---

## 🤖 Meet the Agents

### 1. **Stock Market Researcher** 🔍
- **Role**: Gathers and analyzes stock market data.
- **Tools**: Yahoo Finance API, Technical Analysis Libraries.
- **Output**: Competitive analysis, financial ratios, and trends.

### 2. **Financial Analyst** 📊
- **Role**: Synthesizes data into actionable insights.
- **Tools**: Risk assessment models, valuation metrics.
- **Output**: Risk-return profiles, investment insights.

### 3. **Sentiment Analyst** 🗣️
- **Role**: Analyzes market sentiment from news and social media.
- **Tools**: NLP models, sentiment analysis libraries.
- **Output**: Sentiment scores, emotional context.

### 4. **Investment Strategist** 🎯
- **Role**: Develops tailored investment strategies.
- **Tools**: Portfolio optimization algorithms.
- **Output**: Custom strategies for different investor profiles.

---

## 🛠️ Customization

### Add New Tools
Create a new Python file in the `tools/` directory and decorate it with `@tool`:
```python
from crewai_tools import tool

@tool
def custom_tool(stock: str):
    """Your custom analysis logic."""
    return analysis_results
```

### Modify Agents
Edit the `agents/financial_agents.py` file to add new capabilities:
```python
def custom_agent(self) -> Agent:
    return Agent(
        role="Custom Agent",
        goal="Perform custom analysis",
        backstory="Expert in custom financial analysis",
        tools=[custom_tool],
        verbose=True
    )
```

### Update Tasks
Edit the `tasks/analysis_tasks.py` file to define new workflows:
```python
def custom_task(self) -> Task:
    return Task(
        description="Perform custom analysis",
        agent=self.custom_agent(),
        expected_output="Detailed custom analysis report"
    )
```

---

## 📊 Example Output

### Sample Report (`report.md`)
```markdown
# Financial Analysis Report for AAPL

## Technical Analysis
- **50-day MA**: $170.50
- **200-day MA**: $160.20
- **RSI**: 65.4 (Neutral)

## Fundamental Analysis
- **P/E Ratio**: 28.5
- **Market Cap**: $2.8T
- **Dividend Yield**: 0.55%

## Sentiment Analysis
- **Overall Sentiment**: Positive (0.72)
- **Key Drivers**: Strong earnings report, new product launch.

## Risk Assessment
- **Beta**: 1.25
- **Sharpe Ratio**: 1.8
- **Max Drawdown**: 12.3%

## Investment Strategy
- **Conservative**: 30% allocation
- **Balanced**: 50% allocation
- **Aggressive**: 70% allocation
```

---

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [Ollama Models](https://ollama.ai/library)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Plotly Visualization](https://plotly.com/python/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Made with ❤️ by Mzkk. Let's revolutionize financial analysis with AI! 🚀
[Financial Analysis Multi-Agent System Article](https://generativeai.pub/financial-analysis-multi-agent-with-open-source-llms-using-crewai-and-ollama-models-9f20076f8995)
