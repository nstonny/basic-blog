import json

def get_blog_posts():
    with open("posts.json", "r") as f:
        return json.load(f)

def get_post_by_id(post_id: int):
    posts = get_blog_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None

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

def delete_blog_post(post_id: int):
    posts = get_blog_posts()
    posts =[post for post in posts if post["id"] != post_id]
    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)

def update_blog_post(post_id: int, title: str, author: str, content: str):
    posts = get_blog_posts()
    for post in posts:
        if post["id"] == post_id:
            post["title"] = title
            post["author"] = author
            post["content"] = content
            break
    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)
