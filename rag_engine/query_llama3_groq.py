import os
import requests
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def query_llama3(prompt):
    api_key = os.getenv("groq_api_key")
    if not api_key:
        raise ValueError("Missing 'groq_api_key' in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",  
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)

    try:
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        json_data = response.json()
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", response.text)
        raise e
    except ValueError:
        print("Failed to parse JSON:", response.text)
        raise

    if 'choices' not in json_data:
        print("Unexpected API response:", json_data)
        raise ValueError("API response missing 'choices' key.")

    return json_data['choices'][0]['message']['content']
