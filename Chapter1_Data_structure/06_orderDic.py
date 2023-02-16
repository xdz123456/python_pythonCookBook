from collections import OrderedDict


# keep the order of init the dic
d = OrderedDict()
d['foo'] = 1
d['bar'] = 44
d['spam'] = 33
d['grok'] = 44

for key in d:
    print(key, d[key])
