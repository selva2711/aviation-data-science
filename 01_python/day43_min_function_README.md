# Day 43: Python min() Function

## Overview
Learn how Python's built-in `min()` function identifies the smallest value from a collection of numbers using aviation-related examples.

## 🧠 Topics Covered
- Python `min()` function
- Finding the smallest integer
- Finding the smallest float
- Comparing flight data
- Working with lists
- Using `append()` to collect values
- Processing flight records using a `for` loop

## ✈️ Aviation Examples
- Comparing passenger counts
- Finding the lowest flight delay
- Comparing cabin temperatures
- Processing multiple Qatar Airways flight records

## 📖 Example
```python
flights = [
    {"flight": "QR100", "passengers": 180, "delay": 15, "temperature": 22.5},
    {"flight": "QR200", "passengers": 250, "delay": 45, "temperature": 25.8},
    {"flight": "QR300", "passengers": 320, "delay": 20, "temperature": 24.2}
]

passengers = []
delays = []
temperatures = []

for flight in flights:
    passengers.append(flight["passengers"])
    delays.append(flight["delay"])
    temperatures.append(flight["temperature"])

print("Lowest Passengers:", min(passengers))
print("Lowest Delay:", min(delays), "minutes")
print("Lowest Temperature:", min(temperatures))
```

## Output
```text
Lowest Passengers: 180
Lowest Delay: 15 minutes
Lowest Temperature: 22.5
```

## 🔑 Key Learning
- `min()` returns the smallest value.
- It works with integer and float values.
- It can compare values stored in a list.
- `append()` adds values to a list.
- A `for` loop can process multiple flight records.
- `min()` helps identify the lowest value in aviation datasets.

## 🚀 Progress
Python Fundamentals — Day 43 completed.

## Conclusion
The Python `min()` function is useful for finding the smallest values in aviation datasets, such as passenger counts, flight delays, and temperature readings.
