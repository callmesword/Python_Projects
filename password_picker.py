import string
import random

#opening files that contains adjectives and nouns and setting them as lists
with open("adj.txt") as adjs_file, open("nouns.txt") as nouns_file:
	adjs = []
	nouns = []

	for adj in adjs_file.readlines():
		adjs.append(adj.strip())
		for noun in nouns_file.readlines():
			nouns.append(noun.strip())

def password():
	#random adjective
	rand_adj = random.choice(adjs)
	#random noun
	rand_noun = random.choice(nouns)
	#random number
	num = random.choice(string.digits)
	#random punctuation
	punc = random.choice(string.punctuation)
	return rand_adj+rand_noun+num+num+punc+punc

#output message
print("welcome to 'Pick me a strong password' program")
print("###############################################")
print("Type 'pass' to generate a password and 'exit' to exit the program")
print("###############################################")

user = str(input("==> "))
while user != 'exit':
	if user == 'pass':
		print("your password is:",string.capwords(password()))
		user = str(input("==> "))
else:
	if user == 'exit':
		print("Thanks for using the program")

adjs_file.close()
nouns_file.close()