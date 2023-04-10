import matplotlib.pyplot as plt
from src.Space_Complexity.GaliliGianCarlo_complexity import space_complexity_galil_giancarlo

# Test the function
n_values = range(100, 5000, 100)
space_complexities = [space_complexity_galil_giancarlo(n) for n in n_values]

# Plot the results
plt.plot(n_values, space_complexities)
plt.xlabel("Input size")
plt.ylabel("Space complexity (in bytes)")
plt.title("Space complexity of Galil-Giancarlo algorithm")
plt.show()
