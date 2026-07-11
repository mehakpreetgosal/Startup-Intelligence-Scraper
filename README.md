# 🚀 Startup Intelligence Scraper

An AI-powered web application that automatically collects startup information from the web, analyzes the content using a Large Language Model (LLM), and generates structured business insights.

The project combines **web scraping**, **search APIs**, and **Generative AI** to help users quickly understand startups without manually reading multiple websites.

---

# 📌 Features

- 🔍 Search any startup by name
- 🌐 Scrape startup information from the web
- 🤖 AI-generated startup analysis
- 📊 Clean and structured output
- 💻 User-friendly Flask web interface
- ⚡ Fast response using Groq LLM
- 📱 Responsive frontend

---

# ⚙ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

---

## Backend

- Python
- Flask

---

## Libraries

- BeautifulSoup4
- Requests
- Regular Expressions (re)
- SerpAPI
- Groq Python SDK

---

## APIs Used

### SerpAPI

Used for searching startup websites and relevant information from Google Search.

Purpose:

- Search startup names
- Fetch search results
- Retrieve startup webpages

---

### Groq API

Used for Large Language Model inference.

Purpose:

- Summarize startup information
- Analyze business model
- Generate structured insights

---

# 🧠 Workflow

```
User Input
      │
      ▼
Enter Startup Name
      │
      ▼
SerpAPI Search
      │
      ▼
Retrieve Website
      │
      ▼
BeautifulSoup Web Scraping
      │
      ▼
Extract Text Content
      │
      ▼
Send Text to Groq LLM
      │
      ▼
AI Analysis
      │
      ▼
Display Structured Report
```

---

# 🌐 Web Scraping Workflow

The project uses **BeautifulSoup** for web scraping.

### Step 1

The user enters the startup name.

Example

```
OpenAI
```

---

### Step 2

SerpAPI searches Google for the startup.

Example query

```
OpenAI startup
```

---

### Step 3

The first relevant webpage is selected.

---

### Step 4

Python Requests downloads the webpage HTML.

---

### Step 5

BeautifulSoup parses the HTML document.

Example:

```python
soup = BeautifulSoup(html, "html.parser")
```

---

### Step 6

Unnecessary HTML elements are ignored while readable text is extracted.

Example:

- Paragraphs
- Headings
- Lists

---

### Step 7

The extracted content is cleaned using regular expressions.

Examples:

- Remove extra spaces
- Remove line breaks
- Remove unnecessary symbols

---

### Step 8

The cleaned text is sent to the LLM.

---

### Step 9

The AI generates a structured startup report.

---

# 🤖 LLM Prompt Workflow

The extracted webpage content is provided to the Groq LLM with a carefully designed prompt.

The model is instructed to analyze:

- Startup overview
- Products or services
- Target audience
- Business model
- Funding (if available)
- Competitive advantages
- Industry
- Future potential

The LLM converts raw web content into meaningful business intelligence.

---

# 📊 Output Format

The generated report includes:

- Startup Name
- Company Overview
- Industry
- Products & Services
- Business Model
- Target Market
- Key Highlights
- Competitive Advantage
- Future Opportunities
- AI Summary

---

# 🧩 Workflow Diagram

```
+-------------------+
| User Input        |
+-------------------+
          |
          v
+-------------------+
| SerpAPI Search    |
+-------------------+
          |
          v
+-------------------+
| Startup Website   |
+-------------------+
          |
          v
+-------------------+
| BeautifulSoup     |
| Web Scraping      |
+-------------------+
          |
          v
+-------------------+
| Clean Text        |
+-------------------+
          |
          v
+-------------------+
| Groq LLM          |
+-------------------+
          |
          v
+-------------------+
| Startup Report    |
+-------------------+
```

---

# 📋 Requirements

- Python 3.10+
- Flask
- Requests
- BeautifulSoup4
- SerpAPI Key
- Groq API Key

---
# Screenshots


