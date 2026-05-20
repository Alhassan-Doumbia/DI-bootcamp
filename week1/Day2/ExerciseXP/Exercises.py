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
        
        try:
            howManyAreThey=int(input("How many are you ? : "))
        except ValueError:
            print("Please enter a valid number")
            return

        for i in range(0,howManyAreThey):
            try:
                FinalFamilyMemberDict.update({input('type your name :'): int(input("type your age :"))})
            except ValueError:
                print("Please enter a valid age")
                return
        else:
            print("you got registred , we'll give you the ticket cost in a while ")

        for member in FinalFamilyMemberDict:
            if(FinalFamilyMemberDict[f"{member}"]<3):
                 print(f"{member},your ticket is free")
                 
            elif(FinalFamilyMemberDict[f"{member}"]>=3 and FinalFamilyMemberDict[f"{member}"]<=12 ):
                TotalCost+=10
                print(f"{member},your ticket cost 10$")
                
            elif(FinalFamilyMemberDict[f'{member}']>12):
                TotalCost+=15
                print(f"{member},your ticket is 15$")
                
        print(f"the total cost is :{TotalCost} ")

         
#======================Divider========================================
# Exercise 3: Zara
# # Instructions
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
    print(f"the number of key here in the dictionnary is :{len(brand)}")
    
    #Print all the keys of the dictionnary
    
    keyList=brand.keys()
    
    for element in keyList:
        print(element)

#======================Divider========================================

#Exercise 4 : Some geography 

def describe_city(city,country="Unknown"):
    print(f"{city} is a city in {country}")

describe_city("Abidjan")

#======================Divider========================================

# Exercise 5 : Random

import random 

#Create a function with a parameter which accept a number between 1 and 100
def randomFunc(number):
    randomNumber=random.randint(1, 100)

    if (number==randomNumber):
        print("you are successful")
    else:
        print("you failed")

    print(f"the random number was {randomNumber} and your number was {number}")
    

if __name__ == "__main__":

    try:
        func_param=int(input("enter a number between 1-100 : "))

        if(func_param>0 and func_param<=100):
            randomFunc(func_param)
        else:
            print("chose another Number")

    except ValueError:
        print("Please enter a valid number")

#======================Divider========================================

# 🌟 Exercise 6 : Let’s create some personalized shirts !

def makeShirt(size="large",text="I love Python"):
    print(f"summary ; your size is {size} and the text on your shirt {text}")

makeShirt()
makeShirt("medium")
makeShirt("extra large","Hassan is a ducking Diamond")


#======================Divider========================================
#Exercise 7 : Weather Advice

def get_random_temp():
    import random
    return random.uniform(-10,40)


def main():
    temp=get_random_temp()

    print(f"The temperature right now is {temp} degrees Celsius.")

    if(temp<0):
        print("Brrr, that’s freezing! Wear some extra layers today.")
        
    elif(temp>=0 and temp<=16):
        print("Quite chilly! Don’t forget your coat.")
        
    elif(temp>16 and temp<=23):
        print("Nice weather")
        
    elif(temp>=24 and temp<=32):
        print("A bit warm, stay hydrated")
        
    elif(temp>32 and temp<=40):
        print("It’s really hot! Stay cool")

main()

def get_random_temp_bonus():
    # Modify get_random_temp() to return temperatures specific to each season.
    import random
    
    summer_months = [6, 7, 8]
    winter_months = [12, 1, 2]
    autumn_months = [9, 10, 11]
    
    try:
        month = int(input("Enter the month number (1-12): "))
    except ValueError:
        print("Please enter a valid month")
        return

    if month in summer_months:
        return random.uniform(25, 40)  # Summer temperatures
    
    elif month in autumn_months:
        return random.uniform(10, 25)  # Autumn temperatures
    
    elif month in winter_months:
        return random.uniform(-10, 10)  # Winter temperatures
    
    else:  # spring
        return random.uniform(10, 20)  # Spring temperatures


def mainBonus():
    
    try:
        month = int(input("Enter the month number (1-12): "))
    except ValueError:
        print("Please enter a valid month")
        return

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

# 🌟 Exercise 8: Pizza Toppings

def topping():
    price=10
    toppingList=[]

    while True:
        
        topping=input("enter a pizza Topping : ")

        if(topping=="quit"):
            print(f"the total is : {price}$")
            print(f"your toppings are : {toppingList}")
            break

        toppingList.append(topping)
        print(f"Adding {topping} to your pizza.")
        
        price+=2.50


if __name__ == "__main__":
    topping()