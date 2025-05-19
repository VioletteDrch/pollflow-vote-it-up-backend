import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This loads the .env file into os.environ


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))