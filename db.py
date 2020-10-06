import pymongo

myclient = pymongo.MongoClient("mongodb+srv://test:test@cluster0.kw4id.mongodb.net/mydatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["db"]


mylist = [
  { "Account_name": "Amarr", "Datetime_creation": "12-03-2020"},
  { "Acoount_name": "Garagedoor", "Datetime_creation": "15-03-2020"},
  { "Account_name": "Automationdoor", "Datetime_creation": "25-03-2020"},
  { "Account_name": "Nexus", "Datetime_creation": "05-04-2020"},
  { "Account_name": "Amazon", "Datetime_creation": "10-04-2020"},
]


x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
