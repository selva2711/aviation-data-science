# Day 18 – Default Parameters in Python

## Overview

Today, I learned about default parameters in Python functions and how to use them in aviation-related examples.

## Topics Covered

* Defining functions with default parameter values
* Calling functions without providing optional arguments
* Overriding default values by passing arguments
* Using default parameters in calculations
* Returning calculated values using `return`

## ✈️ Aviation Examples

* Welcoming passengers to different airlines
* Displaying destinations
* Calculating ticket prices
* Calculating available seats
* Applying default values to flight seat calculations

## Key Learning

```python
A default parameter provides a value when an argument is not supplied during a function call. If a different argument is provided, Python uses the supplied value instead.

## Example

def calculate_available_seats(total_seats, booked_seats=100):
    return total_seats - booked_seats

print(calculate_available_seats(300))
print(calculate_available_seats(250, 200))
```

## Conclusion

Default parameters make functions more flexible and reduce the need to provide the same argument repeatedly.

These concepts will help me build reusable Python programs for aviation data analysis.

## 🚀 Progress
Day 18 completed successfully.

