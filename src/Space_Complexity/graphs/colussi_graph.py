import matplotlib.pyplot as plt
from src.Space_Complexity.colussi_complexity import colussi_space

def graph_space_complexity():
    # create a list of input sizes
    input_sizes = list(range(1000, 10001, 1000))

    # create empty lists for space complexity results
    colussi_space_complexity = []

    # calculate space complexity for each input size
    for n in input_sizes:
        s = 'a' * n
        colussi_space_complexity.append(colussi_space(s))

    # plot the results
    plt.plot(input_sizes, colussi_space_complexity, label='Colussi')

    # add axis labels and legend
    plt.xlabel('Input size')
    plt.ylabel('Space complexity (bytes)')
    plt.legend()

    # show the plot
    plt.show()

graph_space_complexity()
