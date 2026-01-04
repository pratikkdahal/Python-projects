#inside a infinite loop
    # ask to roll the dice

    #if user enters y
    #generate two random numbers 

    #if user enters n
    #print thank you

    #if user enters any except y and n
    #print invalid choice



import random

def get_numbers():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"({die1}, {die2})")

def get_choice():
    choice = input("Do you want to roll the dice? (y/n): ").lower()
    return choice

while True:
    choice = get_choice()

    if choice == "y":
        get_numbers()
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice, try again.")
