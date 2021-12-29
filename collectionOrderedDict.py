from collections import OrderedDict
# ordinary_dictionary = {}

# ordinary_dictionary['a'] = 3
# ordinary_dictionary['b'] = 2
# ordinary_dictionary['a'] = 3
# print(ordinary_dictionary)

# ordered_dictionary = OrderedDict()
# ordered_dictionary['a'] = 2
# ordered_dictionary['b'] = 1
# ordered_dictionary['a'] = 2
# print(ordered_dictionary)
# print(ordered_dictionary.get('a'))
# print(len(ordered_dictionary))
# n = input().split()
# name = n[-1]
# age = n[:-1]
# print(n)
# new = n[-1]
# new1 = n[:-1]
# new3 = n[::-1]
# print(f"new: {new}\nnew1: {new1}\nnew3: {new3}\n")
# print(f"Name: {name}\nage: {age}")
od = OrderedDict() # od means ordered dicttionary
n = int(input("Enter the total number of item: "))

for i in range(n):
    item = input().split()
    item_price = int(item[-1])
    item_name = " ".join(item[:-1])
    if od.get(item_name):
        od[item_name] += item_price
    else:
        od[item_name] = item_price
print(od)
for key, value in od.items():
    print(f"{key} {value}")


# from collections import*
# N = int(input());
# d = OrderedDict();
# for i in range(N):
#     item = input().split()
#     itemPrice = int(item[-1])
#     itemName = " ".join(item[:-1])
#     if(d.get(itemName)):
#         d[itemName] += itemPrice
#     else:
#         d[itemName] = itemPrice
# print(d)
# for i in d.keys():
#     print(i, d[i])