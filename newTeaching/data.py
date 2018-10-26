import datetime

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

new_date = datetime.date(year, month, day).isoweekday()

if new_date == 1:
	new_date = "Monday"
elif new_date == 2:
	new_date = "Tuesday"
elif new_date == 3:
	new_date = "Wednesday"
elif new_date == 4:
	new_date = "Thursday"
elif new_date == 5:
	new_date = "Friday"	
elif new_date == 6:
	new_date = "Saturday"
elif new_date == 7:
	new_date = "Sunday"

print("The day of the week is: {}".format(new_date))