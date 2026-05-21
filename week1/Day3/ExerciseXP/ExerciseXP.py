#   Exercise 1 : Cats
#Instructions 
#Use the Cat class to create three cat objects with different names and ages.


# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.


# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        
    def __str__(self):
        return(f"the cat name is{self.name} and its age is {self.age}")
        
    #  def __lt__(self,other):
    #      return "YES"
    

chat1=Cat(2,"Kirby")
chat2=Cat(1,"Miaouusse")
chat3=Cat(5,"Le Grando")

def findOldestCat(cat1,cat2,cat3):
    catList=[]
    catAge=[]
    catList.append(cat1)
    catList.append(cat2)
    catList.append(cat3)
    
    for e in range(0,len(catList)):
        catAge.append(catList[e].age)
    #trouvons index du plus grand maintenant vu que l'index du plus grand sera au même index que son objet
    oldestCatIndex=catAge.index(max(catAge))
    # print(f"the oldest cat is {catList[oldestCatIndex].name}")
    # print(catList[oldestCatIndex])
    return catList[oldestCatIndex]
   
   
oldestCat=findOldestCat(chat1,chat2,chat3)
oldestCateAge=oldestCat.age
oldestCatName=oldestCat.name

print(f"the oldest cat is {oldestCatName}, and is {oldestCateAge} years old")


#==========================Divider========================================
# Exercise 2 : Dogs
# Instructions
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.



# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.


# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.


# Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.


# Step 4: Compare Dog Sizes

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def jump(self, x):
        print(f"the dog jumped {x} cm high ! ")

    def barking(self):
        print(f"{self.name} goes woof !!!")

    def __eq__(self, other):
        if isinstance(other, Dog):
            if other.height == self.height:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, Dog):
            if other.height < self.height:
                return False
            else:
                return True
        
davids_dog=Dog("david",145)
sarahs_dog=Dog("sarah",100)

print(davids_dog.name)
print(sarahs_dog.name)

print(davids_dog<sarahs_dog)
#compare dog size now 
if(davids_dog<sarahs_dog):
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:    
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")


#==========================Divider========================================

# Exercise 3 :Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists


# Instructions:

# Create a Song class with a method to print song lyrics line by line.



# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


# Example:

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    def __init__(self,lyrics=none):
        if lyrics is None:
            self.lyrics=[]
    def sing_me_a_song(self):
        #should print each lyrics of the song on a new line.
        for lyric in self.lyrics:
            print(f"{lyric}")

stairway = Song(["There\'s a lady who\'s sure", "all that glitters is gold", "and she\'s buying a stairway to heaven"])

stairway.sing_me_a_song()
        

#======Divider ===================================
#Exercise 4 : Afternoon at the zoo 
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):

# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():

# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):

# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():

# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
class Zoo:
    def __init__(self, name, animal=None):
        self.name = name

        if animal is None:
            self.animal = []

    def add_animal(self, newAnimal):
        if newAnimal not in self.animal:
            self.animal.append(newAnimal)

    def sell_animal(self, animalToSell):
        if animalToSell in self.animal:
            self.animal.remove(animalToSell)

    def get_animals(self):
        for animal in self.animal:
            print(animal)

    def sort_animals(self):
        sortedAnimal = sorted(self.animal)
        sortedAnimalDict = {}

        for animal in sortedAnimal:
            sortedAnimalDict.update({animal[0]: []})

        for key in sortedAnimalDict:
            for Animal in sortedAnimal:
                if Animal[0] == key:
                    sortedAnimalDict[key].append(Animal)

        return sortedAnimalDict
