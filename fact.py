import os
import random

def clear():
    if os.name == 'nt':
    	os.system('cls')
    else:
        os.system('clear')
clear()

prefixes = 'JKLMNOPQ'
suffix = 'ack'
index = 0
for item in prefixes:
	if prefixes[index] == 'O':
		print item + "u" + suffix
	else:
		print item + suffix
	index += 1

print "\n"

def count(letter, word):
	# count = 0
	# for item in word:
	# 	if item == letter:
	# 		count += 1
	count = word.count(letter)
	print "The letter {} is in your string for {} times.".format(letter,count)

count("5","55kj5")

def polindrom(word1,word2):
	if word1[:] == word2[::-1]:
		# return True
		print "good"
	else:
		print "nope"

polindrom("noot","noon")