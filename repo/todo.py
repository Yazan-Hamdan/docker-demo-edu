from typing import List
from models.todo import Todo
from request_models.todo import TodoReqModel
from response_models.todo import TodoResModel

todos = []


def get_all_todos() -> List[TodoResModel]:
    todo_responses = [TodoResModel(**document.dict()) for document in todos]
    return todo_responses


def get_todo_by_id(todo_id: str) -> TodoResModel:
    for todo in todos:
        if todo.id == todo_id:
            todo_response = TodoResModel(**todo.dict())
            return todo_response
    return None


def add_todo(todo: TodoReqModel) -> TodoResModel:
    new_todo_db = Todo(**todo.dict())
    todos.append(new_todo_db)
    new_todo_response = TodoResModel(**new_todo_db.dict())
    return new_todo_response


def update_todo_by_id(todo_id: str, new_todo: TodoReqModel) -> TodoResModel:
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            new_todo_db = Todo(**new_todo.dict())
            todos[i] = new_todo_db
            new_todo_response = TodoResModel(**new_todo_db.dict())
            return new_todo_response
    return None


def delete_todo_by_id(todo_id: str):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return None
    return None
