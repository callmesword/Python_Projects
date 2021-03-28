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
	print("+------------------------------------+")
	print("| Welcome player 1, What's your name?|")
	print("+------------------------------------+")
	
	player1_name = input("===> ")
	p1 = Player(player1_name,0)
	
	tries = 5 
	
	print(p1.name+"'s","Turn")
	
	while tries >= 1:
		dice = random.randint(1,6)
		try:
			p1_choice = int(input("Enter a num between 1 & 6:  "))
		except(ValueError):
			print("+--------------------+")
			print("| Type Only numbers! | ")
			print("+--------------------+")
			p1_choice = int(input("Enter a num between 1 & 6:  "))
		if p1_choice in range(1,7):
			print("ROOLING.....")
			time.sleep(0.5)
			if p1_choice == dice:
				print("+----------------------+")
				print("| Good job! keep going |")
				print("+----------------------+")
				p1.add_score(p1.score)
				print("+-------------------------+")
				print("| Your score so far is: {}|".format(p1.score))
				print("+-------------------------+")
			else:
				tries -= 1
				print("+------------------+")
				print("| wrong! try again |")
				print("+------------------+")
				print("You have",tries,"tries left\n")
		else:
			print("+----------------------+")
			print("| Number out of range! |")
			print("+----------------------+")

	else:
		print("Welcome player 2, What's your name?")
		player2_name = input("===> ")
		p2 = Player(player2_name,0)
		
		tries = 5 
		print(p2.name+"'s","Turn")
		
		while tries >= 1:
			dice = random.randint(1,6)
			try:
				p2_choice = int(input("Enter a num between 1 & 6:  "))
			except(ValueError):
				print("+--------------------+")
				print("| Type Only numbers! | ")
				print("+--------------------+")
				p2_choice = int(input("Enter a num between 1 & 6:  "))
			if p2_choice in range(1,7):
				print("ROOLING.....")
				time.sleep(0.5)
				if p2_choice == dice:
					print("+----------------------+")
					print("| Good job! keep going |")
					print("+----------------------+")
					p2.add_score(p2.score)
					print("+-------------------------+")
					print("| Your score so far is: {} |".format(p2.score))
					print("+-------------------------+")
				else:
					tries -= 1
					print("+------------------+")
					print("| wrong! try again |")
					print("+------------------+")
					print("You have",tries,"tries left\n")
			else:
				print("+----------------------+")
				print("| Number out of range! |")
				print("+----------------------+")
		else:
			if p1.score > p2.score:
				winner = p1.name
				print("LOADING RESULTS......")
				time.sleep(1)
				print(p1.name+"'s score is:",p1.score)
				time.sleep(1)
				print(p2.name+"'s score is:",p2.score)
				print("The winner is:\n")
				time.sleep(1)
				print("+-----------+")
				print('|',winner,'|')
				print("+-----------+")
			elif p2.score > p1.score:
				winner = p2.name
				print("LOADING RESULTS......")
				print(p1.name+"'s score is:",p1.score)
				time.sleep(1)
				print(p2.name+"'s score is:",p2.score)
				time.sleep(1)
				print("The winner is:\n")
				time.sleep(1)
				print("+-----------+")
				print('|',winner,'|')
				print("+-----------+")
			else:
				print("<><><><><><><><><><><><>")
				print("LOADING RESULTS......")
				time.sleep(1)
				print(p1.name+"'s score is:",p1.score)
				time.sleep(1)
				print(p2.name+"'s score is:",p2.score)
				time.sleep(1)
				print("+------+")
				print("| TIE! |")
				print("+------+")
start()
