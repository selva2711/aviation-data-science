
# Day 32: Python all() Function
# Aviation Data Science

# Example 1: Pre-flight checks
pre_flight_checks = [True, True, True, True, True]

print("All Checks Passed:", all(pre_flight_checks))

print()

# Example 2: Check flight delays
flight_delays = [5, 10, 35, 15]

all_delays_acceptable = all(
    delay < 30 for delay in flight_delays
)

print("All Delays Under 30 Minutes:", all_delays_acceptable)

print()

# Example 3: Passenger count check
passengers = [120, 150, 80, 180]

all_above_100 = all(
    count >= 100 for count in passengers
)

print("All Flights Have 100+ Passengers:", all_above_100)

print()

# Example 4: Combine any() and all()
flight_numbers = ["QR100", "QR200", "QR300"]
flight_delays = [10, 35, 15]

for flight, delay in zip(flight_numbers, flight_delays):
    print(flight, "-", delay, "minutes")

any_delayed = any(delay > 0 for delay in flight_delays)
all_under_30 = all(delay < 30 for delay in flight_delays)

print("Any Flight Delayed:", any_delayed)
print("All Flights Under 30 Minutes:", all_under_30)

# Output

All Checks Passed: True

All Delays Under 30 Minutes: False

All Flights Have 100+ Passengers: False

QR100 - 10 minutes
QR200 - 35 minutes
QR300 - 15 minutes
Any Flight Delayed: True
All Flights Under 30 Minutes: False
