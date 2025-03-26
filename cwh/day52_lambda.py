# Lambda functions uses instead of simple defining functino
# def avg(a,b,c):
#     return (a+c) / c

# a,b,c = 0
avg = lambda a,b,c : (a+b)/c
print(avg(2,5,3))

