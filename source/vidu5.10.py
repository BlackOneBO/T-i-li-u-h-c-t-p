import numpy as np
x = np.array([[1,2], [3,4]]) # Tạo một mảng numpy hai chiều với 2 hàng và 2 cột

print(np.num(x)) # In ra số lượng phần tử trong mảng x
print(np.sum(x, axis=0)) # Tính tổng các phần tử theo cột
print(np.sum(x, axis=1)) # Tính tổng các phần tử theo hàng
v = np.array([1,2,3])
print(v) # In ra mảng v
print(v.T)  # In ra chuyển vị của mảng v (không thay đổi gì vì v là mảng một chiều)