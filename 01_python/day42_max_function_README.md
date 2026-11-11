# Day 42: Python max() Function

## Overview
Learn how Python's built-in `max()` function identifies the largest value from a collection of numbers using aviation-related examples.

## 🧠 Topics Covered
- Python `max()` function
- Finding the largest integer
- Finding the largest float
- Comparing flight data
- Working with lists
- Using `append()` to collect values
- Processing flight records using a `for` loop

## ✈️ Aviation Examples
- Comparing passenger counts
- Finding the highest flight delay
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

print("Highest Passengers:", max(passengers))
print("Highest Delay:", max(delays), "minutes")
print("Highest Temperature:", max(temperatures))
```

## Output
```text
Highest Passengers: 320
Highest Delay: 45 minutes
Highest Temperature: 25.8
```

## 🔑 Key Learning
- `max()` returns the largest value.
- It works with integer and float values.
- It can compare values stored in a list.
- `append()` adds values to a list.
- A `for` loop can process multiple flight records.
- `max()` helps identify the highest value in aviation datasets.

## 🚀 Progress
Python Fundamentals — Day 42 completed.

## Conclusion
The Python `max()` function is useful for finding the largest values in aviation datasets, such as passenger counts, flight delays, and temperature readings.
