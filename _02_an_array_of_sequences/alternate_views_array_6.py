from array import array

octets = array('B', range(6))
matrix_1x6 = memoryview(octets)
print(matrix_1x6.tolist())

matrix_2x3 = matrix_1x6.cast('B', [2, 3])
print(matrix_2x3.tolist())

matrix_3x2 = matrix_1x6.cast('B', [3, 2])
print(matrix_3x2.tolist())

matrix_2x3[1, 1] = 22
matrix_3x2[1, 1] = 33
print(octets)
