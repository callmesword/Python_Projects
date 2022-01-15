import json

database = open("data_base.json", "r")
data = json.load(database)

def update_database(data, filename="data_base.json"):
	with open(filename, 'r+') as file:
		js_load = json.load(file)
		file.seek(0)
		js_load["users"].append(data)
		json.dump(js_load, file, indent = 4)

def  check_data(database, user):
	for data in database["users"]:
		for usr in data.keys():
			if usr == user:
				return True

def check_password(data, username, password):
	for ls in data["users"]:
		for user,pin in ls.items():
			if user == username and password == pin:
				return True

def signup():
	data = {}
	username = input("ENTER YOUR USERNAME: ")
	password = input("ENTER A PASSWORD: ")
	if username not in data:
		data[username] = password
		update_database(data)

def authenticate(data):
	username = input("USERNAME: ")
	if check_data(data,username):
		password = input("PASSWORD: ")
		if check_password(data, username, password):
			print(" <<ACCESS GRANTED !>>")
		else:
			print("<<INCORRECT PASSWORD. ACCESS DENIED !>>")
	else:
		print("USER NOT FOUND ! WOULD YOU LIKE TO SIGNUP?")
		user_choice = input("Y/N: ")
		if user_choice == 'y' or user_choice == 'Y':
			signup()
		else:
			print("ENTER YOUR USERNAME AND PASSWORD TO LOGIN !")
			authenticate(data)

authenticate(data)
