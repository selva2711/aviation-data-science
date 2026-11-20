
# Day 47: Python reversed() Function
# Aviation Data Science Practice

# Example 1: Reverse Flight Numbers
flights = ["QR100", "QR200", "QR300", "QR400", "QR500"]

reverse_flights = list(reversed(flights))

print("Original Flights:", flights)
print("Reversed Flights:", reverse_flights)


# Example 2: Reverse Passenger Names
passengers = ["Arun", "Priya", "David", "Sara", "John"]

reverse_passengers = list(reversed(passengers))

print("Original Passengers:", passengers)
print("Reversed Passengers:", reverse_passengers)


# Example 3: Reverse Flight Delays
flight_delays = [15, 30, 45, 60, 20]

reverse_delays = list(reversed(flight_delays))

print("Original Flight Delays:", flight_delays)
print("Reversed Flight Delays:", reverse_delays)


# Example 4: Reverse a String
flight_number = "QATAR"

reverse_text = "".join(reversed(flight_number))

print("Original Airline Name:", flight_number)
print("Reversed Airline Name:", reverse_text)


# Example 5: Reverse Flight Records
flights = [
    {"flight": "QR100", "delay": 15},
    {"flight": "QR200", "delay": 30},
    {"flight": "QR300", "delay": 45},
    {"flight": "QR400", "delay": 60},
    {"flight": "QR500", "delay": 20}
]

flight_numbers = []

for flight in flights:
    flight_numbers.append(flight["flight"])

reverse_flights = list(reversed(flight_numbers))

print("Original Flights:", flight_numbers)
print("Reversed Flights:", reverse_flights)

# Output

Original Flights: ['QR100', 'QR200', 'QR300', 'QR400', 'QR500']
Reversed Flights: ['QR500', 'QR400', 'QR300', 'QR200', 'QR100']

Original Passengers: ['Arun', 'Priya', 'David', 'Sara', 'John']
Reversed Passengers: ['John', 'Sara', 'David', 'Priya', 'Arun']

Original Flight Delays: [15, 30, 45, 60, 20]
Reversed Flight Delays: [20, 60, 45, 30, 15]

Original Airline Name: QATAR
Reversed Airline Name: RATAQ

Original Flights: ['QR100', 'QR200', 'QR300', 'QR400', 'QR500']
Reversed Flights: ['QR500', 'QR400', 'QR300', 'QR200', 'QR100']
