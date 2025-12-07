from fastapi import FastAPI,HTTPException

from app.schemas import postuser

app = FastAPI()

texts = {1:{"dhrutabrata":{"Biotechnology"}},
         2:{"saloni":{"computer science"}}        
        }

@app.get("/home")
def home():
    return{"message":"hello"}

@app.get("/hello")
def hello():
    return{"message":"do u know me"}

@app.get("/post/{id}")
def get_by_id(id:int):
    if id not in texts:
        raise HTTPException(status_code=404,detail="post not found")
    return texts.get(id)

@app.post("/user")
def user(post:postuser)->postuser:
    return{
        "meesage":"user create",
        "data":post
       }