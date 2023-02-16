# If items are hashable:
def dedupte(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupte(a)))
b = list(set(a))
print(b)
