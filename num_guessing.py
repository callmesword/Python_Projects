import random

#the range the user wants, F means from and T means To
f = int(input("From: "))
t = int(input("To: "))

# stores the random num
random_num = random.randint(f,t)

# the allowed attempts the user wants
att = int(input("How many times you wanna attempt? : "))

# the user is guessing
usr_guess = int(input('Guess a number between {} and {}: '.format(f,t)))


# This loop checks if the gussed num == the random
# the loop will break if the user failed to guess the number after 3 attempts

while att > 1:
	
	if usr_guess == random_num:
		print("Good job! You Guessed it!")
		break
	else:
		att -= 1
		print('So close! Try {} more time(s)'.format(att))
		usr_guess = int(input('Guess a number between {} and {}: '.format(f,t)))
	
else:
	print("GAME OVER!")
