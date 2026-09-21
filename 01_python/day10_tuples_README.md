# Day 10 - Python Tuples

## 📚 Topic

Python Tuples

## 🎯 Learning Objectives

Today I learned how to:

- Create Python Tuples
- Access Tuple items using indexes
- Use `len()` with Tuples
- Understand Tuple immutability
- Understand the difference between Lists and Tuples

## 🔹 1. Creating a Tuple

A Tuple stores multiple values in a single variable.

Tuples are created using parentheses `()`.

### Example:

Python
flight_info = ("QR170", "Doha", "Mumbai")

Output:
('QR170', 'Doha', 'Mumbai')

## 🔹 2. Tuple Indexing

Like Lists, Tuple indexing starts from 0.

QR170  → Index 0
Doha   → Index 1
Mumbai → Index 2

### Example:

Python
print(flight_info[0])
print(flight_info[1])
print(flight_info[2])

Output:
QR170
Doha
Mumbai

## 🔹 3. Using len() with Tuples

The len() function counts the number of items in a Tuple.

### Example:

Python
flight_info = ("QR170", "Doha", "Mumbai")

print(len(flight_info))

Output:
3

## 🔒 4. Tuple Immutability

Tuples are immutable.

This means that once a Tuple is created, its items cannot be changed.

### Example:

Python
flight_route = ("Doha", "Chennai", "Mumbai")

Trying to change an item:

Python
flight_route[0] = "London"

is not allowed.

## 🔄 List vs Tuple

| Feature    | List  | Tuple |
| ---------- | ----- | ----- |
| Syntax     | `[ ]` | `( )` |
| Changeable | Yes   | No    |
| Indexing   | Yes   | Yes   |
| `len()`    | Yes   | Yes   |

## ✈️ Aviation Application
Tuples can be useful for storing fixed aviation information such as:
Flight number
Origin airport
Destination airport
Aircraft information
Fixed route information

## For example:

Python
flight_info = ("QR170", "Doha", "Mumbai")

This represents a fixed flight route.

## 🛠️ Skills Practiced
Python Tuples
Tuple indexing
len()
Immutable data
List vs Tuple
Aviation-based Python examples

## 🚀 Progress
Day 10 completed successfully.
