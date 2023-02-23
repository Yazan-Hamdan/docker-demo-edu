import uvicorn as uvicorn
from fastapi import FastAPI

from routes import todo

app = FastAPI(title="a simple todo list app", name="todo")

app.include_router(router=todo.router)

if __name__ == '__main__':
	uvicorn.run(app, host="0.0.0.0", port=8080)
