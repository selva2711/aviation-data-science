
# Day 30: Python sum() Function
# Aviation Data Science Practice

flight_numbers = ["QR170", "QR500", "QR700"]
passengers = [100, 150, 200]
ticket_prices = [500, 700, 600]

revenues = []

for flight, count, price in zip(
    flight_numbers, passengers, ticket_prices
):
    revenue = count * price
    revenues.append(revenue)

    print("Flight:", flight)
    print("Passengers:", count)
    print("Ticket Price: Rs.", price)
    print("Revenue: Rs.", revenue)
    print()

print("Total Revenue: Rs.", sum(revenues))

# Output

Flight: QR170
Passengers: 100
Ticket Price: Rs. 500
Revenue: Rs. 50000

Flight: QR500
Passengers: 150
Ticket Price: Rs. 700
Revenue: Rs. 105000

Flight: QR700
Passengers: 200
Ticket Price: Rs. 600
Revenue: Rs. 120000

Total Revenue: Rs. 275000
