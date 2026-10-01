# Day 17 - Functions

# 1. Basic Function
def greetings():
    print("Welcome to Aviation Data Science")
    print("Hi Welcome to Qatar Airways")


greetings()


# 2. Function with a Parameter
def welcome_airline(airline):
    print("Welcome to", airline)


welcome_airline("Qatar Airways")
welcome_airline("Emirates")
welcome_airline("Singapore Airlines")


# 3. Function with Multiple Parameters
def flight_route(flight_number, destination, origin):
    print("Flight:", flight_number)
    print("Destination:", destination)
    print("Origin:", origin)


flight_route("QR170", "Mumbai", "Doha")
flight_route("QR500", "Chennai", "London")
flight_route("QR700", "London", "Dubai")


# 4. Function with Return
def calculate_seats(passengers, booked_seats):
    seats = passengers - booked_seats
    return seats


def calculate_total(passengers, ticket_price):
    total = passengers * ticket_price
    return total


available = calculate_seats(200, 70)
revenue = calculate_total(5, 500)

print("Available Seats:", available)
print("Total Revenue:", revenue)


# 5. Return with If/Else
def check_flight_status(delay_minutes):
    if delay_minutes == 0:
        return "On Time"
    else:
        return "Delayed"


status = check_flight_status(30)

print("Flight Status:", status)


# 6. Calculate Available Seats
def calculate_available_seats(total_seats, booked_seats):
    available = total_seats - booked_seats
    return available


available_seats = calculate_available_seats(300, 245)

print("Available Seats:", available_seats)

# Output

Welcome to Aviation Data Science
Hi Welcome to Qatar Airways

Welcome to Qatar Airways
Welcome to Emirates
Welcome to Singapore Airlines

Flight: QR170
Destination: Mumbai
Origin: Doha
Flight: QR500
Destination: Chennai
Origin: London
Flight: QR700
Destination: London
Origin: Dubai

Available Seats: 130
Total Revenue: 2500

Flight Status: Delayed

Available Seats: 55
