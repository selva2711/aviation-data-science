
# Day 29: Python min() and max()
# Aviation Data Science Practice

flight_passengers = [
    ("QR170", 180),
    ("QR500", 250),
    ("QR700", 120),
    ("QR900", 300)
]

lowest_flight = min(
    flight_passengers,
    key=lambda flight: flight[1]
)

highest_flight = max(
    flight_passengers,
    key=lambda flight: flight[1]
)

print("Flight with Fewest Passengers:", lowest_flight)
print("Flight with Most Passengers:", highest_flight)

# Output


Flight with Fewest Passengers: ('QR700', 120)
Flight with Most Passengers: ('QR900', 300)
