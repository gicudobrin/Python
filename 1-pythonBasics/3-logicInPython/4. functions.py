# Example of a function:
# def function_name(argument):

import os
import random

def hows_the_parrot():
	print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name):
	if name.lower() == 'kenneth':
		print("Kenneth's a lumberjack and he's OK!")
	else:
		print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Kenneth")
lumberjack("ANA")

def average(num1,num2):
	return (num1*num2)/2
avg = average(23,46)
print(avg)

def printer(count):
    print("Hi " * count)
printer(10)

def palindrom(word1,word2):
	if word1[:] == word2[::-1]:
		# return True
		print "good"
	else:
		print "nope"

polindrom("noot","noon")

def count(letter, word):
	# count = 0
	# for item in word:
	# 	if item == letter:
	# 		count += 1
	count = word.count(letter)
	print "The letter {} is in your string for {} times.".format(letter,count)

count("5","55kj5")

def greetPerson(*name):
	print('Hello', name)

greetPerson('Frodo', 'Sauron')

# def clear():
# 	if os.name == 'nt':
# 		os.system('cls') 
# 	else:
# 		os.system('clear')

# clear()

numbers = [23,45,34,23,78]
print numbers
for i in [0,1,2,3,4]:
	numbers[i] = numbers[i] * 2

print numbers

prefixes = 'JKLMNOPQ'
suffix = 'ack'
index = 0
for item in prefixes:
	if prefixes[index] == 'O':
		print item + "u" + suffix
	else:
		print item + suffix
	index += 1