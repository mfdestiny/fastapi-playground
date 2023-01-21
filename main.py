from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()


class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class User(BaseModel):
    username: str = Field(
        alias="name",
        title="the username",
        description = "username of user",
        min_length = 1,
        max_length = 20,
        default = None
    )
    profile_info: ProfileInfo
    liked_posts: Optional[List[int]] = Field(
        description = "array of post ids the user liked",
        min_items = 2,
        max_items = 10
    )

def get_user_info() -> User:
    profile_info = {
        "short_description": "howdy",
        "long_bio": "im a cowboy"
    }

    profile_info = ProfileInfo(**profile_info)

    user_content = {
        'name': "wiz khalifa",
        'profile_info': profile_info,
        'liked_posts': [1] * 9
    }


    return User(**user_content)

@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()
    return user

