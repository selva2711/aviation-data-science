
# Day 45: Python len() Function
# Aviation Data Science Practice

# Example 1: Count Passengers
passengers = ["Arun", "Priya", "David", "Sara", "John"]

total_passengers = len(passengers)

print("Passenger List:", passengers)
print("Total Passengers:", total_passengers)


# Example 2: Count Flight Numbers
flights = ["QR100", "QR200", "QR300", "QR400"]

total_flights = len(flights)

print("Flight Numbers:", flights)
print("Total Flights:", total_flights)


# Example 3: Count Seven Passengers
passengers = [
    "Arun", "Priya", "David", "Sara",
    "John", "Meena", "Robert"
]

print("Passenger List:", passengers)
print("Total Passengers:", len(passengers))


# Example 4: Count Characters in Flight Number
flight_number = "QR100"

total_characters = len(flight_number)

print("Flight Number:", flight_number)
print("Total Characters:", total_characters)


# Example 5: Count Flights Using Flight Records
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320},
    {"flight": "QR400", "passengers": 400},
    {"flight": "QR500", "passengers": 300},
    {"flight": "QR600", "passengers": 400}
]

flight_numbers = []

for flight in flights:
    flight_numbers.append(flight["flight"])

total_flights = len(flight_numbers)

print("Flight Numbers:", flight_numbers)
print("Total Flights:", total_flights)

# Output

Passenger List: ['Arun', 'Priya', 'David', 'Sara', 'John']
Total Passengers: 5
Flight Numbers: ['QR100', 'QR200', 'QR300', 'QR400']
Total Flights: 4
Passenger List: ['Arun', 'Priya', 'David', 'Sara', 'John', 'Meena', 'Robert']
Total Passengers: 7
Flight Number: QR100
Total Characters: 5
Flight Numbers: ['QR100', 'QR200', 'QR300', 'QR400', 'QR500', 'QR600']
Total Flights: 6
