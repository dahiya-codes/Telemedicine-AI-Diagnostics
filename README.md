# 🏥 AI-Driven Telemedicine Diagnostics

An advanced multi-agent framework designed to automate clinical data analysis and handwritten medical record evaluation.

---

## 🛠️ Setup Instructions
To get this project running locally, follow these steps:

 **Clone the Repository:**
   ```bash
   git clone [https://github.com/dahiya-codes/Telemedicine-AI-Diagnostics.git](https://github.com/dahiya-codes/Telemedicine-AI-Diagnostics.git)
  cd Telemedicine-AI-Diagnostics

## 🏃 Run Steps
Once the environment is set up, follow these steps to execute the project:

### **Primary Workflow**
To run the main Agentic AI orchestration (generates research and PPT):
```bash
uv run python src/main.py
   
**System Architecture & Approach**
Multi-Agent Orchestration: Uses a specialized "Crew" of agents (defined in crew.py) to handle clinical data parsing and diagnostic validation.

Knowledge Integration: Leverages the knowledge/ directory to provide the LLM with medical context for higher accuracy.

MCP Integration: (Briefly mention how you used the Model Context Protocol if applicable).
