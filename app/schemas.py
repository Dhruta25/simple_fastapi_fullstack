from pydantic import BaseModel

class postuser(BaseModel):
    name:str
    email:str
    phone:int