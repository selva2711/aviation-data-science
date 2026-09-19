# Day 8 - Python List Methods

flight_numbers = ["QR700", "QR170", "QR900", "QR500"]

print("Original List:", flight_numbers)

flight_numbers.sort()
print("Sorted List:", flight_numbers)

flight_numbers.reverse()
print("Reversed List:", flight_numbers)

flight_numbers.remove("QR700")
print("After Remove:", flight_numbers)

flight_numbers.pop(1)
print("After Pop:", flight_numbers)

# Output

Original List: ['QR700', 'QR170', 'QR900', 'QR500']
Sorted List: ['QR170', 'QR500', 'QR700', 'QR900']
Reversed List: ['QR900', 'QR700', 'QR500', 'QR170']
After Remove: ['QR900', 'QR500', 'QR170']
After Pop: ['QR900', 'QR170']
