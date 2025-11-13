import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1)) # Tạo một mảng bằng cách lặp lại mảng v thành 4 hàng
print(vv) # In ra mảng vv
y = x + vv # Cộng mảng x với mảng vv
print(y) # In ra mảng y sau khi đã thực hiện phép cộng