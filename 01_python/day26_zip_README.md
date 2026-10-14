# Day 26 – zip() Function in Python

## Overview

Today, I learned about the Python `zip()` function and how to combine related values from two or more lists.

## 🧠 Topics Covered

- Understanding the `zip()` function
- Combining two lists
- Combining three lists
- Converting zip results into a list
- Using `zip()` with a `for` loop
- Accessing flight details
- Calculating individual flight fares
- Calculating the grand total

## ✈️ Aviation Examples

I used the `zip()` function to combine flight numbers, passenger counts, and ticket prices. I also calculated individual flight fares and the grand total using the combined data.

## 📖 Example

```python
flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [180, 220, 150]
ticket_prices = [500, 700, 600]

grand_total = 0

for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    total_fare = count * price
    grand_total += total_fare

print("Grand Total:", grand_total)
```

Output:

```text
Grand Total: 334000
```

## 🔑 Key Learning

The `zip()` function combines corresponding items from multiple iterables. It is useful for processing related data together. When the iterables have different lengths, `zip()` stops at the shortest iterable by default.

## 🚀 Progress

Day 26 completed successfully.

## Conclusion

The `zip()` function helps organize and process related data in Python. It can be useful for aviation analytics tasks involving flight numbers, passenger counts, ticket prices, and fare calculations.
