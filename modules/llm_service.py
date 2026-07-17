"""
llm_service.py

Handles communication with Gemini using the new Google GenAI SDK.
"""

import os
from urllib import response
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

# Create client
client = genai.Client(api_key=API_KEY)


def generate_ai_report(prompt):
    """
    Generate AI traffic analysis.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        print(response)
        
        print("========== GEMINI RESPONSE ==========")
        print(response)
        print("=====================================")

        print("TEXT =", response.text)

        return response.text

    except Exception as e:

        return f"Error: {e}"