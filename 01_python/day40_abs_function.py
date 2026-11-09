
# Day 40: Python abs() Function
# Aviation Data Science

# Example 1: Basic absolute values
delay_minutes = -25
temperature_difference = -4.5
distance_difference = 120

print(abs(delay_minutes))
print(abs(temperature_difference))
print(abs(distance_difference))

print()

# Example 2: Flight schedule differences
flight_1_delay = -15
flight_2_delay = 30
flight_3_delay = -8

print("Flight QR100:", abs(flight_1_delay), "minutes")
print("Flight QR200:", abs(flight_2_delay), "minutes")
print("Flight QR300:", abs(flight_3_delay), "minutes")

print()

# Example 3: Temperature differences
cabin_difference = -3.5
outside_difference = -12.8
engine_difference = 5.6

print("Cabin Temperature Difference:", abs(cabin_difference))
print("Outside Temperature Difference:", abs(outside_difference))
print("Engine Temperature Difference:", abs(engine_difference))

print()

# Example 4: Airport distance differences
flight_1_distance = -150.5
flight_2_distance = 275.8
flight_3_distance = -90.25

print("Flight QR100 Distance:", abs(flight_1_distance), "km")
print("Flight QR200 Distance:", abs(flight_2_distance), "km")
print("Flight QR300 Distance:", abs(flight_3_distance), "km")

print()

# Example 5: Process multiple flight records
flights = [
    {"flight": "QR100", "time_difference": -15, "temperature": -3.5},
    {"flight": "QR200", "time_difference": 30, "temperature": -5.8},
    {"flight": "QR300", "time_difference": -8, "temperature": 2.5}
]

for flight in flights:
    time_diff = abs(flight["time_difference"])
    temp_diff = abs(flight["temperature"])

    print("Flight:", flight["flight"])
    print("Time Difference:", time_diff, "minutes")
    print("Temperature Difference:", temp_diff)
    print()

# Output

25
4.5
120

Flight QR100: 15 minutes
Flight QR200: 30 minutes
Flight QR300: 8 minutes

Cabin Temperature Difference: 3.5
Outside Temperature Difference: 12.8
Engine Temperature Difference: 5.6

Flight QR100 Distance: 150.5 km
Flight QR200 Distance: 275.8 km
Flight QR300 Distance: 90.25 km

Flight: QR100
Time Difference: 15 minutes
Temperature Difference: 3.5

Flight: QR200
Time Difference: 30 minutes
Temperature Difference: 5.8

Flight: QR300
Time Difference: 8 minutes
Temperature Difference: 2.5
