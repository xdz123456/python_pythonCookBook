prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Same function with different express
p1 = {key: value for key, value in prices.items() if value > 40}
p2 = dict((key, value) for key, value in prices.items() if value > 200)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p3 = {key: value for key, value in prices.items() if key in tech_names}
print(p1)
print(p2)
print(p3)
