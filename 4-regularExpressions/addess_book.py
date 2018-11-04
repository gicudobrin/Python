import re

names_file = open("names.txt",encoding="utf-8")
data = names_file.read()
names_file.close()

print(data)
print(re.match(r'Love', data))
print(re.search(r'Ana', data))