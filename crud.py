import json

def get_blog_posts():
    with open("posts.json", "r") as f:
        return json.load(f)

def add_blog_post(title: str, author: str, content: str):
    posts = get_blog_posts()
    new_post = {
                "id": max(post["id"] for post in posts) + 1,
                "title": title,
                "author": author,
                "content": content
                }
    posts.append(new_post)
    with open("posts.json", "w") as f:
         json.dump(posts, f, indent=4)