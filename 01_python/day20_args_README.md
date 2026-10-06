# Day 20 – *args in Python

## Overview

Today, I learned how to use `*args` in Python functions.

## Topics Covered

- Using `*args`
- Passing multiple positional arguments
- Using `for` loops with `*args`
- Calculating totals using multiple arguments
- Returning results from a function

## ✈️ Aviation Examples

I used `*args` to:

- Store multiple flight numbers
- Display multiple flights
- Calculate total passengers across multiple flights

## 📖 Example

```python
def show_flights(*flights):
    for flight in flights:
        print("Flight:", flight)

show_flights("QR170", "QR500", "QR700")
```

## 📖 Calculation Example

```python
def total_passengers(*passengers):
    total = 0

    for count in passengers:
        total = total + count

    return total
```

## 🔑 Key Learning

*args allows a function to accept multiple positional arguments.
The values can be processed one by one using a for loop.

## 🚀 Progress
Day 20 completed successfully.

Conclusion

Today, I learned how *args can make Python functions flexible and reusable for aviation data analysis.
