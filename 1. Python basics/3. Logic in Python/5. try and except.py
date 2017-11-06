try:
	count = int(raw_input("Give me a number: "))
except ValueError:
	print("That's not a number!")
else:
	print("Hi " * count)



def add(a,b):
    try:
        print("The first number is {}".format(a))
        print("The second number is {}".format(b))
        return float(a) + float(b)
    except ValueError:
        return None
    else:
    	print(a + b)
        

suma = add(45,25)
print(suma)
print("Suma este {}".format(suma))