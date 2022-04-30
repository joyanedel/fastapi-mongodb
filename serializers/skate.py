def skateEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "brand": item["brand"],
        "model": item["model"],
        "year": item["year"],
        "color": item["color"],
        "price": item["price"]
    }

def skateEntities(collection) -> list:
    return [skateEntity(item) for item in collection]