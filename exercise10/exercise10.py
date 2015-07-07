import numpy as np
from matrices import *

EPSILON = 10**(-9)

def print_divided(s):
    space = " "*int((30 - len(s))/2)
    print("------------------------------")
    print(space + s + space)
    print("------------------------------")

# Non-negative matrix factorization
# Input (A, k)
#   A: the n x m matrix to be factorized
#   k: the number of factors to use
# Output (W, H)
#   W: the n x k feature matrix
#   H: the k x m coefficient matrix

def nmf(A, k):
    (m, n) = A.shape
    min_dist = float("inf")
    
    # Run the algorithm 10 times and take the best
    # since it is dependent on the random initialization
    for t in range(0, 10):
        # Initialize W and H randomly
        W = np.random.rand(m, k)
        H = np.random.rand(k, n)

        # Multiplicative update for Frobenius norm
        for i in range(0, 200):
            H_num = (W.T).dot(A)
            H_denom = (W.T).dot(W).dot(H) + EPSILON
            H = H*(H_num/H_denom)

            W_num = A.dot(H.T)
            W_denom = W.dot(H).dot(H.T) + EPSILON
            W = W*(W_num/W_denom)
        
        # Use this iteration if the distance is minimized
        dist = np.linalg.norm(A - W.dot(H))
        
        if(dist < min_dist):
            W_best, H_best = W, H
            min_dist = dist
        
    return (W_best, H_best)

# Task 2
task_2_matrix = np.array([[ 1,  2,  0],
        [ 0,  3,  0],
        [ 2, -4,  2]])

print_divided("Task 2")
W, H = nmf(task_2_matrix, 3)

print_divided("W")
print_matrix(W)

print_divided("H")
print_matrix(H)

print_divided("WH")
print_matrix(W.dot(H))

# Task 3
term_doc = np.array([[1, 0, 0, 1, 0, 0, 0, 0, 0],
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

W, H = nmf(term_doc, 2)

term_term = W.dot(W.T)
doc_doc = H.T.dot(H)

term_labels = ['human', 'interface', 'computer', 'user', 'system', 'response', 'time', 'EPS', 'survey', 'trees', 'graph', 'minor']
doc_labels = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]

print_divided("Task 3")

print_divided("Term-Term Matrix")
print_matrix(term_term)

print_divided("Doc-Doc Matrix")
print_matrix(doc_doc)

plot_matrix(term_term, "Term-Term Matrix", term_labels)
plot_matrix(doc_doc, "Doc-Doc Matrix", doc_labels)