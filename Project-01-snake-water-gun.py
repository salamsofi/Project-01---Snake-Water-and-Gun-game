# PROJECT 1: SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our childhood. If you haven't, google the
# rules of this game and write a python program capable of playing this game with the
# user.

import random 

computer = random.choice([-1,0,1])

print("Enter 's' for 'Snake', 'w' for 'water', and 'g' for 'Gun'")

youStr = input("Enter your choice: ")
youDict = {'s' : 1, 'w' : -1, 'g' : 0}

reversed_Dict = {1 : 'Snake', -1 : 'Water', 0 : 'Gun'}

you = youDict[youStr]

print(f"You choose {reversed_Dict[you]} and computer choose {reversed_Dict[computer]}")

if youStr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

if computer == you:
    print("Draw!!! Try Again")
else:
    if ((computer - you == 2 ) or (computer - you == -1)):
        print("You Lost!!! Try Again")
    else:
        print("You Won!!!")
# or else:
#     if computer == 1 and you == -1: 2
#         print("You Lost!!! Try Again")
        
#     elif computer == 1 and you == 0: 1
#         print("You won!!!")

#     elif computer == 0 and you == 1: -1
#         print("You Lost!!! Try Again")
                
#     elif computer == 0 and you == -1: 1
#         print("You won!!!")

#     elif computer == -1 and you == 1: -2
#         print("You Won!!!")
    
#     elif computer == -1 and you == 0: -1
#         print("You Lost!!! Try Again")

#     else:
#         print("Something went wrong")
