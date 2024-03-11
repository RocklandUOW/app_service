from pydantic import BaseModel

class PassCheck(BaseModel):
    username: str
    password: str