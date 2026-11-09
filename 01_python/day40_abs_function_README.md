# Day 40: Python abs() Function

## Overview
Learn how Python's `abs()` function returns the absolute value of a number through aviation-related examples.

## 🧠 Topics Covered
- Python `abs()` function
- Absolute values of integers
- Absolute values of floats
- Handling positive and negative values
- Processing flight records using loops
- Working with lists of dictionaries

## ✈️ Aviation Examples
- Measuring flight schedule time differences
- Checking temperature differences
- Calculating airport distance differences
- Processing multiple flight records

## 📖 Example
```python
flights = [
    {"flight": "QR100", "time_difference": -15, "temperature": -3.5},
    {"flight": "QR200", "time_difference": 30, "temperature": -5.8},
    {"flight": "QR300", "time_difference": -8, "temperature": 2.5}
]

for flight in flights:
    time_diff = abs(flight["time_difference"])
    temp_diff = abs(flight["temperature"])

    print("Flight:", flight["flight"])
    print("Time Difference:", time_diff, "minutes")
    print("Temperature Difference:", temp_diff)
    print()
```

## Output
```text
Flight: QR100
Time Difference: 15 minutes
Temperature Difference: 3.5

Flight: QR200
Time Difference: 30 minutes
Temperature Difference: 5.8

Flight: QR300
Time Difference: 8 minutes
Temperature Difference: 2.5
```

## 🔑 Key Learning
- `abs(number)` returns the absolute value.
- Negative numbers become positive.
- Positive numbers remain unchanged.
- `abs()` works with both integers and floats.
- It can measure the magnitude of a difference, but does not identify whether a flight is early or late.

## 🚀 Progress
Python Fundamentals — Day 40 completed.

## Conclusion
The `abs()` function helps measure numerical differences in aviation data, including flight timing and temperature values.
