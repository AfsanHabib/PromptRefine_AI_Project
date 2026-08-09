# PromptRefine      [![Live Demo](https://img.shields.io/badge/Live-Demo-2563EB?style=for-the-badge)](https://afsan-promptrefine.streamlit.app/)

An AI-powered prompt engineering workspace for analyzing, scoring,  improving, and comparing prompts before sending them to a language
model.




## Project Overview

**PromptRefine** is a developer-focused AI application
designed to help users understand and improve the quality of their
prompts. Instead of sending an unstructured prompt directly to an AI model, the application analyzes the prompt, identifies missing information,
evaluates prompt quality, and uses Gemini AI to generate an improved
version. The project combines **deterministic Python-based analysis** with
**LLM-powered semantic analysis and optimization**. 

## AI-Assisted Development Journey

This project was developed as a hands-on AI engineering project with
substantial assistance from **Claude, GPT, and Gemini** throughout the
development process.
**The user interface was built with maximum assistance from AI tools**.

A major part of the development process involved debugging code
generated with AI assistance. Many errors and integration issues were encountered during AI-generated implementation. These issues were systematically investigated and resolved with the help of AI. **AI was used as a development partner, not as a replacement for testing or engineering decisions.**

## Why I Built This
Large language models can produce very different results from small
changes in prompt structure. I built Prompt Optimizer Studio to explore how an AI engineering application can combine:
-   Python application logic
-   Prompt engineering
-   LLM APIs
-   Structured LLM output
-   Pydantic validation
-   Deterministic analysis
-   Hybrid scoring
-   Streamlit UI
-   Cloud deployment

The goal was not simply to call an AI API, but to build a complete,
usable AI-powered developer tool around an LLM.


## Technology Stack

  **Python**                          Core application and analysis logic

  **Streamlit**                       Interactive web application

  **Gemini API**                      AI-powered semantic analysis and
                                      prompt optimization

  **Google GenAI SDK**                Gemini API integration

  **Pydantic**                        Structured response validation

  **SQLite**                          Prompt history persistence

  **python-dotenv**                   Local environment variable
                                      management






## Core Workflow

``` text
User Prompt
     |
     v
Local Prompt Analyzer
     |
     +-- Word Count
     +-- Sentence Count
     +-- Role Detection
     +-- Constraint Detection
     +-- Output Format Detection
     +-- Example Detection
     |
     v
Gemini AI
     |
     +-- Clarity Analysis
     +-- Context Analysis
     +-- Specificity Analysis
     +-- Missing Information
     +-- Prompt Optimization
     |
     v
Hybrid Scoring Engine
     |
     +-- Local Analysis
     +-- Gemini Analysis
     |
     v
Final Score + Improvement
     |
     v
Streamlit Interface
     |
     +-- Optimized Prompt
     +-- Prompt Variations
     +-- Analysis Report
     +-- Prompt History
```


## How It Works

### 01 --- Analyze

The application performs deterministic analysis of the user's prompt,
inspecting characteristics such as word count, sentence count, role
presence, constraints, output format, examples, and prompt structure.

### 02 --- Score

The application combines local analysis with Gemini's semantic
evaluation using a hybrid scoring engine. The scoring process evaluates
dimensions such as clarity, context, and specificity.

The final score is calculated by the application's scoring engine rather
than relying entirely on the LLM.

### 03 --- Optimize

Gemini analyzes the semantic quality of the prompt and generates a
substantially improved version while preserving the user's original
intent.

### 04 --- Compare

The application analyzes the optimized prompt again and compares the
original and optimized scores to provide a measurable view of
improvement.




 

## Installation & Setup

### 1. Clone the Repository

``` bash
git clone <https://github.com/AfsanHabib/PromptRefine_AI_Project>
cd PromptRefine_AI_Project
```
### 2. Create a Virtual Environment
Windows:
``` bash
python -m venv venv
venv\Scripts\activate
```
macOS/Linux:
``` bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 4. Configure Gemini API
Create a `.env` file in the project root:
``` env
GEMINI_API_KEY=your_gemini_api_key_here
```
Never commit your `.env` file to GitHub.

### 5. Run the Application
``` bash
streamlit run app.py
```

## Usage

1.  Open the application and navigate to **Optimizer**.
2.  Enter a prompt.
3.  Click **Optimize Prompt**.
4.  Review the prompt score, clarity, specificity, word count, sentence
    count, and missing information.
5.  Review the optimized prompt and alternative prompt styles.
6.  Compare the original and optimized scores.
7.  Save, copy, or download results as needed.








## Features

### Prompt Intelligence

-   Prompt quality scoring
-   Hybrid scoring engine
-   Clarity analysis
-   Context analysis
-   Specificity analysis
-   Word count analysis
-   Sentence count analysis
-   Role detection
-   Constraint detection
-   Output format detection
-   Example detection
-   Missing information detection

### AI-Powered Optimization

-   Gemini-powered prompt analysis
-   Optimized prompt generation
-   Standard prompt variation
-   Zero-shot prompt variation
-   Few-shot prompt variation
-   Developer-oriented prompt variation
-   System prompt variation
-   JSON-mode prompt variation

### Comparison & Improvement

-   Original prompt score
-   Optimized prompt score
-   Score improvement calculation
-   Original vs. optimized analysis
-   Visual prompt intelligence metrics

### History & Persistence

-   Prompt history
-   SQLite persistence
-   View previous prompts
-   View previous scores
-   View optimized prompts
-   Delete saved prompts

### Export & Productivity

-   Copy optimized prompts
-   Download optimized prompts
-   Download analysis reports

### User Interface

-   Dark developer-focused interface
-   Streamlit-based responsive layout
-   Sidebar navigation
-   Optimizer page
-   History page
-   About page
-   Custom CSS styling
-   Visual metric cards
-   Prompt comparison sections



## Future Improvements

Potential future directions include:

1.  Automated prompt evaluation datasets
2.  A/B testing of original and optimized prompts
3.  Model-to-model prompt comparison
4.  Prompt template libraries
5.  Advanced prompt versioning
6.  Analytics dashboards
7.  Evaluation metrics based on actual model outputs
8.  Automated regression testing for prompt optimization
9.  User accounts and cloud persistence
10. Support for additional LLM providers



## Afsan Habib

-   GitHub: [GitHub Profile](https://github.com/AfsanHabib)
-   LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/afsan-habib-566340215/)
-   Facebook: [Facebook Profile](https://www.facebook.com/afsanhabib10)
