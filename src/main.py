from fastapi import FastAPI
from src.routes import part_router, category_router
from src.database import client

app = FastAPI()

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app.include_router(part_router, prefix="/part", tags=["parts"])
app.include_router(category_router, prefix="/category", tags=["categories"])
