"""
Development (with auto-reload):
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
"""

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from crud import get_blog_posts, add_blog_post, delete_blog_post, get_post_by_id, update_blog_post

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    blog_posts = get_blog_posts()
    return templates.TemplateResponse(request, 'index.html', context={"posts": blog_posts})

@app.get("/add", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(request, 'add.html')

@app.post("/add")
async def add_post(
        request:Request,
        title: str = Form(...),
        author: str = Form(...),
        content: str = Form(...) ):
    add_blog_post(title, author, content)
    return RedirectResponse(url="/", status_code=303)

@app.get("/delete/{post_id}")
async def delete_post(post_id: int):
    delete_blog_post(post_id)
    return RedirectResponse(url="/", status_code=303)

@app.get("/update/{post_id}", response_class=HTMLResponse)
async def update_form(request: Request, post_id: int):
    post = get_post_by_id(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse(request, 'update.html', context={"post": post})

@app.post("/update/{post_id}")
async def update_post(post_id: int,
                      title: str = Form(...),
                      author: str = Form(...),
                      content: str = Form(...)):
    post = get_post_by_id(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    update_blog_post(post_id, title, author, content)
    return RedirectResponse(url="/", status_code=303)




