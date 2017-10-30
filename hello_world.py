"""my_list=[1,2,3,4,5,6]
print(my_list)
my_list.append('ce mai faci?')
print(my_list)
my_list.extend([4,5,6])
print(my_list)
my_list.remove(5)
print(my_list)
my_list.remove(5)
print(my_list)
my_list.remove(6)
print(my_list
"""

items = ['abc','cde','asf','dfg']

def loopy(items,ana):
    for item in items:
        index0 = item[0]
        if index0 == 'a':
            continue
        else:
            print(item)
loopy('asdf',6)

      