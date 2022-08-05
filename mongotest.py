import pymongo
client = pymongo.MongoClient("mongodb+srv://ankurkr12:ankurwavey.2@ankurkr12.mievg0m.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"shudhanshu",
    "email" : "shudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )