# Day 12 - Python Set Operations ✈️

## Topics Learned

Today I learned how to perform operations between Python sets using aviation-related examples.

### 1. Union `|`

Union combines all unique values from two sets.

python
all_routes = qatar_routes | emirates_routes

### 2. Intersection &

Intersection returns only the values that are common in both sets.

python
common_routes = qatar_routes & emirates_routes

### 3. Difference -

Difference returns values that exist in the first set but not in the second set.

python
qatar_only = qatar_routes - emirates_routes

### 4. Symmetric Difference ^

Symmetric difference returns values that are different between the two sets and excludes common values.

python
different_routes = qatar_routes ^ emirates_routes

### Aviation Example

python
qatar_routes = {"Mumbai", "Chennai", "London"}
emirates_routes = {"Mumbai", "London", "Dubai"}

### Key Takeaways
| → Union → All unique values
& → Intersection → Common values
- → Difference → First set only
^ → Symmetric Difference → Non-common values

### 🛠️ Skills Practiced 
Python Sets
Set Operations
Aviation Route Analysis
Python Operators

### 🚀 Progress
Day 12 completed successfully.
