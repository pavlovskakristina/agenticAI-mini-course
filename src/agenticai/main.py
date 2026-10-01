import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # This will load the .env file

# This will get the value of the OPENROUTER_API_KEY environment variable
api_key = os.environ.get("OPENROUTER_API_KEY")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Is New York City is a good place to live? Use one paragraph maximum.",
        }
    ],
)

print(response.choices[0].message.content)
