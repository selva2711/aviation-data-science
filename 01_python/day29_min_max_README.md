
# Day 29: Python min() and max() Functions

## 📌 Overview
In this lesson, I learned how to find the smallest and largest values in Python. I also learned to identify flights with the fewest and most passengers using min(), max(), and lambda.

## 🧠 Topics Covered
- min() function
- max() function
- Finding the lowest and highest values
- Using key with lambda
- Working with tuples

## ✈️ Aviation Examples
- Finding the lowest ticket price
- Finding the highest ticket price
- Identifying flights with the fewest passengers
- Identifying flights with the most passengers

## 📖 Example

```python id="m2j4x8"
flight_passengers = [
    ("QR170", 180),
    ("QR500", 250),
    ("QR700", 120),
    ("QR900", 300)
]

lowest_flight = min(
    flight_passengers,
    key=lambda flight: flight[1]
)

highest_flight = max(
    flight_passengers,
    key=lambda flight: flight[1]
)

print("Flight with Fewest Passengers:", lowest_flight)
print("Flight with Most Passengers:", highest_flight)
```

## 📤 Output

```text id="6c0x4k"
Flight with Fewest Passengers: ('QR700', 120)
Flight with Most Passengers: ('QR900', 300)
```

## 🔑 Key Learning
- min() returns the smallest value.
- max() returns the largest value.
- key=lambda flight: flight[1] selects the passenger count for comparison.
- With this key, min() and max() return the complete tuple for the selected flight.

## 🚀 Progress
- Completed Day 29
- Practiced min() and max()
- Applied lambda to aviation passenger data

## Conclusion
The min() and max() functions help identify minimum and maximum values in aviation datasets. They are useful for quick comparisons and basic data analysis.
