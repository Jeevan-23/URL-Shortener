from fastapi import FastAPI
from app.api.url_router import router

app = FastAPI(title="URL Shortener API")

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "URL Shortener Running"
    }