# Day 14 - Python Dictionary Methods
# Aviation Data Science Learning

flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR170",
    "origin": "Doha",
    "destination": "Mumbai",
    "passengers": 250
}

# Get dictionary keys
print("Keys:", flight.keys())

# Get dictionary values
print("Values:", flight.values())

# Get key-value pairs
print("Items:", flight.items())

# Safely get a value
print("Destination:", flight.get("destination"))
print("Aircraft:", flight.get("aircraft"))

# Update existing values and add a new key-value pair
flight.update({
    "destination": "Chennai",
    "passengers": 280,
    "aircraft": "A350"
})

print("Updated Flight:", flight)

# Output

Keys: dict_keys(['airline', 'flight_number', 'origin', 'destination', 'passengers']) 

Values: dict_values(['Qatar Airways', 'QR170', 'Doha', 'Mumbai', 250]) 

Items: dict_items([('airline', 'Qatar Airways'), ('flight_number', 'QR170'), ('origin', 'Doha'), ('destination', 'Mumbai'), ('passengers', 250)]) 

Destination: Mumbai 

Aircraft: None 

Updated Flight: {'airline': 'Qatar Airways', 'flight_number': 'QR170', 'origin': 'Doha', 'destination': 'Chennai', 'passengers': 280, 'aircraft': 'A350'}
