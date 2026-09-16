# Day 5 – Python Conditional Statements

## 📚 What I Learned

Today I learned about Python conditional statements.

Conditional statements allow Python to make decisions based on conditions.

The main keywords are:

- `if`
- `elif`
- `else`

The condition produces either `True` or `False`.

## 1. `if` Statement

The `if` statement runs a block of code when a condition is `True`.

## python
passengers = 280

if passengers > 250:
    print("High passenger count")

Output:
High passenger count

## 2. if and else

The else block runs when the if condition is False.

passengers = 180

if passengers > 250:
    print("High passenger count")
else:
    print("Normal passenger count")

Output:
Normal passenger count

## 3. if, elif and else

elif means "else if" and allows Python to check another condition.

passengers = 280

if passengers > 300:
    print("Very High")
elif passengers > 250:
    print("High")
else:
    print("Normal")

Output:
High

## ✈️ Aviation Example

Flight delay can be classified using conditional statements.

delay_minutes = 45

if delay_minutes == 0:
    print("On Time")
elif delay_minutes <= 30:
    print("Slight Delay")
else:
    print("Major Delay")

Output:
Major Delay

## 🎯 Key Takeaways
Conditional statements help Python make decisions.
if checks the first condition.
elif checks another condition.
else runs when the conditions above are False.
Conditions produce True or False.
Indentation is important in Python.
A colon : is required after if, elif, and else conditions.
Conditional statements are useful for analyzing aviation data.

## 🚀 Learning Journey
Day 5 completed successfully.

