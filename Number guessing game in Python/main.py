"""
    this is a simple game , for using the conditions & user input 
    and ot put , using random and math modules to make the things 
    easy 
    """
import random
import math

lowestNumber = int(input(" please enter a number for your lowest Number : "))
highestNumber = int(input(" please enter a number for your highest Number : "))

if lowestNumber < highestNumber :
    pass
else:
    highestNumber = int(input(" please enter a valid number for your highest Number : "))

randomNumber = random.randint(lowestNumber , highestNumber)
i = 1 # this is for the condition to check wheter the user guess the number right or wrong
counter=0
userNumber = 0
while i :
    userNumber = int(input(" please enter your guess : "))
    counter += 1
    if userNumber < randomNumber:
        print(f"{userNumber} is lower than the game Number")
    elif userNumber > randomNumber:
        print(f"{userNumber} is higher than the game Number")
    elif userNumber == randomNumber:
        print(f"congratulations You won \n The number was {userNumber}\n you find it with {counter} tries.")
        i = 0 

'''developed by Mehrab_mahmoudifar
    Thank You ♥
    '''
