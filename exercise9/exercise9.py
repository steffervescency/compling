import numpy as np

def matrix_string(matrix):
    m = matrix.tolist()
    result = []
    for row in m:
        result.append("\t".join([str(round(i, 3)) for i in row]))
    return "\n".join(result)

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

dd2 = (s * d.T).T * (s * d.T)
tt2 = (t * s) * (t * s).T

# Task 3

sp = s[[0, 1]][:, [0, 1]]
tp = t[:][:, [0, 1]]
dp = d[:][:, [0, 1]]

dd3 = (sp * dp.T).T * (sp * dp.T)
tt3 = (tp * sp) * (tp * sp).T

print("Task 1 - Document-docment")
print(matrix_string(dd1))
# print("Task 1 - Term-term")
# print(matrix_string(tt1))
#
print("Task 2 - Document-docment")
print(matrix_string(dd2))
# print("Task 3 - Term-term")
# print(matrix_string(tt2))
#
# print("Task 3 - Document-docment")
# print(matrix_string(dd3))
# print("Task 3 - Term-term")
# print(matrix_string(tt3))