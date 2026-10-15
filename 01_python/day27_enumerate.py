# Day 27: Python enumerate()
# Aviation Data Science Practice

flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [180, 220, 150]

total_passengers = 0

for index, (flight, count) in enumerate(
    zip(flight_numbers, passengers), start=1
):
    print("Flight No:", index)
    print("Flight:", flight)
    print("Passengers:", count)
    print()

    total_passengers += count

print("Total Passengers:", total_passengers)

# Output


Flight No: 1
Flight: QR170
Passengers: 180

Flight No: 2
Flight: QR500
Passengers: 220

Flight No: 3
Flight: QR700
Passengers: 150

Total Passengers: 550

