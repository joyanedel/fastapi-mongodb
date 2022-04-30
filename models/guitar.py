from pydantic import BaseModel

class GuitarModel(BaseModel):
    brand:  str
    model:  str
    year:   int
    color:  str
    price:  float