from pydantic import BaseModel

class Post(BaseModel):
    rocktype: str
    title: str
    picture: str
    description: str
    location: list[float]
    hashtags: list[str]
    liked: list[str]
    user_id: str