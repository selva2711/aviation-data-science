# Day 9 - Python List Operations

## 📚 Topic

Python List Operations

## 🎯 Learning Objectives

Today I learned how to:

- Combine two Lists using `+`
- Check whether a value exists using `in`
- Check whether a value does not exist using `not in`
- Work with aviation-based List examples

## 🔹 1. Combining Two Lists

The `+` operator can combine two Lists into one new List.

### Example:

Python
morning_flights = ["QR170", "QR500"]
evening_flights = ["QR700", "QR900"]

all_flights = morning_flights + evening_flights

print(all_flights)

Output:
['QR170', 'QR500', 'QR700', 'QR900']

## 🔹 2. Using in

The in operator checks whether a value exists in a List.

### Example:

Python
flight_numbers = ["QR170", "QR500", "QR700"]

print("QR500" in flight_numbers)

Output:
True

The result is True because "QR500" exists in the List.

## 🔹 3. Using not in

The not in operator checks whether a value does not exist in a List.

### Example:

Python
flight_numbers = ["QR170", "QR500", "QR700"]

print("QR900" not in flight_numbers)

Output:
True

The result is True because "QR900" is not in the List.

## ✈️ Aviation Application

List operations can be useful in aviation data analysis.

For example:

Combining morning and evening flight schedules
Checking whether a flight number exists
Checking whether a flight is missing from a schedule
Working with groups of flight information

## 🧠 Key Takeaways
| Operation           | Purpose                               |
| ------------------- | ------------------------------------- |
| `list1 + list2`     | Combines two Lists                    |
| `value in list`     | Checks whether a value exists         |
| `value not in list` | Checks whether a value does not exist |

## 🛠️ Skills Practiced
Python Lists
List concatenation
in
not in
Boolean results
Aviation-based Python examples

## 🚀 Progress
Day 9 completed successfully.
