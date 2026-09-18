# Day 7 - Python Lists

## 📚 Topic

Python Lists

## 🎯 Learning Objectives

Today I learned how to:

- Create Python Lists
- Access List items using indexes
- Change List values
- Add new values using `append()`
- Count List items using `len()`

## 🔹 1. Creating a List

A Python List stores multiple values in a single variable.

### Example:

python
flight_numbers = ["QR170", "QR500", "QR700"]

Lists are created using square brackets [].

## 🔹 2. Accessing List Items

Python List indexing starts from 0.

QR170 → Index 0
QR500 → Index 1
QR700 → Index 2

### Example:

python
print(flight_numbers[0])

Output:
QR170

## 🔹 3. Changing a List Value

A List value can be changed by using its index.

python
flight_numbers[1] = "QR600"

print(flight_numbers)

Output:
['QR170', 'QR600', 'QR700']

## 🔹 4. Adding a New Value

The append() method adds a new item to the end of a List.

python
flight_numbers.append("QR900")

print(flight_numbers)

Output:
['QR170', 'QR500', 'QR700', 'QR900']

## 🔹 5. Counting List Items

The len() function returns the number of items in a List.

python
print(len(flight_numbers))

Output:
4

## ✈️ Aviation Application
Python Lists can be used to store:

Flight numbers
Airport names
Passenger names
Aircraft information
Routes
Ticket prices

Lists are useful when working with collections of aviation data.

## 🧠 Key Takeaways
| Concept    | Purpose            |
| ---------- | ------------------ |
| `[]`       | Create a List      |
| `[index]`  | Access a List item |
| `append()` | Add a new item     |
| `len()`    | Count the items    |

## 🛠️ Skills Practiced
Python Lists
List indexing
Updating List values
append()
len()
Aviation-based Python examples

## 🚀 Progress
Day 7 completed successfully.

