# Day 16 - List of Dictionaries

## 📌 Topic
List of Dictionaries in Python

## 📖 What I Learned

Today I learned how to store multiple dictionaries inside a list.

A list of dictionaries is useful for representing multiple records, such as flight information.

## 🔑 Key Concepts

```
### 1. Creating a List of Dictionaries

```python
flights = [
    {
        "flight_number": "QR170",
        "origin": "Doha",
        "destination": "Mumbai"
    },
    {
        "flight_number": "QR500",
        "origin": "Doha",
        "destination": "Chennai"
    }
]

### 2. Accessing a Dictionary

flights[0]

### 3. Accessing a Specific Value

flights[0]["flight_number"]

### 4. Using a For Loop

for flight in flights:
    print(flight)

### 5. Accessing Values Inside a Loop

for flight in flights:
    print(flight["flight_number"])

6. Using If with a List of Dictionaries

for flight in flights:
    if flight["destination"] == "Chennai":
        print(flight)
```

### ✈️ Aviation Application

List of dictionaries can be used to represent multiple flights and their details.

Example:

Flight Number
Origin
Destination
Passengers
Aircraft
Flight Status

### 🧠 Key Takeaway

A list can store multiple dictionaries, and loops can be used to process each dictionary one by one.

List → Dictionary → Key → Value

### 🚀 Progress
Day 16 completed successfully.


