# Day 12 - Python Set Operations
# Aviation Data Science Learning

qatar_routes = {"Mumbai", "Chennai", "London"}
emirates_routes = {"Mumbai", "London", "Dubai"}

# Union
all_routes = qatar_routes | emirates_routes
print("All Routes:", all_routes)

# Intersection
common_routes = qatar_routes & emirates_routes
print("Common Routes:", common_routes)

# Difference
qatar_only = qatar_routes - emirates_routes
print("Qatar Only:", qatar_only)

# Symmetric Difference
different_routes = qatar_routes ^ emirates_routes
print("Different Routes:", different_routes)

# Output

All Routes: {'Mumbai', 'Dubai', 'London', 'Chennai'} 

Common Routes: {'Mumbai', 'London'} 

Qatar Only: {'Chennai'} 

Different Routes: {'Dubai', 'Chennai'}
