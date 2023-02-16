from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# Fist check key 'z''s  value in a, then b
c = ChainMap(a, b)
del c['x']
print(c['z'])