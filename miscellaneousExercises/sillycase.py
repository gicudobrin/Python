def sillycase(iterable):
	half1 = len(iterable)//2
	new1 = (iterable[:half1]).lower()
	new2 = (iterable[half1:]).upper()
	return new1 + new2

print(sillycase('claudIUu'))