import numpy as np

aMax = np.array([[2,2,2,2],
                [4,4,4,4]])

print('note: The outer [] represent the matrix.\nInside it are array which represet row and col')
print(aMax) # print out the array inside []
print('matrix depth:', aMax.ndim) # show the depth of the array
print("matrix's shape (row to col):", aMax.shape) 
print('matrix size:', aMax.size) # 
print('matrix data type:', aMax.dtype) # data type

