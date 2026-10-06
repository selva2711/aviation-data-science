# Day 20 - *args in Python

# 1. Using *args with Flight Numbers
def show_flights(*flights):
    for flight in flights:
        print("Flight:", flight)

show_flights("QR170", "QR500", "QR700", "QR800")

print()

# 2. Using *args with Passenger Counts
def total_passengers(*passengers):
    total = 0

    for count in passengers:
        total = total + count

    return total

print("Total Passengers:", total_passengers(100, 150, 200))

print()

# 3. Final Aviation Practice
def show_flight_passengers(*flights):
    for flight in flights:
        print("Flight:", flight)

show_flight_passengers("QR170", "QR500", "QR700", "QR800")

print()

def calculate_total_passengers(*passengers):
    total = 0

    for count in passengers:
        total = total + count

    return total

print("Total Passengers:", calculate_total_passengers(120, 150, 180))

# Output

Flight: QR170
Flight: QR500
Flight: QR700
Flight: QR800

Total Passengers: 450

Flight: QR170
Flight: QR500
Flight: QR700
Flight: QR800

Total Passengers: 450
