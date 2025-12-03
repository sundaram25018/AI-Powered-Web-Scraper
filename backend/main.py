from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_website
from analyzer import analyze_content
import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapeRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "AI Web Scraper API is running"}

@app.post("/scrape")
async def scrape_and_analyze(request: ScrapeRequest):
    try:
        # 1. Scrape the website
        scraped_data = await scrape_website(request.url)
        
        # 2. Analyze with AI
        analysis_report = await analyze_content(scraped_data)
        
        return {
            "url": request.url,
            "scraped_content_length": len(scraped_data),
            "report": analysis_report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
