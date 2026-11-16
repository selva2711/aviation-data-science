
# Day 44: Python sum() Function
# Aviation Data Science Practice

# Example 1: Total Passengers
passengers = [180, 250, 320]

total_passengers = sum(passengers)

print("Passenger Counts:", passengers)
print("Total Passengers:", total_passengers)


# Example 2: Total Ticket Revenue
ticket_prices = [5000, 7500, 6000]

total_revenue = sum(ticket_prices)

print("Ticket Prices:", ticket_prices)
print("Total Revenue:", total_revenue)


# Example 3: Total Passengers from Flight Records
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320}
]

passenger_counts = []

for flight in flights:
    passenger_counts.append(flight["passengers"])

total_passengers = sum(passenger_counts)

print("Passenger Counts:", passenger_counts)
print("Total Passengers:", total_passengers)


# Example 4: Total Flight Delays
flight_delays = [15, 45, 20]

total_delay = sum(flight_delays)

print("Flight Delays:", flight_delays)
print("Total Delay:", total_delay, "minutes")


# Example 5: Total Passengers from Five Flights
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320},
    {"flight": "QR400", "passengers": 400},
    {"flight": "QR500", "passengers": 300}
]

passenger_counts = []

for flight in flights:
    passenger_counts.append(flight["passengers"])

total_passengers = sum(passenger_counts)

print("Passenger Counts:", passenger_counts)
print("Total Passengers:", total_passengers)

# Output

Passenger Counts: [180, 250, 320]
Total Passengers: 750
Ticket Prices: [5000, 7500, 6000]
Total Revenue: 18500
Passenger Counts: [180, 250, 320]
Total Passengers: 750
Flight Delays: [15, 45, 20]
Total Delay: 80 minutes
Passenger Counts: [180, 250, 320, 400, 300]
Total Passengers: 1450
