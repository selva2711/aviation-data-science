# Day 8 - Python List Methods

## 📚 Topic

Python List Methods and Operations

## 🎯 Learning Objectives

Today I learned how to use important Python List methods:

- `remove()`
- `pop()`
- `sort()`
- `reverse()`

## 🔹 1. `remove()`

The `remove()` method removes a specific value from a List.

### Example:

Python
flight_numbers = ["QR170", "QR500", "QR700", "QR900"]

flight_numbers.remove("QR700")

print(flight_numbers)

Output:
['QR170', 'QR500', 'QR900']

## 🔹 2. pop()

The pop() method removes an item using its index.

Example:

Python
airports = ["Doha", "Chennai", "Mumbai", "London"]

airports.pop(2)

print(airports)

Output:
['Doha', 'Chennai', 'London']
Index 2 contained "Mumbai", so "Mumbai" was removed.

## 🔹 3. sort()

The sort() method arranges List items in ascending or alphabetical order.

Example:

Python
flight_numbers = ["QR700", "QR170", "QR900", "QR500"]

flight_numbers.sort()

print(flight_numbers)

Output:
['QR170', 'QR500', 'QR700', 'QR900']

## 🔹 4. reverse()

The reverse() method reverses the current order of a List.

Example:

airports = ["Doha", "Chennai", "Mumbai", "London"]

airports.reverse()

print(airports)

Output:
['London', 'Mumbai', 'Chennai', 'Doha']

## ✈️ Aviation Application

List methods are useful when working with aviation data such as:

Flight numbers
Airport names
Passenger information
Flight routes
Aircraft information

For example, flight numbers can be sorted, removed, or reordered while processing aviation datasets.

## 🧠 Key Takeaways
| Method          | Purpose                         |
| --------------- | ------------------------------- |
| `remove(value)` | Removes a specific value        |
| `pop(index)`    | Removes an item using its index |
| `sort()`        | Sorts the List                  |
| `reverse()`     | Reverses the current order      |

## 🛠️ Skills Practiced
Python List methods
remove()
pop()
sort()
reverse()
List indexing
Aviation-based Python examples

## 🚀 Progress
Day 8 completed successfully.
