import re

text = 'yeah, but no, but yeah, but no, but yeah'
# exact match
print(text == 'yeah')

# match start or end
print((text.endswith('yeah')))
print(text.endswith('no'))

print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print("yes")
else:
    print("no")


date_pattern = re.compile(r'\d+/+\d+/+\d+')
if date_pattern.match(text1):
    print("Matched")

print(date_pattern.findall(text1))
