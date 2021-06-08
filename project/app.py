from postgres import sqlalchemy_connect_and_query
from pymongo import MongoClient


def mongo_connect_and_query():
    client = MongoClient(
        "mongodb://root:1234@mongo:27017/project?authSource=admin"
    )
    db = client.project
    user_collection = db.user

    result = user_collection.find()
    for row in result:
        print(row)

    client.close()


sqlalchemy_connect_and_query()
# mongo_connect_and_query()
