from pymongo import MongoClient

conn = MongoClient(host='mongo', port=27017)
db = conn.local