import uuid
from pydantic import BaseModel, Field, field_validator
from src.database import db


class CategoryOut(BaseModel):
    id: str = Field(alias='_id')
    name: str
    parent_name: str | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "category1",
                "parent_name": "basecategory1"
            }
        }
    }


class CategoryIn(CategoryOut):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    parent_name: str | None = None

    @field_validator("name", mode='before')
    @classmethod
    def validate_name(cls, name: str):
        if name and (db['categories'].find_one({'name': name})):
            raise ValueError(f"Category '{name}' already exists")
        return name

    @field_validator("parent_name", mode='before')
    @classmethod
    def validate_parent_name(cls, parent_name: str | None):
        if parent_name and not (db['categories'].find_one({"name": parent_name})):
            raise ValueError(f"Invalid parent category name '{parent_name}'")
        return parent_name


class CategoryUpdate(CategoryIn):
    id: None = None
    name: str | None = None
    parent_name: str | None = None

    @field_validator("name", mode='before')
    @classmethod
    def validate_name(cls, name: str):
        return name


class Location(BaseModel):
    room: int = Field(ge=0)
    bookcase: int = Field(ge=0)
    shelf: int = Field(ge=0)
    cuvette: int = Field(ge=0)
    column: int = Field(ge=0)
    row: int = Field(ge=0)


class PartOut(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    serial_number: str
    name: str
    description: str
    category: str
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    location: Location

    model_config = {
        "json_schema_extra": {
            "example": {
                "serial_number": "1235446371",
                "name": "ssd",
                "description": "description",
                "category": "category name",
                "quantity": 10,
                "price": 123.45,
                "location": {
                    "room": 5,
                    "bookcase": 5,
                    "shelf": 5,
                    "cuvette": 5,
                    "column": 5,
                    "row": 5
                }
            }
        }
    }


class PartIn(PartOut):

    @field_validator('serial_number', mode='before')
    @classmethod
    def validate_serial_number(cls, serial_number: str):
        if serial_number and (db['parts'].find_one({'serial_number': serial_number})):
            raise ValueError(f"Part with serial number '{serial_number}' already exists")
        return serial_number

    @field_validator('category', mode='before')
    @classmethod
    def validate_category(cls, part_category: str):
        if part_category:
            category = db['categories'].find_one({'name': part_category})
            if not category:
                raise ValueError(f"Category with name '{part_category}' does not exist")
            if not category['parent_name']:
                raise ValueError(f"Part cannot be assigned to base category '{part_category}'")
        return part_category


class PartUpdate(PartIn):
    id: None = None
    serial_number: str | None = None
    name: str | None = None
    description: str | None = None
    category: str | None = None
    quantity: int | None = Field(ge=0, default=None)
    price: float | None = Field(ge=0, default=None)
    location: Location | None = None

    @classmethod
    def validate_serial_number(cls, serial_number: str):
        return serial_number
