list = [1,2,3]
print(list)

list + [4,5,6]


list += [4,5,6]
print(list)

# append lets us add another item to our list - single item
list.append(7)
print(list )
list.append([8,9])
print(list)

# if we want to add multiple items we can use extend

list.extend([10,11,12])

print(list)

list.remove([8,9])
print(list)

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