#EXERCISE 1 :
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
def listToDict():
    keys=["Ten","Twenty","Thirty"]
    values=[10,20,30]
    
    KV_dict={}
    for i in range(0,3):
        KV_dict.update({keys[i]:values[i]})
        
    print(KV_dict)
        

# =====================Divider============================

#Exercise 2: Cinemax #2
#INSTRUCTION
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


def cineMax():
        FinalFamilyMemberDict={}
        TotalCost=0
        howManyAreThey=int(input("How many are you ? : "))
        for i in range(0,howManyAreThey):
            FinalFamilyMemberDict.update({input('type your name :'): int(input("type your age :"))})
        else:
            print("you got registred , we'll give you the ticket cost in a while ")

        for member in FinalFamilyMemberDict:
            if(FinalFamilyMemberDict[f"{member}"]<3):
                 print(f"{member}n,your ticket is free")
                 
            elif(FinalFamilyMemberDict[f"{member}"]>3 and FinalFamilyMemberDict[f"{member}"]<12 ):
                TotalCost+=10
                print(f"{member},your ticket cost 10$")
                
            elif(FinalFamilyMemberDict[f'{member}']>12):
                TotalCost+=15
                print(f"{member},your ticket is 15$")
        print(f"the total cost is :{TotalCost} ")

         
cineMax()

#======================Divider========================================
# Exercise 3: Zara
# # Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

# Create and manipulate a dictionary that contains information about the Zara brand.
def ZaraBrand():
    brand={
    'name':'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men','women','children','home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green'] 
        }
}

#Changing number store to 2 
    brand.update({'number_stores': 2})
    
    #Print a sentence describing Zara’s clients using the type_of_clothes key.
    print(f"Zara's clients are : {brand['type_of_clothes']}")
    
    brand.update({'country_creation': "Spain"})
    
    #Check if international_competitors exists and, if so, add “Desigual” to the list
    
    if("international_competitors" in brand):
        brand["international_competitors"].append("Desigual")
    
    #Delete the creation_date key.
    brand.pop('creation_date')
    
    #Print the last item in international_competitors.
    print(brand['international_competitors'][len(brand['international_competitors'])-1])
    
    #Print the major colors in the US.
    for color in brand['major_color']['US']:
        print(color)
    
    #Print the number of keys in the dictionary.
    count=0
    for items in enumerate(brand):
        count+=1
    
    print(f"the number of key here in the dictionnary is :{count}")
    
    #Print all the keys of the dictionnary
    
    keyList=brand.keys()
    
    for element in keyList:
        print(element)

#======================Divider========================================
ns
#Exercise 4 : Some geography 
#Goal: Create a function that describes a city and its country.

# Step 1: Define a Function with Parameters

# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.


# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.


# Step 3: Call the Function

# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").



def describe_city(city,country="Unknown"):
    print(f"{city} is a city in {country}")

describe_city("Abidjan")

#======================Divider========================================

# Exercise 5 : Random
# Goal: Create a function that generates random numbers and compares them.

# Key Python Topics:

# random module
# random.randint() function
# Conditional statements (if, else)


# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.


# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.


# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100.


import random 

#Create a function with a parameter which accept a number between 1 and 100
def randomFunc(number):
    randomNumber=random.randint(1, 100)

    if (number==randomNumber):
        print("you are successful")
    else:
        print("you failed")

    print(f"the random number was {randomNumber} and your number was {number}")
    
func_param=int(input("enter a number between 1-100 : "))

if(func_param>0 and func_param<=100):
    randomFunc(func_param)
else:
    print("chose another Number")

#======================Divider========================================
# 🌟 Exercise 6 : Let’s create some personalized shirts !
# Goal: Create a function to describe a shirt’s size and message, with default values.

# Key Python Topics:

# Functions with parameters and default values
# Keyword arguments


# Step 1: Define a Function with Parameters

# Define a function called make_shirt().
# This function should accept two parameters: size and text.


# Step 2: Print a Summary Message

# Set up the function to display a sentence summarizing the shirt’s size and message.


# Step 3: Call the Function



# Step 4: Modify the Function with Default Values

# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.


# Step 5: Call the Function with Default and Custom Values

# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.


def makeShirt(size="large",text="I love Python"):
    print(f"summary ; your size is {size} and the text on your shirt {text}")
makeShirt()
makeShirt("medium")
makeShirt("extra large","Hassan is a ducking Diamond")


#======================Divider========================================
#Exercise 7 : Weather Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
# 🌟 Exercise 7 : Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Key Python Topics:

# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)


# Step 1: Create the get_random_temp() Function

# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.


# Step 2: Create the main() Function

# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”


# Step 3: Provide Temperature-Based Advice

# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


# Step 4: Floating-Point Temperatures (Bonus)

# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.


# Step 5: Month-Based Seasons (Bonus)

# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.


def get_random_temp():
    import random
    return random.uniform(-10,40)


def main():
    temp=get_random_temp()

    elif(temp>0 and temp<16):
        print("Quite chilly! Don’t forget your coat.")
    elif(temp>16 and temp<23):
        print("Nice weather")
    elif(temp>24 and temp<32):
        print("A bit warm, stay hydrated")
    elif(temp>33 and temp<40):
        print("It’s really hot! Stay cool")
main()

def get_random_temp_bonus():
    # Modify get_random_temp() to return temperatures specific to each season.
    import random
    summer_months = [6, 7, 8]
    winter_months = [12, 1, 2]
    autumn_months = [9, 10, 11]
    spring_months = [3, 4, 5]
    
    month = int(input("Enter the month number (1-12): "))
    if month in summer_months:
        return random.uniform(25, 40)  # Summer temperatures
    elif month in autumn_months:
        return random.uniform(10, 25)  # Autumn temperatures
    elif month in winter_months:
        return random.uniform(-10, 10)  # Winter temperatures
    else:  # spring
        return random.uniform(10, 20)  # Spring temperatures


def mainBonus():
    month = int(input("Enter the month number (1-12): "))
    summer_months = [6, 7, 8]
    winter_months = [12, 1, 2]
    autumn_months = [9, 10, 11]
    spring_months = [3, 4, 5]
    temp = get_random_temp_bonus()
      print(f"the temperature now is {temp}")
    if(month in summer_months):
        print("It's summer! Enjoy the warm weather!")
    elif(month in winter_months):
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif(month in autumn_months):
        print("It's autumn! Enjoy the crisp weather!")
    elif(month in spring_months):
        print("It's spring! Enjoy the blooming weather!")
        

#============================Divider========================================

 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


def topping():
    price=10
    while True:
         if(topping="quit"):
             print(f"the total is : {price}")
             break
        topping=str(input("enter a pizza Topping : "))
        price+=2.50