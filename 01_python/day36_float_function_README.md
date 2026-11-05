# Day 36: Python float() Function

## Overview
Learn how Python's `float()` function converts values into decimal numbers through aviation-related examples.

## 🧠 Topics Covered
- Python `float()` function
- Converting strings into floats
- Converting integers into floats
- Checking data types using `type()`
- Performing decimal calculations
- Converting dictionary values
- Processing a list of flight dictionaries

## ✈️ Aviation Examples
- Converting ticket prices into float values
- Converting fuel costs into decimal numbers
- Calculating ticket and fuel costs
- Processing multiple flight records

## 📖 Example
```python
flights = [
    {"flight": "QR100", "ticket_price": "450.50"},
    {"flight": "QR200", "ticket_price": "650.75"},
    {"flight": "QR300", "ticket_price": "850.25"}
]

for flight in flights:
    price = float(flight["ticket_price"])

    print("Flight:", flight["flight"])
    print("Ticket Price:", price)
    print("Data Type:", type(price))
```

## Output
```text
Flight: QR100
Ticket Price: 450.5
Data Type: <class 'float'>

Flight: QR200
Ticket Price: 650.75
Data Type: <class 'float'>

Flight: QR300
Ticket Price: 850.25
Data Type: <class 'float'>
```

## 🔑 Key Learning
- `float(value)` converts a valid numeric value into a float.
- Numeric strings such as `"450.50"` can be converted into floats.
- Integers such as `180` become `180.0`.
- Float values support decimal calculations.
- `type()` helps verify the resulting data type.
- Invalid numeric strings cannot be directly converted using `float()`.

## 🚀 Progress
Python Fundamentals — Day 36 completed.

## Conclusion
The `float()` function helps prepare aviation data containing decimal values for calculations and analysis.
