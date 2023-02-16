# first transform then reduction
nums = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nums)
print(s)


def getanodd():
    for i in range(100):
        if i % 2 == 0:
            yield i


print(list(getanodd()))
