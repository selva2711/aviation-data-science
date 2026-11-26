# Day 51: filter(), any() and all()
# Aviation Data Science - Python Practice

# Example 1: Flight Delay Analysis

flight_delays = [15, 45, 90, 120, 30]

# Filter flights delayed more than 60 minutes
delayed_flights = list(
    filter(lambda minutes: minutes > 60, flight_delays)
)

# Check whether any flight is delayed more than 100 minutes
any_long_delay = any(
    minutes > 100 for minutes in flight_delays
)

# Check whether all flight delays are valid
all_valid_delays = all(
    minutes >= 0 for minutes in flight_delays
)

print("All Flight Delays:", flight_delays)
print("Flights Delayed More Than 60 Minutes:", delayed_flights)
print("Any Flight Delayed More Than 100 Minutes:", any_long_delay)
print("All Flight Delays Are Valid:", all_valid_delays)


# Example 2: Airline Ticket Price Analysis

ticket_prices = [5000, 8500, 12000, 6500, 9500]

# Filter ticket prices above 7000
expensive_tickets = list(
    filter(lambda price: price > 7000, ticket_prices)
)

# Check whether any ticket price is above 10000
any_high_price = any(
    price > 10000 for price in ticket_prices
)

# Check whether all ticket prices are positive
all_prices_valid = all(
    price > 0 for price in ticket_prices
)

print("All Ticket Prices:", ticket_prices)
print("Tickets Above 7000:", expensive_tickets)
print("Any Ticket Above 10000:", any_high_price)
print("All Ticket Prices Are Valid:", all_prices_valid)

# Output

All Flight Delays: [15, 45, 90, 120, 30]
Flights Delayed More Than 60 Minutes: [90, 120]
Any Flight Delayed More Than 100 Minutes: True
All Flight Delays Are Valid: True
All Ticket Prices: [5000, 8500, 12000, 6500, 9500]
Tickets Above 7000: [8500, 12000, 9500]
Any Ticket Above 10000: True
All Ticket Prices Are Valid: True
