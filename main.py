"""
Development (with auto-reload):
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from crud import get_blog_posts

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    blog_posts = get_blog_posts()
    return templates.TemplateResponse(request, 'index.html', context={"posts": blog_posts})