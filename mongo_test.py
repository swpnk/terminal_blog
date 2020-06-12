__author__ = 'Swapnik'

import pymongo
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['test']
collection = database['students']

students = [student for student in collection.find({})]
print(students)
