
# Day 33: Python bool() Function
# Aviation Data Science

# Example 1: Basic Boolean conversion
print("Number 1:", bool(1))
print("Number 0:", bool(0))
print("Empty String:", bool(""))
print("Flight Code:", bool("QR202"))

print()

# Example 2: Passenger availability
passengers = 0
print("Has Passengers:", bool(passengers))

print()

# Example 3: Flight number availability
flight_number = ""
print("Flight Number Available:", bool(flight_number))

print()

# Example 4: Passenger list availability
passenger_list = []
print("Passenger List Available:", bool(passenger_list))

print()

# Example 5: Flight status availability
flight_status = "On Time"
print("Flight Status Available:", bool(flight_status))

print()

# Example 6: Flight details
flight_details = {
    "flight": "QR202",
    "passengers": 180
}
print("Flight Details Available:", bool(flight_details))

# Output

Number 1: True
Number 0: False
Empty String: False
Flight Code: True

Has Passengers: False

Flight Number Available: False

Passenger List Available: False

Flight Status Available: True

Flight Details Available: True
