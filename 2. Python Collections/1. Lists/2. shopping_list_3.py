# have a HELP command
# have a SHOW command
# clean code up in general

import os

# make a list to hold onto our items

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")




def show_help():
    clear_screen()
    # print out instructions on how to use the app
    print("What shall we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    clear_screen()
    # print out the list
    print("Here's your list:")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))  
        index += 1 
    print("-" * 10)

def add_to_list(new_item):
     # add new items to our list
    clear_screen()
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item,len(shopping_list)))

show_help()   

while True:
    # ask for new items
    
    new_item = raw_input("> ")
    
    # be able to quit the app
    
    if new_item.upper() == 'DONE' or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    else:
        add_to_list(new_item)
    
show_list()