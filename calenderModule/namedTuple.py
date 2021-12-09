from collections import namedtuple

# point = namedtuple('Point','x,y')
# p1 = point(1,2)
# p2 = point(3,4)
# product = (p1.x * p2.x) + (p1.y * p2.y)
# print(product)

# Car = namedtuple('Car', 'Price Mileage Colour Class')
# hilux = Car(Price=1000, Mileage=30, Colour= 'cyan', Class= 'Y')
# print(hilux)
# print(hilux.Class)

if __name__ == '__main__':
    n = int(input()) # number of total students
    input_feilds = ','.join(input().split()) # input_feilds store column feilds like id, marks, name, Class
    school = namedtuple('School', input_feilds)
    sum = 0 # store std marks
    for i in range(n):
        input_feilds_data = input().split()
        std_data = school(*input_feilds_data)
        sum += int(std_data.MARKS) # typecast str to int
    print(sum/n)
    print(sum)
