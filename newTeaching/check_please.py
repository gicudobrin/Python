import math

def split_check(total, number_of_people):
	if number_of_people <= 1:
		raise ValueError("More than one person is required to split check!!!!!!")
	return total / number_of_people


amount_due = split_check(83.5678, 0)
print(math.ceil(amount_due))
