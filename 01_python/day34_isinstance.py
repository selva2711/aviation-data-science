
# Day 34: Python isinstance() Function
# Aviation Data Science

# Example 1: Basic data type checks
flight_number = "QR202"
passengers = 180
ticket_price = 450.50

print("Flight Number is String:", isinstance(flight_number, str))
print("Passengers is Integer:", isinstance(passengers, int))
print("Ticket Price is Float:", isinstance(ticket_price, float))

print()

# Example 2: Check passenger count type
passengers = "180"

if isinstance(passengers, int):
    print("Passenger Count is Valid Type")
else:
    print("Passenger Count has Wrong Type")

print()

# Example 3: Validate all passenger counts
passenger_counts = [180, "220", 150, 200]

all_integers = all(
    isinstance(count, int) for count in passenger_counts
)

print("All Passenger Counts Are Integers:", all_integers)

print()

# Example 4: Validate flight records
flights = [
    ("QR100", 180),
    ("QR200", "220"),
    ("QR300", 150)
]

for flight_number, passengers in flights:
    if isinstance(flight_number, str) and isinstance(passengers, int):
        print(flight_number, "- Data Types Correct")
    else:
        print(flight_number, "- Check Data Types")

# Output

Flight Number is String: True
Passengers is Integer: True
Ticket Price is Float: True

Passenger Count has Wrong Type

All Passenger Counts Are Integers: False

QR100 - Data Types Correct
QR200 - Check Data Types
QR300 - Data Types Correct
