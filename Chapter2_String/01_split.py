import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
line_list_1 = re.split(r'(;|,|\s)\s*', line)
line_list_2 = re.split(r'[,;\s]\s*', line)
print(line_list_1)
print(line_list_2)
