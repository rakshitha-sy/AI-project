import os
import google.generativeai as genai

# 1. Configure your Gemini API Key securely from environment variables
# (Or enter it when prompted if not set in your environment)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = input("Enter your Gemini API Key: ")

genai.configure(api_key=api_key)

# 2. Initialize the correct Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. Get prescription input from the user
prescription = input("Enter your prescription text: ")

# 4. Create the prompt and generate content
prompt = f"Explain this prescription in simple, clear words for a patient:\n{prescription}"

response = model.generate_content(prompt)

# 5. Print the final explanation
print("\nExplanation:")
print(response.text)
