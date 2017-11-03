# if statement

# if money > apple_cost:
# 	buy_apples()
# else:
# 	find_another_snack()


age = 8 * 365
if age > 20000:
	print("Wow, over 10000 (exact = {}) days old!".format(age))
elif age < 1000:
	print("You are in the middle of your life!")
elif age > 10500:
	print("I love you!")
else:
	print("Keep going! You'll get there!")

# if not age = 20

# in keyword use to check for containment or inclusion

days_open = ["Monday","Tuesday","Wednesday","Thursday"]
today = "Tuesday"
if today in days_open:
	print("Come on in!")
else:
	print("Sorry! We're closed!")

# not in