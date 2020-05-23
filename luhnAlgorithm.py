def number_maker():
    """Nathaniel Lowis 18/01/18
    Inputs - number (string)
    Outputs - number(string)
    Allows user to enter credit card number then to validate it """
    
    number = input("Please enter your number: ")            #This will input a number as a string
    
    while number.isdigit() == False:                    #This validates it until it is just numbers
        number = input("Please enter a number: ")
        
    return number       #returns to the main program
    
#---------------------------------------------------------------------------------------------------------------------------------------------------


def checker(number):
    """Nathaniel Lowis - 18/01/18
    Inputs - number(string)
    Outputs - Whether it is a credit number
    This will check if it is a number"""
    
    checkerNumber = number[-1]          #Takes the last number
    total = 0                       #sets totals to 0
    count = 0                       #The posistion of the string
    number2 = number[:-1]               #Takes all but last digit
    
    for element in number2:             #For every digit in number2
        evenOrNot = count % 2            #Checks if it is in a even posistion 0,2,4...
        count = count + 1     #total increments
        if evenOrNot == 0:
            total = total + int(element)        #total increases by the number
        else:
            stringElement = int(element)                #The number is made an integers and then multiplied by 2 and made a string
            multiplyElement = str(stringElement *2)
            
            try:                                                                #This will check if there is 1 or 2 digits in the number
                addedDigits = int(multiplyElement[0]) + int(multiplyElement[1])   #2 numbers are added together
            except:
                addedDigits = int(multiplyElement[0])    
                
            total = total + addedDigits             #total increases by the addedDigits
            
    strTotal = str(total)               #total changed to a string and last digit taken
    finalNumber = str(10 -int(strTotal[-1]))
    
    if finalNumber == checkerNumber:            #If checker and finalNumber == its a credit card if not ints not a credit card number   
        print(number, "is a real Credit Card number")
    else:
        print(number, "is not a real Credit Card number")
#---------------------------------------------------------------------------------------------------------------------------------------------------


def again():
    """ This will ask the user whether they want to do the program again.  """
    programAgain = input("Do you want to do the program again? Y or N: ")       #This will ask the user whether they want to re do the program
    
    while programAgain not in ["Y", "y", "yes", "Yes","YES", "No", "NO", "n", "N", "no"]:
        programAgain = input("Do you want to do the program again? Y or N: ")
        
    if programAgain in ["Y", "y", "yes", "Yes","YES"]:     #This will check where to go next
        answer = True  #This will then be returned and the menu will be while answer = True
    else:
        answer = False


    return answer
#---------------------------------------------------------------------------------------------------------------------------------------------------

#main
looper = True           #Sets looper to True
while looper == True:               #while looper == True it will do the 3 functions
    numberToUse = number_maker()
    checker(numberToUse)
    looper = again()
        
