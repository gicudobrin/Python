# Strings are a grouping of characters, letters, numbers, 
# spaces, emoji, whatever, in-between two sets of quote marks.
# strings are immutable which means that we cant change something in the same string
# We can use single or double quotes, but they have to be the same on both sides.
# we can't delete things from a string

print('He\'s right')
print("""He's right""")
print('''He's right''')

long_string = """Here's a new line!


It's right there!"""
print(long_string)
print(str(5))

# Strings concatenation

print("Hello" + " " + "there!")

name = "Claudiu"
name += " "
name += "Craciunoiu"

print(name)

var = "a"
var1 = str(5)
print(var + var1)

# You can't subtract or divide strings
# You can multiply them

print("=" * 10)

status_message = "Hey, we have 8 people using the site right now."
status_message = "Hey we have {} people using the site right now."
print(status_message.format(7)) 
print("Hey we have {} {} using the site right now".format(5, "dogs"))

# {} is a placeholder

print("=" * 10)

nume = "Americanu"
subject = "Treehouse loves" + " " + nume
print(subject)

numele = "Claudiu"
subiect = "Treehouse loves {}".format(numele)
print(subiect)