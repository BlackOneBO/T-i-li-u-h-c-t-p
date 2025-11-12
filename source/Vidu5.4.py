import numpy as np # Thêm thư viện numpy để làm việc với mảng
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) # Tạo một mảng numpy hai chiều với 3 hàng và 4 cột
row_r1 = a[1, :] # Lấy hàng thứ 1 dưới dạng 1 chiều
row_r2 = a[1:2, :] # Lấy hàng thư 1 dưới dạng 2 chiều
print(row_r1, row_r1.shape) # lệnh in ra hàng 1 và kích thước của nó    
print(row_r2, row_r2.shape) # Lệnh in ra hàng 2 và kích thước của nó
col_r1 = a[:, 1] # Lấy cột thứ 1 dưới dạng 1 chiều  
col_r2 = a[:, 1:2] # Lấy cột thứ 1 dưới dạng 2 chiều
print(col_r1, col_r1.shape) # lệnh in ra cột 1 và kích thước của nó
print(col_r2, col_r2.shape) # Lệnh in ra cột 2 và kích thước của nó