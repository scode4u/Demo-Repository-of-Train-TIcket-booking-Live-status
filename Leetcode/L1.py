# 1. 
# for i in range(4):
#     for j in range(4):
#         print("*",end="  ")
#     print()

# 2. 
# for i in range(9):
#     for j in range(i):
#         print("* ",end="")
#     print(" ")
# 
# 3.
# for i in range(10):
#     for j in range(1,i):
#         print(j,end=" ")
#     print(" ")

# 4.
# for i in range(10):
#     for j in range(0,i):
#         print(i, end=" ")
#     print(" ")

# 5.
# for i in range(10):
#     for j in range(i,10):
#         print("* ",end=" ")
#     print(" ")

# 6.
# for i in range(5):
#     for j in range(5 - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()

# 7.
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(2*n-2 * i-1):
#         print("*", end="")
#     print()

# 8.
# for i in range(10):
#     for j in range(i):
#         print("*",end="")
#     print("")
# for i in range(10): 
#     for j in range(i,10):
#         print("*",end="")
#     print("")

# class Solution:
#     def evenlyDivides(N):
#         N = str(N)
#         for i in range(len(N)):
#             N = int(N)
#             if i % 2 == 0:
#                 count = i + 1
#             print(count)


#     N = int(input())
#     evenlyDivides(N)

number  = 123
for i in range(number[-5:-2]):
    print(number)