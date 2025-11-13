import numpy as np
# Compute outer product of vectors
v = np.array([1,2,3]) # v has shape (3,)
w = np.array([4,5]) # w has shape (2,)
print(np.reshape(v, (3, 1)) * w) # Dong lệnh này in ra tích ngoài của v và w
x = np.array([[1,2,3], [4,5,6]]) # Dong lệnh này tạo một mảng numpy hai chiều với 2 hàng và 3 cột
print(x + v) # dòng lệnh này cộng mảng x với mảng v, sử dụng tính chất phát sóng của numpy
print((x.T + w).T)#Dòng lệnh này cộng mảng x với mảng w, sử dụng tính chất phát sóng của numpy
print(x + np.reshape(w, (2, 1))) # Dòng lệnh này cộng mảng x với mảng w, sử dụng tính chất phát sóng của numpy