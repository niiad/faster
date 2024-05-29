from fastapi import FastAPI
from todos import todo

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo.todo_router)
