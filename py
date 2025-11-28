# content_generator.py
import os
import json
from typing import Dict, List
from openai import AzureOpenAI
from dotenv import load_dotenv
import base64
import requests

load_dotenv()

class SmartContentGenerator:
    def __init__(self):
        self.azure_openai_client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2023-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        self.dalle_endpoint = os.getenv("AZURE_OPENAI_DALLE_ENDPOINT")
        self.dalle_key = os.getenv("AZURE_OPENAI_DALLE_KEY")
        
        self.chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    
    def generate_blog_post(self, topic: str, tone: str = "professional", 
                          length: str = "medium") -> Dict:
        """Generate a complete blog post"""
        
        length_map = {
            "short": "300-500 words",
            "medium": "600-800 words", 
            "long": "900-1200 words"
        }
        
        prompt = f"""
        Write a {tone} blog post about: {topic}
        Length: {length_map[length]}
        
        Please structure it as follows:
        1. Engaging title
        2. Introduction paragraph
        3. 3-5 main points with subheadings
        4. Conclusion
