import random

#welcome message
print("Welcome! Please choose the range of numbers and the number of attempts you want""\n")

#the range the user wants, F means from and T means To
try:
	f = int(input("From: "))
except:
	print("invalid input")
	f = int(input("From: "))
try:
	t = int(input("To: "))
except:
    print("invalid input")
    t = int(input("To: "))

# the allowed attempts the user wants
try:
	att = int(input("How many times you wanna attempt?\n"+'==> '))
except:
	print("invalid input, type a valid number")
	att = int(input("How many times you wanna attempt?\n"+'==> '))
# the user is guessing
try:
	usr_guess = int(input('Guess a number between {} and {}, you have {} attempts. GOOD LUCK!\n==> '.format(f,t,att)))
except:
	print("Invalid input! type a valid number")
	usr_guess = int(input('Guess a number between {} and {}, you have {} attempts. GOOD LUCK!\n==> '.format(f,t,att)))

#score
score = 0

# This loop checks if the gussed num == the random
# the loop will break if the user failed to guess the number after the chosen attempts and it'll add 1 to the score each time the guess is right
while att > 1:
	# generating a random number
	random_num = random.randint(f,t)

	if usr_guess == random_num:
		print("Good job! You Guessed it! you earned 1 XP!")
		score += 1
		try:
			usr_guess = int(input('Guess a number between {} and {}\n==> '.format(f,t)))
		except:
			print("Invalid input! type a valid number")
			usr_guess = int(input('Guess a number between {} and {}\n==> '.format(f,t)))
	else:
		att -= 1
		print('So close! Try {} more time(s), the number was {}'.format(att,random_num))
		try:
			usr_guess = int(input('Guess a number between {} and {}\n==> '.format(f,t)))
		except:
			print("Invalid input! type a valid number")
			usr_guess = int(input('Guess a number between {} and {}\n==> '.format(f,t)))
		random_num = random.randint(f,t)
else:
	if score < 5:
		print("\n")
		print("Game Over! try again!")
		print("You Score is:",score)
	elif score >= 5:
		print("\n")
		print("WOW you did a great job!!")
		print("You Score is:",score)
