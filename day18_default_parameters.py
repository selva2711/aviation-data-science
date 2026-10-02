```python
# Day 18 - Default Parameters in Python

# 1. Default Parameter: Airline
def welcome_airline(airline="Qatar Airways"):
    print("Welcome to", airline)


welcome_airline()
welcome_airline("Emirates")
welcome_airline("Singapore Airlines")


# 2. Default Parameter: Destination
def welcome(destination="Doha"):
    print("Welcome to", destination)


welcome()
welcome("London")
welcome("Singapore")
welcome("Oslo")


# 3. Default Parameter: Ticket Price
def calculate_ticket_price(passengers, ticket_price=500):
    total = passengers * ticket_price
    return total


print("Total:", calculate_ticket_price(3))
print("Total:", calculate_ticket_price(3, 800))


# 4. Default Parameter: Booked Tickets
def seats(passengers, booked_ticket=5):
    available_seats = passengers - booked_ticket
    return available_seats


print("Available Seats:", seats(10, 9))
print("Available Seats:", seats(10))


# 5. Aviation Example: Available Seats
def calculate_available_seats(total_seats, booked_seats=100):
    available = total_seats - booked_seats
    return available


print("Flight QR170:", calculate_available_seats(300))
print("Flight QR500:", calculate_available_seats(250, 200))
print("Flight QR700:", calculate_available_seats(180, 150))
```

# Output

Welcome to Qatar Airways
Welcome to Emirates
Welcome to Singapore Airlines
Welcome to Doha
Welcome to London
Welcome to Singapore
Welcome to Oslo
Total: 1500
Total: 2400
Available Seats: 1
Available Seats: 5
Flight QR170: 200
Flight QR500: 50
Flight QR700: 30
