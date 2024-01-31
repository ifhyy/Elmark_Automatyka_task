from pymongo import MongoClient
import os
from dotenv import dotenv_values


basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config = dotenv_values(os.path.join(basedir, '.env'))
client = MongoClient(config["MONGODB_URI"])

db = client[config["DB_NAME"]]
