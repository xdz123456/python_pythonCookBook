from fnmatch import fnmatch, fnmatchcase
# use fnmatch to find the wildcard pattern

fnmatch('foo.txt', '*.txt')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

a = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(a)

