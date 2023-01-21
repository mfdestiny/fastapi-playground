from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class User(BaseModel):
    username: str
    profile_info: ProfileInfo
    liked_posts: Optional[List[int]] = None

def get_user_info() -> User:
    profile_info = {
        "short_description": "howdy",
        "long_bio": "im a cowboy"
    }

    profile_info = ProfileInfo(**profile_info)

    content = {
        'username': "test_user",
        'profile_info': profile_info,
        'liked_posts': [1]
    }


    return User(**content)

@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()
    return user



@app.get("/", response_class=PlainTextResponse)
def home():
    return "back at home"
