from pydantic import BaseModel

class SkateModel(BaseModel):
    brand:  str
    model:  str
    year:   int
    color:  str
    price:  float