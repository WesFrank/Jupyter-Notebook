from matplotlib import pyplot as plt

# Median Salary for Developers versus Age

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='>', label='All Devs')

# Median Salary for Python Developers versus Age

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='b', linestyle=':', marker='o', label='Python')

# Plot information

plt.xlabel('Ages')

plt.ylabel('Median Salary (USD)')

plt.title('Median Salary (USD) by Age')

# Assign Legends to Curves

plt.legend()

# Make Plot

plt.show()