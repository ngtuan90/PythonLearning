from collections import Counter

input=raw_input('Enter your string:')

############ Cach 1 ##############
chars = input.split()
for char in set(chars):
    num = chars.count(char)
    print char , ':' ,num

######### Cach 2 ##############
counter = Counter(chars)
print counter
print counter.values()
print counter.keys()
