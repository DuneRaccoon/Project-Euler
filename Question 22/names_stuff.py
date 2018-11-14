import string
with open('p022_names.txt') as names:
    names = sorted([e.strip('"') for e in names.read().split(',')])
print(sum([sum([string.ascii_uppercase.index(letter)+1 for letter in name]) * \
           (names.index(name)+1) for name in names]))
