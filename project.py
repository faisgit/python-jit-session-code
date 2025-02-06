# Project: Analyzing Sales Data
# Objective:
# Generate fake sales data using NumPy.
# Analyze and manipulate data using Pandas.
# Visualize trends and insights using Matplotlib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate Random Sales Data
np.random.seed(42)  # Ensure reproducibility

num_days = 30  # Sales data for a month
dates = pd.date_range(start="2024-01-01", periods=num_days)
products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
sales_data = {
    'Date': dates,
    'Product': np.random.choice(products, num_days),
    'Units Sold': np.random.randint(5, 50, num_days),
    'Price per Unit': np.random.randint(5000, 50000, num_days)  # In currency units
}

# Step 2: Create Pandas DataFrame
df = pd.DataFrame(sales_data)
df['Total Sales'] = df['Units Sold'] * df['Price per Unit']

# Display first few rows
print("Sales Data Sample:\n", df.head())

# Step 3: Data Analysis
total_revenue = df['Total Sales'].sum()
avg_sales_per_day = df['Total Sales'].mean()
best_selling_product = df.groupby('Product')['Total Sales'].sum().idxmax()

print(f"\nTotal Revenue: ${total_revenue}")
print(f"Average Sales per Day: ${avg_sales_per_day:.2f}")
print(f"Best Selling Product: {best_selling_product}")

# Step 4: Visualizing Sales Trends

# Plot 1: Sales Trend Over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Total Sales'], marker='o', linestyle='-', color='b', label="Daily Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Daily Sales Trend")
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Plot 2: Sales by Product
plt.figure(figsize=(8, 5))
df.groupby('Product')['Total Sales'].sum().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.show()
