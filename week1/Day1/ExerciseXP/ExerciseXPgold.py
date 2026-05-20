#Challenge 1 Whats the season 
#INSTRUCTION
# 1. Ask the user to input a month (1 to 12).
# 2. Display the season of the month received:
# - Spring runs from March (3) to May (5)
# - Summer runs from June (6) to August (8)
# - Autumn runs from September (9) to November (11)
# - Winter runs from December (12) to February (2)

def monthWeather():
    user_month=input("please enter the month:")
    spring_months=["March","April","May"]
    summer_months=["June","July","August"]
    autumn_months=["September","October","November"]
    winter_months=["December","January","February"]
    if user_month in spring_months:
        print("The season is Spring")
    elif user_month in summer_months:
        print("the season is summer")
    elif user_month in autumn_months:
        print("the season is autumn")
    elif user_month in winter_months:
        print("the season is winter")

# ====================================divider===============
#Challenge 2 : For loop
#INSTRUCTION
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

def printNumbers():
    for number in range (0,20):
        print(number)
def printEvenNumbers():
    for number in range(0,20):
        if(number%2==0):
            print(number)

# ====================================divider===============
#Challenge 3 : While loop
# #INSTRUCTION
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.
def keepAsking():
    while True:
        user_name=input("please enter yout name :")
        if user_name : 
            print("thank you")
            break


#=====================================divider===============
#Challenge 4 : check the indexes 
#INSTRUCTION
# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.

# Example: if input is Cortana we should be printing the index 1
def checkIndexes():
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    user_name=input("please enter a name:")
    if user_name in names : 
        print( f"the first occurence of the name is at indexn:{names.index(user_name)}")
    else :
        print("the name is not in the list")


#=====================================divider===============
#Challenge 5 : Greatest Number

#INSTRUCTION 
# Ask the user for 3 numbers and print the greatest number.
def greatestNumber():
   
    while True:
        numbers=[]
        try:
            for i in range (0,3):
                if(i==0):
                    user_number=int(input("please enter the 1st number:"))
                    numbers.append(user_number)
                elif(i==1):
                    user_number=int(input("please enter the 2nd number:"))
                    numbers.append(user_number)
                else:
                    user_number=int(input("please enter the 3rd number:"))
                    numbers.append(user_number)
                
            print(f"the greatest number is : {max(numbers)}")
        except ValueError:
            print("please enter a valid number")
        except Exception as e:
            print(f"an error occurred: {e}")
#NOTE FROM THE STUDENT : Ihave used the max() function to find the greatest number  and i tried something new that i learned recently which is error management to make sure that the user enters a valid number and to catch any other unexpected errors that may occur during the execution of the program.
#=====================================divider===============

#Challenge 6 : Random Number 
#INSTRUCTION
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says “Winner”.
# If the user guesses the wrong number print a message that says “Better luck next time.”
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost.
def randomNumber():

    import random
    try:
        user_number=[]
        won_game=0
        lost_game=0
        for i in range (0,10):
            user_number.append(int(input("please enter a number:")))
        computer_choice=random.choice(user_number)

        while True:
            stop_flag=0
            user_guess=int(input("please guess the computer choice:"))
            if user_guess==computer_choice:
                print("congratulations you guessed the correct number")
                won_game+=1
                break
            else:
                print("try again")
                stop_flag+=1
            if stop_flag==3:
                lost_game+=1
                print(f"sorry you have used all your attempts the correct number was {computer_choice}")
                break
    except ValueError:
        print("please enter a valid number")
    except Exception as e:
        print(f"an error occurred: {e}")

