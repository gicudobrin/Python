import os
#import random


def clear():
	if os.name == 'nt':
		os.system('cls') 
	else:
		os.system('clear')

clear()

numbers = [23,45,34,23,78]
print numbers
for i in [0,1,2,3,4]:
	numbers[i] = numbers[i] * 2

print numbers