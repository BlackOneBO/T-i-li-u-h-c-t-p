import numpy as np
a = np.array([1, 2, 3]) # dòng lệnh này là tạo một mảng numpy một chiều với các phần tử 1, 2, 3
print(type(a)) # Dòng lệnh này in ra kiểu dữ liệu của biến a hiển thị rằng nó là một mảng numpy
print(a.shape) # Dòng lệnh này in ra kích thước của mảng a, cho biết nó có 3 phần tử trong một chiều
print(a[0], a[1], a[2]) # Dòng lệnh này truy cập và in ra các phần tử mảng a theo chỉ số của chúng  
a[0] = 5 # Dòng lệnh này gán giá trị cho phần tử a[0] thành 5
print(a) # Dòng lệnh này in ra mảng a sau khi thay đổi mảng phần tử đầu tiên của mảng
b = np.array([[1,2,3],[4,5,6]]) # Dòng lệnh này tạo một mảng numpy hai chiều với 2 hàng và 3 cột
print(b.shape) # Dòng lệnh này in ra kích thước của mảng b, cho biết nó có 2 hàng và 3 cột  
print(b[0, 0], b[0, 1], b[1, 0]) # Dòng lệnh này truy cập và in ra các phần tử cụ thể trong mảng b theo chỉ số hàng và cột