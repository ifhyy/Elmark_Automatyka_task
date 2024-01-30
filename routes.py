from typing import List

from fastapi import APIRouter, Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from config.database import db as database
from models import CategoryIn, CategoryOut, CategoryUpdate, PartIn, PartOut, PartUpdate

part_router = APIRouter()
category_router = APIRouter()


@part_router.get("/", response_model=List[PartOut])
def list_parts():
    parts = list(database["parts"].find())
    return parts


@part_router.get("/{id}", response_model=PartOut)
def get_part(id: str):
    if (part := database["parts"].find_one({"_id": id})) is not None:
        return part

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Part with id {id} not found")


@part_router.post("/", status_code=status.HTTP_201_CREATED, response_model=PartOut)
def create_part(part: PartIn = Body()):
    part = jsonable_encoder(part)
    new_part = database["parts"].insert_one(part)
    created_part = database["parts"].find_one({"_id": new_part.inserted_id})
    return created_part


@part_router.put("/{id}", response_model=PartOut)
def update_part(id : str, part: PartUpdate = Body()):
    update_data = {k: v for k, v in part.model_dump().items() if v is not None}


    if len(update_data) >= 1:
        if 'serial_number' in update_data:
            serial_number = update_data['serial_number']
            existing = database["parts"].find_one({"serial_number": serial_number})
            if existing and existing['_id'] != id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail=f"Part with serial number {serial_number}"
                                           f" already exists, choose another")

        database["parts"].update_one({'_id': id}, {'$set': update_data})
    if (result_part := database["parts"].find_one({"_id": id})) is not None:
        return result_part

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Part with id {id} not found")


@part_router.delete("/{id}")
def delete_part(id: str, response: Response):
    delete_result = database["parts"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Part with id {id} not found")


@part_router.get("/search/")
def search_part(id: str = None, serial_number: str = None, name: str = None, description: str = None,
                category: str = None, quantity: int = None, price: float = None):
    search_query = {}
    if id is not None:
        search_query["_id"] = id
    if serial_number is not None:
        search_query["serial_number"] = serial_number
    if name is not None:
        search_query["name"] = name
    if description is not None:
        search_query["description"] = description
    if category is not None:
        search_query["category"] = category
    if quantity is not None:
        search_query["quantity"] = int(quantity)
    if price is not None:
        search_query["price"] = float(price)
    search_result = list(database["parts"].find(search_query))
    return search_result


@category_router.get("/", response_model=List[CategoryOut])
def list_categories():
    categories = list(database["categories"].find())
    return categories


@category_router.get("/{id}", response_model=CategoryOut)
def get_category(id: str):
    if (category := database["categories"].find_one({"_id": id})) is not None:
        return category

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")


@category_router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryOut)
def create_category(category: CategoryIn = Body()):
    category = jsonable_encoder(category)
    new_category = database["categories"].insert_one(category)
    created_category = database["categories"].find_one({"_id": new_category.inserted_id})

    return created_category


@category_router.put("/{id}", response_model=CategoryOut)
def update_category(id: str, category: CategoryUpdate = Body()):
    update_data = {k: v for k, v in category.model_dump().items() if v is not None}
    current_category = database["categories"].find_one({"_id": id})

    if len(update_data) >= 1:
        if 'name' in update_data:
            name = update_data['name']
            existing = database["categories"].find_one({"name": name})
            if existing and existing['_id'] != id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail=f"Category with name {name} already exists, choose another name")
            current_category_name = current_category['name']
            database["categories"].update_many({"parent_name": current_category_name},
                                               {"$set": {"parent_name": name}})

        if 'parent_name' in update_data:
            if current_category['name'] == update_data['parent_name']:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail=f"Category can't have the same parent name")

        database["categories"].update_one({"_id": id}, {"$set": update_data})

    if (result_category := database["categories"].find_one({"_id": id})) is not None:
        return result_category

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")


@category_router.delete("/{id}")
def delete_category(id: str, response: Response):
    category = database['categories'].find_one({"_id": id})
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")
    is_parent = database["categories"].find_one({"parent_name": category["name"]})
    if is_parent:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category can't be deleted")
    is_used = database["parts"].find_one({"category": category["name"]})
    if is_used:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category is used so can't be deleted")

    delete_result = database["categories"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
