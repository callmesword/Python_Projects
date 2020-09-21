import random
# a function to compute the difference between the guessed num and the random num
def diff(usr_inp,random_num):
    return random_num - usr_inp
# stores the random num
random_num = random.randint(1,2)
# the user is guessing
usr_guess = int(input('Guess a number between 1 and 100: '))
# the allowed attempts 
attempts = 3

diff = diff(random_num,usr_guess)
# This loop checks if the gussed num == the random
# the loop will break if the user failed to guess the number after 3 attempts
while attempts > 1:
    
    if usr_guess == random_num:
        print("Good job! You Guessed it!")
        break
    elif diff < 10:
        attempts -= 1
        print('So close! Try {} more time(s)'.format(attempts))
        usr_guess = int(input('Guess a number between 1 and 100: '))
    
else:
    print("GAME OVER!")


		

	



