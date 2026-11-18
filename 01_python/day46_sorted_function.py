
# Day 46: Python sorted() Function
# Aviation Data Science Practice

# Example 1: Sort Flight Delays
flight_delays = [45, 15, 30, 10, 25]

sorted_delays = sorted(flight_delays)

print("Original Flight Delays:", flight_delays)
print("Sorted Flight Delays:", sorted_delays)


# Example 2: Sort Passenger Counts
passengers = [250, 180, 320, 150, 400]

sorted_passengers = sorted(passengers)

print("Original Passenger Counts:", passengers)
print("Sorted Passenger Counts:", sorted_passengers)


# Example 3: Sort Flight Numbers
flights = ["QR300", "QR100", "QR500", "QR200", "QR400"]

sorted_flights = sorted(flights)

print("Original Flights:", flights)
print("Sorted Flights:", sorted_flights)


# Example 4: Sort Flight Delays in Descending Order
flight_delays = [15, 45, 20, 60, 10]

sorted_delays = sorted(flight_delays, reverse=True)

print("Original Flight Delays:", flight_delays)
print("Descending Order:", sorted_delays)


# Example 5: Sort Delays from Flight Records
flights = [
    {"flight": "QR100", "delay": 45},
    {"flight": "QR200", "delay": 15},
    {"flight": "QR300", "delay": 60},
    {"flight": "QR400", "delay": 20},
    {"flight": "QR500", "delay": 10}
]

delays = []

for flight in flights:
    delays.append(flight["delay"])

sorted_delays = sorted(delays)

print("Original Delays:", delays)
print("Sorted Delays:", sorted_delays)

# Output

Original Flight Delays: [45, 15, 30, 10, 25]
Sorted Flight Delays: [10, 15, 25, 30, 45]

Original Passenger Counts: [250, 180, 320, 150, 400]
Sorted Passenger Counts: [150, 180, 250, 320, 400]

Original Flights: ['QR300', 'QR100', 'QR500', 'QR200', 'QR400']
Sorted Flights: ['QR100', 'QR200', 'QR300', 'QR400', 'QR500']

Original Flight Delays: [15, 45, 20, 60, 10]
Descending Order: [60, 45, 20, 15, 10]

Original Delays: [45, 15, 60, 20, 10]
Sorted Delays: [10, 15, 20, 45, 60]
