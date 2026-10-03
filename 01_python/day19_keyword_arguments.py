```python
# Day 19 - Keyword Arguments in Python

# 1. Basic Keyword Arguments
def flight_details(flight_number, origin, destination):
    print("Flight Number:", flight_number)
    print("Origin:", origin)
    print("Destination:", destination)


flight_details(
    destination="Mumbai",
    flight_number="QR170",
    origin="Doha"
)

print()


# 2. Positional Arguments
flight_details("QR700", "Dubai", "London")

print()


# 3. Mixing Positional and Keyword Arguments
flight_details("QR170", destination="Mumbai", origin="Doha")

print()


# 4. All Keyword Arguments
flight_details(
    flight_number="QR500",
    destination="Chennai",
    origin="London"
)

print()


# 5. Default Parameter with Keyword Arguments
def ticket_details(flight_number, destination, passengers=100):
    print("Flight Number:", flight_number)
    print("Destination:", destination)
    print("Passengers:", passengers)


ticket_details("QR170", "Mumbai")

print()

ticket_details(
    flight_number="QR500",
    destination="Chennai",
    passengers=150
)

print()

ticket_details("QR700", destination="London", passengers=200)
```
