def count(letter, word):
	counter = word.count(letter)
	print("The letter {} is in your word for {} times.".format(letter,counter))

count('a', 'Cacat')