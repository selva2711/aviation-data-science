
# Day 30: Python sum() Function

## 📌 Overview
In this lesson, I learned how to use Python's sum() function to calculate totals. I applied it to aviation data to calculate flight-wise ticket revenue and total revenue.

## 🧠 Topics Covered
- sum() function
- Working with lists
- zip() function
- for loops
- append() method
- Revenue calculations

## ✈️ Aviation Examples
- Calculating revenue for individual flights
- Combining passenger counts and ticket prices
- Calculating total revenue across flights

## 📖 Example

```python id="xg8x0a"
flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [100, 150, 200]
ticket_prices = [500, 700, 600]

revenues = []

for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    revenue = count * price
    revenues.append(revenue)

    print("Flight:", flight)
    print("Passengers:", count)
    print("Ticket Price: Rs.", price)
    print("Revenue: Rs.", revenue)
    print()

print("Total Revenue: Rs.", sum(revenues))
```

## 📤 Output

```text id="q5plab"
Flight: QR170
Passengers: 100
Ticket Price: Rs. 500
Revenue: Rs. 50000

Flight: QR500
Passengers: 150
Ticket Price: Rs. 700
Revenue: Rs. 105000

Flight: QR700
Passengers: 200
Ticket Price: Rs. 600
Revenue: Rs. 120000

Total Revenue: Rs. 275000
```

## 🔑 Key Learning
- sum() adds all numeric values in an iterable.
- zip() combines corresponding values from multiple lists.
- append() stores each calculated revenue in a list.
- sum(revenues) calculates the total revenue.

## 🚀 Progress
- Completed Day 30
- Practiced sum() with aviation data
- Calculated flight-wise and total revenue

## Conclusion
The sum() function is useful for calculating totals in aviation data analysis, including passenger totals and ticket revenue.
