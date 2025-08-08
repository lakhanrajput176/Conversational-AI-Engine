# Conversational AI Recruitment Assistant 

## Overview
This is a proof-of-concept **AI-powered chatbot** designed to assist recruiters in pre-screening candidates.
It simulates integration with an Applicant Tracking System (ATS) and uses **Natural Language Processing (NLP)** to parse resumes,
ask qualifying questions, and generate candidate scores.

> This demo uses dummy data and mock APIs to replicate real-world functionality without exposing any proprietary code or data.

## Key Features
- Conversational pre-screening powered by ChatGPT API (demo)
- Resume parsing and skills extraction (demo logic)
- Candidate scoring and recommendations
- Mock ATS integration and workflow automation (Power Automate flows)

## Tech Stack
- AI & NLP: OpenAI ChatGPT API (placeholder in demo)
- Bot Framework: Azure Bot Services (integration notes in app.py)
- Automation: Power Automate (sample flow JSON provided)
- Language: Python (Flask example and API logic)
- Hosting: Azure (recommended)

## Getting Started (Demo)
1. Clone the repo
2. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API keys in a `.env` file (for demo, you can leave empty):
   ```bash
   OPENAI_API_KEY=your_key_here
   ```
4. Run the demo:
   ```bash
   python app.py
   ```
5. Open the local Flask endpoint (default `http://127.0.0.1:5000/chat`) to interact with demo endpoints.

## Project Structure
```
📂 conversational-ai-recruitment-assistant
 ├── README.md
 ├── requirements.txt
 ├── app.py
 ├── data
 │   └── dummy_resumes.json
 ├── docs
 │   └── architecture.png
 └── flows
     └── power_automate_flow_example.json
```

## Notes
- This is a demonstration project. Replace placeholders with real API keys and secure secrets management for production.
- Do not expose real candidate data in public repos; use anonymized or synthetic data only.
