 # 	Lists are great but sometimes you want to be sure your data is safe and unchangeable. 
	# Python gives us tuples for exactly this use (and a lot more).

 # 	I didn't mention it in the video because it should be an assumption by now, 
	# but you can use del to delete an entire tuple. You cannot delete just a single item from the tuple, 
	# though, of course, since tuples are immutable.

my_tuple = (1,2,3)
print(my_tuple)
my_pop = tuple([1,2,3])
print(my_pop)


string = "abcdefgh"
stringt = string[::-2]
print(stringt)

a = 5
b = 20

a, b = b, a

print(a,b)

c = b, a

print(c)

print("\n")

for index, letter in enumerate("abcdefghijklmnopqrstuvxyz"):
	print("{}: {}".format(index + 1, letter))


print("\n")

count = 1
for item in "abcdefghijklmnopqrstuvxyz":
	print("{}: {}".format(count, item))
	count += 1

def stringcases(my_string):
	return (my_string.upper(), my_string.lower(), my_string.title(), my_string[::-1])

print(stringcases("ce mai faci tu mai bubulina?"))

