import matplotlib.pyplot as plt
from src.Space_Complexity.krutMorris_complexity import kruskal_morris_space

input_sizes = [10, 100, 1000, 10000, 100000, 1000000]
space_complexities = []

for size in input_sizes:
    space_complexities.append(kruskal_morris_space(size))

plt.plot(input_sizes, space_complexities)
plt.xlabel("Input Size")
plt.ylabel("Space Complexity")
plt.title("Kruskal-Morris Algorithm Space Complexity")
plt.show()