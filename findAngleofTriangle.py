import math
if __name__ == '__main__':
    AB = int(input("Enter AB side of right triangle: "))
    BC = int(input("Enter BC side of right triangle: "))
    AC = math.sqrt(AB**2+BC**2) # find the square root 
    BC /=2.0
    AC /=2.0
    angle = round(math.degrees(math.acos(BC/AC)))
    print(BC)
    # print(u'\xb0')
    print(f"{str(angle)}\xb0")  # unicode value of degree