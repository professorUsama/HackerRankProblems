# if __name__ == '__main__':
#     n = int(input())
#     for outer in range(1,n+1):
#         for inner in range(1,outer+1):
#             print(inner,end="")
#         for reverse in range(inner-1, 0,-1):
#             print(reverse,end="")

#         print("")

for i in range(1,int(input())+1):
    print(((10**i-1)//(9))**2)