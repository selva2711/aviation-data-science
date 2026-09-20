# Day 9 - Python List Operations

morning_flights = ["QR170", "QR500"]
evening_flights = ["QR700", "QR900"]

all_flights = morning_flights + evening_flights

print("All Flights:", all_flights)

print("QR500 Available:", "QR500" in all_flights)

print("QR300 Available:", "QR300" in all_flights)

print("QR300 Not Available:", "QR300" not in all_flights)

# Output

All Flights: ['QR170', 'QR500', 'QR700', 'QR900']
QR500 Available: True
QR300 Available: False
QR300 Not Available: True
