def matrixMultiplication(matA, matB):
  # Get the dimensions of the matrices
  m = len(matA)
  n = len(matA[0])
  p = len(matB[0])

  # Initialize the resulting matrix with zeros
  matC = [[0 for _ in range(p)] for _ in range(m)]

  # Perform matrix multiplication
  for i in range(m):
    for j in range(p):
      for k in range(n):
        matC[i][j] += matA[i][k] * matB[k][j]

  return matC


# Given matrices
matrixA = [[1, 2, 3], [2, 2, 3], [1, 2, 3]]
matrixB = [[3, 1, 2], [2, 4, 6], [1, 1, 1]]

print("\nMatrix A:")
for x in matrixA:
  print(x)

print("\nMatrix B:")
for x in matrixB:
  print(x)

# Perform the matrix multiplication
result = matrixMultiplication(matrixA, matrixB)
print("\nResult ----->")
for x in result:
  print(x)
