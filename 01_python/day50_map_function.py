
# Day 50: map() Function
# Aviation Data Science - Python Practice

# 1. Convert flight distances from KM to Miles
flight_distances = [100, 250, 500, 1000]

distances_miles = list(
    map(lambda km: round(km * 0.621371, 2), flight_distances)
)

# 2. Apply 5% discount to ticket prices
ticket_prices = [5000, 7500, 6000, 8000]

discounted_prices = list(
    map(lambda price: round(price * 0.95, 2), ticket_prices)
)

# 3. Convert flight delays from minutes to hours
delays_minutes = [60, 120, 90, 180]

delays_hours = list(
    map(lambda minutes: round(minutes / 60, 2), delays_minutes)
)

# Display Results
print("Flight Distances (Miles):", distances_miles)
print("Discounted Ticket Prices:", discounted_prices)
print("Flight Delays (Hours):", delays_hours)

# Output

Flight Distances (Miles): [62.14, 155.34, 310.69, 621.37]
Discounted Ticket Prices: [4750.0, 7125.0, 5700.0, 7600.0]
Flight Delays (Hours): [1.0, 2.0, 1.5, 3.0]
