# Day 15 - Looping Through a Dictionary ✈️

## Overview

Today I learned how to use Python `for` loops to process dictionary data.

## Topics Learned

```
### 1. Loop Through Dictionary Keys

A `for` loop can be used to access dictionary keys one by one.

python
for key in flight:
    print(key)

### 2. Loop Through Dictionary Values

The .values() method can be used to process dictionary values one by one.

for value in flight.values():
    print(value)

### 3. Loop Through Key-Value Pairs

The .items() method allows us to access both keys and values.

for key, value in flight.items():
    print(key, ":", value)

### 4. Dictionary + If Condition

A loop can be combined with an if condition to find specific information.

for key, value in flight.items():
    if key == "passengers":
        print("Total Passengers:", value)

### ✈️ Aviation Example

flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR170",
    "origin": "Doha",
    "destination": "Mumbai",
    "passengers": 280,
    "aircraft": "A350"
}
```

### 🧠 Key Takeaways
for key in dictionary → loops through keys
for value in dictionary.values() → loops through values
for key, value in dictionary.items() → loops through key-value pairs
for + if → can be used to select specific information

### ✈️ Aviation Application
Dictionary loops can be used to process and analyze structured flight information efficiently.

### 🛠️ Skills Practiced
Python for loops
Dictionary keys
Dictionary values
Dictionary items
Conditional filtering
Aviation data processing

### 🚀 Progress
Day 11 completed successfully.


