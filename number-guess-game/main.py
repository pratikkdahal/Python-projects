
import random

random_num = random.randint(1,100)

while True:
    try:

        user_num = int(input("Enter a number between 1 to 100: "))

        if random_num == user_num:
            print("Yayy! you guessed it right masterrr.")
            break
        elif random_num > user_num:
            print("Too low!")
        
        else:
            print("Too high!")
    except ValueError:
        print("Invalid choice")


