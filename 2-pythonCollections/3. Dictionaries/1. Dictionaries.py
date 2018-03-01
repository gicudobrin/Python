# Dictionaries, or dicts, are usually constructed with the {} literals. You provide a key, a colon, and then a value.

# course = {"title": "Python Collections"}

# You can access the keys by using [] and the key name.

# course["title"]
# "Python Collections"

# KeyError


# .update() - Pass in a dictionary of keys and values to create or update in a single step.

# You can override a single key by assigning a new value to it. And you can delete a key by using del and the key's name.

# Unpacking a dictionary - Pulling multiple keys and their values of out of a dictionary to feed them to a function.

# >>> my_dict = {'name': 'Kenneth'}
# >>> "Hi, my name is {name}!".format(**my_dict)
# "Hi, my name is Kenneth!"
# Packing a dictionary - Putting multiple keyword arguments into a single dictionary.

# >>> def packing(**kwargs):
# ...     print(len(kwargs))
# >>> packing(name="Kenneth")
# 1



# >>> my_dict = {'a': 1, 'b': 2, 'c': 3}
# >>> for key in my_dict:
# . . .     print(key)
# a
# b
# c

# #### New Terms

# * `.keys()` - this method returns an iterable of all of the keys in a dictionary.
# * `.values()` - this method returns an iterable of all of the values in the dictionary.
# * `.items()` - this method is basically a combo of the above two. It returns an iterable of key/value pairs inside of tuples (more on them in the next stage!).