
# Day 28: Python sorted() Function
# Aviation Data Science Practice

flight_prices = [
    ("QR170", 1500),
    ("QR500", 500),
    ("QR700", 1200),
    ("QR900", 800)
]

ascending = sorted(flight_prices, key=lambda flight: flight[1])

descending = sorted(
    flight_prices,
    key=lambda flight: flight[1],
    reverse=True
)

print("Lowest to Highest:")
print(ascending)

print()

print("Highest to Lowest:")
print(descending)

# Output


Lowest to Highest:
[('QR500', 500), ('QR900', 800), ('QR700', 1200), ('QR170', 1500)]

Highest to Lowest:
[('QR170', 1500), ('QR700', 1200), ('QR900', 800), ('QR500', 500)]
