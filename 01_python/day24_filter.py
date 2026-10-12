```python
# Day 24: Python filter() Function
# Aviation Data Science Practice

# Example 1: Filter expensive tickets
ticket_prices = [500, 1200, 800, 1500, 900, 2000]

def expensive_ticket(price):
    return price > 1000

filtered_prices = list(
    filter(expensive_ticket, ticket_prices)
)

print("Original Prices:", ticket_prices)
print("Filtered Prices:", filtered_prices)

print()

# Example 2: Filter with lambda
ticket_prices = [500, 1200, 800, 1500, 900, 2000]

expensive_tickets = list(
    filter(lambda price: price > 1000, ticket_prices)
)

print("Original Prices:", ticket_prices)
print("Expensive Tickets:", expensive_tickets)

print()

# Example 3: Filter on-time flights
flight_delays = [0, 15, 0, 30, 10, 0]

on_time_flights = list(
    filter(lambda delay: delay == 0, flight_delays)
)

print("All Flight Delays:", flight_delays)
print("On-Time Flights:", on_time_flights)

print()

# Example 4: Filter delayed flights
flight_delays = [0, 15, 0, 30, 10, 25]

delayed_flights = list(
    filter(lambda delay: delay >= 15, flight_delays)
)

print("All Flight Delays:", flight_delays)
print("Delayed Flights:", delayed_flights)

print()

# Example 5: Filter passenger counts
passengers = [150, 250, 180, 320, 200, 400]

high_passenger_flights = list(
    filter(lambda count: count > 200, passengers)
)

print("All Passenger Counts:", passengers)
print("High Passenger Counts:", high_passenger_flights)

print()

# Example 6: Filter tickets and calculate total
ticket_prices = [500, 1000, 1500, 800, 2000, 1200]

expensive_tickets = list(
    filter(lambda price: price >= 1000, ticket_prices)
)

print("All Ticket Prices:", ticket_prices)
print("Expensive Tickets:", expensive_tickets)
print("Total of Expensive Tickets:", sum(expensive_tickets))
```

# Output

```text
Original Prices: [500, 1200, 800, 1500, 900, 2000]
Filtered Prices: [1200, 1500, 2000]

Original Prices: [500, 1200, 800, 1500, 900, 2000]
Expensive Tickets: [1200, 1500, 2000]

All Flight Delays: [0, 15, 0, 30, 10, 0]
On-Time Flights: [0, 0, 0]

All Flight Delays: [0, 15, 0, 30, 10, 25]
Delayed Flights: [15, 30, 25]

All Passenger Counts: [150, 250, 180, 320, 200, 400]
High Passenger Counts: [250, 320, 400]

All Ticket Prices: [500, 1000, 1500, 800, 2000, 1200]
Expensive Tickets: [1000, 1500, 2000, 1200]
Total of Expensive Tickets: 5700
```
