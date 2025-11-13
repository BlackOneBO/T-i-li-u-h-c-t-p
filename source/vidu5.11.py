import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Tạo một mảng rỗng có cùng kích thước với mảng x
for i in range(4):
    y[i, :] = x[i, :] + v
print(y) # In ra mảng y sau khi đã thực hiện phép cộng từng hàng của x với v