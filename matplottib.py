import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotting
plt.plot(x, y, label="Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Wave using Matplotlib")
plt.legend()
plt.show()
