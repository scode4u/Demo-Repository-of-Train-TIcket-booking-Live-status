def findUnion(a,b):
    a = set(a)
    b = set(b)
    c = a.union(b)
    c = list(c)
    c.sort()
    return c
print(findUnion([-7,8],[-8,-3,8]))
# Completed     