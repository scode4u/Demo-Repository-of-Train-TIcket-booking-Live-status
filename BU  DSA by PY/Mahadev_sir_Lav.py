# Write a Python program to assign the values 5, 3.14, and "Hello, Python!" to variables a, b, and c respectively. Print the values and their data types.
a = int(input("Enter the value : "))
b = float(input("Enter the value : "))
c = input("Enter the value : ")
print(f"{type(a)} and it's output is : {a}")
print(f"{type(b)} and it's output is : {b}")
print(f"{type(c)} and it's output is : {c}")


# Write a Python program to calculate the area of a rectangle. The program should take the length and width as inputs from the user and output the area.

breadth = int(input("Enter the breadth : "))
length = int(input("Enter the Length : "))
area = breadth*length
print("Area of rectangle is : ",area)

# Write a Python program to concatenate two strings "Hello" and "World!" with a space in between and print the result.

str1 = input()
str2 = input()
print(f"{str1} {str2}")

# Write a Python program to check if a number entered by the user is even or odd. Print an appropriate message based on the result.

num = int(input("Enter the number : "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

