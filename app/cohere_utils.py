import cohere
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(API_KEY)

def generate_blog(topic: str) -> str:
    response = co.generate(
        model='command',  # Free-tier model
        prompt=f"Write a blog on the topic: {topic}",
        max_tokens=400,
        temperature=0.7
    )
    return response.generations[0].text.strip()
