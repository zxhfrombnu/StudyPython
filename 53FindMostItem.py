import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(3, grades))
print(heapq.nsmallest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price':201},
    {'ticker': 'GOOG', 'price':800},
    {'ticker': 'FB', 'price':54},
    {'ticker': 'MSFT', 'price':313},
    {'ticker': 'TUNA', 'price':68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['ticker']))