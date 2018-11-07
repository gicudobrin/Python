print("This program will check how many times a letter is in a word!")
word = raw_input("Type a word: ")
letter = raw_input("Type a letter: ")
count = 0
for item in word:
	if item == letter:
		count += 1
print("The letter {} is in your word for {} times.".format(letter,count))