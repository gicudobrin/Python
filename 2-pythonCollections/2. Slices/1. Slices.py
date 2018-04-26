# We don't always want the entirety of a list or string. 
# Sometimes we just want part of it, and Python calls these sub-string or sub-lists "slices"

# [start:stop]
# [inclusive:exclusive]

# Both start and stop are optional. If you leave off start, the slice will start at the beginning of the iterable. If you leave off stop, the slice will continue until the end of the iterable.

# By using this behavior, you can quickly make copies of iterables by slicing them from front to back with [:].

# slices = segments = substrings

messy_list = [4,5,3,1,2]
print(messy_list)
clean_list = messy_list[:] # make a copy from a list #  Copy the entire list with a slice.
clean_list.sort()
print(clean_list)

favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
slice1 = favorite_things[1:4]
print(favorite_things)
print(slice1)
slice2 = favorite_things[5:]
print(slice2)

sorted_things = favorite_things[:]
sorted_things.sort()
print(sorted_things)

# slicing with a step
# [start:stop:step]

# Steps change how Python counts as it moves through the creation of a slice. 
# Positive steps, like 2, skip items from left to right. 
# Negative steps, like -1, move from right to left through the collection.

print("\n")

numbers = list(range(20))
print(numbers)
print(numbers[::2]) # prints out the even numbers

print("Oklahoma"[::2]) 

print("")

print(numbers[::-1]) # reverse the list

print("abcdefg"[::-1])


# del my_list[2:5] # remove this slice

grades = [70, 82, 94, 105, "B", "A", 72, "D"] 
print(grades)
grades [4:6] = [89, 94] # replace the middle two letter grades with 89 and 94
print(grades)


# Sillycase

string = "treehouse"
# set string input to be "treehouse"


def sillycase(string):
    half = len(string) // 2  # // floor division to get half.
# preset a variable half to equal the rounded length of input divided by 2
    first_half = string[:half].lower()
# preset variable first_half equal to input first half lowered
    last_half = string[half:].upper()
# perset variable last_half equal to input last half uppered
    result = first_half + last_half
# set a new variable result equal to the concatenation of both
    return result
# return the variable result out side function


sillycase(string)
# call to function
print(sillycase(string))
# print the function to screen