import numpy as np
v = np.array([1,2,3]) # Dòng lệnh này tạo một mảng numpy một chiều với 3 phần tử
w = np.array([4,5]) # Dòng lệnh này tạo một mảng numpy một chiều với 2 phần tử
print(np.reshape(v, (3, 1)) * w) # Dòng lệnh này in ra tích ngoài của v và w
x = np.array([[1,2,3], [4,5,6]]) # Dòng lệnh này tạo một mảng numpy hai chiều với 2 hàng và 3 cột
print(x + v) # Dòng lệnh này cộng mảng x với mảng v, sử dụng tính chất phát sóng của numpy
print((x.T + w).T) # Dòng lệnh này cộng mảng x với mảng w, sử dụng tính chất phát sóng của numpy
print(x + np.reshape(w, (2, 1))) # Dòng lệnh này cộng mảng x với mảng w, sử dụng tính chất phát sóng của numpy
print(x * 2) # Dòng lệnh này nhân tất cả các phần tử của mảng x với 2