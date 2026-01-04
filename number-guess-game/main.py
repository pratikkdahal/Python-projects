
# import random

# random_num = random.randint(1,100)

# while True:
#     try:

#         user_num = int(input("Enter a number between 1 to 100: "))

#         if random_num == user_num:
#             print("Yayy! you guessed it right masterrr.")
#             break
#         elif random_num > user_num:
#             print("Too low!")
        
#         else:
#             print("Too high!")
#     except ValueError:
#         print("Invalid choice")

import random

random_num = random.randint(1,100)

def user_num():
    num = int(input("Enter a number between 1 to 100: "))
    return num

while True:
    try:
        user_guess = user_num()
        if random_num == user_guess:
            print("Yayy! You guessed it master.")
            break
        elif random_num > user_guess:
            print("Too low!")
        
        else:
            print("Too high!")

    except ValueError:
        print("Invalid Choice!!!")