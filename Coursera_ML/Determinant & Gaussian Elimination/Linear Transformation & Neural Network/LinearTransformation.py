import numpy as np
 
 # transform 2 diamension matrix to 3 diamension matrix (1 cols, 3 rows)
def T(v): # take 2D array as input
    # create 3x3 array full of zeros
    w = np.zeros((3,1));
    
    # mul the 1st row of the matrix 
    w[0, 0] = v[0, 0]; # set it as the first value of w matrix
    # mul the 2nd row of the matrix
    w[2, 0] = v[1, 0]; # set it as the 3rd value of w matrix

    return w    
 
 # u = np.array(1,3); # 1 row by 3 col matrix
ma = np.array([[2],[3]]) # matrix a
mv = np.array([[4],[2]]) # matrix v
k = 9

print(' transform 2d to 3d: with ')
print(T(ma))

# multiply transform matrix
print(k * T(ma));
# transform sum of 2 matrix
'''
T(kv) = k.T(v)
'''
print('sum of m:\n', T(ma + mv)) 
print(f'T(kv) = k.T(v) with k = {k}:\n', k*T(ma + mv)) 
print('sum of m:\n', T(ma) + T(mv)) 



# 12 thasng 5 thi CSDL
