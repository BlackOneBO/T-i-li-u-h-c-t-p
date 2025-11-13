import numpy as np
a = np.zeros((2,2)) # Dòng lênh này tạo ra một mảng numpy hai chiều với 2 hàng và 2 cột và tất cả giá trị trong mảng là số 0
b = np.ones((1,2)) # Dòng lệnh này tạo ra một mảng numpy hai chiều với 1 hàng và 2 cột và tất cả các giá trị trong mảng là số 1
c = np.full((2,2), 7) # Dòng lệnh này tạo ra một mảng numpy hai chiều với 2 hàng và hai cột và tất cả các giá trị là số 7
d = np.eye(2) # Dòng lệnh này tạo ra một mảng numpy hai chiều với 2 hàng, 2 cột và các giá trên đường chéo chính là 1 và các giá trị khác là 0 
e = np.random.random((2,2)) # Lệnh này tạo một mảng numpy hai chiều với hai hàng và 2 cột với giá trị bên trong mảng là ngẫu nhiên phân phối đều từ 0 đến 1 nếu nó là int còn float thì từ 0.0 đến 1.0