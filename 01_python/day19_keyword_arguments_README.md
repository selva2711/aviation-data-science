# Day 19 – Keyword Arguments in Python

### Overview
Today, I learned about keyword arguments and how to pass arguments to Python functions using parameter names.

## 🧠 Topics Covered
* Positional arguments
* Keyword arguments
* Changing the order of keyword arguments
* Mixing positional and keyword arguments
* Using keyword arguments with default parameters

## ✈️ Aviation Examples
* Displaying flight numbers, origins, and destinations
* Showing passenger counts
* Creating reusable flight information functions

## 🔑 Key Learning
Keyword arguments assign values using parameter names, making function calls easier to read. Positional arguments must come before keyword arguments when both are used in a function call.

## 📖 Example

```python
def flight_details(flight_number, origin, destination):
    print("Flight Number:", flight_number)
    print("Origin:", origin)
    print("Destination:", destination)

flight_details("QR170", destination="Mumbai", origin="Doha")
```

## 🚀 Progress
Day 19 completed successfully.

### Conclusion
Keyword arguments improve code readability and flexibility. These concepts will help me write reusable Python functions for aviation data analysis.




