
# Day 47: Python reversed() Function

## Overview
Learned how to use Python's built-in reversed() function to reverse the order of elements in a sequence.

## 🧠 Topics Covered
- Introduction to reversed()
- reversed() with Lists
- reversed() with Strings
- Using list() with reversed()
- Using join() with reversed()
- Using reversed() with for loops
- Using append() to collect flight numbers

## ✈️ Aviation Examples
- Reversing flight numbers
- Reversing passenger names
- Reversing flight delays
- Reversing airline name characters
- Reversing flight records

## 📖 Example

```python
flights = ["QR100", "QR200", "QR300", "QR400", "QR500"]

reverse_flights = list(reversed(flights))

print("Original Flights:", flights)
print("Reversed Flights:", reverse_flights)
```

## Output

```text
Original Flights: ['QR100', 'QR200', 'QR300', 'QR400', 'QR500']
Reversed Flights: ['QR500', 'QR400', 'QR300', 'QR200', 'QR100']
```

## 🔑 Key Learning
- reversed() reverses the order of elements.
- list() converts the reversed result into a list.
- reversed() does not sort values.
- "".join() combines reversed characters into a string.
- reversed() works with lists and strings.

## 🚀 Progress
- Completed Day 47 Python practice.
- Practiced five aviation-related examples.
- Successfully used reversed() with lists, strings, and flight records.

## Conclusion
The Python reversed() function is useful for reversing the order of aviation data, including flight numbers, passenger lists, and flight records.
