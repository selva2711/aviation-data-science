
# Day 52: Python Functions - def and return

## Overview
Today, I learned how to create reusable functions using Python's def keyword and return statement.

I practiced these concepts with aviation-related examples by calculating flight ticket revenue for multiple flights.

## 🧠 Topics Covered
- Understanding Python functions
- Creating functions using def
- Understanding function parameters
- Using the return statement
- Calling a function
- Reusing functions
- Performing calculations using functions

## ✈️ Aviation Examples
- Calculating QR720 flight revenue
- Calculating QR500 flight revenue
- Calculating total revenue from multiple flights
- Reusing one function for different flight details

## 📖 Example

```python
def calculate_revenue(ticket_price, passengers):
    revenue = ticket_price * passengers
    return revenue


qr720_revenue = calculate_revenue(9000, 120)
qr500_revenue = calculate_revenue(7500, 160)

total_revenue = qr720_revenue + qr500_revenue

print("QR720 Revenue:", qr720_revenue)
print("QR500 Revenue:", qr500_revenue)
print("Total Revenue:", total_revenue)
```

## Output

```text
QR720 Revenue: 1080000
QR500 Revenue: 1200000
Total Revenue: 2280000
```

## 🔑 Key Learning
- def is used to create a function.
- Parameters allow functions to receive input values.
- return sends a result back from a function.
- Functions help avoid repeating the same code.
- A single function can be reused for multiple flights.

## 🚀 Progress
- Learned how to create functions using def.
- Learned how to use return.
- Practiced function parameters.
- Reused functions for multiple flight calculations.
- Completed Day 52 practice exercises.

## Conclusion
Today, I learned how to create and reuse Python functions using def and return.

These concepts are useful for aviation data analysis, flight revenue calculations, and building reusable data science programs.
