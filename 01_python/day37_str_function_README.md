# Day 37: Python str() Function

## Overview
Learn how Python's `str()` function converts values into strings through aviation-related examples.

## 🧠 Topics Covered
- Python `str()` function
- Converting integers into strings
- Checking data types with `type()`
- Combining strings and numeric values
- Displaying flight information

## ✈️ Aviation Examples
- Converting flight numbers into text
- Displaying passenger counts
- Showing ticket prices
- Combining flight number, passenger count, and gate number in one line

## 📖 Example
```python
flight_number = 700
passengers = 240
gate_number = 12

print("QR" + str(flight_number) + " | Passengers: " + str(passengers) + " | Gate: " + str(gate_number))
```

## Output
```text
QR700 | Passengers: 240 | Gate: 12
```

## 🔑 Key Learning
- `str(value)` converts a value into a string.
- `type()` can verify the resulting data type.
- Strings can be joined with `+`.
- Numeric values must be converted to strings before joining them directly with text using `+`.
- `str()` does not change the original variable automatically.

## 🚀 Progress
Python Fundamentals — Day 37 completed.

## Conclusion
The `str()` function helps format aviation information for readable output and reports.
