from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name:       str
    email:      str
    password:   str