for name in ['Bob', 'Emily', 'Jane']:
	print("Hello " + name)

print(" ")

for letter in "abcdefghijklmnopqrstuvwxyz":
	print(letter.upper())

print(" ")

for num in [1, 2, 3, 4]:
	if num % 2 == 0:
		print(num)
	
print(" ")

start = 10
while start:
	print(start)
	start -= 1


print(" ")

names = ['ana', 'dana', 'ioana', 'QUIT', 'diana']
for name in names:
	if name == 'QUIT':
		break
	print(name)



print(" ")


for name in names:
	if name == 'QUIT':
		continue
		print(name)
	else:
		print("My name is {}.".format(names[0]))

print(" ")

age = input("Wat's your age?\n")
print(age)

