import numpy as np


e = 5
print(e)

v = np.array([-4, 8, 5])
print(v)
print(v.reshape(1, 3))
print(v.reshape(3, 1))
m = np.array([[1, 0, -9], [3, -6, 7]])
print(m)
print(m.T)
print(type(e))
print(type(v))
print(type(m))
e_array = np.array([5])
print(type(e_array))
print(v.shape)
print(m.shape)
m2 = np.array([[-4, 8, 5], [-4, 8, 5]])
print(m + m2)
print(m - m2)
print(m2 + 2)
print(m2 * 2)
print(np.dot(m, m2.T))
