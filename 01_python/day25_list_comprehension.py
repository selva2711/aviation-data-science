```python
# Day 25: List Comprehension in Python
# Aviation Data Science Practice

# Example 1: Update ticket prices
ticket_prices = [400, 600, 800, 1000]

updated_prices = [price + 100 for price in ticket_prices]

print("Original Prices:", ticket_prices)
print("Updated Prices:", updated_prices)

print()

# Example 2: Filter expensive tickets
ticket_prices = [500, 1200, 800, 1500, 900, 2000]

expensive_tickets = [
    price for price in ticket_prices if price > 1000
]

print("All Ticket Prices:", ticket_prices)
print("Expensive Tickets:", expensive_tickets)

print()

# Example 3: Classify ticket prices
ticket_prices = [500, 1200, 800, 1500, 900, 2000]

ticket_status = [
    "Expensive" if price >= 1000 else "Affordable"
    for price in ticket_prices
]

print("Ticket Prices:", ticket_prices)
print("Ticket Status:", ticket_status)

print()

# Example 4: Format flight numbers
flight_numbers = ["170", "500", "700", "800"]

qatar_flights = [
    "QR" + flight for flight in flight_numbers
]

print("Original Flight Numbers:", flight_numbers)
print("Qatar Airways Flights:", qatar_flights)

print()

# Example 5: Filter tickets and increase prices by 10%
ticket_prices = [500, 1000, 1500, 800, 2000, 1200]

expensive_tickets = [
    price for price in ticket_prices if price >= 1000
]

updated_prices = [
    round(price * 1.10, 2) for price in expensive_tickets
]

print("Original Prices:", ticket_prices)
print("Expensive Tickets:", expensive_tickets)
print("Prices After 10% Increase:", updated_prices)
```

# Output

```text
Original Prices: [400, 600, 800, 1000]
Updated Prices: [500, 700, 900, 1100]

All Ticket Prices: [500, 1200, 800, 1500, 900, 2000]
Expensive Tickets: [1200, 1500, 2000]

Ticket Prices: [500, 1200, 800, 1500, 900, 2000]
Ticket Status: ['Affordable', 'Expensive', 'Affordable', 'Expensive', 'Affordable', 'Expensive']

Original Flight Numbers: ['170', '500', '700', '800']
Qatar Airways Flights: ['QR170', 'QR500', 'QR700', 'QR800']

Original Prices: [500, 1000, 1500, 800, 2000, 1200]
Expensive Tickets: [1000, 1500, 2000, 1200]
Prices After 10% Increase: [1100.0, 1650.0, 2200.0, 1320.0]
```
