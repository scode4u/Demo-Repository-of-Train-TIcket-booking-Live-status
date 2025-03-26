# a = int(input())
# for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")




# try except using exception handling 

try:
    a = int(input())
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print("Sorry Invalid Input")

print("It means we're outside of the loop")