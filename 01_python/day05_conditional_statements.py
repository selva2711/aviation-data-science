# Day 5 - Python Conditional Statements
# Aviation Data Science Learning Journey

# If and Else
passengers = 280

if passengers > 250:
    print("High passenger count")
else:
    print("Normal passenger count")


# Checking Available Seats
available_seats = 40

if available_seats > 50:
    print("Seats available")
else:
    print("Limited seats")


# If, Elif and Else
delay_minutes = 45

if delay_minutes == 0:
    print("On Time")
elif delay_minutes <= 30:
    print("Slight Delay")
else:
    print("Major Delay")

# Output
High passenger count
Limited seats
Major Delay
