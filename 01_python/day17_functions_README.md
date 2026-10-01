# Day 17 - Functions

## 📌 Topic

Functions in Python

## 📖 What I Learned

Today I learned how to create and use functions in Python.

Functions help organize code into reusable blocks that can perform specific tasks.

```python
## 🔑 Key Concepts

### 1. Creating a Function

def greetings():
    print("Welcome to Aviation Data Science")

greetings()

The def keyword is used to create a function.

### 2. Function with a Parameter

def welcome_airline(airline):
    print("Welcome to", airline)

welcome_airline("Qatar Airways")

A parameter allows us to pass data into a function.

### 3. Multiple Parameters

def flight_route(flight_number, destination, origin):
    print("Flight:", flight_number)
    print("Destination:", destination)
    print("Origin:", origin)

A function can have multiple parameters.

### 4. Using return

def calculate_seats(passengers, booked_seats):
    seats = passengers - booked_seats
    return seats

The return statement sends a result back from the function.

### 5. Return with If/Else

def check_flight_status(delay_minutes):
    if delay_minutes == 0:
        return "On Time"
    else:
        return "Delayed"

A function can use conditions and return different results.
```

### ✈️ Aviation Applications

Functions can be used for:

Calculating available seats
Calculating ticket revenue
Checking flight status
Processing flight information
Reusing common calculations

### 🧠 Key Takeaway

Function → Input → Process → Return → Result

### 🚀 Progress
Day 17 completed successfully.

