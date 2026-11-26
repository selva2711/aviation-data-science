
# Day 51: filter(), any() and all()

## Overview
Today, I learned how to filter data based on conditions and check whether some or all values satisfy a condition using Python.

I practiced these concepts with aviation-related examples such as flight delay analysis and airline ticket price analysis.

## 🧠 Topics Covered
- Understanding the filter() function
- Using lambda with filter()
- Understanding the any() function
- Understanding the all() function
- Filtering values based on conditions
- Checking conditions in lists

## ✈️ Aviation Examples
- Filtering flights delayed more than 60 minutes
- Checking whether any flight is delayed more than 100 minutes
- Checking whether all flight delays are valid
- Filtering ticket prices above ₹7,000
- Checking whether any ticket price is above ₹10,000
- Checking whether all ticket prices are positive

## 📖 Example

```python
flight_delays = [15, 45, 90, 120, 30]

delayed_flights = list(
    filter(lambda minutes: minutes > 60, flight_delays)
)

any_long_delay = any(
    minutes > 100 for minutes in flight_delays
)

all_valid_delays = all(
    minutes >= 0 for minutes in flight_delays
)

print("Flights Delayed More Than 60 Minutes:", delayed_flights)
print("Any Flight Delayed More Than 100 Minutes:", any_long_delay)
print("All Flight Delays Are Valid:", all_valid_delays)
```

## Output

```text
Flights Delayed More Than 60 Minutes: [90, 120]
Any Flight Delayed More Than 100 Minutes: True
All Flight Delays Are Valid: True
```

## 🔑 Key Learning

- filter() selects values that satisfy a given condition.
- any() returns True if at least one value satisfies a condition.
- all() returns True only if every value satisfies a condition.
- lambda can be used with filter() to create short functions.

## 🚀 Progress
- Learned filter().
- Learned any().
- Learned all().
- Practiced aviation-related examples.
- Completed Day 51 practice exercises.

## Conclusion
Today, I learned how to filter aviation data and check conditions using Python's filter(), any(), and all() functions.

These concepts are useful for analyzing flight delays, ticket prices, and airline operational data.
