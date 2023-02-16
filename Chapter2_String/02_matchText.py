import os
import re
# check begin with, check end with
filename = 'spam.txt'
print(filename.endswith('.txt'))
url = 'http://www.python.org'
print(url.startswith("http"))
filename = os.listdir('.')
print(filename)
python_files = [name for name in filename if name.endswith(".py")]
print(python_files)

url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))


