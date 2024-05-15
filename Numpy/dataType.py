import numpy as np

# allow 1 dtype only in 1 array
# must be n by n matrix. (2x2 not 2x3) 
aMax = np.array([[2,2,2],
                [4, 2, "5"]], dtype=np.int32) # force dtype to int32

print(aMax);
print(aMax.dtype); # return <U11 mean data contain string
print(aMax[1][1].dtype);
print(aMax[0][1].dtype);
print(type(aMax[0][1])); # return wrong data type
  
d = {'1': 'A'}
ap = np.array([[d,1,2],
               [2,4,5]]);
print(ap)
print(ap.dtype)
