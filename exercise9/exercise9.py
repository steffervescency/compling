import numpy as np
import matplotlib.pyplot as plt
import sys

# Round numpy matrix entries to make it easier to read on printing
def matrix_string(matrix, num_digits=3):
    m = matrix.tolist()
    result = []
    for row in m:
        result.append("\t".join([str(round(i, num_digits)) for i in row]))
    return "\n".join(result)

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
    

# Task 1
mat = np.matrix([[1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 2, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1]])

dd1 = mat.T * mat
tt1 = mat * mat.T

# Task 2

t, s, d = np.linalg.svd(mat, full_matrices=0)
s = s * np.identity(9)

dd2 = (s * d).T * (s * d)
tt2 = (t * s) * (t * s).T

# Task 3

sp = s[[0, 1]][:, [0, 1]]
tp = t[:][:, [0, 1]]
dp = d[[0,1]][:]

dd3 = (sp * dp).T * (sp * dp)
tt3 = (tp * sp) * (tp * sp).T


if __name__ == "__main__":
    args = sys.argv
    if(len(args) != 3 or args[1] not in ["plot", "print"] or args[2] not in ["terms", "docs"]):
        print("Usage:")
        print("python exercise9.py [plot | print] [terms | docs]")
        exit()
    
    if(args[2] == "terms"):
        matrices = [tt1, tt2, tt3]
        labels = ['human', 'interface', 'computer', 'user', 'system', 'response', 'time', 'EPS', 'survey', 'trees', 'graph', 'minor']
        base_title = "Term-term similarity"
    else:
        matrices = [dd1, dd2, dd3]
        labels = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]
        base_title = "Document-document similarity"
    
    for i in range(1, 4):
        title = base_title + " " + str(i)
        if(args[1] == "print"):
            print(title)
            print(matrix_string(matrices.pop(0)))
        else:
            plot_matrix(matrices.pop(0), title, labels)