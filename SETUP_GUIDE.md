# Setup Guide - Telemedicine Research & Presentation Project

## Quick Start Checklist

- [ ] Python 3.10-3.13 installed
- [ ] UV package manager installed
- [ ] Gemini API key configured in `.env`
- [ ] Slide Master file in project root
- [ ] Kiro PowerPoint MCP Power installed
- [ ] Dependencies installed (`uv sync`)

## Detailed Setup Instructions

### Step 1: Install UV Package Manager

If you don't have UV installed:

```bash
pip install uv
```

Or follow the official installation guide: https://docs.astral.sh/uv/

### Step 2: Configure Environment Variables

Your `.env` file should contain:

```env
MODEL=gemini/gemini-2.0-flash-001
GEMINI_API_KEY=AIzaSyD-JJxyOCNntDeTE9JQNz7fTNHnC5nqUWU
CREWAI_TRACING_ENABLED=true
```

**Important**: Replace the API key with your own if needed.

To get a Gemini API key:
1. Visit https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy it to your `.env` file

### Step 3: Place Slide Master File

Ensure the Slide Master file is in the project root directory:

```
telemedicine_project/
├── AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx  ← HERE
├── src/
├── .env
└── ...
```

This file is **mandatory** and defines the design language for all generated slides.

### Step 4: Install Kiro PowerPoint MCP Power

The PowerPoint generation requires the Kiro PowerPoint MCP Power:

1. **Option A: Via Kiro Interface**
   - Open Kiro's power management panel
   - Search for "PowerPoint" or "MCP"
   - Install the PowerPoint MCP Power
   - Verify installation

2. **Option B: Via Command Line** (if available)
   ```bash
   kiro power install powerpoint-mcp
   ```

3. **Verify Installation**
   - Check that the power is listed in Kiro's installed powers
   - Ensure it's enabled and active

### Step 5: Install Project Dependencies

From the project root directory:

```bash
uv sync
```

This will install:
- crewai[tools]==1.14.1
- All required dependencies
- Tool packages (SerperDevTool, FileReadTool, etc.)

### Step 6: Verify Installation

Run a quick verification:

```bash
# Check Python version
python --version  # Should be 3.10-3.13

# Check UV installation
uv --version

# Check project structure
ls -la src/telemedicine_project/

# Verify Slide Master exists
ls -la "AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx"
```

### Step 7: Test Run (Optional)

Before running the full workflow, you can test individual components:

```bash
# Test the crew configuration
crewai test -n 1 -m gemini/gemini-2.0-flash-001
```

## Running the Project

Once setup is complete:

```bash
crewai run
```

Or:

```bash
uv run python src/telemedicine_project/main.py
```

## Expected Execution Flow

1. **Initialization** (5-10 seconds)
   - Load agents and tasks
   - Initialize tools
   - Connect to Gemini API

2. **Research Phase** (3-5 minutes)
   - Research Specialist searches for telemedicine information
   - Analyzes market trends, technical hurdles, clinical impacts
   - Generates `telemedicine_research.md`

3. **Presentation Phase** (2-4 minutes)
   - Presentation Architect reads research file
   - Structures content into 10-15 slides
   - Applies Slide Master design
   - Generates `Final_Submission.pptx`

4. **Completion**
   - Both files saved in project root
   - Summary displayed in console

## Troubleshooting Common Issues

### Issue: "uv: command not found"
**Solution**: Install UV package manager
```bash
pip install uv
```

### Issue: "Python version not supported"
**Solution**: Install Python 3.10-3.13
- Download from https://www.python.org/downloads/
- Or use pyenv: `pyenv install 3.11`

### Issue: "GEMINI_API_KEY not found"
**Solution**: 
1. Check `.env` file exists in project root
2. Verify the key is correctly formatted
3. Ensure no extra spaces or quotes

### Issue: "Slide Master file not found"
**Solution**: 
1. Verify filename exactly matches: `AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx`
2. Ensure it's in the project root (not in a subdirectory)
3. Check file permissions

### Issue: "PowerPoint MCP Power not available"
**Solution**:
1. Open Kiro power management
2. Install PowerPoint MCP Power
3. Restart Kiro if necessary
4. Verify power is enabled

### Issue: "Module 'crewai' not found"
**Solution**: Install dependencies
```bash
uv sync
```

### Issue: "SerperDevTool requires API key"
**Solution**: Add to `.env` (optional, for enhanced web search)
```env
SERPER_API_KEY=your_serper_api_key
```
Get a key from https://serper.dev/

## Advanced Configuration

### Custom LLM Model

To use a different model, update `.env`:

```env
MODEL=openai/gpt-4o
OPENAI_API_KEY=your_openai_key
```

Or in `agents.yaml`, change the `llm` parameter:

```yaml
research_specialist:
  llm: openai/gpt-4o
  # ... rest of config
```

### Adjust Slide Count

In `tasks.yaml`, modify the presentation task:

```yaml
presentation_creation_task:
  description: >
    ... Generate 12-18 slides dynamically ...  # Change from 10-15
```

### Enable Memory

In `crew.py`, enable memory for cross-session learning:

```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
        memory=True,  # Add this line
    )
```

### Add Knowledge Sources

Create knowledge files in the `knowledge/` directory and reference them:

```python
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_source = PDFKnowledgeSource(file_paths=["knowledge/telemedicine_guide.pdf"])

@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
        knowledge_sources=[pdf_source],
    )
```

## Project Maintenance

### Update Dependencies

```bash
uv lock
uv sync
```

### Reset Memories (if enabled)

```bash
crewai reset-memories -a
```

### View Task Outputs

```bash
crewai log-tasks-outputs
```

### Train the Crew

```bash
crewai train -n 5 -f training.json
```

## Next Steps

After successful setup:

1. Run the workflow: `crewai run`
2. Review `telemedicine_research.md` for research quality
3. Open `Final_Submission.pptx` to verify presentation
4. Customize agents/tasks as needed
5. Experiment with different topics or configurations

## Support Resources

- **CrewAI Documentation**: https://docs.crewai.com
- **Kiro Documentation**: Check Kiro's help section
- **Project Issues**: Review execution logs for detailed errors
- **Community**: CrewAI Discord - https://discord.com/invite/X4JWnZnxPb

## File Checklist

Ensure these files exist and are properly configured:

```
✓ .env                                    # Environment variables
✓ AI Bubble_... (1).pptx                 # Slide Master
✓ src/telemedicine_project/crew.py       # Crew orchestration
✓ src/telemedicine_project/main.py       # Entry point
✓ src/telemedicine_project/config/agents.yaml
✓ src/telemedicine_project/config/tasks.yaml
✓ src/telemedicine_project/tools/powerpoint_tool.py
✓ pyproject.toml                         # Project config
✓ README.md                              # Project documentation
```

You're all set! Run `crewai run` to start the workflow.
