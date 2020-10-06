from flask import Flask, render_template, redirect, request, session, g, flash, url_for

import datetime
import sys
import random
import time

import json
import requests

import mydb

#This is how you tell python that this is a flask application
app = Flask(__name__)

#GCP( Good Coding Practice)
app.secret_key = "siddharth"

#python is an indented language
#python uses indentation to indicate a block of code belonging to certain function or for, if, etc..

@app.route("/")
def index():
	name = "priyanka sid sundar"
	#global usernames
	cursor = mydb.get_db()
	userinfolist = []
	for d in cursor:
		userinfolist.append(d)
	return render_template('base.html', user=name, userlist =userinfolist)


@app.route("/", methods=['POST'])
def updatedb():
	name = request.form['username']
	print (name) 
	global usernames
	usernames.append(name)
	return redirect(url_for('index'))
"""
def generate_test_data():
	dt = datetime.datetime(2010, 12, 1)
	end = datetime.datetime(2010, 12, 30, 23, 59, 59)
	step = datetime.timedelta(days=4)
	result = []
	user_list = []
	user_date_map = {}
	user_id = 5
	while dt < end:
		date = dt.strftime('%Y-%m-%d')
		result.append(date)
		user_list.append(user_id)
		user_date_map[str(user_id)] = date
		mydb.save_userdata(user_date_map)
		user_date_map = {} 
		dt += step
		user_id = user_id+7
	print (result)
	print (user_list)
	print (user_date_map)

	return 
"""

if __name__=="__main__":
	app.debug = True
	app.run()