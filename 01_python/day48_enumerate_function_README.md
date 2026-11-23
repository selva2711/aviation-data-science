
# Day 48: Python enumerate() Function

## Overview
Learned how to use Python's built-in enumerate() function to access the index and value of each item in a sequence.

## 🧠 Topics Covered
- Introduction to enumerate()
- enumerate() with Lists
- Index and Value
- Default Index Starting from 0
- Using start=1
- enumerate() with Dictionaries
- enumerate() with for loops
- Calculating Total Passengers

## ✈️ Aviation Examples
- Displaying flight numbers with index positions
- Displaying passenger names with index positions
- Starting flight numbering from 1
- Displaying flight records with passenger counts
- Calculating total passengers across flights

## 📖 Example

```python id="c2d3j1"
flights = ["QR100", "QR200", "QR300", "QR400"]

for index, flight in enumerate(flights, start=1):
    print(index, flight)
```

## Output

```text id="wsk7xh"
1 QR100
2 QR200
3 QR300
4 QR400
```

## 🔑 Key Learning
- enumerate() provides an index and an item.
- The default index starts from 0.
- start=1 makes the index begin from 1.
- enumerate() works with lists and dictionaries inside loops.
- It helps organize and display flight records.
- Passenger totals can be calculated inside an enumerate() loop.

## 🚀 Progress
- Completed Day 48 Python practice.
- Practiced five aviation-related examples.
- Successfully used enumerate() with lists and flight records.

## Conclusion
The Python enumerate() function is useful for tracking item positions and organizing aviation data such as flight numbers, passenger names, and flight records.
