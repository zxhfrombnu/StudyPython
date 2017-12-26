stocks = {
    'GOOG': 520,
    'FB': 76,
    'YHOO': 39.2,
    'AMZN': 306,
    'AAPL': 99.7
}

# sort by number
min_value = min(sorted(zip(stocks.values(),stocks.keys())))
print('min_value', min_value)

max_value = max(sorted(zip(stocks.values(),stocks.keys())))
print('max_value', max_value)

print('sort by number', sorted(zip(stocks.values(), stocks.keys())))
# sort by name
print('sort by name', sorted(zip(stocks.keys(), stocks.values())))
