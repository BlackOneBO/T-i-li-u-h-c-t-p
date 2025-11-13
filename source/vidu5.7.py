import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2) # Tạo một mảng boolean với cùng kích thước như 'a', với giá trị True tại các vị trí mà phần tử của 'a' lớn hơn 2
print(bool_idx) # In ra mảng boolean
print(a[bool_idx]) # In ra các phần tử của 'a' tại các vị trí mà mảng boolean có giá trị True
print(a[a > 2]) # Cách viết ngắn gọn hơn để in ra các phần tử của 'a' lớn hơn 2