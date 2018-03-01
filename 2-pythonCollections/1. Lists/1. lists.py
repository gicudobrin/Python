# collections or containers: list, string,

# I'm sure you remember, but just to refresh:

# Lists are mutable, which means they can be changed in place
# Lists have an order, something comes first, second, etc
# List items can be accessed by their index using bracket notation[]
# You can make a list with [] literals or by using the list() function

# There's more than one way to add things to your lists! Let's look at `.extend()`, `.append()`, and `.insert()`.

# Methods used

# .append(<value>) - Add a new value onto the end of a list.

# .extend(<iterable>) - Make a list longer by adding on the members of another iterable.

# .insert(<index>, <value>) - Add a value to a list at a particular index.

# You can, of course, also add lists together with the + operator. To do this in place, you'd use the increment operator +=.


favorite_things = ["mere", 'pere', 'bere']
print(favorite_things)
favorite_things += ["banane"]
print(favorite_things)
favorite_things.append(["cirese"])
print(favorite_things)
del favorite_things[-1]
print(favorite_things)
favorite_things.extend(["prune", "capsune"])
print(favorite_things)
a = [1,2,3]
a.extend("abc")
print(a)
print("")
print("\n")
del favorite_things[1]
print(favorite_things)
print("\n")
print(favorite_things)
favorite_things.insert(1, "portocale")
print(favorite_things)





# Lists aren't always perfectly formed. Sometimes you have to take things out. Let's look at the del keyword 
# and the .remove()method to learn two different ways of taking out list members.

# del - A keyword for removing items from iterables or deleting whole variables.

# .remove() - A list method that removes items from a list by their value.

# .pop() will remove and return the last item from a list.
# .pop(<index>) will remove whatever item is at <index>, assuming something is.
# If there's nothing left in the list, or the provided index isn't available, .pop() will raise an IndexError.

# Vowels
print("\n")
def disemvowel(word):
    vowels = "aeiouAEIOU"
    new_word = []

    for letter in word:
        if letter not in vowels:
            new_word.append(letter)

    new_word = ''.join(new_word)
    return new_word

a = raw_input("Type a word: ")
print("Your word is: {}".format(a))
b = disemvowel(a)
print(b)


messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0, messy_list.pop(3))
print(messy_list)
messy_list.remove(False)
del messy_list[1]
del messy_list[3]
print(messy_list)
