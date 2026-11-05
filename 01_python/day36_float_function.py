
# Day 36: Python float() Function
# Aviation Data Science

# Example 1: Convert string to float
ticket_price = "450.50"

price_number = float(ticket_price)

print(price_number)
print(type(price_number))

print()

# Example 2: Convert aviation data into floats
ticket_price = "750.25"
fuel_cost = "1250.75"

ticket_price = float(ticket_price)
fuel_cost = float(fuel_cost)

print(ticket_price + 50.50)
print(fuel_cost + 100.25)

print(type(ticket_price))
print(type(fuel_cost))

print()

# Example 3: Convert integer into float
passengers = 180
ticket_price = 650

passengers_float = float(passengers)
price_float = float(ticket_price)

print(passengers_float)
print(price_float)

print(type(passengers_float))
print(type(price_float))

print()

# Example 4: Convert flight record values
flight = {
    "flight_number": "QR900",
    "ticket_price": "750.50",
    "fuel_cost": "1250.75"
}

ticket_price = float(flight["ticket_price"])
fuel_cost = float(flight["fuel_cost"])

print("Flight:", flight["flight_number"])
print("Ticket Price:", ticket_price)
print("Fuel Cost:", fuel_cost)

print("Ticket Price Type:", type(ticket_price))
print("Fuel Cost Type:", type(fuel_cost))

print("Total Cost:", ticket_price + fuel_cost)

print()

# Example 5: Process multiple flight records
flights = [
    {"flight": "QR100", "ticket_price": "450.50"},
    {"flight": "QR200", "ticket_price": "650.75"},
    {"flight": "QR300", "ticket_price": "850.25"}
]

for flight in flights:
    price = float(flight["ticket_price"])

    print("Flight:", flight["flight"])
    print("Ticket Price:", price)
    print("Data Type:", type(price))
    print()

# Output

450.5
<class 'float'>

800.75
1351.0
<class 'float'>
<class 'float'>

180.0
650.0
<class 'float'>
<class 'float'>

Flight: QR900
Ticket Price: 750.5
Fuel Cost: 1250.75
Ticket Price Type: <class 'float'>
Fuel Cost Type: <class 'float'>
Total Cost: 2001.25

Flight: QR100
Ticket Price: 450.5
Data Type: <class 'float'>

Flight: QR200
Ticket Price: 650.75
Data Type: <class 'float'>

Flight: QR300
Ticket Price: 850.25
Data Type: <class 'float'>
