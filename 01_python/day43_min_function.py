
# Day 43: Python min() Function
# Aviation Data Science

# Example 1: Passenger comparison
passengers = [180, 250, 320]

lowest = min(passengers)

print("Passenger Counts:", passengers)
print("Lowest Passengers:", lowest)

print()

# Example 2: Flight delay comparison
delays = [15, 45, 20]

lowest_delay = min(delays)

print("Flight Delays:", delays)
print("Lowest Delay:", lowest_delay, "minutes")

print()

# Example 3: Temperature comparison
temperatures = [22.5, 25.8, 24.2]

lowest_temperature = min(temperatures)

print("Cabin Temperatures:", temperatures)
print("Lowest Temperature:", lowest_temperature)

print()

# Example 4: Multiple flight records
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320}
]

passenger_counts = []

for flight in flights:
    passenger_counts.append(flight["passengers"])

lowest = min(passenger_counts)

print("Passenger Counts:", passenger_counts)
print("Lowest Passengers:", lowest)

print()

# Example 5: Final aviation practice
flights = [
    {"flight": "QR100", "passengers": 180, "delay": 15, "temperature": 22.5},
    {"flight": "QR200", "passengers": 250, "delay": 45, "temperature": 25.8},
    {"flight": "QR300", "passengers": 320, "delay": 20, "temperature": 24.2}
]

passengers = []
delays = []
temperatures = []

for flight in flights:
    passengers.append(flight["passengers"])
    delays.append(flight["delay"])
    temperatures.append(flight["temperature"])

print("Lowest Passengers:", min(passengers))
print("Lowest Delay:", min(delays), "minutes")
print("Lowest Temperature:", min(temperatures))

# Output

Passenger Counts: [180, 250, 320]
Lowest Passengers: 180

Flight Delays: [15, 45, 20]
Lowest Delay: 15 minutes

Cabin Temperatures: [22.5, 25.8, 24.2]
Lowest Temperature: 22.5

Passenger Counts: [180, 250, 320]
Lowest Passengers: 180

Lowest Passengers: 180
Lowest Delay: 15 minutes
Lowest Temperature: 22.5
