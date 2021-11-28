from pymongo import MongoClient
from pprint import pprint

sandbox = MongoClient('mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = sandbox.gym

customers = db.customers.find()

lista_customers = []

for item in customers:
    lista_customers.append(item)

print(lista_customers[0])