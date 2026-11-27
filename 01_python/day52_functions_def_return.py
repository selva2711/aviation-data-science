# Day 52: Python Functions - def and return
# Aviation Data Science - Python Practice

# Function to calculate flight revenue

def calculate_revenue(ticket_price, passengers):
    revenue = ticket_price * passengers
    return revenue


# Flight 1
qr720_revenue = calculate_revenue(9000, 120)

# Flight 2
qr500_revenue = calculate_revenue(7500, 160)

# Calculate total revenue
total_revenue = qr720_revenue + qr500_revenue

# Display results
print("QR720 Revenue:", qr720_revenue)
print("QR500 Revenue:", qr500_revenue)
print("Total Revenue:", total_revenue)

# Output

QR720 Revenue: 1080000
QR500 Revenue: 1200000
Total Revenue: 2280000
