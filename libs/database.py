import pymongo
import os
from bson import json_util
import json


#MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = 'mongodb://root:IflsMF01@ds211504.mlab.com:11504/code-institute-data-centric'
DBS_NAME = "code-institute-data-centric"
COLLECTION_NAME = "recipeDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

def find():
    cursor = coll.find()
    recipes = json.loads(json_util.dumps(cursor))
    return recipes

def findOne(fltr):
    result = coll.find_one(fltr)
    recipe = json.loads(json_util.dumps(result))
    return recipe

def insert(doc):
    result = coll.insert_one(doc)
    return result

def updateOne(fltr, updte):
    result = coll.update_one(fltr, updte)
    return result
    
def deleteOne(fltr):
    result = coll.delete_one(fltr)
    return result