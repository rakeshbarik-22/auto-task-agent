import google.generativeai as genai

from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")

def summarize_text(text):
    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text
def generate_email(text):
    response = model.generate_content(f"Write a professional email:\n{text}")
    return response.text

def search_answer(query):
    response = model.generate_content(f"Answer this:\n{query}")
    return response.text

def onboarding_agent(user_input):
    response = model.generate_content(f"Help this user with onboarding: {user_input}")
    return response.text