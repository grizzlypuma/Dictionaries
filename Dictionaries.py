# 1. Write a Python program to sort (ascending and descending) a dictionary by value.

import operator

d = {'cat': 2, 'dog': 3, 'zebra':6, 'lion': 1}

print('Original disctionary: ', d)

#sorting by key(animal)
sorted_d = sorted(d.items())
print('Dictionary in ascendin order by key(animal) : ', sorted_d)
sorted_d_reverse = sorted(d.items(), reverse = True)
print('Dictionary in descending order by key(animal) : ', sorted_d_reverse)
#sorting by value(number)
sorted_d = sorted(d.items(), key = operator.itemgetter(1))
print('Dictionary in ascendin order by value(number) : ', sorted_d)
sorted_d_reverse = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
print('Dictionary in descending order by value(number) : ', sorted_d_reverse)

#Write a Python program to add a key to a dictionary.

d = {0: 10, 1: 20}
print(f"Initial dictionary: {d}")

d.update({2:30})
print(f"dictionary after update: {d}")

# Create three dictionaries 'dic1', 'dic2', and 'dic3' with key-value pairs.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)
print(f"Concatenated dictionary: {dic4}")