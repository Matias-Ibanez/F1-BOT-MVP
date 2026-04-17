from fastapi import FastAPI

from app.api.session import router 

app = FastAPI()

app.include_router(router)