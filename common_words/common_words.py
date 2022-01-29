import string
punc = string.punctuation

def common_word(dictt):
	common = []
	for element in dictt:
		if dictt[element] > 1:
			common.append(element)
	#return common
	for word in common:
		if word != '':
			print(word)


with open("file.txt") as txt:
	txt = txt.readlines()
	words_dict = {}
	for sentence in txt:
		for word in sentence.split(" "):
			word = word.rstrip("\n" + punc)
			if word not in words_dict:
				words_dict[word] = 1
			else:
				words_dict[word] += 1

print("These words appeared more than once:\n")
print("----------------")
common_word(words_dict)
print("----------------")
