
# Day 49: Python zip() Function

## Overview
Learned how to use Python's built-in zip() function to combine two or more lists based on their positions.

## 🧠 Topics Covered
- Introduction to zip()
- Combining Two Lists
- Combining Three Lists
- zip() with Flight Numbers
- zip() with Passenger Counts
- zip() with Flight Delays
- Using zip() with for loops
- Creating Flight Details

## ✈️ Aviation Examples
- Combining flight numbers and passenger counts
- Combining flight numbers and delays
- Combining three aviation data lists
- Displaying flight details using for loops
- Analyzing multiple flight records

## 📖 Example

```python id="o8k3nd"
flight_numbers = ["QR100", "QR200", "QR300"]
passengers = [180, 250, 320]

flight_details = list(zip(flight_numbers, passengers))

print("Flight Details:", flight_details)
```

## Output

```text id="k7xt3n"
Flight Details: [('QR100', 180), ('QR200', 250), ('QR300', 320)]
```

## 🔑 Key Learning
- zip() combines values from multiple lists.
- Values are paired based on their positions.
- zip() can combine two or more lists.
- list() converts the zip result into a list.
- for loops can process zipped values one by one.

## 🚀 Progress
- Completed Day 49 Python practice.
- Practiced five aviation-related examples.
- Successfully used zip() with two and three lists.

## Conclusion
The Python zip() function is useful for combining aviation datasets such as flight numbers, passenger counts, and flight delays.
