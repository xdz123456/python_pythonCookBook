import re

text_1 = 'yeah, but no, but yeah, but no, but yeah'
text_2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# Task1 replace all no to yes
print(text_1.replace("no", 'yes'))

# Task2 transform XX/XX/XXXX to XXXX/XX/XX
date_pattern = re.compile(r"(\d+)/(\d+)/(\d+)")
print(date_pattern.sub(r"\3-\1-\2", text_2))

new_text, n = date_pattern.subn(r"\3-\1-\2", text_2)
print(n, new_text)