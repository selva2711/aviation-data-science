# Day 34: Python isinstance() Function

## Overview
Learn how to use Python's `isinstance()` function to check data types and validate aviation records.

## 🧠 Topics Covered
- `isinstance()` function
- Python data types: `str`, `int`, and `float`
- Type checking with `if` and `else`
- Combining `isinstance()` with `all()`
- Using `and` to validate multiple conditions

## ✈️ Aviation Examples
- Checking flight number types
- Validating passenger counts
- Checking ticket price data types
- Validating multiple flight records

## 📖 Example
```python id="7c1g2f"
flight_number = "QR700"
passengers = "220"

if isinstance(flight_number, str) and isinstance(passengers, int):
    print("Flight Data Types Are Correct")
else:
    print("Check Flight Data Types")
```

## Output
```text id="k5k5r8"
Check Flight Data Types
```

## 🔑 Key Learning
- `isinstance(value, type)` checks whether a value belongs to a specified type.
- `isinstance()` returns a Boolean result: `True` or `False`.
- Quotation marks make numeric-looking text a string, such as `"220"`.
- Combining type checks helps identify records that need review.
- Type validation checks the data type, not whether the value is otherwise valid.

## 🚀 Progress
Python Fundamentals — Day 34 completed.

## Conclusion
The `isinstance()` function helps validate data types before processing flight records and other aviation datasets.
