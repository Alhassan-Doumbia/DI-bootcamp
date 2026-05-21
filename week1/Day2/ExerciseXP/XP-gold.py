#Exercise 1 : birthdays 
def ExerciseOne():
    birthdays={
        "Djenebou":"2005/03/08",
        "Mom":"1966/12/28",
        "Dad":"1965/05/05",
        "Hassan":"2005/02/22",
        "Souleyman":"2018/05/3O"
    }

    print("hi, welcome. you can look up the brithdays of the poeple in the list")
    user_choice=input("choose a name :")
    user_choice=user_choice.title()
    if user_choice in birthdays:
        print(f"the birthday of {user_choice} is {birthdays[user_choice]} ")

#==================================Divider========================================
# Exercise 2: Birthdays Advanced
# Before asking the user to input a person's name, print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for person's name”).
def ExerciseTwo():
    birthdays={
        "Djenebou":"2005/03/08",
        "Mom":"1966/12/28",
        "Dad":"1965/05/05",
        "Hassan":"2005/02/22",
        "Souleyman":"2018/05/3O"
    }
    print("hi, welcome. you can look up the brithdays of the poeple in the list")
    print(f"here are all the names in the list:{birthdays.keys()}")
    user_choice=input("choose a name :")
    user_choice=user_choice.title()
    if user_choice in birthdays:
        print(f"the birthday of {user_choice} is {birthdays[user_choice]} ")
    else:
        print("sorry, we don't have the birthday of this person in our list")

#==========================Divider========================================
# Exercise 3: 
# Exercise 3: Check the index
# nstructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list, print out the index of the first occurence of the name.

# Example: if input is 'Cortana' we should be printing the index 1

def exercise3:
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    try:
        userInput=input("enter a name : ")
        userInput=userInput.title()
        if(userInput in names):
            print(f"the index of the first occurence  of this word is {names.index(userInput)}")
        else:
            print("this word is not in our name list")
    except Exception as e : 
        print(f"there might be an error in the program , check {e}")