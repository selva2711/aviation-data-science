# Day 31: Python any() and all()

## Overview
Learn how to use Python's `any()` and `all()` functions to evaluate flight statuses, delay conditions, and safety alerts.

## 🧠 Topics Covered
- `any()` function
- `all()` function
- Boolean values: `True` and `False`
- Generator expressions
- Conditional checks with aviation data

## ✈️ Aviation Examples
- Detect whether any flight is delayed
- Check whether all flights are delayed
- Identify major flight delays
- Detect safety alerts

## 📖 Example
```python
flight_status = [True, False, True, True]

print("Any Flight Delayed:", any(flight_status))
print("All Flights Delayed:", all(flight_status))
```

## Output
```text
Any Flight Delayed: True
All Flights Delayed: False
```

## 🔑 Key Learning
- `any()` returns `True` when at least one item is truthy.
- `all()` returns `True` when every item is truthy.
- Both functions are useful for checking conditions across collections of data.

## 🚀 Progress
Python Fundamentals — Day 31 completed.

## Conclusion
The `any()` and `all()` functions help analyze aviation data efficiently by checking whether one or all conditions are satisfied.
