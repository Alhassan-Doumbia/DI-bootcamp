#EXERCISE 1
#  Instructions
# Print the following output using one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
print("helloworld"*4)


#=======================================Divider========================================
#EXERCISE 2

# Instructions
# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).
Result=(99**3)*8
print(Result)

#=======================================Divider========================================
#EXERCISE 3
# Instructions
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare



>>> 5 < 3 #False
>>> 3 == 3 #True
>>> 3 == "3" #False
>>> "3" > 3 #error
>>> "Hello" == "hello"#False



#=======================================Divider========================================
#EXERCISE 4
#Your_computer_brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."
computer_brand = "Hp"
print(f"i have a {computer_brand} computer")


#=======================================Divider========================================
#EXERCISE 5
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name="hassan"
age=21
shoe_size=42
info=f"{name}is a {age} year old coal beacoming a diamond . 100% carbon just the value increasing, and his shoesize  which is {shoe_size} btw "

print(info)


#=======================================Divider========================================
#EXERCISE 6
# Instructions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World"
a=6
b=4
if a>b:
    print("hello world")



#=======================================Divider========================================
#EXERCISE 7
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

user_input = int(input("enter a number :"))
if user_input%2==0:
    print("the number is even")
else:
    print("the number is odd")




#=======================================Divider========================================
#EXERCISE 8
#Whats your name 
#Instructions
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

name = input("what is your name? ")
if name=="hassan":
    print("welcome back BIG BOSS ")
else :
    print("welcome , your name is meh")


#a  com so that i can change the commit lol


#=======================================Divider========================================

#EXERCISE 9
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
height=float(input("what is your height in cm? : "))
if height>=145:
    print("you are tall enough to ride the roller coaster")
else:
    print("you are not tall enough to ride the roller coaster? You need to grow some more to ride")



#a  com so that i can change the commit lol
#=======================================Divider========================================