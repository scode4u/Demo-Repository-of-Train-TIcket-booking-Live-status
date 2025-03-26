# m1 = [[1,2],
#       [3,4]]
# m2 = [[4,5],
#       [6,7]]
# result = [[0,0],
#           [0,0]]
# for i in range(len(m1)):
#     for j in range(len(m2[0])):
#         for k in range(len(m1)):
#             result[i][j] +=  m1[i][k] * m2[k][j]
# for r in result:
#     print(r)
    
# m1 = [[1,2,3],
#       [3,4,5],
#       [4,5,6]]
# m2 = [[6,7,8],
#       [7,8,9],
#       [8,9,0]]
# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
# for i in range(len(m1)):
#     for j in range(len(m2)):
#         for k in range(len(m1)):
#             result[i][j] +=  m1[i][k] * m2[k][j]
# for r in result:
#     print(r)


# m1 = [[1,2],
#       [3,4]]
# m2 = [[6,8],
#       [7,9]]
# result = [[0,0],
#           [0,0]]
# for i in range(len(m1)):
#     for j in range(len(m2)):
#         for k in range(len(m1)):
#             result[i][j] +=  m1[i][k] * m2[k][j]
# for r in result:
#     print(r)

def strassen(A,B):
    n = len(A)

    mid = n // 2
    a11 = A[:mid , :mid]
    a12 = A[:mid , mid:]
    a21 = A[mid: , :mid]
    a22 = A[mid: , mid:]
    b11 = B[:mid , :mid]
    b12 = B[:mid , mid:]
    b21 = B[mid: , :mid]
    b22 = B[mid: , mid:]

    P1 = strassen(a11 , b12 - b12)
    P2 = strassen(a11 + a12 , b22)
    P3 = strassen(a21 + a22 , b11)
    P4 = strassen(a22 , b21 - b11)
    P5 = strassen(a11 + a22 , b11 + b22)
    P6 = strassen(a11 - a22 , b21 + b22)
    P7 = strassen(b11 - a21 , b11 + b12)

    c11 = P5 + P4 - P2 + P6
    c12 = P1 + P2
    c13 = P3 + P4
    c22 = P5 + P1 - P3 - P7
