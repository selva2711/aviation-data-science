# Day 33: Python bool() Function

## Overview
Learn how Python's `bool()` function converts values into Boolean values (`True` or `False`) using aviation-related examples.

## 🧠 Topics Covered
- `bool()` function
- Truthy and falsy values
- Numbers and strings
- Empty lists and dictionaries
- Checking data availability

## ✈️ Aviation Examples
- Checking passenger availability
- Checking whether a flight number is available
- Checking flight status
- Checking whether flight details exist

## 📖 Example
```python
flight_number = "QR202"
passengers = []
flight_status = "On Time"

print("Flight Number Available:", bool(flight_number))
print("Passenger List Available:", bool(passengers))
print("Flight Status Available:", bool(flight_status))
```

## Output
```text
Flight Number Available: True
Passenger List Available: False
Flight Status Available: True
```

## 🔑 Key Learning
- `bool()` returns `True` for truthy values and `False` for falsy values.
- Zero, empty strings, empty lists, empty dictionaries, and `None` are falsy.
- Non-zero numbers and non-empty strings or collections are truthy.
- `bool()` helps check whether data is available, but it does not verify whether that data is valid or accurate.

## 🚀 Progress
Python Fundamentals — Day 33 completed.

## Conclusion
The `bool()` function is useful for understanding Boolean logic and checking data availability in aviation applications.
