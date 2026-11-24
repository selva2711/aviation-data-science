
# Day 49: Python zip() Function
# Aviation Data Science Practice

# Example 1: Combine Flight Numbers and Passengers
flight_numbers = ["QR100", "QR200", "QR300"]
passengers = [180, 250, 320]

flight_details = list(zip(flight_numbers, passengers))

print("Flight Details:", flight_details)


# Example 2: Combine Flight Numbers and Delays
flight_numbers = ["QR100", "QR200", "QR300", "QR400"]
delays = [15, 30, 45, 20]

flight_details = list(zip(flight_numbers, delays))

print("Flight Details:", flight_details)


# Example 3: Combine Three Lists
flight_numbers = ["QR100", "QR200", "QR300"]
passengers = [180, 250, 320]
delays = [15, 30, 45]

flight_details = list(zip(flight_numbers, passengers, delays))

print("Complete Flight Details:", flight_details)


# Example 4: Use zip() with a for loop
flight_numbers = ["QR100", "QR200", "QR300"]
passengers = [180, 250, 320]

for flight, passenger in zip(flight_numbers, passengers):
    print(flight, "-", passenger, "passengers")


# Example 5: Complete Aviation Flight Analysis
flight_numbers = ["QR100", "QR200", "QR300", "QR400", "QR500"]
passengers = [180, 250, 320, 400, 300]
delays = [15, 30, 45, 20, 10]

for flight, passenger, delay in zip(flight_numbers, passengers, delays):
    print(flight, "-", passenger, "passengers,", delay, "minutes delay")

# Output

Flight Details: [('QR100', 180), ('QR200', 250), ('QR300', 320)]

Flight Details: [('QR100', 15), ('QR200', 30), ('QR300', 45), ('QR400', 20)]

Complete Flight Details: [('QR100', 180, 15), ('QR200', 250, 30), ('QR300', 320, 45)]

QR100 - 180 passengers
QR200 - 250 passengers
QR300 - 320 passengers

QR100 - 180 passengers, 15 minutes delay
QR200 - 250 passengers, 30 minutes delay
QR300 - 320 passengers, 45 minutes delay
QR400 - 400 passengers, 20 minutes delay
QR500 - 300 passengers, 10 minutes delay
