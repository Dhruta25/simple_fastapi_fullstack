# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/home")
# def home():
#     return {"message":"helloworld"}

import uvicorn
from app.app import app

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000,reload=True)