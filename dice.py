import random
import time

#Players
class Player():
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def add_score(self,score):
    	self.score = score + 1
    	return score

#start
def start():
	print("Welcome player 1, What's your name?")
	player1_name = input("===> ")
	p1 = Player(player1_name,0)
	tries = 5 
	print(p1.name+"'s","Turn")
	while tries >= 1:
		dice = random.randint(1,6)
		print("\n")
		try:
			p1_choice = int(input("Enter a num between 1 & 6:  "))
		except:
			print("Invalid number! try again")
			p1_choice = int(input("Enter a num between 1 & 6:  "))
		print("ROOLING.....")
		time.sleep(1)
		if p1_choice == dice:
			print("Good job! keep going")
			p1.add_score(p1.score)
			print("Your score so far is:",p1.score)
		else:
			tries -= 1
			print("wrong! try again")
			print("You have",tries,"tries left\n")
	else:
		print("Welcome player 2, What's your name?")
		player2_name = input("===> ")
		p2 = Player(player2_name,0)
		tries = 5 
		print(p2.name+"'s","Turn")
		while tries >= 1:
			dice = random.randint(1,6)
			print("\n")
			try:
				p2_choice = int(input("Enter a num between 1 & 6:  "))
			except:
				print("Invalid number! try again")
				p2_choice = int(input("Enter a num between 1 & 6:  "))
			print("ROOLING.....")
			time.sleep(1)
			if p2_choice == dice:
				print("Good job! keep going")
				p2.add_score(p2.score)
				print("Your score so far is:",p2.score)
			else:
				tries -= 1
				print("wrong! try again")
				print("You have",tries," tries left\n")
		else:
			if p1.score > p2.score:
				winner = p1.name
				print("LOADING RESULTS......")
				time.sleep(0.4)
				print("The winner is:\n")
				time.sleep(0.5)
				print("<><><><><><><>")
				print("   "+p1.name)
				print("<><><><><><><>")
			elif p2.score > p1.score:
				winner = p2.name
				print("LOADING RESULTS......")
				time.sleep(0.4)
				print("The winner is:\n")
				time.sleep(0.5)
				print("<><><><><><><>")
				print("   "+p2.name)
				print("<><><><><><><>")
			else:
				print("LOADING RESULTS......")
				print("<><><>")
				print(" TIE!")
				print("<><><>")
start()