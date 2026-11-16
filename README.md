# AI Prescription Explainer

A lightweight Python command-line tool powered by Google's Gemini API (`gemini-1.5-flash`). It takes complex medical prescription notes and translates them into clear, patient-friendly explanations.

---

## Features
- **Plain-Language Summaries:** Breaks down medical abbreviations, dosages, and instructions into everyday terms.
- **Secure API Handling:** Reads your Gemini API key from environment variables (with an interactive fallback prompt) so sensitive keys are never exposed in public repositories.
- **Fast Execution:** Built using the lightweight `gemini-1.5-flash` model for quick responses.

---

## Tech Stack
- **Language:** Python 3.8+
- **AI SDK:** `google-generativeai`

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rakshitha-sy/AI-project.git](https://github.com/rakshitha-sy/AI-project.git)
   cd AI-project

   ---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rakshitha-sy/AI-project.git](https://github.com/rakshitha-sy/AI-project.git)
   cd AI-project
   
*Install the required library:

Bash
pip install google-generativeai

*Set up your Gemini API Key:
Obtain a free API key from Google AI Studio, then set it in your terminal:

*Windows (Command Prompt):

DOS
set GEMINI_API_KEY=your_actual_api_key_here

*Windows (PowerShell):

PowerShell
$env:GEMINI_API_KEY="your_actual_api_key_here"

*macOS / Linux:

Bash
export GEMINI_API_KEY="your_actual_api_key_here"

* How to Run
Make sure your Python script file is in the repository (e.g., project.py).

Run the script in your terminal:

Bash
python project.py
*Type or paste your prescription text when prompted and press Enter to see the simplified explanation.

*Disclaimer
This tool is built for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified doctor or pharmacist regarding your medications.
