# Day 38: Python int() Function

## Overview
Learn how Python's `int()` function converts values into integers through aviation-related examples.

## 🧠 Topics Covered
- Python `int()` function
- Converting strings into integers
- Converting floats into integers
- Checking data types using `type()`
- Converting dictionary values
- Processing a list of flight dictionaries

## ✈️ Aviation Examples
- Converting passenger counts from strings into integers
- Converting flight numbers into integers
- Processing ticket price and passenger values
- Analyzing multiple flight records

## 📖 Example
```python
flights = [
    {"flight": "QR100", "passengers": "180"},
    {"flight": "QR200", "passengers": "220"},
    {"flight": "QR300", "passengers": "150"}
]

for flight in flights:
    passengers = int(flight["passengers"])

    print("Flight:", flight["flight"])
    print("Passengers:", passengers)
    print("Data Type:", type(passengers))
```

## Output
```text
Flight: QR100
Passengers: 180
Data Type: <class 'int'>
Flight: QR200
Passengers: 220
Data Type: <class 'int'>
Flight: QR300
Passengers: 150
Data Type: <class 'int'>
```

## 🔑 Key Learning
- `int(value)` converts a valid value into an integer.
- Numeric strings such as `"250"` can be converted into `250`.
- `int()` removes the decimal portion of a float; it does not round it.
- `type()` helps verify the resulting data type.
- Integer values can be used in mathematical calculations.
- Invalid numeric strings cannot be directly converted using `int()`.

## 🚀 Progress
Python Fundamentals — Day 38 completed.

## Conclusion
The `int()` function helps prepare aviation data for numerical calculations and analysis.
