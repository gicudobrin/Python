TICKET_PRICE = 10

tickets_remaining = 100

# Run this code continuously until we run out of tickets

while tickets_remaining >= 1:

	# Output how many tickets are remainig using the tickets_remaining variable

	print("There are {} tickets remaining.".format(tickets_remaining))

	# Gather the user's name and assign it to a new variable

	name = input("What is your name?\n")

	# Prompt the user by name and ask how many tickets they would like
	try:
		num_tickets = int(input("How many tickets would you like, {}?\n".format(name)))
		if num_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
	except ValueError as err:

		print("Oh no, we ran into an issue!! {}. Please try again!".format(err))

	else:
		# Calculate the price (number of tickets multiplied by the price) and assign it to a variable

		amount_due = num_tickets * TICKET_PRICE

		# Output the price to the screen

		print("The total due is ${}.".format(amount_due))

		# Prompt the user if they want to proceed

		shall_proceed = input("Do you want to proceed? Y/N ")

		# If they want to proceed
		if shall_proceed.lower() == "y":
			# print out to the screen "SOLD!" to confirm purchase
			print("SOLD!")
			# and then decrement the tickets remaining by the number of tickets purchased
			tickets_remaining -= num_tickets
		# Otherwise... 
		else:
			# thanks them by name
			print("Thank you anyways, {}!".format(name))

# Notify user that the tickets are sold out 
print("Sorry the tickets are all sold out!!!!!!")