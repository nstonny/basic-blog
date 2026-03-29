import json

def get_blog_posts():
    with open("posts.json", "r") as f:
        return json.load(f)