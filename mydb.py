from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	#con = MongoClient('mongodb://superadmin:masterkey1029384756@ds335668.mlab.com:35668/nexus?retryWrites=false')
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/mydatabase?retryWrites=true&w=majority')
	db = con.mydatabase
	col = db.db

"""	
def col_survey():
	global col
	connect_db()
	data_from_db = col.find({})
	return data_from_db
"""



def get_db():
	global col
	connect_db()
	data_from_db = col.find({})
	return data_from_db


"""
def save_customer(data):
	global col
	connect_db()
	col.insert(data)
	return 

"""

def save_userdata(data):
	global col
	connect_db()
	col.insert(data)
	return 