from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    number_of_posts: int

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    number_of_posts: Optional[int] = None

users = {
    1: {
        "username": "user1",
        "password": "123456",
        "number_of_posts": 45
    },
    2: {
        "username": "user2",
        "password": "98765",
        "number_of_posts": 2
    }
}

@app.get("/")
async def root():
    return {"message": "This is the root"}

@app.get("/get-user/{user_id}")
def get_user(user_id: int = Path(description="The ID of the user", gt=0)):
    return users[user_id]

@app.get("/get-user-by-name")
def get_user(username: Optional[str]):
    for user_id in users:
        if users[user_id]["username"] == username:
            return users[user_id]
    return {"Data": "Not found"}


@app.post("/create-user/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in users:
        return {"Error user ID already exists"}

    users[user_id] = user
    return users[user_id]

@app.put("/update-user/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        return {"Error user ID does not exist"}

    if user.password != None:
        users[user_id]["password"] = user.password

    if user.username != None:
        users[user_id]["username"] = user.username

    if user.number_of_posts != None:
        users[user_id]["number_of_posts"] = user.number_of_posts

    return users[user_id]


@app.delete("/delete-user")
def delete_user(user_id: int = Query(..., description="The ID of the user to be deleted.", gt=0)):
    if user_id not in users:
        return {"Error": "ID does not exist"}
    del users[user_id]
    return {"Success": "User deleted."}