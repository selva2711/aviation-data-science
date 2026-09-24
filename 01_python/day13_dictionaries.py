# Day 13 - Python Dictionaries
# Aviation Data Science Learning

flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR700",
    "origin": "Doha",
    "destination": "London",
    "passengers": 250
}

# Access dictionary values
print("Airline:", flight["airline"])
print("Flight Number:", flight["flight_number"])
print("Origin:", flight["origin"])
print("Destination:", flight["destination"])
print("Passengers:", flight["passengers"])

# Change a value
flight["passengers"] = 275

# Add new key-value pairs
flight["aircraft"] = "A350"

# Remove a key-value pair
del flight["origin"]

# Dictionary length
print("Updated Flight:", flight)
print("Total Details:", len(flight))

# Check whether keys exist
print("aircraft" in flight)
print("origin" in flight)
