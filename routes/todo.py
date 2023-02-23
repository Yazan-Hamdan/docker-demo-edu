from fastapi import APIRouter, status
from typing import List
from response_models.todo import TodoResModel
from request_models.todo import TodoReqModel
from repo.todo import update_todo_by_id, add_todo, get_all_todos,\
	get_todo_by_id

# create a router
router = APIRouter(prefix="/v1/todo", tags=["todo"])


@router.get("/", response_model=List[TodoResModel], status_code=status.HTTP_200_OK)
async def get_todos_controller():
	return get_all_todos()


@router.get("/{id}", response_model=TodoResModel, status_code=status.HTTP_200_OK)
async def get_todo_by_id_controller(todo_id: str):
	todo = get_todo_by_id(todo_id=todo_id)
	return todo


@router.post("/", response_model=TodoResModel, status_code=status.HTTP_201_CREATED)
async def create_todo_controller(todo: TodoReqModel):
	return add_todo(todo=todo)


@router.put("/{id}", response_model=TodoResModel, status_code=status.HTTP_200_OK)
async def update_todo_by_id_controller(todo_id: str, todo: TodoReqModel):
	new_todo = update_todo_by_id(todo_id=todo_id, new_todo=todo)
	return new_todo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_by_id_controller(todo_id: str):
	pass
