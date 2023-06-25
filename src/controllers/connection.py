from var.vars import *
from pymongo  import MongoClient

"""
Create a connection with mongo db and creates / establish a connection
with a database given
"""

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]