# Use the Counter
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

# Return a kind of dictionary
counter_a = Counter(words)
counter_b = Counter(morewords)

top_three = counter_a.most_common(1)
print(top_three)


counter_c = counter_b + counter_a
print(counter_c)
# Use combine ma
counter_c.update(words)
print(counter_c)
