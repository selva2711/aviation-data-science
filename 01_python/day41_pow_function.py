
# Day 41: Python pow() Function
# Aviation Data Science

# Example 1: Basic pow() function
base = 2
exponent = 3

result = pow(base, exponent)

print("Base:", base)
print("Exponent:", exponent)
print("Result:", result)

print()

# Example 2: Aviation seating calculation
rows = 3
sections = 3

total = pow(rows, sections)

print("Rows:", rows)
print("Sections:", sections)
print("Total:", total)

print()

# Example 3: Power calculations
base = 5

result_1 = pow(base, 2)
result_2 = pow(base, 3)

print("Base:", base)
print("Power 2:", result_1)
print("Power 3:", result_2)

print()

# Example 4: Multiple flight calculations
flights = [
    {"flight": "QR100", "base": 2},
    {"flight": "QR200", "base": 3},
    {"flight": "QR300", "base": 4}
]

for flight in flights:
    result = pow(flight["base"], 2)

    print("Flight:", flight["flight"])
    print("Base:", flight["base"])
    print("Power 2:", result)
    print()

# Example 5: Final practice
flights = [
    {"flight": "QR100", "base": 2, "power": 3},
    {"flight": "QR200", "base": 3, "power": 2},
    {"flight": "QR300", "base": 4, "power": 2}
]

for flight in flights:
    result = pow(flight["base"], flight["power"])

    print("Flight:", flight["flight"])
    print("Base:", flight["base"])
    print("Power:", flight["power"])
    print("Result:", result)
    print()

# Output

Base: 2
Exponent: 3
Result: 8

Rows: 3
Sections: 3
Total: 27

Base: 5
Power 2: 25
Power 3: 125

Flight: QR100
Base: 2
Power 2: 4

Flight: QR200
Base: 3
Power 2: 9

Flight: QR300
Base: 4
Power 2: 16

Flight: QR100
Base: 2
Power: 3
Result: 8

Flight: QR200
Base: 3
Power: 2
Result: 9

Flight: QR300
Base: 4
Power: 2
Result: 16
