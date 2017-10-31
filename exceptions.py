def add(x, y):
    try:
        a = float(x)  
        b = float(y)
    except ValueError:
        return None
    else:
        return a + b
sum = add(l, 3)
print(sum)

Te pup si te iubesc!
