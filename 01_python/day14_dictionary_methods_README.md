# Day 14 - Python Dictionary Methods ✈️

## Overview

Today I learned important Python Dictionary methods using aviation-related flight data.

## Methods Learned

```
### 1. `.keys()`

Returns all keys from a dictionary.

flight.keys()

### 2. .values()

Returns all values from a dictionary.

flight.values()

### 3. .items()

Returns all key-value pairs.

flight.items()

### 4. .get()

Safely retrieves the value associated with a key.

flight.get("destination")

If the key does not exist, .get() returns None by default.

### 5. .update()

Updates existing values and can add new key-value pairs.

flight.update({
    "destination": "Chennai",
    "passengers": 280,
    "aircraft": "A350"
})

### ✈️ Aviation Example

flight = {
    "airline": "Qatar Airways",
    "flight_number": "QR170",
    "origin": "Doha",
    "destination": "Mumbai",
    "passengers": 250
}
```

### 🧠 Key Takeaways
.keys() → Get keys
.values() → Get values
.items() → Get key-value pairs
.get() → Safely get a value
.update() → Update or add data

### ✈️ Aviation Application
Dictionary methods are useful for inspecting and updating structured flight information in aviation data analysis.

### 🛠️ Skills Practiced
Python Dictionaries
Dictionary Methods
Data Access
Data Updating
Aviation Data Representation

### 🚀 Progress
Day 14 completed successfully
