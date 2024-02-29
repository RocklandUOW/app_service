from fastapi import FastAPI
from routers import account_router, post_router
from pymongo import MongoClient

app = FastAPI()

# default origin of the url
@app.get("/")
def home():
    return {"message":"Smile and Wave Boys!"}

# include all the routes from routers folder
app.include_router(account_router.router)
app.include_router(post_router.router)