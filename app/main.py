from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.cohere_utils import generate_blog
from app.db import collection

app = FastAPI()

class BlogRequest(BaseModel):
    topic: str

@app.post("/generate-blog")
def generate_blog_route(request: BlogRequest):
    topic = request.topic.strip().lower()

    # checking for the existing blog 
    existing = collection.find_one({"topic": topic})
    if existing:
        return {"topic": existing["topic"], "blog": existing["blog"]}

    try:
        blog_text = generate_blog(request.topic)
        record = {"topic": topic, "blog": blog_text}
        collection.insert_one(record)
        response= record.copy()
        if "_id" in response:
            del response["_id"]
        return response
    except Exception as e :
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/blogs")
def get_all_blogs():
    blogs = list(collection.find({}, {"_id": 0}))  # hide MongoDB ID
    return blogs

@app.get("/blog/{topic}")
def get(topic: str):
    blog = collection.find_one({"topic": topic})
    if blog:
        return blog
    else:
        return None