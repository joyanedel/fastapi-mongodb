from passlib.hash import sha256_crypt

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"] 
    }

def userEntities(collection) -> list:
    return [userEntity(item) for item in collection]