# Day 39: Python round() Function

## Overview
Learn how Python's `round()` function rounds decimal numbers to a specified number of decimal places through aviation-related examples.

## 🧠 Topics Covered
- Python `round()` function
- Rounding to the nearest integer
- Rounding to one decimal place
- Rounding to two decimal places
- Processing flight records using loops
- Combining `sum()` and `round()`
- Calculating total flight costs

## ✈️ Aviation Examples
- Rounding flight ticket prices
- Rounding fuel costs and airport taxes
- Processing multiple flight records
- Calculating total ticket prices
- Calculating ticket and fuel costs for flights

## 📖 Example
```python
flights = [
    {"flight": "QR100", "ticket_price": 450.678, "fuel_cost": 1200.456},
    {"flight": "QR200", "ticket_price": 650.456, "fuel_cost": 1500.789},
    {"flight": "QR300", "ticket_price": 850.789, "fuel_cost": 1800.123}
]

for flight in flights:
    ticket_price = round(flight["ticket_price"], 2)
    fuel_cost = round(flight["fuel_cost"], 2)

    total_cost = round(ticket_price + fuel_cost, 2)

    print("Flight:", flight["flight"])
    print("Ticket Price:", ticket_price)
    print("Fuel Cost:", fuel_cost)
    print("Total Cost:", total_cost)
```

## Output
```text
Flight: QR100
Ticket Price: 450.68
Fuel Cost: 1200.46
Total Cost: 1651.14

Flight: QR200
Ticket Price: 650.46
Fuel Cost: 1500.79
Total Cost: 2151.25

Flight: QR300
Ticket Price: 850.79
Fuel Cost: 1800.12
Total Cost: 2650.91
```

## 🔑 Key Learning
- `round(number)` rounds a number to the nearest integer.
- `round(number, 1)` rounds to one decimal place.
- `round(number, 2)` rounds to two decimal places.
- `sum()` calculates the total of numeric values.
- `round()` helps display calculated values with reduced decimal precision.
- Python uses round-half-to-even behavior for exact halfway cases.

## 🚀 Progress
Python Fundamentals — Day 39 completed.

## Conclusion
The `round()` function helps present decimal-based aviation calculations in a simpler and more readable format.
