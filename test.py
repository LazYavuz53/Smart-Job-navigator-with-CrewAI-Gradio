import os
from dotenv import load_dotenv

load_dotenv()

# Print the OpenAI API key to ensure it's being loaded correctly
print(f"OpenAI API Key: {os.getenv('OPENAI_API_KEY')}")
