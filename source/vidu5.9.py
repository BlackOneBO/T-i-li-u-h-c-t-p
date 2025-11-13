import numpy as np

x = np.array([[1, 2], [3, 4]]) # Tạo một mảng numpy hai chiều với 2 hàng và 2 cột
y = np.array([[5, 6], [7, 8]]) # Tạo một mảng numpy hai chiều khác với 2 hàng và 2 cột
v = np.array([9, 10]) # Tạo một mảng numpy một chiều với 2 phần tử
w = np.array([11, 12]) # Tạo một mảng numpy một chiều khác với 2 phần tử

print(v.dot(w)) # In ra kết quả của phép nhân vô hướng giữa hai mảng v và w
print(np.dot(v, w)) # Sử dụng hàm dot của numpy để thực hiện phép nhân vô hướng giữa hai mảng v và w
print(x.dot(v)) # In ra kết quả của phép nhân ma trận giữa mảng x và v
print(np.dot(x, v)) # Sử dụng hàm dot của numpy để thực hiện phép nhân ma trận giữa mảng x và v
print(x.dot(y)) # In ra kết quả của phép nhân ma trận giữa hai mảng x và y
print(np.dot(x, y)) # Sử dụng hàm dot của numpy để thực hiện phép nhân ma trận giữa hai mảng x và y