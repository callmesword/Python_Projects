import sys
import random
import time
import getpass
import pyfiglet


#Guess
guess = ["even","odd"]

#animated loading
def loading(n,message):
	print(message)
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
	for i in range(len(animation)):
		time.sleep(n)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()

	print("\n")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#encrypt player input. usesful for mode 2.
def enc_input(inp):
	input_saved = int(getpass.getpass(inp))
	return input_saved

#console effect
def console_effect(txt):
	result = pyfiglet.figlet_format(txt)
	print(result)

#Even or odd
def check_odd_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

def winner(pl_name):
	name = str(pl_name).upper()
	console_effect("THE WINNER")
	time.sleep(0.5)
	console_effect("IS")
	time.sleep(0.5)	
	console_effect(name)

def print_menu(file_name):
	print("\n"*100)
	#reads the text from mode_1_menu.txt
	file = open(file_name,'r')
	with file as reader:
		line = reader.readline()
		while line != '':
			print(line, end='')
			line = reader.readline()
		print("\n")


#Player class to store info
class Player:
	def __init__(self,name):
		self.name = name

#first Message
console_effect("WELCOME")
time.sleep(0.5)
console_effect("TO")
time.sleep(0.5)
console_effect("MARBELS")
time.sleep(1)

#Welcome
def welcome():
	print_menu("welcome.txt")
	
	print("\n         >>>>> TYPE '1' FOR MODE 1 OR '2' FOR MODE 2 <<<<<")
	print("           >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
	mode = input("\n==> ")
	while mode != '1' and mode != '2':
		print("\n         >>>>> TYPE '1' FOR MODE 1 OR '2' FOR MODE 2 <<<<<")
		print("           >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<")
		mode = input("\n==> ")
	else:
		if mode == '1':
			mode_1_menu()
		elif mode == '2':
			mode_2_menu()

#mode 1 menu
def mode_1_menu():
	print_menu("mode_1_menu.txt")
	
	print("\n            >>>>> TYPE '1' TO START OR '0' TO GO BACK TO THE MENU <<<<<")
	print("              >>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	
	menu = int(input("==> "))
	if menu == 1:
		loading(0.1,"LOADING MODE 1...")
		mode_1()
	elif menu == 0:
		loading(0.1,"LOADING MENU...")
		welcome()

#mode 1
def mode_1():
	pl = 10
	com = 10
	while pl <= 20 and com <= 20 and pl > 0 and com > 0:
		print("\n            >>>>>   HIDE YOUR MARBS !  <<<<<")
		print("              >>>>>>>>>>>>><<<<<<<<<<<<<<<")
		pl_marbs = int(input("==> "))
		if pl_marbs <= pl:
			loading(0.1,"COMPUTER IS GUESSING...")
			
			com_marbs = random.randint(1,10)
			com_guess = random.choice(guess)
			
			#if the computer is right
			if check_odd_even(pl_marbs) == True and com_guess == "even" or check_odd_even(pl_marbs) == False and com_guess == "odd":
				if com_marbs >= pl_marbs:
					com = com + pl_marbs
					pl -= pl_marbs
				elif com_marbs < pl_marbs:
					com = com + com_marbs
					pl -= com_marbs
			
				print("\n            >>>>> COMPUTER IS RIGHT ! <<<<<")
				print("              >>>>>>>>>>>>>>>><<<<<<<<<<<")
				print("\nCOMPUTER HID {} MARBELS.".format(com_marbs))
				print("\nYOU: {} marbles left | COMPUTER: {} marbles left.".format(pl,com))
			
			#if the player is right
			elif check_odd_even(pl_marbs) == True and com_guess == 'odd' or check_odd_even(pl_marbs) == False and com_guess == 'even':
				if pl_marbs >= com_marbs:
					pl += com_marbs
					com -= com_marbs
				elif pl_marbs < com_marbs:
					pl = pl + pl_marbs
					com -= pl_marbs
			
				print("\n            >>>>> COMPUTER IS WRONG ! <<<<<")
				print("              >>>>>>>>>>>>>>>><<<<<<<<<<<")
				print("COMPUTER HID {} MARBLES.".format(com_marbs))
				print("\nYOU: {} marbles left | COMPUTER: {} marbles left.".format(pl,com))
		else:
			print("YOU DON'T HAVE {}. CHOOSE AN AMOUNT LESS OR EQAUL TO {}.".format(pl_marbs,pl))
			continue

	else:
		console_effect("\n> GAME OVER <")
		loading(0.2,"LOADING RESULTS....")
		if pl >= 20 or com <= 0:
			console_effect("> YOU WIN <")
		else:
			console_effect("> YOU LOST <")

#Mode 2 menu
def mode_2_menu():
	print_menu("mode_2_menu.txt")

	print("\n            >>>>> TYPE '1' TO START OR '0' TO GO BACK TO THE MENU <<<<<")
	print("              >>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	menu = input("==> ")
	
	while menu != '1' and menu != '0':
		print("\n            >>>>> TYPE '1' TO START OR '0' TO GO BACK TO THE MENU <<<<<")
		print("              >>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
		menu = input("==> ")

	else:
		if menu == '1':
			loading(0.1,"LOADING MODE 2...")
			mode_2()
		elif menu == '0':
			loading(0.1,"LOADING MENU...")
			welcome()

#mode_2
def mode_2():
	p1_name = input("Player 1, Enter your name : ")
	print(">>>>>>>>>><<<<<<<<<<<<<")
	p2_name = input("Player 2, Enter your name : ")
	print(">>>>>>>>>><<<<<<<<<<<<<\n")

	pl1_marbs = 10
	pl2_marbs = 10

	p1_win = 0
	p2_win = 0

	p1_turn = False
	p2_turn = False

	while p2_turn == False and p1_win == 0 and p2_win == 0:
		p1 = enc_input("PLAYER 1, HIDE YOUR MARBS:  ")
		print(">>>>>>>>>><<<<<<<<<<<<<")
		p2 = enc_input("PLAYER 2, HIDE YOUR MARBS:  ")
		print(">>>>>>>>>><<<<<<<<<<<<<\n")
		
		p2_guess = input("PLAYER 2 IT'S YOUR TURN TO GUESS: ")

		print("PLAYER 1 HID {} >< PLAYER 2 HID {}".format(p1,p2))
		print("-------------------------------")
		
		if p2_guess == 'e' or p2_guess == 'E':
			print("PLAYER 2 GUESS: EVEN")
			print("+------------------+")
		elif p2_guess == 'o' or p2_guess == 'O':
			print("PLAYER 2 GUESS: ODD")
			print("+------------------+")
		
		#if player 2 is right
		if check_odd_even(p1) == True and p2_guess == 'e' or p2_guess == 'E' or check_odd_even(p1) == False and p2_guess == 'o' or p2_guess == 'O':
			print("PLAYER 2 IS RIGHT !")
			print(">>>>>>>>><<<<<<<<<<")
			if p2 <= p1:
				pl2_marbs += p1
				pl1_marbs -= p1
			elif p2 > p1:
				pl2_marbs += p1
				pl1_marbs -= p1
		#if player 2 is wrong
		else:
			print("PLAYER 2 IS WRONG !")
			print(">>>>>>>>><<<<<<<<<<")
			if p2 <= p1:
				pl2_marbs -= p2
				pl1_marbs += p2
			elif p2 > p1:
				pl2_marbs -= p1
				pl1_marbs += p1
		
		print("\nPLAYER 1: {}  <<<>>>  PLAYER 2: {}".format(pl1_marbs,pl2_marbs))

		if pl1_marbs >= 20 or pl2_marbs <= 0:
			p1_win = 1
			p2_turn = False
			console_effect("> GAME OVER <\n")
			winner(p1_name)
			break
		elif pl2_marbs >= 20 or pl1_marbs <= 0:
			p2_win = 1
			p1_turn = False
			console_effect("> GAME OVER <\n")
			winner(p2_name)
			break
		elif pl1_marbs == 20:
			p1_win = 1
			p2_turn = False
			console_effect("> GAME OVER <\n")
			winner(pl_1)
			break
		elif pl2_marbs == 20:
			p2_win = 1
			p1_turn = False
			console_effect("> GAME OVER <\n")
			winner(pl_2)
			break
		
		p2_turn = True

		while p2_turn == True and p1_win == 0 and p2_win == 0:
			p1 = enc_input("PLAYER 1, HIDE YOUR MARBS:  ")
			print(">>>>>>>>>><<<<<<<<<<<<<")
			p2 = enc_input("PLAYER 2, HIDE YOUR MARBS:  ")
			print(">>>>>>>>>><<<<<<<<<<<<<\n")
			p1_guess = input("PLAYER 1 IT'S YOUR TURN TO GUESS: ")

			print("PLAYER 1 HID {} >< PLAYER 2 HID {}".format(p1,p2))
			print("+-----------------------------+")
			
			if p1_guess == 'e' or p1_guess == 'E':
				print("PLAYER 1 GUESS: EVEN")
				print("+------------------+")
			elif p1_guess == 'o' or p1_guess == 'O':
				print("PLAYER 1 GUESS: ODD")
				print("+------------------+")

			#if player 1 is right
			if check_odd_even(p2) == True and p1_guess == 'e' or p1_guess == 'E' or check_odd_even(p2) == False and p1_guess == 'o' or p1_guess == 'O':
				print("PLAYER 1 IS RIGHT !")
				print(">>>>>>>>><<<<<<<<<<")
				if p1 <= p2:
					pl1_marbs += p1
					pl2_marbs -= p1
				elif p1 > p2:
					pl1_marbs += p2
					pl2_marbs -= p2
			#if player 1 is wrong
			else:
				print("PLAYER 1 IS WRONG !")
				print(">>>>>>>>><<<<<<<<<<")
				if p1 <= p2:
					pl1_marbs -= p1
					pl2_marbs += p1
				elif p1 > p2:
					pl1_marbs -= p1
					pl2_marbs += p2
			
			print("\nplayer 1: {}  <<<>>>  player 2: {}".format(pl1_marbs,pl2_marbs))
			
			p2_turn = False
			p1_turn = True

		else:
			if pl1_marbs >= 20 or pl2_marbs <= 0:
				p1_win = 1
				p2_turn = False
				console_effect("> GAME OVER <\n")
				winner(p1_name)
				break
			elif pl2_marbs >= 20 or pl1_marbs <= 0:
				p2_win = 1
				p1_turn = False
				console_effect("> GAME OVER <\n")
				winner(p2_name)
				break
			elif pl1_marbs == 20:
				pl1_win = 1
				p2_turn = False
				console_effect("> GAME OVER <\n")
				winner(pl_1)
				break
			elif pl2_marbs == 20:
				p2_win = 1
				p1_turn = False
				onsole_effect("> GAME OVER <\n")
				winner(pl_2)
				break

welcome()