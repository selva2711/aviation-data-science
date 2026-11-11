
# Day 42: Python max() Function
# Aviation Data Science

# Example 1: Passenger comparison
passengers = [180, 250, 320]

highest = max(passengers)

print("Passenger Counts:", passengers)
print("Highest Passengers:", highest)

print()

# Example 2: Flight delay comparison
delays = [15, 45, 20]

highest_delay = max(delays)

print("Flight Delays:", delays)
print("Highest Delay:", highest_delay, "minutes")

print()

# Example 3: Temperature comparison
temperatures = [22.5, 25.8, 24.2]

highest_temperature = max(temperatures)

print("Cabin Temperatures:", temperatures)
print("Highest Temperature:", highest_temperature)

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

highest = max(passenger_counts)

print("Passenger Counts:", passenger_counts)
print("Highest Passengers:", highest)

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

print("Highest Passengers:", max(passengers))
print("Highest Delay:", max(delays), "minutes")
print("Highest Temperature:", max(temperatures))

# Output

Passenger Counts: [180, 250, 320]
Highest Passengers: 320

Flight Delays: [15, 45, 20]
Highest Delay: 45 minutes

Cabin Temperatures: [22.5, 25.8, 24.2]
Highest Temperature: 25.8

Passenger Counts: [180, 250, 320]
Highest Passengers: 320

Highest Passengers: 320
Highest Delay: 45 minutes
Highest Temperature: 25.8
