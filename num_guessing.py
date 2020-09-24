import random

#Welcome message
print('Welcome! Please enter the range of nums you want and number of attempts')

#the range the user wants/ 'F' means from, 'T' means to
f = int(input('From: '))
t = int(input('To: '))

# stores the random num
random_num = random.randint(f,t)

# the allowed attempts 
attempts = int(input("Select number of attempts you want (MAX 10): "))

# the user is guessing
usr_guess = int(input('Guess a number between {} and {}: '.format(f,t)))

# This loop checks if the gussed num == the random
# the loop will break if the user failed to guess the number after 3 attempts
while attempts > 1:
    
    if usr_guess == random_num:
        print("Good job! You Guessed it!")
        break
    else:
        attempts -= 1
        print('So close! Try {} more time(s)'.format(attempts))
        usr_guess = int(input('Guess a number between 1 and 20: '))
    
else:
    print("GAME OVER! Try again")

	



