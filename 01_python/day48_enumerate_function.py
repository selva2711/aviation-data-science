
# Day 48: Python enumerate() Function
# Aviation Data Science Practice

# Example 1: Flight Numbers with Index
flights = ["QR100", "QR200", "QR300", "QR400"]

for index, flight in enumerate(flights):
    print(index, flight)


# Example 2: Passenger Names with Index
passengers = ["Arun", "Priya", "David", "Sara", "John"]

for index, passenger in enumerate(passengers):
    print(index, passenger)


# Example 3: Start Index from 1
flights = ["QR100", "QR200", "QR300", "QR400"]

for index, flight in enumerate(flights, start=1):
    print(index, flight)


# Example 4: Flight Records with Index
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320},
    {"flight": "QR400", "passengers": 400}
]

for index, flight in enumerate(flights, start=1):
    print(index, flight["flight"], "-", flight["passengers"], "passengers")


# Example 5: Complete Flight Analysis
flights = [
    {"flight": "QR100", "passengers": 180},
    {"flight": "QR200", "passengers": 250},
    {"flight": "QR300", "passengers": 320},
    {"flight": "QR400", "passengers": 400},
    {"flight": "QR500", "passengers": 300}
]

total_passengers = 0

for index, flight in enumerate(flights, start=1):
    print(index, flight["flight"], "-", flight["passengers"], "passengers")
    total_passengers += flight["passengers"]

print("Total Passengers:", total_passengers)

# Output

0 QR100
1 QR200
2 QR300
3 QR400

0 Arun
1 Priya
2 David
3 Sara
4 John

1 QR100
2 QR200
3 QR300
4 QR400

1 QR100 - 180 passengers
2 QR200 - 250 passengers
3 QR300 - 320 passengers
4 QR400 - 400 passengers

1 QR100 - 180 passengers
2 QR200 - 250 passengers
3 QR300 - 320 passengers
4 QR400 - 400 passengers
5 QR500 - 300 passengers
Total Passengers: 1450
