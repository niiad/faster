from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "example schema 1"},
                    {"item": "example schema 2"},
                    {"item": "example schema 3"}
                ]
            }
        }

