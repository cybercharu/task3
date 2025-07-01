import pymongo 

#connecting with mongodb
print("Welcome to Pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db= client['electric_power_consumption']
collection=db['individual_household']

# creating new collection : timeseries_collection
if "timeseries_collection" not in db.list_collection_names():
    db.create_collection(
        "timeseries_collection",
        timeseries={
            "timeField": "timestamp",
            "granularity": "minutes"
        }
    )
if "cleaned_data" not in db.list_collection_names():
    db.create_collection(
        "cleaned_data")
