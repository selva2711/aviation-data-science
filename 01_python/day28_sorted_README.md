
# Day 28: Python sorted() Function

## 📌 Overview
In this lesson, I learned how to sort Python data in ascending and descending order. I also learned to sort aviation flight records by ticket price.

## 🧠 Topics Covered
- The sorted() function
- Ascending order
- Descending order using reverse=True
- Sorting tuples
- Sorting with key and lambda

## ✈️ Aviation Examples
- Sorting ticket prices from lowest to highest
- Sorting ticket prices from highest to lowest
- Organizing flight records by ticket price

## 📖 Example

```python
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
```

## 📤 Output

```text
Lowest to Highest:
[('QR500', 500), ('QR900', 800), ('QR700', 1200), ('QR170', 1500)]

Highest to Lowest:
[('QR170', 1500), ('QR700', 1200), ('QR900', 800), ('QR500', 500)]
```

## 🔑 Key Learning
- sorted() returns a new sorted list.
- reverse=True sorts in descending order.
- key=lambda flight: flight[1] sorts tuples using their second value.
- The original list remains unchanged.

## 🚀 Progress
- Completed Day 28
- Practiced ascending and descending sorting
- Applied sorting to aviation ticket-price data

## Conclusion
The sorted() function helps organize aviation data and compare flight ticket prices efficiently.
