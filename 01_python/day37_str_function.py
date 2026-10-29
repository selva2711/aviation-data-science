
# Day 37: Python str() Function
# Aviation Data Science

# Example 1: Convert integers to strings
passengers = 250
flight_number = 700

passengers_text = str(passengers)
flight_text = str(flight_number)

print(passengers_text)
print(type(passengers_text))

print(flight_text)
print(type(flight_text))

print()

# Example 2: Combine text and numbers
flight_number = 202
passengers = 180

print("QR" + str(flight_number))
print("Passengers: " + str(passengers))

print()

# Example 3: Flight details
flight_number = 900
passengers = 220
ticket_price = 650.50

print("Flight: QR" + str(flight_number))
print("Passengers: " + str(passengers))
print("Ticket Price: $" + str(ticket_price))

print()

# Example 4: Combine multiple aviation values
flight_number = 700
passengers = 240
gate_number = 12

print("QR" + str(flight_number) + " | Passengers: " + str(passengers) + " | Gate: " + str(gate_number))

# Output

250
<class 'str'>
700
<class 'str'>

QR202
Passengers: 180

Flight: QR900
Passengers: 220
Ticket Price: $650.5

QR700 | Passengers: 240 | Gate: 12
