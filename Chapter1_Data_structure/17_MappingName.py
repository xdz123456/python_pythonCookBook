from collections import namedtuple

# namedtuple is immutable
UserTuple = namedtuple("User", ['username', 'phone_number'])

user_1 = UserTuple("Sam199948", '07934412788')
print(user_1.username)
user_1 = user_1._replace(username="Hope")

username, joined = user_1
print(username)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
