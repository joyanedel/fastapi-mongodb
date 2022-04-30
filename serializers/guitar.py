def guitarEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "brand": item["brand"],
        "model": item["model"],
        "year": item["year"],
        "color": item["color"],
        "price": item["price"]
    }

def guitarEntities(collection) -> list:
    return [guitarEntity(item) for item in collection]