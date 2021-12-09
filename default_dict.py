from collections import defaultdict

d = defaultdict(list)

# d['Python'].append("good")
# d['Python'].append("wide range")
# d['usama'].append("amjid")


# print(d)
# for i in d:
#     print(i)

n , m = map(int, input().split())

for i in range(1, n+1):
    d[input()].append(i)

print(d)
print(len(d['a']))
for j in range(1,m+1):
    key = input()
    if len(d[key]) > 0:
        # print(" ".join(str(c) for c in d[key]))
        print(" ".join(str(c) for c in d[key]))
    else:
        print(-1)