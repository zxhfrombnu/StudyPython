stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549
}

# zip(k,v in stocks)

min_price_byValue = min(zip(stocks.values(), stocks.keys()))
min_price_byKey = min(zip(stocks.keys(), stocks.values()))
print(min_price_byKey)
print(min_price_byValue)