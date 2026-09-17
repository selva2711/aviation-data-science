# Day 6 - Python Logical Operators

## 📚 Topic
Python Logical Operators

## 🎯 Learning Objectives

Today I learned how to use Python logical operators:

- `and`
- `or`
- `not`

## 🔹 1. AND Operator

The `and` operator returns `True` only when both conditions are `True`.

### Example:

## python
passengers = 280
available_seats = 40

if passengers > 250 and available_seats < 50:
    print("Flight is busy")

Output:
Flight is busy

## 🔹 2. OR Operator

The or operator returns True when at least one condition is True.

Example:

## python
passengers = 180
available_seats = 40

if passengers > 300 or available_seats < 50:
    print("Special attention")

Output:
Special attention

##🔹 3. NOT Operator

The not operator reverses a Boolean value.

not True → False
not False → True

Example:

## python
flight_delayed = False

print(not flight_delayed)

Output:
True

## ✈️ Aviation Application

Logical operators are useful in aviation data analysis for checking multiple conditions.

For example:

High passenger count AND limited seats
Flight delay OR low seat availability
Checking whether a flight is NOT delayed

## 🧠 Key Takeaways
Operator	Meaning
and	Both conditions must be True
or	At least one condition must be True
not	Reverses True/False
🛠️ Skills Practiced
Python and
Python or
Python not
Boolean expressions
Conditional statements
Aviation-based examples

## 🚀 Progress
Day 6 completed successfully.
