import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini client
# Ensure GEMINI_API_KEY is set in environment variables
# genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # Moved inside function

async def analyze_content(content: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("DEBUG: GEMINI_API_KEY not found in environment variables.")
        return "Error: GEMINI_API_KEY not found. Please check your .env file."
    
    genai.configure(api_key=api_key)
    
    if not content:
        return "No content to analyze."
    
    # Gemini 1.5 Flash is good for large context, but we'll still be mindful
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    prompt = f"""
    You are an expert web analyst. 
    Analyze the following website content and provide a detailed report.
    
    Report Structure:
    1. **Summary**: A brief overview of what the website is about.
    2. **Key Features/Services**: Bullet points of main offerings.
    3. **Target Audience**: Who is this website for?
    4. **Sentiment/Tone**: The general tone of the content.
    
    Website Content:
    {content[:30000]} 
    """
    # Truncate to ~30k chars to be safe, though Flash can handle more.
    
    try:
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing content: {str(e)}"
