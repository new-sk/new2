import numpy as np

data = np.array([[1,2,3],[4,5,6.]])
data = np.zeros([2,3],int)
data = np.ones([2,3])
data = np.random.random([2,3])



print(data, data.shape, data.ndim, data.dtype)

d1 = np.arange(6)
d2 = d1.reshape([2,3])
print(d1, d1.shape, d1.ndim, d1.dtype)
print(d2, d2.shape, d2.ndim, d2.dtype)

d2[1,1] = -1
print(d1)
print(d2)

d3 = d1.reshape([2,3]).copy()
d3[1,1] = 500
print(d1)
print(d3)

print(np.add(d2,d3))

