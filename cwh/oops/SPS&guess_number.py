# import random

# def game(user , computer):
#     print("user input is : ",user)
#     print("Computer chooses : ",computer)
#     if ((user == 0 and computer == 0) or (user == 1 and computer == 1) or (user == 2 and computer == 2)):
#         print("It's a tie")
#     elif ((user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0)):
#         print("Computer Wins")
#     else:
#         print("User Wins")
    

# user = int(input("Enter 0 for Stone, 1 for Paper, Enter 2 for Scissor :"))
# computer = random.randint(0,2)

# game(user , computer)




# import random

# def guess(computer_guess_value):
#     count = 0

#     while True:
#         user_input = int(input("Guess the number between from 1 to 100: "))
#         count += 1

#         if user_input < computer_guess_value:
#             print("Too small number")

#         elif user_input > computer_guess_value:
#             print("Too large number")

#         else:
#             print("Your guess is right..!!")
#             print("You guessed the number in", count, "times")
            
#             if count <= 2:
#                 print("You're wonderful!")
#             elif count > 3:
#                 print("You're a fucking looser asswhole just fuck yourself")
#             break  # Exit the loop after the correct guess

# computer_guess_value = random.randint(1, 100)
# guess(computer_guess_value)

