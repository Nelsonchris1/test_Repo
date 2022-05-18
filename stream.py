from pymongo import MongoClient, CursorType
import time
import pymongo
redis_uri='redis://:hostname.redislabs.com@mypassword:12345/0'
# r = redis.StrictRedis(url=redis_uri)

url = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"

print("Starting")
client = MongoClient(url)
oplog = client.local.oplog.rs
# first = oplog.find().sort('$natural', pymongo.ASCENDING).limit(-1).next()
# ts = first['ts']
# {'ts': {'$gt': ts}}
while True:
    cursor = oplog.find({}, cursor_type = CursorType.TAILABLE_AWAIT)
    cursor.add_option(8)
    while cursor.alive:
        for doc in cursor:
            ts = doc['ts']
            # r.set(doc['h'], doc)
            print(doc)

        time.sleep(1)