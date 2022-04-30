from bson import ObjectId
from fastapi import APIRouter, status
from config.database import db
from models.skate import SkateModel
from serializers import skate as skateSerializer

router = APIRouter(prefix='/skates')

@router.get('', status_code=status.HTTP_200_OK)
def list():
    """Returns all skates in system"""
    return skateSerializer.skateEntities(db["skate"].find())

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: str):
    """Get skate by its id"""
    skate = db["skate"].find_one({"_id": ObjectId(id)})
    return skateSerializer.skateEntity(skate)


@router.post('', status_code=status.HTTP_201_CREATED)
def post(skate: SkateModel):
    """Add skate to system"""
    _skate = dict(skate)
    id = db["skate"].insert_one(_skate).inserted_id

    return {"id": str(id)}


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id: str, skate: SkateModel):
    "Update skate from system"
    db["skate"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(skate)})


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    """Delete user from system by its id"""
    db["skate"].find_one_and_delete({"_id": ObjectId(id)})