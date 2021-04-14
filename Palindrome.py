import time

#function to check if the word is palindrome
def palindrome(text):
	current_text = text
	reversed_text = current_text[::-1]
	if current_text == reversed_text:
		return True
	else:
		return False

# a list that contains the inputed words by the user
words_inputed = []
#word counter
words = 5
#a loop that checks if the user inputed 5 words
while words >= 1:
	user = input("Enter 5 words: ")
	words_inputed.append(user)
	words -= 1
#lists that contains the palindrome words and non_palindrome words
palindrome_words = []
non_plaindrome_words = []

for word in words_inputed:
	if palindrome(word) == True:
		palindrome_words.append(word)
	else:
		non_plaindrome_words.append(word)

#output
time.sleep(1)
print("You inputed {} palindrome word(s) and {} non palindrome word(s)".format(len(palindrome_words),len(non_plaindrome_words)))
print("+------------------------------------------------------------+\n")
print("Palindrome words:",palindrome_words)
print("non_plaindrome_words:",non_plaindrome_words)
