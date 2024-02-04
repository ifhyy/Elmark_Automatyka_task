# Elmark_Automatyka_task
Rest API for Elmark Automatyka recruitment task. FastAPI was chosen as a main framework as it is a good solution for REST API development and Mongodb interaction.
Author: Artem Stupak
## Setup instructions
1. Clone this repository using git clone
```shell
git clone https://github.com/ifhyy/Elmark_Automatyka_task.git
cd Elmark_Automatyka_task
```
2. Configure application by creating .env file based on provided .env.example
```shell
MONGODB_URI="mongodb+srv://rekrutacja:BZijŌwEru0oELxT@cluster11.yxu8n2k.mongodb.net/"
DB_NAME='ARTEM_STUPAK'
```
3. Build docker image by running
```shell
docker build -t elmark_task .
```
4. Run docker container
```shell
docker run -d -p 7777:8000 elmark_task
```

## API documentation
### FastAPI Swagger UI
Fastapi initially provides automatically-generated documentation by Swagger which can also be used for manual endpoints testing.
```shell
http://localhost:7777/docs#
```

### Endpoints
### Part
### 1. GET /part/

Returns a list of parts.

#### Parameters
- None

#### Response
```shell
[
  {
    "_id": "3a9663da-b7c3-4935-8bc7-46c604fd4592",
    "category": "category name",
    "description": "description",
    "location": {
      "bookcase": 5,
      "column": 5,
      "cuvette": 5,
      "room": 5,
      "row": 5,
      "shelf": 5
    },
    "name": "part name",
    "price": 123.45,
    "quantity": 10,
    "serial_number": "1235446371"
  }
]
```
### 2. POST /part/

Creates new part.

#### Parameters
Body:
- name (string, required): The name of the part
- category (string, required): The category of the part
- description (string, required): The description of the part
- location (object, required):
  - bookcase (integer, required)
  - column (integer, required)
  - cuvette (integer, required)
  - room (integer, required)
  - row (integer, required)
  - shelf (integer, required)
- price (float, required): The price of the part
- quantity (integer, required): Quantity of parts available
- serial_number (string, required): The serial number of the part

#### Example
```shell
{
  "category": "category name",
  "description": "description",
  "location": {
    "bookcase": 5,
    "column": 5,
    "cuvette": 5,
    "room": 5,
    "row": 5,
    "shelf": 5
  },
  "name": "part name",
  "price": 123.45,
  "quantity": 10,
  "serial_number": "1235446371"
}
```

#### Response
```shell
{
  "_id": "3a9663da-b7c3-4935-8bc7-46c604fd4592",
  "category": "category name",
  "description": "description",
  "location": {
    "bookcase": 5,
    "column": 5,
    "cuvette": 5,
    "room": 5,
    "row": 5,
    "shelf": 5
  },
  "name": "ssd",
  "price": 123.45,
  "quantity": 10,
  "serial_number": "1235446371"
}
```
### 3. GET /part/{id}

Returns part by id.

#### Paremeters
Path parameter
- id (string, required): The id of part

#### Response
```shell
{
  "_id": "3a9663da-b7c3-4935-8bc7-46c604fd4592",
  "category": "category name",
  "description": "description",
  "location": {
    "bookcase": 5,
    "column": 5,
    "cuvette": 5,
    "room": 5,
    "row": 5,
    "shelf": 5
  },
  "name": "ssd",
  "price": 123.45,
  "quantity": 10,
  "serial_number": "1235446371"
}
```
### 4. PUT /part/{id}

Updates specific part.

#### Paremeters
Path parameter
- id (string, required): The id of part

Body
- name (string, optional): The name of the part
- category (string, optional): The category of the part
- description (string, optional): The description of the part
- location (object, optional):
  - bookcase (integer, required)
  - column (integer, required)
  - cuvette (integer, required)
  - room (integer, required)
  - row (integer, required)
  - shelf (integer, required)
- price (float, optional): The price of the part
- quantity (integer, optional): Quantity of parts available
- serial_number (string, optional): The serial number of the part

#### Response
```shell
{
  "_id": "3a9663da-b7c3-4935-8bc7-46c604fd4592",
  "category": "category name",
  "description": "description",
  "location": {
    "bookcase": 5,
    "column": 5,
    "cuvette": 5,
    "room": 5,
    "row": 5,
    "shelf": 5
  },
  "name": "ssd",
  "price": 123.45,
  "quantity": 10,
  "serial_number": "1235446371"
}
```
### 5. DELETE /part/{id}

Deletes specific part.

#### Parameters
Path parameter
- id (string, required): The id of part

#### Response
```shell
204 No Content
```
### 6. GET /part/search/?{query_param}={value}

Searches part by its fields values. 0 or more parameters can be applied.

#### Parameters
Query parameters
- name (string, optional): The name of the part
- category (string, optional): The category of the part
- description (string, optional): The description of the part
- price (float, optional): The price of the part
- quantity (integer, optional): Quantity of parts available
- serial_number (string, optional): The serial number of the part

#### Response
```shell
[
  {
    "_id": "3a9663da-b7c3-4935-8bc7-46c604fd4592",
    "category": "category name",
    "description": "description",
    "location": {
      "bookcase": 5,
      "column": 5,
      "cuvette": 5,
      "room": 5,
      "row": 5,
      "shelf": 5
    },
    "name": "part name",
    "price": 123.45,
    "quantity": 10,
    "serial_number": "1235446371"
  }
]
```

### Category
### 1. GET /category/

Returns a list of categories.

#### Parameters
- None

#### Response
```shell
[
  {
    "_id": "f8123065-819e-4149-99ee-e1fe53c8e6de",
    "name": "basecat2",
    "parent_name": null
  },
  {
    "_id": "9f669bea-3971-406e-a22d-b4c3d19b1367",
    "name": "home",
    "parent_name": "basecat2"
  }
]
```
### 2. POST /category/

Creates new category.

#### Parameters
Body:
- name (string, required): The name of the category
- parent_name (string, optional): The name of parent category

#### Example
```shell
{
  "name": "category name",
  "parent_name": "parent name"
}
```

#### Response
```shell
{
  "_id": "f8123065-819e-4149-99ee-e1fe53c8e6de",
  "name": "basecat2",
  "parent_name": null
}
```
### 3. GET /category/{id}

Returns category by id.

#### Paremeters
Path parameter
- id (string, required): The id of the category.

#### Response
```shell
{
  "_id": "f8123065-819e-4149-99ee-e1fe53c8e6de",
  "name": "basecat2",
  "parent_name": null
}
```
### 4. PUT /category/{id}

Updates specified category.

#### Paremeters
Path parameter
- id (string, required): The id of the category.

Body:
- name (string, optional): The name of the category
- parent_name (string, optional): The name of parent category

#### Response
```shell
{
  "_id": "f8123065-819e-4149-99ee-e1fe53c8e6de",
  "name": "basecat2",
  "parent_name": null
}
```
### 5. DELETE /category/{id}

Deletes specific category.

#### Parameters
Path parameter
- id (string, required): The id of the category.

#### Response
```shell
204 No Content
```
