from random import randint

print("Welcome! choose an option and play against the computer","\n""if you want to quit the game type 'exit' GOOD LUCK!!")

actions_lst = ["Rock","Paper","Scissors"]

computer = actions_lst[randint(0,2)]

player = False

while player == False:
	player = input("Rock, Paper, Scissors?: ")
	if player == computer:
		print("Tie")
	elif player == "Rock":
		if computer == "Paper":
			print("You lose.....,!",computer,"covers",player)
		else:
			print("You win.....,!",player,"Smashes",computer)
	elif player == "Paper":
		if computer == "Rock":
			print("You Win!.....,",player,"Covers",computer)
		else:
			print("You lose!.....,",computer,"Cut",player)
	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!.....,",computer,"Smashes",player)
		else:
			print("You win!.....",player,"cut",computer)
	else:
		if player == "exit":
			break
		else:
			print("Invalid input! Try again")
	player = False
	actions_lst[randint(0,2)]

