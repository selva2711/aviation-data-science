# Day 13 - Python Dictionaries ✈️

## Overview

Today I learned about Python Dictionaries and how they can be used to store structured aviation data using key-value pairs.

## Topics Learned

### 1. Creating a Dictionary

A dictionary stores data in `key: value` format.

```python
flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR700",
    "origin": "Doha",
    "destination": "London",
    "passengers": 250
}

### 2. Accessing Values

Dictionary values can be accessed using their keys.

print(flight["airline"])
print(flight["destination"])

### 3. Changing Values

Dictionary values can be updated using the key.

flight["passengers"] = 275

### 4. Adding New Key-Value Pairs

New data can be added using a new key.

flight["aircraft"] = "A350"

### 5. Removing Data

The del keyword removes a key-value pair.

del flight["origin"]

### 6. Dictionary Length

The len() function returns the number of key-value pairs.

print(len(flight))

### 7. Checking Keys

The in operator can be used to check whether a key exists.

print("aircraft" in flight)
print("origin" in flight)

### ✈️ Aviation Application
Dictionaries are useful for representing structured flight information such as:
Airline
Flight number
Origin
Destination
Passenger count
Aircraft type

### 🧠 Key Takeaways
Dictionary uses { }
Data is stored as key: value
Values can be accessed using keys
Dictionaries are mutable
New key-value pairs can be added
Existing values can be updated
del removes key-value pairs
len() counts key-value pairs
in checks whether a key exists

### 🛠️ Skills Practiced
Python Dictionaries
Key-Value Data
Data Access
Data Updating
Data Management
Aviation Data Representation

### 🚀 Progress
Day 13 completed successfully.




