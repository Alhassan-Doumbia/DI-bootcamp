# Instructions:

# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.



# Step 1: Create the Siamese Class

# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.


# Step 2: Create a List of Cat Instances

# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.


# Step 3: Create a Pets Instance

# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.


# Step 4: Take Cats for a Walk

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.
# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# On crée la classe Siamese AVANT de l'instancier
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


siamese = Siamese("Kirby", 2)
bengal = Cat("Miaousse", 1)
chartreux = Cat("Chatouille", 3)

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)
sara_pets.walk()



#============Divider===================================
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking" # Retourner une string est plus propre pour le print() extérieur

    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self, other):
        if isinstance(other, Dog): # Correction ici
            other_dog_power = other.run_speed() * other.weight
            current_dog_power = self.run_speed() * self.weight # Correction ici (self.weight)
            
            if other_dog_power > current_dog_power:
                print(f"{other.name} is the winner") # Correction ici (other.name)
            else:
                print(f"{self.name} is the winner")

dog1 = Dog("Médor", 2, 14)
dog2 = Dog("Brutus", 4, 10)
dog3 = Dog("Goat", 1, 12)

print(dog1.bark())
print(dog2.run_speed())
dog1.fight(dog2) # Pas de print() ici car la méthode s'en occupe déjà


# ===========================Divider========================================
# In a new Python file, import the Dog class from the previous exercise.

#Exercise 3 : Dogs Domesticated
# Instructions
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.



# Key Python Topics:

# Inheritance
# super() function
# *args
# Random module


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.


# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.





from moduleFile import Dog

class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        super().__init__(name,age,weight)
        self.trained=trained

    def train(self):
        print(self.bark())
        self.trained=True

    def play(self,*args):
        dogNames=[self.name]
        for dog in args:
            dogNames.append(f"{dog.name} ")
        print(f"{' '.join(dogNames)} all play together")

    def do_a_trick(self):
        if(self.trained):
            import random
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(random.choice(tricks))
    
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.
pet_dog1 = PetDog("Buddy", 3, 20)
pet_dog2 = PetDog("Charlie", 5, 25)
pet_dog1.train()
pet_dog1.play(pet_dog2)
pet_dog1.do_a_trick()


#==========================Divider========================================

#Execise4: Family and person classes 
# Goal:

# Practice working with classes and object interactions by modeling a family and its members.



# Key Python Topics:

# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)


# Instructions:

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.


# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)


# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.


# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.


class Person:
    def __init__(self, first_name, age): # Pas de last_name ici selon la consigne
        self.first_name = first_name
        self.age = age
        self.last_name = "" 

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [] 

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name # On lui donne le nom de famille
        self.members.append(new_member)
        print(f"Congratulations to the new born {first_name} {self.last_name} !")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
               
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                  
                    print("Sorry, you are not allowed to go out with your friends.")
                
        
    def family_presentation(self):
        print(f"Family {self.last_name} :")
        for member in self.members:
            print(f"{member.first_name} is {member.age} years old")

# Tests
family1 = Family("Smith")
family1.born("John", 30)
family1.born("Emily", 15)

family1.check_majority("John")
family1.check_majority("Emily")
family1.family_presentation()

if(family1.member[0].is_18()):
    print(f"{family1.member[0].name} can go out")
else:
    print(f"{family1.member[0].name} cannot go out")


