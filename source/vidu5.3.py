import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) # Tạo một mảng numpy hai chiều với 3 hàng và 4 cột
b = a[:2, 1:3] # Tạo một mảng con bằng cách cắt mảng a, lấy 2 hàng đầu tiên và cột thứ 1 đến cột thứ 2
print(a[0, 1]) # In ra phần tử ở hàng 0, cột 1 của mảng a
b[0, 0] = 77 # Thay đổi giá trị của phần tử ở hàng 0, cột 0 của mảng b thành 77
print(a[0, 1]) # In ra phần tử ở hàng 0, cột 1 của mảng a sau khi thay đổi mảng b