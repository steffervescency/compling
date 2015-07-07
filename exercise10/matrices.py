import numpy as np
import matplotlib.pyplot as plt

# Plot the given matrix with a grayscale colormap
def plot_matrix(matrix, title, labels):
    fig, ax = plt.subplots()
    
    dims = matrix.shape

    ax.imshow(matrix*-1, cmap=plt.cm.gray, interpolation='nearest')
    ax.set_title(title)

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks(np.arange(0, dims[0], 1.0))
    ax.yaxis.set_ticklabels(labels)
    ax.xaxis.set_ticks(np.arange(0, dims[0], 1.0))
    ax.xaxis.set_ticklabels(labels, rotation=90)

    plt.show()

# Round numpy matrix entries to make it easier to read on printing
def print_matrix(matrix, num_digits=3):
    m = matrix.tolist()
    result = []
    for row in m:
        result.append("\t".join([str(round(i, num_digits)) for i in row]))
    print("\n".join(result))