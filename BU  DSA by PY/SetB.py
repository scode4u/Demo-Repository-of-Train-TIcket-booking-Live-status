# Ques1 Write a Python program to print the first 10 positive integers (1 through 10) using a for loop.

# Name : Suryansh Singh
# Enrollment No. : S24MCAG0050

# for i in range(1,11):
#     print(i,end=" ")    


# Ques 2 Write a Python program to calculate the sum of all even numbers between 1 and 100 using a while loop.

# Name : Suryansh Singh
# Enrollment No. : S24MCAG0050

# num = 1
# total = []
# while(num <= 100):
#     if num % 2 == 0:
#         total.append(num)
#     num += 1
# print(sum(total))

# total = []
# for i in range(101):
#     if i % 2 == 0:
#         total.append(i)
# print(sum(total))

# Ques 3 Write a Python program that asks the user to enter a grade percentage (0 to 100) and then prints the corresponding letter grade (A, B, C, D, or F) based on standard grading scales.

# Name : Suryansh Singh
# Enrollment No. : S24MCAG0050

# ask_for_grades = float(input("Enter the grades percentage : "))
# if (ask_for_grades <= 20):
#     print("Yout grade is 'F' ")
# elif ( 20 < ask_for_grades <= 40):
#     print("Your grade is 'D' ")
# elif ( 40 < ask_for_grades <= 60):
#     print("Your grade is 'C' ")
# elif (60 < ask_for_grades <= 80):
#     print("Your grade is 'B' ")
# elif (80 < ask_for_grades <= 100):
#     print("Your grade is 'A' ")
# else:
#     print("Error submission")


# Ques 4 Write a Python program that prints a right-angled triangle pattern of stars (*) with 5 rows. 

# Name : Suryansh Singh
# Enrollment No. : S24MCAG0050

num = 5
for i in range(1 , num + 1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
