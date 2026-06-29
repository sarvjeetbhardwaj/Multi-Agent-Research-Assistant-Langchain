# Multi-Agent Research Assistant (LangChain)

This project is a multi-agent research assistant built with LangChain and Google Gemini. It searches the web, scrapes relevant sources, drafts a research report, and critiques the report before returning a final result.

## Features

- Uses a search agent to gather recent and relevant web results
- Uses a reader agent to scrape and extract meaningful content from a selected URL
- Uses an LLM-powered writer chain to generate a structured research report
- Uses a critic chain to review the report and provide feedback

## Project Structure

- src/agents/agents.py: defines the search, reader, writer, and critic agents/chains
- src/pipeline/pipeline.py: orchestrates the research workflow
- src/tools/tools.py: contains the web search and URL scraping tools
- main.py: entry point for running the pipeline
- app.py: placeholder for future UI or app integration

## Requirements

- Python 3.10+
- Internet access for web search and scraping
- API keys for:
  - Google Gemini
  - Tavily

## Setup

1. Clone the repository
2. Create and activate a virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root with your API keys

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Run the Project

Run the main pipeline:

```bash
python main.py
```

You can also change the topic in main.py before running:

```python
topic = 'The impact of AI on job market in 2026'
```

## Example Output

The pipeline will print:
- search results from the web search agent
- scraped content from the selected URL
- a generated research report
- critic feedback for the report

## Notes

- The current implementation uses Google Gemini via LangChain and Tavily for search.
- Scraping may be affected by website protections or anti-bot measures.
- If you want to extend the project, a web UI or Streamlit app can be added around the pipeline.
