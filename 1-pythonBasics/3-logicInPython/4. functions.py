# Example of a function:
# def function_name(argument):

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