import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # Dong lệnh này tạo một mảng numpy hai chiều với 4 hàng và 3 cột
print(a) 
b = np.array([0, 2, 0, 1]) # Tạo một mảng numpy một chiều với 4 phần tử
print(a[np.arange(4), b]) # In ra các phần tử của mảng 'a' tại các vị trí được chỉ định bởi mảng 'b'
a[np.arange(4), b] += 10 # Thêm 10 vào các phần tử của mảng 'a' tại các vị trí được chỉ định bởi mảng 'b'
print(a) # In ra mảng 'a' sau khi đã thực hiện phép cộng