# n = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
# print(set(n))
from functools import reduce
def average(array):
    ans = round(reduce(lambda a,b:a+b,set(array))/len(set(array)),3)
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    avg = average(arr)
    print(avg)