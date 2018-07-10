# Create a new empty list named shopping_list

shopping_list = []

# Create a function named add_to_list that declares a parameter named item

def add_to_list(item):
	# Add the item to the list
	shopping_list.append(item)
	# Notify the user that the item was added and show the total number of items in the list
	print("{} was added to the list. The list contains now {} items.".format(item, len(shopping_list)) )

def show_list():
	if shopping_list == []:
		print("Ooops! Your list is empty. You shall put some items in it.\nTo add an item to your list, please type the name of your item and then press Enter.")
	else:
		print("There is your list:")
		for i in shopping_list:
			print("* " + i)

def show_help():
	print("What shall we pick up from the store?")
	print("""
Enter "DONE" to stop adding items.
Enter "HELP" to show the help.
Enter "SHOW" to show your list.
""")

show_help()

while True:

	new_item = raw_input("> ")
	if new_item.upper() == "DONE":
		break
	elif new_item.upper() == "HELP":
		show_help()
		continue
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	# Call add_to_list function with new_item as an argument
	add_to_list(new_item)
show_list()