age = int(raw_input("What is your age?  "))
name = raw_input("What is your name?  ")
year = 2018 + (100 - age)
print("Hello {}. In {} you'll be 100 years old.".format(name,year))

number = int(raw_input("Give me a number:  "))
if number % 2 == 0:
	print("The number is even!")
else:
	print("The number is odd!")