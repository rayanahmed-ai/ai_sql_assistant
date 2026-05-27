# AI SQL Assistant

An AI-powered Natural Language to SQL reporting system built using Python, Streamlit, LangGraph, Groq LLMs, FAISS RAG, and Microsoft SQL Server.

The system allows users to ask business questions in plain English, automatically generates SQL queries, retrieves data from SQL Server, validates the SQL, and exports reports in CSV format.

---

# Project Objective

Traditional reporting systems require technical knowledge and fixed reports. This project aims to create an intelligent assistant that enables users to retrieve business data using natural language.

The system:
- Understands user intent
- Identifies missing information
- Asks clarification questions
- Generates SQL queries automatically
- Executes queries safely
- Displays results in tabular format
- Exports reports to CSV

---

# Features

- Natural Language to SQL conversion
- Intelligent clarification system
- Multi-turn conversational querying
- SQL Server integration
- RAG-based schema retrieval
- SQL validation and safety checks
- Context-aware query understanding
- CSV export functionality
- Interactive Streamlit UI
- Dynamic visualizations
- Confidence-based query validation
- Irrelevant query rejection

---

# Example Queries

```text
Show monthly sales region-wise

Get me product-wise sales for May 2025

List customers who purchased more than 50000 last year

Show employee-wise order count for this month

Give me total sales for 2025
```

---

# Clarification Examples

## User Query

```text
Show sales
```

## Assistant

```text
What time period would you like to see sales for?
```

---

## User Query

```text
Get product-wise sales
```

## Assistant

```text
Do you want monthly, yearly, or overall product-wise sales?
```

---

# Tech Stack

- Python
- Streamlit
- LangGraph
- Groq LLM
- LangChain
- FAISS
- SQLAlchemy
- Microsoft SQL Server
- spaCy
- Pandas

---

# Project Structure

```text
├── database/
│   ├── connection.py
│   ├── query_executor.py
│   ├── schema_loader.py
│   └── __init__.py
│
├── exports/
│   ├── exporter.py
│   └── __init__.py
│
├── faiss_schema_db/
│   ├── index.faiss
│   └── index.pkl
│
├── graph/
│   ├── nodes.py
│   ├── state.py
│   ├── workflow.py
│   └── __init__.py
│
├── llm/
│   ├── sql_generator.py
│   └── __init__.py
│
├── nlp/
│   ├── spacy_processor.py
│   └── __init__.py
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── __init__.py
│
├── validation/
│   ├── build_validation_rag.py
│   ├── relevance_checker.py
│   ├── schema_metadata.py
│   ├── sql_validator.py
│   ├── validation_agent.py
│   ├── validation_retriever.py
│   └── __init__.py
│
├── streamlit_ui.py
├── requirements.txt
├── README.md
```

---

# System Workflow

```text
User Query
    ↓
spaCy NLP Processing
    ↓
Schema Retrieval (RAG)
    ↓
Validation Agent
    ↓
Clarification Questions (if needed)
    ↓
SQL Generation
    ↓
SQL Validation
    ↓
SQL Execution
    ↓
Result Visualization
    ↓
CSV Export
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository_url>

cd internship_task
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# Streamlit Cloud Deployment

Go to:

```text
Streamlit Dashboard → App → Settings → Secrets
```

Add:

```toml
API_KEY = "your_google_api_key"

GROQ_API_KEY = "your_groq_api_key"

azurepw = "your_sql_password"
```

---

# SQL Server Configuration

Update:

## `database/connection.py`

```python
server = "your_server_name"

database = "your_database_name"
```

---

# Run Application

```bash
streamlit run streamlit_ui.py
```

---

# Safety Features

The system prevents dangerous SQL execution.

Blocked SQL operations:
- DELETE
- DROP
- UPDATE
- INSERT
- ALTER
- TRUNCATE

Only SELECT queries are allowed.

---

# Validation Features

The validation agent:
- Detects incomplete business queries
- Asks clarification questions only when required
- Uses confidence scoring
- Prevents infinite clarification loops
- Rejects unrelated prompts
- Maintains conversational context

---

# Example Validation Logic

## Query

```text
Show sales
```

## Clarification Needed

Because:
- time period missing
- aggregation unclear

---

## Query

```text
Give me total sales for May 2025
```

## No Clarification Needed

Because:
- business intent is clear
- time period is provided
- query is actionable

---

# Output Features

- Interactive result tables
- Generated SQL display
- Validation status display
- Confidence score display
- CSV export
- Dynamic charts and visualizations

---

# Future Improvements

- Authentication and user roles
- Dashboard generation
- Scheduled report generation
- Voice-based querying
- Multi-database support
- Query caching
- Natural language chart generation

---

# Author

Rayan Ahmed

AI-Powered Natural Language SQL Reporting System Internship Project
