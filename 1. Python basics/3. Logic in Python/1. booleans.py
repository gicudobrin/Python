# we can have two boolean values: true and false

# True = 1
# False = 0
# None = nothing

print(True + True)
print(True + False)
print(False + False)

# bool() - function

# everything that's empty is considered false

print(bool([]))

# anything that's not empty is true.

print(bool("2"))
print(bool(None))

right = "a"
wrong = ""

print("+"*10)

print(bool(right))
print(bool(wrong))

# Python has seven comparators, or comparison operators. 
# Each of them returns True or False. Here they are:

# Operator	Comparison
# ==	A is equal to B
# !=	A is not equal to B
# <		A is less than B
# >		A is greater than B
# <=	A is less than, or equal to, B
# >=	A is greater than, or equal to, B
# is	A has the same memory address as B - to see if a variable is none