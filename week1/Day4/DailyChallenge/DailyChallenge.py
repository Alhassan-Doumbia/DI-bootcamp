#DAILY CHALLENGE 
#INSTRUCTION

# Goal:

# Create a Pagination class that simulates a basic pagination system.



# Step 1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.


# Step 2: Implement the __init__ Method

# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Behavior:

# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.


# Step 3: Implement the get_visible_items() Method

# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.


# Step 4: Implement Navigation Methods

# These methods should help navigate through pages:

# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

# first_page()
# → Navigates to the first page.

# last_page()
# → Navigates to the last page.

# next_page()
# → Moves one page forward (if not already on the last page).

# previous_page()
# → Moves one page backward (if not already on the first page).

# 📝 Note:

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.


# Bonus

# Step 5: Add a Custom __str__() Method

# This magic method should return a string displaying the items on the current page, each on a new line.
# Example:




import math
class Pagination:

    def __init__(self, items=None, page_size=10):

        if items is None:
            self.items = []
        else:
            self.items = items

        self.page_size = page_size
        self.current_idx = 0

        self.number_of_pages = math.ceil(len(self.items) / self.page_size) if self.page_size > 0 else 0
#Nombre de pages / j'opte pour une variable d'objets pour ce qui est du nombre de pages car  chaque instance aura son nombre de pages . Alors qu'une variable de classe donne le même nombre de page partout et si elle est redefinie , cree tot simplement une variable d'objet pareille à celle de classe mais qui vient juste cacher . DE quoi bien pertuber mon code après. 

    def get_visible_items(self):

        start = self.current_idx * self.page_size
        stop = start + self.page_size

        return self.items[start:stop]
        #Pourquoi ? parce qu'à chaque  pas , on a la position de depard est le résultat de 10*par la page actuelle et la page presentant environs 10 pages , on ajoute tout simplement 10 pages '


    def go_to_page(self, page_num):
        
        if page_num < 1 or page_num > self.number_of_pages:
            raise ValueError("page number out of range")
          

        self.current_idx = page_num - 1
        return self.get_visible_items()


    def first_page(self):

        self.current_idx = 0
        return self.get_visible_items()


    def last_page(self):

        self.current_idx = self.number_of_pages - 1
        return self.get_visible_items()


    def next_page(self):

        if self.current_idx < self.number_of_pages - 1:
            self.current_idx += 1

        return self.get_visible_items()


    def previous_page(self):

        if self.current_idx > 0:
            self.current_idx -= 1

        return self.get_visible_items()
        
    #Bonus 
    # self.datas_to_show=self.go_to_page(self.page_size) #test
    
    def __str__(self):
        datas_to_show=self.get_visible_items()
        return "\n".join(datas_to_show)
        # datas_to_return=[]
        # for data in datas_to_show:
        #     datas_to_return.append(data)
        # return "\n".join(datas_to_return)
        # return "\n".join(datas_to_show)
        
        
        #utilisation de lambda un peu comme les fonctions anonyme en javascript pour pouvoir utiliser map
       
        
#Batterie de TESTTTT
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError

# print(p.get_visible_items())
# print(p.__str__())