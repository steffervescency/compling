import numpy as np
import matplotlib.pyplot as plt

def matrix_string(matrix):
    m = matrix.tolist()
    result = []
    for row in m:
        result.append("\t".join([str(round(i, 3)) for i in row]))
    return "\n".join(result)

def plot_matrix(matrix, title):
    fig, ax = plt.subplots()
    
    dims = matrix.shape

    ax.imshow(matrix*-1, cmap=plt.cm.gray, interpolation='nearest')
    ax.set_title(title)

    # Move left and bottom spines outward by 10 points
    ax.spines['left'].set_position(('outward', dims[0]))
    ax.spines['bottom'].set_position(('outward', dims[1]))
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

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



plot_matrix(dd1, "Document-document similarity 1")
plot_matrix(dd2, "Document-document similarity 2")
plot_matrix(dd3, "Document-document similarity 3")

plot_matrix(tt1, "Term-term similarity 1")
plot_matrix(tt2, "Term-term similarity 2")
plot_matrix(tt3, "Term-term similarity 3")


# print("Task 1 - Document-docment")
# print(matrix_string(dd1))
# print("Task 1 - Term-term")
# print(matrix_string(tt1))
#
# print("Task 2 - Document-docment")
# print(matrix_string(dd2))
# print("Task 3 - Term-term")
# print(matrix_string(tt2))
#
print("Task 3 - Document-docment")
print(matrix_string(dd3))
print("Task 3 - Term-term")
print(matrix_string(tt3))