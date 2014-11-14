

import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()

db = client.test_database

collection = db.test_collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert(post)
print post_id

db.collection_names()

posts.find_one()

#client = MongoClient('mongodb://localhost:27017/')

#db = pymongo.Connection('localhost', 27017).game
#u_id = db.users.find_one({'username' : "test"})['_id']

#ship = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
#engine = db.player_items.find_one({'u_id' : u_id, 'object' : "Engine", 'p_id': ship['_id']})

#x_min = db.universe.find().sort("x_pos" , 1).limit(1)

