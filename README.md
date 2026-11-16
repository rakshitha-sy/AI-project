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
