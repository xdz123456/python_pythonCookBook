prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

# zip return an iterator
price_max = max(zip(prices.values(), prices.keys()))
price_min = min(zip(prices.values(), prices.keys()))
price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_max)
print(price_min)
print(price_sorted)

