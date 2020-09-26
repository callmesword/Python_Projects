    
import random
 
# Open the Mad Libs text file
f = open('madlibs.txt','r')
 
# Read the whole file and store each line in a list
madlibText = f.readlines()
 
# Choose a random line from the list
madlib = random.choice(madlibText)
 
# Ask the user to input a noun
noun = input("Enter a noun: ")
 
# Replace the blank with the user's input
madlib = madlib.replace("blank", noun)
 
# Print out the Mad Lib including the user's response
print(madlib)