import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client.books5
books = db.bklist
# doc = {"field":"value"}
# books.insert_one(doc)
for item in books.find():
    obj = {}
    obj["book name"] = books["field"]
    print(obj["book name"])