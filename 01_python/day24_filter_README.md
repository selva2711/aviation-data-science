# Day 24 – filter() Function in Python

## Overview

Today, I learned about the Python `filter()` function and how to select items from a list based on a condition.

## 🧠 Topics Covered

- Understanding the `filter()` function
- Using `filter()` with regular functions
- Using `filter()` with lambda functions
- Filtering ticket prices
- Identifying on-time flights
- Filtering delayed flights
- Filtering passenger counts
- Using comparison operators
- Calculating totals with `sum()`

## ✈️ Aviation Examples

I used the `filter()` function to select expensive tickets, identify on-time and delayed flights, and find flights with passenger counts above a specified value.

## 📖 Example

```python
ticket_prices = [500, 1000, 1500, 800, 2000, 1200]

expensive_tickets = list(
    filter(lambda price: price >= 1000, ticket_prices)
)

print(expensive_tickets)
print(sum(expensive_tickets))
```

Output:

```text
[1000, 1500, 2000, 1200]
5700
```

## 🔑 Key Learning

The `filter()` function selects items from an iterable when they satisfy a specified condition. Using `filter()` with lambda functions makes simple filtering operations concise and readable.

## 🚀 Progress

Day 24 completed successfully.

## Conclusion

The `filter()` function is useful for selecting relevant data in Python. It can help with aviation analytics tasks such as filtering ticket prices, flight delays, and passenger data.
