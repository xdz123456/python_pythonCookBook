from itertools import compress
my_list = [1, 4, -5, 10, -7, 2, 3, -1]
my_list_filter = [n for n in my_list if n > 0]
print(my_list_filter)

clip_neg = [n if n > 0 else -1 for n in my_list]
print(clip_neg)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
count_boolean = [n > 5 for n in counts]
print(count_boolean)
# An Iterator
add_list = list(compress(addresses, count_boolean))
print(add_list)

