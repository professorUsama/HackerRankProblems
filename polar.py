# import cmath

# num = complex(input("Enter number: "))
# # num = complex(int(input("Enter number: ")))
# z = cmath.polar(num)
# print(z)

import cmath
num = complex(input())
print(cmath.polar(num)[0])
print(cmath.polar(num)[1])