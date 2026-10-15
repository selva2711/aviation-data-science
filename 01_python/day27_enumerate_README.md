
# Day 27: Python enumerate() Function

## 📌 Overview
In this lesson, I learned how to use Python's enumerate() function to add an index to each item while looping through aviation data.

## 🧠 Topics Covered
- Understanding enumerate()
- Using start=1
- Combining enumerate() with zip()
- Looping through flight information
- Calculating total passengers

## ✈️ Aviation Examples
- Numbering flight records
- Displaying flight numbers and passenger counts
- Calculating the total number of passengers across flights

## 📖 Example

```python
flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [180, 220, 150]

total_passengers = 0

for index, (flight, count) in enumerate(
    zip(flight_numbers, passengers), start=1
):
    print("Flight No:", index)
    print("Flight:", flight)
    print("Passengers:", count)
    print()

    total_passengers += count

print("Total Passengers:", total_passengers)
```

## 📤 Output

```text
Flight No: 1
Flight: QR170
Passengers: 180

Flight No: 2
Flight: QR500
Passengers: 220

Flight No: 3
Flight: QR700
Passengers: 150

Total Passengers: 550
```

## 🔑 Key Learning
- enumerate() provides an index and an item during iteration.
- start=1 makes numbering begin at 1 instead of 0.
- zip() combines corresponding items from multiple lists.
- A running total can calculate the total number of passengers.

## 🚀 Progress
- Completed Day 27
- Practiced enumerate() with zip()
- Applied Python loops to aviation data

## Conclusion
The enumerate() function helps number and organize aviation records. Combining it with zip() makes it easier to process related flight information.
