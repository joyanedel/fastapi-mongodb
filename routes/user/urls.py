from bson import ObjectId
from passlib.hash import sha256_crypt
from fastapi import APIRouter, status
from config.database import db
from models.user import UserModel
from serializers import user as userSerializer

router = APIRouter(prefix='/users')

@router.get('', status_code=status.HTTP_200_OK)
def list():
    """Returns all users in system"""
    return userSerializer.userEntities(db["user"].find())

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: str):
    """Get user by its id"""
    user = db["user"].find_one({"_id": ObjectId(id)})
    return userSerializer.userEntity(user)


@router.post('', status_code=status.HTTP_201_CREATED)
def post(user: UserModel):
    """Add user to system"""
    _user = dict(user)
    _user["password"] = sha256_crypt.encrypt(_user["password"])
    _id = db["user"].insert_one(_user).inserted_id

    return {"id": str(_id)}  

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id: str, user: UserModel):
    db["user"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    """Delete user from system by its id"""
    db["user"].find_one_and_delete({'_id': ObjectId(id)})

@router.get('/peo')
def peo():
    return {"message": "peo"}