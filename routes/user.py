from bson import ObjectId
from passlib.hash import sha256_crypt
from fastapi import APIRouter, status
from config.database import conn
from models.user import User
from schemas import user as userSchema

user = APIRouter()

@user.get('/users', status_code=status.HTTP_200_OK)
def list():
    """Returns all users in system"""
    return userSchema.userEntities(conn.local.user.find())

@user.get('/users/{id}', status_code=status.HTTP_200_OK)
def get(id: str):
    """Get user by its id"""
    user = conn.local.user.find_one({"_id": ObjectId(id)})
    return userSchema.userEntity(user)


@user.post('/users', status_code=status.HTTP_201_CREATED)
def post(user: User):
    """Add user to system"""
    _user = dict(user)
    _user["password"] = sha256_crypt.encrypt(_user["password"])
    _id = conn.local.user.insert_one(_user).inserted_id

    return {"id": str(_id)}  

@user.put('/users/{id}', status_code=status.HTTP_200_OK)
def update(id: str, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    """Delete user from system by its id lol"""
    conn.local.user.find_one_and_delete({'_id': ObjectId(id)})