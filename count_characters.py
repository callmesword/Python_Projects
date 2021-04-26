import string

def count_all(txt):
	char_count = 0
	for char in txt:
		char_count += 1
	return char_count

def count_lower(txt):
	lower_count = 0
	lower_chars = string.ascii_lowercase
	for char in txt:
		if char in lower_chars:
			lower_count += 1
	return lower_count

def count_upper(txt):
	upper_count = 0
	upper_chars = string.ascii_uppercase
	for char in txt:
		if char in upper_chars:
			upper_count += 1
	return upper_count

def count_punc(txt):
	punc_count = 0
	punc_chars = string.punctuation
	for char in txt:
		if char in punc_chars:
			punc_count += 1
	return punc_count

def count_spaces(txt):
	space_count = 0
	for char in txt:
		if char == " ":
			space_count += 1
	return space_count


txt = "Hello World !"

print("This string has {} characters in total:\n- {} uppercase\n- {} lowercase\n- {} punctuations\n- {} spaces".format(count_all(txt),count_upper(txt),count_lower(txt),count_punc(txt),count_spaces(txt)))
