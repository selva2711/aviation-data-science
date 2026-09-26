# Day 15 - Looping Through a Dictionary
# Aviation Data Science Learning

flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR170",
    "origin": "Doha",
    "destination": "Mumbai",
    "passengers": 280,
    "aircraft": "A350"
}

# Loop through dictionary keys
for key in flight:
    print(key)

# Loop through dictionary values
for value in flight.values():
    print(value)

# Loop through key-value pairs
for key, value in flight.items():
    print(key, ":", value)

# Find specific information using a condition
for key, value in flight.items():
    if key == "passengers":
        print("Total Passengers:", value)

for key, value in flight.items():
    if key == "aircraft":
        print("Aircraft Type:", value)

# Output

airline
flight_number
origin
destination
passengers
aircraft

Qatar Airways
QR170
Doha
Mumbai
280
A350

airline : Qatar Airways
flight_number : QR170
origin : Doha
destination : Mumbai
passengers : 280
aircraft : A350

Total Passengers: 280
Aircraft Type: A350
