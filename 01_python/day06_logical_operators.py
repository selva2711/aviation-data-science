# Day 6 - Python Logical Operators

passengers = 280
available_seats = 40

if passengers > 250 and available_seats < 50:
    print("Flight is busy")


passengers = 180
available_seats = 40

if passengers > 300 or available_seats < 50:
    print("Special attention")


flight_delayed = False

print(not flight_delayed)

# Output

Flight is busy
Special attention
True
