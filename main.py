from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import part_router, category_router

config = dotenv_values(".env")

app = FastAPI()

# Send a ping to confirm a successful connection
client = MongoClient(config['MONGODB_URI'])
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app.include_router(part_router, prefix="/part", tags=["parts"])
app.include_router(category_router, prefix="/category", tags=["categories"])
