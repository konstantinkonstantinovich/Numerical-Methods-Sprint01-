import numpy as np

def dd(X):
    result = None
    D = np.diag(np.abs(X)) # Find diagonal coefficients
    S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        result = 'Matrix is diagonally dominant!'
    else:
        result = 'Matrix is not diagonally dominant!'
    return result


ITERATION_LIMIT = 1000

# initialize the matrix
A = np.array([[2, 1, 1],
              [1, -1, 0],
              [3, -1, 2]])
# initialize the RHS vector
b = np.array([2, -2, 2])

dd(A)


print(A)
# prints the system
print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for it_count in range(7):
    if it_count != 0:
        print("Iteration {0}: {1}".format(it_count, x))
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x = x_new

print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)