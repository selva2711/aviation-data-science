
# Day 38: Python int() Function
# Aviation Data Science

# Example 1: Convert string to integer
passengers = "250"
passengers_number = int(passengers)

print(passengers_number)
print(type(passengers_number))

print()

# Example 2: Convert flight data into integers
flight_number = "202"
passengers = "180"

flight_number = int(flight_number)
passengers = int(passengers)

print(flight_number + 10)
print(passengers + 20)

print(type(flight_number))
print(type(passengers))

print()

# Example 3: Convert float into integer
ticket_price = 650.75
passengers = 180.90

price_number = int(ticket_price)
passenger_number = int(passengers)

print(price_number)
print(passenger_number)

print(type(price_number))
print(type(passenger_number))

print()

# Example 4: Convert flight record values
flight = {
    "flight_number": "QR900",
    "passengers": "220",
    "ticket_price": 750.50
}

passengers = int(flight["passengers"])

print("Flight:", flight["flight_number"])
print("Passengers:", passengers)
print("Passenger Type:", type(passengers))
print("Total after adding 10:", passengers + 10)

print()

# Example 5: Process multiple flight records
flights = [
    {"flight": "QR100", "passengers": "180"},
    {"flight": "QR200", "passengers": "220"},
    {"flight": "QR300", "passengers": "150"}
]

for flight in flights:
    passengers = int(flight["passengers"])

    print("Flight:", flight["flight"])
    print("Passengers:", passengers)
    print("Data Type:", type(passengers))
    print()

# Output

250
<class 'int'>

212
200
<class 'int'>
<class 'int'>

650
180
<class 'int'>
<class 'int'>

Flight: QR900
Passengers: 220
Passenger Type: <class 'int'>
Total after adding 10: 230

Flight: QR100
Passengers: 180
Data Type: <class 'int'>

Flight: QR200
Passengers: 220
Data Type: <class 'int'>

Flight: QR300
Passengers: 150
Data Type: <class 'int'>
