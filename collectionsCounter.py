from collections import Counter
# list = [2,3,4,5,6,8,7,6,5,18]
# c = Counter(list)
# print(c)
# # c = Counter(list).items()
# # c = Counter(list).keys()
# c = Counter(list).values()
# print(c)
# X = int(input()) #variable to store the number of shoes
# S = Counter(map(int,input().split())) # store the sizez of shoes
# # print(S)
# n = int(input()) # this variable store number of customers
# # N = int()
# earnings = 0
# # print(S[6])
# # S[6] -= 1
# # print(S)
# for customer in range(n):
#     size , price = map(int,input().split())
#     if size in S and S[size] > 0:
#         S[size] -= 1
#         earnings += price
# print(earnings)
 # =============================================================
 
number_of_shoes_in_shop = int(input("Enter the number of shoes in the shop: "))
list_of_shoes_sizez = Counter(map(int,input("Enter sizez of each shoes: enter each shoes of size separated with space").split()))
number_of_customers = int(input("Enter total number of customers in the shop: "))
earnings_from_shoes = 0
for customer in range(number_of_customers):
    shoes_size , shoes_price = map(int,input("Enter size of shoes and its price: ").split())
    if shoes_size in list_of_shoes_sizez and list_of_shoes_sizez[shoes_size] > 0:
        list_of_shoes_sizez[shoes_size] -= 1
        earnings_from_shoes += shoes_price

print(f"The owner of the shop earn money form the shoes is : {earnings_from_shoes}")