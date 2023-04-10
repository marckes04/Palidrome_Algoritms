import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from src.Time_Comparison.colussi_length import colussi_algorithm
from src.Time_Comparison.kruttMorris_length import kruskal_morris_algorithm
from src.Time_Comparison.GaliliGianCarlo_length import galil_giancarlo_algorithm


def generate_palindrome(length):
    """Generate a palindrome string of given length."""
    mid = length // 2
    if length % 2 == 0:
        return 'a' * mid + 'b' * mid
    else:
        return 'a' * mid + 'b' + 'a' * mid


def compare_algorithms():
    """Compare the three palindrome algorithms."""
    # Prepare the data
    lengths = list(range(2, 200))
    colussi_times = []
    kruskal_times = []
    galil_times = []
    for length in lengths:
        s = generate_palindrome(length)

        start_time = time.time()
        colussi_algorithm(s)
        colussi_times.append(time.time() - start_time)

        start_time = time.time()
        kruskal_morris_algorithm(s)
        kruskal_times.append(time.time() - start_time)

        start_time = time.time()
        galil_giancarlo_algorithm(s)
        galil_times.append(time.time() - start_time)

    # Create the plot
    fig, ax = plt.subplots()
    ax.set_title('Comparison of Palindrome Algorithms')
    ax.set_xlabel('Length of String')
    ax.set_ylabel('Time (seconds)')

    colussi_line, = ax.plot(lengths, colussi_times, label='Colussi')
    kruskal_line, = ax.plot(lengths, kruskal_times, label='Kruskal-Morris')
    galil_line, = ax.plot(lengths, galil_times, label='Galil-Giancarlo')
    ax.legend()

    # Create the animation
    def update(frame):
        nonlocal lengths, colussi_times, kruskal_times, galil_times

        if frame == 0:
            return

        # Generate a new palindrome string and update the data
        length = lengths[frame - 1]
        s = generate_palindrome(length)

        start_time = time.time()
        colussi_algorithm(s)
        colussi_times[frame - 1] = time.time() - start_time

        start_time = time.time()
        kruskal_morris_algorithm(s)
        kruskal_times[frame - 1] = time.time() - start_time

        start_time = time.time()
        galil_giancarlo_algorithm(s)
        galil_times[frame - 1] = time.time() - start_time

        # Update the plot
        colussi_line.set_ydata(colussi_times)
        kruskal_line.set_ydata(kruskal_times)
        galil_line.set_ydata(galil_times)

    ani = FuncAnimation(fig, update, frames=len(lengths) + 1, interval=500, repeat=False)
    plt.show()


if __name__ == '__main__':
    compare_algorithms()
