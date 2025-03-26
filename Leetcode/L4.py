# Patterns

# 1234
# 1234
# 1234
# 1234
# n = 5
# for i in range(1,n):
#     for j in range(1,n):
#         print(j, end=" ")
#     print()

# ABCD
# ABCD
# ABCD

# n = 4
# char = 'A'
# for i in range(4):
#     for j in range(4):
#         print(chr(ord('A') + j),end=" ")
#     print()


# 123
# 456
# 789

# n = 1
# for i in range(3):
#     for j in range(3):
#         print(n, end="")
#         n += 1
#     print()


# A
# AB
# ABC

# n = 'A'
# for i in range(3):
#     for j in range(3):
#         print(n, end="")
#         n = chr(ord(n) + 1)
#     print()

# *
# **
# ***
# ****

# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# 1
# 2 2 
# 3 3 3
# 4 4 4 4 
# n = 4
# for i in range(n ):
#     for j in range(i+1):
#         # j += 1
#         print(i+1,end=" ")
#     print()

# A
# B B
# C C C 
# D D D D

# n = 'A'
# for i in range(4):
#     character = chr(ord(n) + i)
#     print(character * (i + 1))  


# 1
# 12
# 123
# 1234

# for i in range(1,5):
#     for j in range(1, i+1):
#         print(j,end="")
#     print()


# 1
# 21
# 321
# 4321
n = 4
for i in range(n):
    for j in range(i+1 , 0):
        j -= 1
        print(j,end=" ")
    print()