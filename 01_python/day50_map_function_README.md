
# Day 50: map() Function

## Overview
Today, I learned how to use Python's map() function to apply an operation to every item in a list. I practiced using aviation-related examples such as flight distance conversion, ticket price discounts, and flight delay conversion.

## 🧠 Topics Covered
- Understanding the map() function
- map(function, iterable) syntax
- Using lambda with map()
- Converting map results into a list using list()
- Using round() for decimal precision

## ✈️ Aviation Examples
- Converting flight distances from kilometers to miles
- Applying a 5% discount to ticket prices
- Converting flight delays from minutes to hours

## 📖 Example

```python
flight_distances = [100, 250, 500, 1000]

distances_miles = list(
    map(lambda km: round(km * 0.621371, 2), flight_distances)
)

print("Flight Distances (Miles):", distances_miles)
```

## Output

```text
Flight Distances (Miles): [62.14, 155.34, 310.69, 621.37]
Discounted Ticket Prices: [4750.0, 7125.0, 5700.0, 7600.0]
Flight Delays (Hours): [1.0, 2.0, 1.5, 3.0]
```

## 🔑 Key Learning
- map() applies a function to every item in an iterable.
- lambda helps write small functions.
- list() converts the map result into a list.
- round() controls decimal precision.

## 🚀 Progress
- Completed map() function basics.
- Practiced lambda with map().
- Completed aviation-related exercises.

## Conclusion
I learned how to use Python's map() function to transform multiple values efficiently. This is useful for processing aviation data such as flight distances, ticket prices, and delays.
