import timeit
import matplotlib.pyplot as plt
from src.sorting.quickSort import quicksort
from src.sorting.heap import heapsort
from src.sorting.merge import mergeSort

# Generate array of random integers
arr = [x for x in range(10000)]
import random
random.shuffle(arr)

# Measure time to sort with each algorithm
quicksort_time = timeit.timeit(lambda: quicksort(arr), number=1)
heapsort_time = timeit.timeit(lambda: heapsort(arr), number=1)
mergesort_time = timeit.timeit(lambda: mergeSort(arr), number=1)

# Plot bar chart
labels = ['quicksort', 'heapsort', 'mergesort']
times = [quicksort_time, heapsort_time, mergesort_time]
plt.bar(labels, times)
plt.ylabel('Time (seconds)')
plt.show()
