# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     i = []
#     happiness = 0
#     for number in range(n):
#         i.append(int(input()))
#     A = set([int(input()) for a in range(m)])
#     B = set([int(input()) for a in range(m)])
#     for check in i:
#         if check in A:
#             happiness +=1
#         elif check in B:
#             happiness -=1
#     print(happiness)

if __name__ == '__main__':
    n,m = map(int,input().split())
    i = list(map(int,input().split()))
    happiness = 0
    A = set(list(map(int,input().split())))
    B = set(list(map(int,input().split())))
    for check in i:
        if check in A:
            happiness +=1
        elif check in B:
            happiness -=1
    print(happiness)