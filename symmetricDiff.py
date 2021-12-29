if __name__ == '__main__':
    # myset = {1,2,3}
    # print(type(myset))
    # print(myset)
    # myset.add(5)
    # print(myset)
    # # myset.update([10,11]) # same
    # myset.update((12,13)) # same 
    # print(myset)
    # myset.discard(12)
    # print(myset)
    # myset.remove(2) # remove and discard same work
    # print(myset)
    sizeM = int(input())
    M = set(map(int,input().split()))
    sizeN = int(input())
    N = set(map(int,input().split()))
    # print(f"{sizeM}\n{M}\n{sizeN}\n{N}")
    res = sorted(M.symmetric_difference(N))
    print(res)
    for number in res:
        print(number)