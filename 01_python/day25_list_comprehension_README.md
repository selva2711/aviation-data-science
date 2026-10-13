# Day 25 – List Comprehension in Python

## Overview

Today, I learned about list comprehension and how to create new lists using concise Python syntax. I also learned how to apply conditions and perform calculations on list items.

## 🧠 Topics Covered

- Understanding list comprehension
- Creating new lists
- Updating ticket prices
- Filtering values using `if`
- Using `if...else` expressions
- Formatting flight numbers
- Increasing ticket prices
- Combining conditions and calculations

## ✈️ Aviation Examples

I used list comprehension to update airline ticket prices, filter expensive tickets, classify ticket prices, and format Qatar Airways flight numbers.

## 📖 Example

```python
ticket_prices = [500, 1000, 1500, 800, 2000, 1200]

expensive_tickets = [
    price for price in ticket_prices if price >= 1000
]

updated_prices = [
    round(price * 1.10, 2) for price in expensive_tickets
]

print("Expensive Tickets:", expensive_tickets)
print("Prices After 10% Increase:", updated_prices)
```

Output:

```text
Expensive Tickets: [1000, 1500, 2000, 1200]
Prices After 10% Increase: [1100.0, 1650.0, 2200.0, 1320.0]
```

## 🔑 Key Learning

List comprehension provides a concise way to create a new list from an existing iterable. It supports expressions, conditions, and conditional expressions, making it useful for filtering and transforming data.

## 🚀 Progress

Day 25 completed successfully.

## Conclusion

List comprehension simplifies many list-processing tasks in Python. It is useful for transforming ticket prices, filtering passenger data, and preparing aviation data for analysis.
