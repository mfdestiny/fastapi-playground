from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()



class User(BaseModel):
    username: str = Field(
        alias= "name",
        title="the username",
        description = "username of user",
        min_length = 1,
        max_length = 20,
        default = None
    )
    liked_posts: List[int] = Field(
        description = "array of post ids the user liked"
    )

    #class Config:
    #    max_any_str_ length = 20

class FullUserProfile(User):
    short_description: str
    long_bio: str

#command + alt + L auto formatting
def get_user_info(user_id: str = "default") -> FullUserProfile:
    profiles_info = {
        "default": {
            "short_description": "howdy",
            "long_bio": "im a cowboy",
        },
        "user_1": {
            "short_description": "user1 bio description",
            "long_bio": "user1 went to the moon"
        }
    }

    profile_info = profiles_info[user_id]

    users_info = {
        "default": {
            "liked_posts": [420] * 9,
            "profile_info": profile_info
        },
        "user_1": {
            "liked_posts": [],
            "profile_info": profile_info
        }
    }
    user_info = users_info[user_id]

    user = User(**user_info)
    full_profile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_profile)


@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():

    full_user = get_user_info()

    return full_user



@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: str):

    full_user = get_user_info(user_id)

    return full_user
