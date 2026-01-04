# random import
#infinite loop 
    #user sanga number magnu paryo
    #random bata aako number ra user ko number compare
    #if same print yayy you guessed
    # if different you faile
    # if invalid show invalid input

import random

def get_number():
    num = random.randint(1,100)
    print(num)

def get_usernum():
    user_num = int(input("Enter a number from 1 to 100: "))
    return get_usernum

while True:

    user_num = get_usernum()
    
    if get_number == get_usernum:
        print("Yayy ! You guessed it right.")
    elif get_number != get_usernum:
        print("You cannot guess, sorry!")
        break
    else:
        print("Invalid number,please enter valid one!")


