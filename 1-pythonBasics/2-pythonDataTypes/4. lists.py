my_list = [1,2,3]
print(my_list)

my_list + [4,5,6]


my_list += [4,5,6]
print(my_list)

# append lets us add another item to our list - single item
my_list.append(7)
print(my_list )
my_list.append([8,9])
print(my_list)

# if we want to add multiple items we can use extend

my_list.extend([10,11,12])

print(my_list)

my_list.remove([8,9])
print(my_list)

# ValueError

colors = ["a","b","c","d","e"]

states = [
    'ACTIVE',
    ['red', 'green', 'blue'],
    'CANCELLED',
    'FINISHED',
    5,
]

states.remove(5)

print(states)

states.remove(['red', 'green', 'blue'])

print(states)

# splitting and joining

# iterable means can be looped through
# ints are not iterable
# strings and lists are iterable

print('hello'.split()) # transform a string into a list

print("red:blue:green".split(":"))

flavors = ['chocolate','mint','strawberry']
print(', '.join(flavors)) # transform a list in a string

print("My favorite flavors are: " + ', '.join(flavors))

print("             ")
print("             ")
print("My favorite flavors are: {}".format(", ".join(flavors)))

# we can only join string items

available = "banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(";")
print(sundaes)

menu = ("Our available flavors are: {}." ).format(", ".join(sundaes))
print(menu)

# index

# a  p  p  l  e
# 0  1  2  3  4
#-5 -4 -3 -2 -1

print(" ")

alpha = "abcde"
print(alpha.index('a'))

alpha_list = list(alpha)
print(alpha_list)
print(alpha_list.index('b'))

print(alpha[0])

var_one = list("abcdet")
print(var_one)
var_two = list("aed")

trash = 99
print(trash)
# del trash
# print(trash)

alpha_list = list(alpha)
del alpha_list[2] # we can delete one single item at once

messy = [5, 2, 8, 1, 3]
del messy[2]
print(messy)
del messy[1]