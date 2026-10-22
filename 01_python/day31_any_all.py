
# Day 31: any() and all()
# Aviation Data Science

# Example 1: Flight delay status
flight_status = [True, False, True, True]

print("Any Flight Delayed:", any(flight_status))
print("All Flights Delayed:", all(flight_status))

print()

# Example 2: Flight delay minutes
flight_delays = [5, 45, 10, 0]

major_delay = any(delay >= 30 for delay in flight_delays)
all_delayed = all(delay > 0 for delay in flight_delays)

print("Major Delay Detected:", major_delay)
print("All Flights Delayed:", all_delayed)

print()

# Example 3: Safety alerts
safety_alerts = [False, False, True]

print("Safety Alert Detected:", any(safety_alerts))
print("All Flights Have Alerts:", all(safety_alerts))

# Output

Any Flight Delayed: True
All Flights Delayed: False

Major Delay Detected: True
All Flights Delayed: False

Safety Alert Detected: True
All Flights Have Alerts: False
