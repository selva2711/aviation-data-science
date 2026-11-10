# Day 41: Python pow() Function

## Overview
Learn how Python's built-in `pow()` function calculates the power of a number using aviation-themed examples.

## 🧠 Topics Covered
- Python `pow()` function
- Base and exponent
- Power calculations
- Using `pow()` with integer values
- Processing multiple flight records
- Using `pow()` inside a for loop

## ✈️ Aviation Examples
- Aviation seating calculation example
- Power calculations using numerical values
- Multiple flight calculations
- Processing flight records such as QR100, QR200, and QR300

## 📖 Example
```python
flights = [
    {"flight": "QR100", "base": 2, "power": 3},
    {"flight": "QR200", "base": 3, "power": 2},
    {"flight": "QR300", "base": 4, "power": 2}
]

for flight in flights:
    result = pow(flight["base"], flight["power"])

    print("Flight:", flight["flight"])
    print("Base:", flight["base"])
    print("Power:", flight["power"])
    print("Result:", result)
    print()
```

## Output
```text
Flight: QR100
Base: 2
Power: 3
Result: 8

Flight: QR200
Base: 3
Power: 2
Result: 9

Flight: QR300
Base: 4
Power: 2
Result: 16
```

## 🔑 Key Learning
- `pow(base, exponent)` calculates the power of a number.
- Base represents the number being multiplied.
- Exponent represents the power.
- `pow(2, 3)` returns 8.
- `pow(3, 2)` returns 9.
- `pow()` can be used with flight records and loops.

## 🚀 Progress
Python Fundamentals — Day 41 completed.

## Conclusion
The Python `pow()` function is useful for calculating powers of numbers. This lesson introduced the function through simple numerical and aviation-themed examples.
