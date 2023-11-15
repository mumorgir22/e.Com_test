from fastapi import FastAPI

from app.template.routes import router

app = FastAPI()

app.include_router(router)
