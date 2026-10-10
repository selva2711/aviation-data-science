```python
# Day 23: Python map() Function
# Aviation Data Science Practice

# Example 1: Add a fee to ticket prices
ticket_prices = [500, 700, 900, 1200]

updated_prices = list(
    map(lambda price: price + 100, ticket_prices)
)

print("Original Prices:", ticket_prices)
print("Updated Prices:", updated_prices)

print()

# Example 2: Add 10% to ticket prices
ticket_prices = [500, 1000, 1500, 2000]

updated_prices = list(
    map(lambda price: round(price * 1.10, 2), ticket_prices)
)

print("Original Prices:", ticket_prices)
print("Prices with 10% Increase:", updated_prices)

print()

# Example 3: Add the QR prefix to flight numbers
flight_numbers = ["170", "500", "700", "800"]

updated_flights = list(
    map(lambda flight: "QR" + flight, flight_numbers)
)

print("Original Flights:", flight_numbers)
print("Updated Flights:", updated_flights)

print()

# Example 4: Calculate total fares using two lists
passengers = [2, 3, 4]
ticket_prices = [500, 700, 900]

total_fares = list(
    map(lambda count, price: count * price,
        passengers, ticket_prices)
)

print("Passengers:", passengers)
print("Ticket Prices:", ticket_prices)
print("Total Fares:", total_fares)

print()

# Example 5: Calculate total fares and grand total
passengers = [5, 2, 3]
ticket_prices = [400, 800, 600]

total_fares = list(
    map(lambda count, price: count * price,
        passengers, ticket_prices)
)

print("Total Fares:", total_fares)
print("Grand Total:", sum(total_fares))
```

# Output

```text
Original Prices: [500, 700, 900, 1200]
Updated Prices: [600, 800, 1000, 1300]

Original Prices: [500, 1000, 1500, 2000]
Prices with 10% Increase: [550.0, 1100.0, 1650.0, 2200.0]

Original Flights: ['170', '500', '700', '800']
Updated Flights: ['QR170', 'QR500', 'QR700', 'QR800']

Passengers: [2, 3, 4]
Ticket Prices: [500, 700, 900]
Total Fares: [1000, 2100, 3600]

Total Fares: [2000, 1600, 1800]
Grand Total: 5400
```
