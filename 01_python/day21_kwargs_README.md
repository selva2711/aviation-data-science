# Day 21 – **kwargs in Python

## Overview
Today, I learned about `**kwargs` in Python functions.

## 🧠 Topics Covered

- Using `**kwargs`
- Passing multiple keyword arguments
- Storing keyword arguments as a dictionary
- Using `.items()` with `**kwargs`
- Accessing specific dictionary values
- Using `**kwargs` with `if` conditions

## ✈️ Aviation Examples

I used `**kwargs` to work with:

- Flight numbers
- Airlines
- Origins
- Destinations
- Aircraft information
- Flight routes

## Example

```python
def flight_details(**details):
    for key, value in details.items():
        print(key, ":", value)

flight_details(
    flight_number="QR170",
    origin="Doha",
    destination="Mumbai"
)
```
## 🔑 Key Learning
**kwargs allows a function to accept multiple keyword arguments.
The arguments are stored as a dictionary containing key-value pairs.

## Difference Between *args and **kwargs
- *args → multiple positional arguments
- **kwargs → multiple keyword arguments

## 🚀 Progress
Day 21 completed successfully.

## Conclusion
Today, I learned how **kwargs can make Python functions flexible and useful for handling aviation-related information.

