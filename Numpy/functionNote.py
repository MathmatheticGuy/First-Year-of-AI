import numpy as np
# ndarray - n-dimensional array
a = np.array([2,2,2,4,3]);
sh = a.shape

# Range. Auto list out numbers
b = np.arange(20);
print(b)

# Step. From the range 0 to 10. skip 2 numbers each step
c = np.arange(0, 10, 2)
print(c)

# Zeros
d = np.zeros(2) # print 0
print(d) 

# Multidimensional matrix
e = np.zeros((2, 10)) # print out 2 by 10 matrix
print('e:', e)

# print values in full array
f = np.full(6, 1); # print out 6 by 3 matrix with 1 as value 
print('full', f)


# Multidimensional full array
f = np.full((6, 3), 1); # print out 6 by 3 matrix with 1 as value 
print('Multidimensional full:\n', f);

aList = [2,4, 5,8,9];
g = np.array(aList);
print(g);

