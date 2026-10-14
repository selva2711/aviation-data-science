```python
# Day 26: Python zip() Function
# Aviation Data Science Practice

# Example 1: Combine flight numbers and passengers
flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [180, 220, 150]

flight_data = list(zip(flight_numbers, passengers))

print("Flight Data:", flight_data)

print()

# Example 2: Combine three lists
flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [180, 220, 150]
ticket_prices = [500, 700, 600]

flight_data = list(
    zip(flight_numbers, passengers, ticket_prices)
)

print("Flight Data:", flight_data)

print()

# Example 3: Display flight details using a for loop
for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    print("Flight:", flight)
    print("Passengers:", count)
    print("Ticket Price:", price)
    print()

# Example 4: Calculate total fare for each flight
for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    total_fare = count * price

    print("Flight:", flight)
    print("Total Fare:", total_fare)
    print()

# Example 5: Calculate the grand total
grand_total = 0

for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    total_fare = count * price
    grand_total += total_fare

print("Grand Total:", grand_total)
```

# Output

```text
Flight Data: [('QR170', 180), ('QR500', 220), ('QR700', 150)]

Flight Data: [('QR170', 180, 500), ('QR500', 220, 700), ('QR700', 150, 600)]

Flight: QR170
Passengers: 180
Ticket Price: 500

Flight: QR500
Passengers: 220
Ticket Price: 700

Flight: QR700
Passengers: 150
Ticket Price: 600

Flight: QR170
Total Fare: 90000

Flight: QR500
Total Fare: 154000

Flight: QR700
Total Fare: 90000

Grand Total: 334000
```

