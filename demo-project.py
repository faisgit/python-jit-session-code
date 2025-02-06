# Project: Analyzing Employee Salary Data
# We will:

# Generate random employee salary data using NumPy.
# Store and manipulate the data using Pandas.
# Visualize the salary distribution using Matplotlib.






import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate random employee salary data
np.random.seed(42)
num_employees = 100
employee_ids = np.arange(1, num_employees + 1)
ages = np.random.randint(22, 60, size=num_employees)
salaries = np.random.randint(30000, 120000, size=num_employees)

# Step 2: Create a Pandas DataFrame
df = pd.DataFrame({'Employee ID': employee_ids, 'Age': ages, 'Salary': salaries})

# Display first few rows
print("Employee Data Sample:\n", df.head())

# Step 3: Calculate some statistics
avg_salary = df['Salary'].mean()
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()

print(f"\nAverage Salary: ${avg_salary:.2f}")
print(f"Max Salary: ${max_salary}")
print(f"Min Salary: ${min_salary}")

# Step 4: Visualize Salary Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Salary'], bins=10, color='skyblue', edgecolor='black')
plt.axvline(avg_salary, color='red', linestyle='dashed', linewidth=2, label=f'Avg Salary: ${avg_salary:.0f}')
plt.xlabel("Salary Range")
plt.ylabel("Number of Employees")
plt.title("Employee Salary Distribution")
plt.legend()
plt.show()
