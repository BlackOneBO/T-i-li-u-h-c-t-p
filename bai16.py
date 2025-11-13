from math import *
h = float(input("Nhap chieu cao vat tha roi xuong: "))
g = 9.81
Vi = float(input("Nhap van toc vat tha : "))
v = sqrt(Vi**2 + 2*g*h)
print("Van toc vat khi cham dat la:", v, "m/s")
