from gc import collect
from bson import ObjectId
from fastapi import APIRouter, status
from config.database import db
from models.guitar import GuitarModel
from serializers import guitar as guitarSerializer

router = APIRouter(prefix='/guitars')

@router.get('', status_code=status.HTTP_200_OK)
def list():
    """Returns all guitars in system"""
    print(f"db type: {type(db['guitar'])}")
    return guitarSerializer.guitarEntities(db["guitar"].find()) 

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: str):
    """Get guitar by its id"""
    guitar = db["guitar"].find_one({"_id": ObjectId(id)})
    return guitarSerializer.guitarEntity(guitar)


@router.post('', status_code=status.HTTP_201_CREATED)
async def post(guitar: GuitarModel):
    """Add guitar to system"""
    _guitar = dict(guitar)
    id =  db["guitar"].insert_one(_guitar).inserted_id

    return {"id": str(id)}


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id: str, guitar: GuitarModel):
    "Update guitar from system"
    db["guitar"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(guitar)})


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    """Delete user from system by its id"""
    db["guitar"].find_one_and_delete({"_id": ObjectId(id)})