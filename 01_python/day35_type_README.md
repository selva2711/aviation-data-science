# Day 35: Python type() Function

## Overview
Learn how Python's `type()` function identifies the data type of a value through aviation-related examples.

## 🧠 Topics Covered
- `type()` function
- Python data types: `str`, `int`, `float`, and `bool`
- Checking values inside lists
- Inspecting dictionary values
- Iterating through dictionary items

## ✈️ Aviation Examples
- Identifying flight number data types
- Checking passenger count and ticket price types
- Inspecting mixed data in ticket price lists
- Reviewing data types in flight records

## 📖 Example
```python
flight = {
    "flight_number": "QR700",
    "passengers": 220,
    "ticket_price": 650.50,
    "delayed": False
}

for key, value in flight.items():
    print(key, "-", type(value))
```

## Output
```text
flight_number - <class 'str'>
passengers - <class 'int'>
ticket_price - <class 'float'>
delayed - <class 'bool'>
```

## 🔑 Key Learning
- `type(value)` returns the type of a value.
- Text inside quotation marks is a string.
- Whole numbers such as `220` are integers.
- Decimal numbers such as `650.50` are floats.
- Boolean values are `True` or `False`.
- `type()` helps inspect data; it does not validate whether the value itself is correct.

## 🚀 Progress
Python Fundamentals — Day 35 completed.

## Conclusion
The `type()` function helps inspect aviation data and understand the structure of values before further analysis.
