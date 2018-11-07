import sys
password = input("Please enter a super secret password!\n")
attempt_count = 1
while password != "opensesame":
	password = input("Invalid password! Please try again!\n") 
	if attempt_count > 3:
		sys.exit("Too many tries!")
	attempt_count += 1
print("Welcome to secret town!")