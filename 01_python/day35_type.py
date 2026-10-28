
# Day 35: Python type() Function
# Aviation Data Science

# Example 1: Basic data types
flight_number = "QR202"
passengers = 180
ticket_price = 450.50
flight_delayed = True

print(type(flight_number))
print(type(passengers))
print(type(ticket_price))
print(type(flight_delayed))

print()

# Example 2: Flight dictionary
flight = {
    "flight_number": "QR700",
    "passengers": 220,
    "ticket_price": 650.50
}

print("Flight Number Type:", type(flight["flight_number"]))
print("Passengers Type:", type(flight["passengers"]))
print("Ticket Price Type:", type(flight["ticket_price"]))

print()

# Example 3: Check data types in a list
ticket_prices = [500, 650.50, "800", 450]

for price in ticket_prices:
    print(price, "-", type(price))

print()

# Example 4: Inspect all flight record values
flight = {
    "flight_number": "QR700",
    "passengers": 220,
    "ticket_price": 650.50,
    "delayed": False
}

for key, value in flight.items():
    print(key, "-", type(value))
  
# Output

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

Flight Number Type: <class 'str'>
Passengers Type: <class 'int'>
Ticket Price Type: <class 'float'>

500 - <class 'int'>
650.5 - <class 'float'>
800 - <class 'str'>
450 - <class 'int'>

flight_number - <class 'str'>
passengers - <class 'int'>
ticket_price - <class 'float'>
delayed - <class 'bool'>
