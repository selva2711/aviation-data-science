# Day 11 - Python Sets

flight_numbers = {"QR700", "QR170", "QR500", "QR170"}

print("Flight Numbers:", flight_numbers)

flight_numbers.add("QR900")

print("After Add:", flight_numbers)

flight_numbers.remove("QR500")

print("After Remove:", flight_numbers)

print("QR900 Available:", "QR900" in flight_numbers)

print("QR300 Available:", "QR300" in flight_numbers)

# Output

Flight Numbers: {'QR170', 'QR500', 'QR700'}

After Add: {'QR170', 'QR500', 'QR900', 'QR700'}

After Remove: {'QR170', 'QR900', 'QR700'}

QR900 Available: True

QR300 Available: False
