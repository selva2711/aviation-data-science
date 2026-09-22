# Day 11 - Python Sets

## 📚 Topic

Python Sets

## 🎯 Learning Objectives

Today I learned how to:

- Create Python Sets
- Understand unique values
- Add values using `add()`
- Remove values using `remove()`
- Check whether a value exists using `in`
- Understand that Sets are unordered

## 🔹 1. Creating a Set

A Set is a collection of unique values.

Sets are created using curly braces `{}`.

### Example:

Python
flight_numbers = {"QR170", "QR500", "QR700"}

## 🔹 2. Sets Do Not Allow Duplicate Values

If a value is added more than once, the Set keeps only one copy.

### Example:

flight_numbers = {"QR170", "QR500", "QR700", "QR170"}

print(flight_numbers)

The duplicate "QR170" is automatically removed.

## 🔹 3. Adding a Value with add()

The add() method adds a new value to a Set.

### Example:

flight_numbers.add("QR900")

print(flight_numbers)

## 🔹 4. Removing a Value with remove()

The remove() method removes a specific value from a Set.

### Example:

flight_numbers.remove("QR500")

print(flight_numbers)

## 🔹 5. Checking a Value with in

The in operator checks whether a value exists in a Set.

### Example:

print("QR900" in flight_numbers)

Output:
True

If the value does not exist:

Output:
False

## 🔹 6. Sets Are Unordered

Sets do not use fixed positions or indexes.

### For example:

flight_numbers = {"QR170", "QR500", "QR700"}

The order displayed by Python may vary.

Therefore, we should not rely on Set item positions.

## ✈️ Aviation Application

Sets can be useful in aviation data analysis when working with unique values such as:

Unique flight numbers
Unique airport codes
Unique destinations
Unique aircraft types
Unique routes

For example, Sets can help identify unique airports or destinations in a dataset.

## 🧠 Key Takeaways
| Concept       | Purpose                      |
| ------------- | ---------------------------- |
| `{ }`         | Create a Set                 |
| Unique values | Duplicate values are removed |
| `add()`       | Add a value                  |
| `remove()`    | Remove a value               |
| `in`          | Check whether a value exists |
| Unordered     | No fixed indexing            |

## 🔄 List vs Tuple vs Set
| Feature    | List    | Tuple   | Set            |
| ---------- | ------- | ------- | -------------- |
| Syntax     | `[ ]`   | `( )`   | `{ }`          |
| Ordered    | Yes     | Yes     | No fixed order |
| Duplicates | Allowed | Allowed | Not allowed    |
| Changeable | Yes     | No      | Yes            |

## 🛠️ Skills Practiced
Python Sets
Unique values
add()
remove()
in
Aviation-based Python examples

## 🚀 Progress
Day 11 completed successfully.
