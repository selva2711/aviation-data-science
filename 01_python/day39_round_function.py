
# Day 39: Python round() Function
# Aviation Data Science

# Example 1: Basic rounding
ticket_price = 750.678

print(round(ticket_price))
print(round(ticket_price, 1))
print(round(ticket_price, 2))

print()

# Example 2: Round aviation costs
ticket_price = 1250.456
fuel_cost = 2450.789
airport_tax = 150.555

print("Ticket Price:", round(ticket_price, 2))
print("Fuel Cost:", round(fuel_cost, 2))
print("Airport Tax:", round(airport_tax, 2))

print()

# Example 3: Round multiple flight records
flights = [
    {"flight": "QR100", "price": 450.678},
    {"flight": "QR200", "price": 650.456},
    {"flight": "QR300", "price": 850.789}
]

for flight in flights:
    price = round(flight["price"], 2)

    print("Flight:", flight["flight"])
    print("Ticket Price:", price)
    print()

# Example 4: Calculate total ticket price
ticket_prices = [450.678, 650.456, 850.789]

total_price = sum(ticket_prices)
rounded_total = round(total_price, 2)

print("Total Ticket Price:", rounded_total)
print("Data Type:", type(rounded_total))

print()

# Example 5: Calculate flight costs
flights = [
    {"flight": "QR100", "ticket_price": 450.678, "fuel_cost": 1200.456},
    {"flight": "QR200", "ticket_price": 650.456, "fuel_cost": 1500.789},
    {"flight": "QR300", "ticket_price": 850.789, "fuel_cost": 1800.123}
]

for flight in flights:
    ticket_price = round(flight["ticket_price"], 2)
    fuel_cost = round(flight["fuel_cost"], 2)

    total_cost = round(ticket_price + fuel_cost, 2)

    print("Flight:", flight["flight"])
    print("Ticket Price:", ticket_price)
    print("Fuel Cost:", fuel_cost)
    print("Total Cost:", total_cost)
    print()

# Output

751
750.7
750.68

Ticket Price: 1250.46
Fuel Cost: 2450.79
Airport Tax: 150.56

Flight: QR100
Ticket Price: 450.68

Flight: QR200
Ticket Price: 650.46

Flight: QR300
Ticket Price: 850.79

Total Ticket Price: 1951.92
Data Type: <class 'float'>

Flight: QR100
Ticket Price: 450.68
Fuel Cost: 1200.46
Total Cost: 1651.14

Flight: QR200
Ticket Price: 650.46
Fuel Cost: 1500.79
Total Cost: 2151.25

Flight: QR300
Ticket Price: 850.79
Fuel Cost: 1800.12
Total Cost: 2650.91
