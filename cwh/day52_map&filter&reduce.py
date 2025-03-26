# Map
# def cube(x):
#     return x*x*x
# newl = []
# lst = [1,2,3,4,5]
# for item in lst:
#     newl.append(cube(item))
# print(newl)

# or using map function 
def map_cube(x):
    return x*x*x
lst = [1,2,3,4,5]
newl = list(map(map_cube, lst)) # by using map , we can perform operation in single line 
print(newl)


# filter 
# def filter_func()
