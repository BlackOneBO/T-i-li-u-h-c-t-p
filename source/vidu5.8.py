import numpy as np

x = np.array([[1, 2], [3, 4]]), dtype=np.float64 # Tạo một mảng numpy hai chiều với kiểu dữ liệu float64
y = np.array([[5, 6], [7, 8]]), dtype=np.float64 # Tạo một mảng numpy hai chiều khác với kiểu dữ liệu float64

print(x + y) # In ra kết quả của phép cộng hai mảng x và y
print(np.add(x, y)) # Sử dụng hàm add của numpy để thực hiện phép cộng hai mảng x và y
print(x - y) # In ra kết quả của phép trừ hai mảng x và y
print(np.subtract(x, y)) # Sử dụng hàm subtract của numpy để thực hiện phép trừ hai mảng x và y
print(x * y) # In ra kết quả của phép nhân hai mảng x và y
print(np.multiply(x, y)) # Sử dụng hàm multiply của numpy để thực hiện phép nhân hai mảng x và y
print(x / y) # In ra kết quả của phép chia hai mảng x và y
print(np.divide(x, y)) # Sử dụng hàm divide của numpy để thực hiện phép chia hai mảng x và y
print(np.sqrt(x)) # Sử dụng hàm sqrt của numpy để tính căn bậc hai của mỗi phần tử trong mảng x