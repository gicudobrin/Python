def squared(num):
    try:
        num = int(num)
        return num ** 2
    except ValueError:
		print("{}'s not a number!".format(num))
    else:
        return len(num) * num

a = (raw_input("Give me a number: "))
print(squared(a))

