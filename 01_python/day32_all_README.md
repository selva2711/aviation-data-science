# Day 32: Python all() Function

## Overview
Learn how Python's `all()` function checks whether every item in an iterable satisfies a condition, using aviation data examples.

## 🧠 Topics Covered
- `all()` function
- Boolean values: `True` and `False`
- Generator expressions
- Conditional checks
- Combining `any()`, `all()`, and `zip()`

## ✈️ Aviation Examples
- Checking pre-flight checklist statuses
- Checking whether all flight delays are under 30 minutes
- Validating passenger counts
- Identifying delays across multiple flights

## 📖 Example
```python
flight_delays = [10, 35, 15]

all_under_30 = all(delay < 30 for delay in flight_delays)

print("All Flights Under 30 Minutes:", all_under_30)
```

## Output
```text
All Flights Under 30 Minutes: False
```

## 🔑 Key Learning
- `all()` returns `True` when every item is truthy.
- If any item is falsy, `all()` returns `False`.
- `any()` checks whether at least one item is truthy.
- These functions are useful for analyzing collections of aviation data.

## 🚀 Progress
Python Fundamentals — Day 32 completed.

## Conclusion
The `all()` function helps validate conditions across multiple records and can be combined with `any()` for aviation data analysis.
