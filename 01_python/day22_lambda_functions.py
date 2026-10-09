```python
# Day 22 - Lambda Functions in Python

# 1. Lambda with One Parameter
ticket_price = lambda price: price + 100

print("Ticket Price:", ticket_price(500))

print()

# 2. Lambda with Two Parameters
calculate_total_fare = lambda price, passengers: price * passengers

print("Total Fare:", calculate_total_fare(500, 3))

print()

# 3. Lambda with Condition
check_ticket = lambda price: "Expensive" if price > 1000 else "Affordable"

print("Ticket 1:", check_ticket(800))
print("Ticket 2:", check_ticket(1500))

print()

# 4. Lambda with Flight Delays
flight_status = lambda delay: "On Time" if delay == 0 else "Delayed"

print("Flight QR170:", flight_status(0))
print("Flight QR500:", flight_status(30))
print("Flight QR700:", flight_status(15))

print()

# 5. Final Practice
ticket_fare = lambda price, passengers: price * passengers

print("Total Fare:", ticket_fare(600, 3))

check_price = lambda price: "Expensive" if price > 1000 else "Affordable"

print("Ticket Status:", check_price(800))

print("Flight QR170:", flight_status(0))
print("Flight QR500:", flight_status(25))
```

# Output

Ticket Price: 600

Total Fare: 1500

Ticket 1: Affordable
Ticket 2: Expensive

Flight QR170: On Time
Flight QR500: Delayed
Flight QR700: Delayed

Total Fare: 1800
Ticket Status: Affordable
Flight QR170: On Time
Flight QR500: Delayed
