# Day 21 - **kwargs in Python

# 1. Basic **kwargs
def flight_details(**details):
    print(details)

flight_details(
    flight_number="QR170",
    origin="Doha",
    destination="Mumbai"
)

print()

# 2. **kwargs with for loop
def display_flight_details(**details):
    for key, value in details.items():
        print(key, ":", value)

display_flight_details(
    flight_number="QR170",
    origin="Doha",
    destination="Mumbai"
)

print()

# 3. Multiple Keyword Arguments
display_flight_details(
    flight_number="QR500",
    airline="Qatar Airways",
    origin="Doha",
    destination="Chennai",
    aircraft="Boeing 777"
)

print()

# 4. **kwargs with Condition
def check_route(**details):
    print("Flight:", details["flight_number"])
    print("Destination:", details["destination"])

    if details["destination"] == "Chennai":
        print("Status: Chennai Route")

check_route(
    flight_number="QR500",
    origin="Doha",
    destination="Chennai"
)

print()

# 5. Final Practice
def flight_information(**details):
    print("Flight Number:", details["flight_number"])
    print("Airline:", details["airline"])
    print("Origin:", details["origin"])
    print("Destination:", details["destination"])

    if details["destination"] == "London":
        print("Route: International")

    print()

    print("All Details:")
    for key, value in details.items():
        print(key, ":", value)

flight_information(
    flight_number="QR700",
    airline="Qatar Airways",
    origin="Doha",
    destination="London"
)

# Output

{'flight_number': 'QR170', 'origin': 'Doha', 'destination': 'Mumbai'}

flight_number : QR170
origin : Doha
destination : Mumbai

flight_number : QR500
airline : Qatar Airways
origin : Doha
destination : Chennai
aircraft : Boeing 777

Flight: QR500
Destination: Chennai
Status: Chennai Route

Flight Number: QR700
Airline: Qatar Airways
Origin: Doha
Destination: London
Route: International

All Details:
flight_number : QR700
airline : Qatar Airways
origin : Doha
destination : London
