# Day 23 – map() Function in Python

## Overview

Today, I learned about the `map()` function and how to apply a function to each item in a list using Python.

## 🧠 Topics Covered

- Understanding the `map()` function
- Using `map()` with regular functions
- Using `map()` with lambda functions
- Updating ticket prices
- Formatting flight numbers
- Using `map()` with two lists
- Calculating ticket fares
- Using `round()` for decimal values
- Calculating totals with `sum()`

## ✈️ Aviation Examples

I used the `map()` function to update airline ticket prices, format flight numbers, calculate passenger fares, and find the grand total of fares.

## 📖 Example

```python
passengers = [2, 3, 4]
ticket_prices = [500, 700, 900]

total_fares = list(
    map(lambda count, price: count * price,
        passengers, ticket_prices)
)

print(total_fares)
```

Output:

```text
[1000, 2100, 3600]
```

## 🔑 Key Learning

The `map()` function applies a specified function to each item in an iterable. It can work with lambda functions and multiple iterables, making it useful for processing data efficiently.

## 🚀 Progress

Day 23 completed successfully.

## Conclusion

The `map()` function helps simplify repetitive calculations and data transformations. It is useful for processing ticket prices, passenger data, and other aviation analytics tasks in Python.
