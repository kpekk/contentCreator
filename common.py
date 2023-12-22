from dotenv import load_dotenv
import os

def get_openai_api_key():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("No OpenAI API key found in environment variables")

    return api_key