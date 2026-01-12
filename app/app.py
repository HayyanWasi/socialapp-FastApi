from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app=FastAPI()


text_posts = {
    1: {"title": "New Posts", "content": "cool test posts"},
    2: {"title": "Python Tips", "content": "FastAPI is extremely fast and easy to learn."},
    3: {"title": "Daily Routine", "content": "Woke up at 6 AM, exercised, and started coding."},
    4: {"title": "Tech News", "content": "AI is transforming the way we write software."},
    5: {"title": "Cooking", "content": "Tried a new recipe for Biryani today, it was spicy!"},
    6: {"title": "Travel", "content": "Planning a trip to the mountains next weekend."},
    7: {"title": "Fitness", "content": "Consistency is the key to seeing physical results."},
    8: {"title": "Gaming", "content": "The new open-world RPG has some amazing graphics."},
    9: {"title": "Movies", "content": "Just watched an old classic movie; it aged well."},
    10: {"title": "Motivation", "content": "Small steps every day lead to big results."}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = post
    return post


@app.delete("/posts/{id}")
def delete_post(id:int):
    post = text_posts.pop(id)
    return post


