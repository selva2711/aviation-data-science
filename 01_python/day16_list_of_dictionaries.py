# Day 16 - List of Dictionaries

flights = [
    {
        "flight_number": "QR170",
        "origin": "Doha",
        "destination": "Mumbai"
    },
    {
        "flight_number": "QR500",
        "origin": "Doha",
        "destination": "Chennai"
    },
    {
        "flight_number": "QR700",
        "origin": "Doha",
        "destination": "London"
    }
]

# Access individual dictionaries
print("First Flight:", flights[0])
print("Second Flight:", flights[1])
print("Third Flight:", flights[2])

# Access specific values
print("First Flight Number:", flights[0]["flight_number"])
print("First Destination:", flights[0]["destination"])

print("Second Flight Number:", flights[1]["flight_number"])
print("Second Destination:", flights[1]["destination"])

# Loop through all flights
for flight in flights:
    print(
        flight["flight_number"],
        flight["origin"],
        "→",
        flight["destination"]
    )

# Find a specific flight
for flight in flights:
    if flight["flight_number"] == "QR500":
        print("Flight Found:", flight)

# Find a flight by destination
for flight in flights:
    if flight["destination"] == "Chennai":
        print("Chennai Flight:", flight)

# Output

First Flight: {'flight_number': 'QR170', 'origin': 'Doha', 'destination': 'Mumbai'}
Second Flight: {'flight_number': 'QR500', 'origin': 'Doha', 'destination': 'Chennai'}
Third Flight: {'flight_number': 'QR700', 'origin': 'Doha', 'destination': 'London'}

First Flight Number: QR170
First Destination: Mumbai
Second Flight Number: QR500
Second Destination: Chennai

QR170 Doha → Mumbai
QR500 Doha → Chennai
QR700 Doha → London

Flight Found: {'flight_number': 'QR500', 'origin': 'Doha', 'destination': 'Chennai'}

Chennai Flight: {'flight_number': 'QR500', 'origin': 'Doha', 'destination': 'Chennai'}
