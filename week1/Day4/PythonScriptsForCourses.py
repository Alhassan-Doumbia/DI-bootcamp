#Inheritance in OOP 
class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

rex = Dog('dog', 4, "Wouaf")
print('This animal is a:', rex.type)
# >> This animal is a dog

rex.fetch_ball()
# >> I am a dog, and I love fetching balls

roger = Animal('Roger', 4, "Grr")
roger.fetch_ball()
# >> AttributeError: 'Animal' object has no attribute 'fetch_ball'


#++++++++++++++++++++++++++++
class Vehicle:
	def __init__(self):
		pass
#Je fais heriter à la classe voiture que je viens créer, les attributs et méthode de Vehicle en mettant vehicle entre les parenthèsed de la nouvelle classe voiture 

class Car(Vehicle):
		def__init__(self):
			pass
	#Bien vrai qu'il puisse avoir lui aussi ses propre variable , il herite aussi des variable de véhicle comme ses propres variables. 



#================Overriding methods
class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        print("I am an DOGGG !!! WOUAFFF!!")

rex = Dog('dog', 4, "Wouaf")
rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!
# " Ensuite si dans une classe enfant , on se permet d’écrire une fonction qui a le même nom qu’une fonction dans la classe parent , c’est comme si l’on réécrivait le fonction en question mais pour la classe enfant , le résultat ne sera donc pas le même que si l’on avait pas recréé la fonction dans la classe enfant . 

# Parce que la classe parent s’étend jusqu’à l’enfant mais l’enfant lui aussi s’étend en rajoutant ses propres fonctions etc  donc si l’une des fonction est *pareille qu’une fonction aprent , c’est la fonction de l’enfant que python prends en compte quand on décide d’appeler cette fonction via l’instance de l’enfant  (objets créé grace à la classe enfant ) 

#Utilisation de Super =======================

class Vehicle:

    def __init__(self,name,brand,color):

        self.name=name
        self.brand=brand
        self.color=color

    def demarrer(self):

        print(f"la voiture {self.name} vient de demarrer VROUM!!!")


# Car hérite de Vehicle
# Donc Car récupère automatiquement :
# - les variables : name, brand, color
# - les méthodes : demarrer()

class Car(Vehicle):
    pass


Toyota=Car("Toyota","Corolla","red")

Toyota.demarrer()


# OUTPUT :
# la voiture Toyota vient de demarrer VROUM!!!


# =======================================================
# COMPREHENSION DES VARIABLES D'OBJETS
# =======================================================

# self représente l'objet lui-même

# Quand on fait :

# Toyota=Car("Toyota","Corolla","red")

# Python fait en réalité :

# self.name="Toyota"
# self.brand="Corolla"
# self.color="red"

# Ces variables appartiennent à l'objet Toyota

print(Toyota.name)
print(Toyota.brand)
print(Toyota.color)

# OUTPUT :
# Toyota
# Corolla
# red


# Chaque objet possède ses propres variables

BMW=Car("BMW","X6","black")

print(BMW.name)

# OUTPUT :
# BMW


# =======================================================
# OVERRIDE
# =======================================================

# Ici on crée une méthode du même nom que celle du parent
# Donc la méthode du parent est remplacée

class Car2(Vehicle):

    def demarrer(self):

        print(f"la voiture {self.name} vient de demarrer VRAAAMMM!!!")


Audi=Car2("Audi","RS6","grey")

Audi.demarrer()

# OUTPUT :
# la voiture Audi vient de demarrer VRAAAMMM!!!


# Vehicle.demarrer() n'est plus utilisé
# Car2 a remplacé la version du parent


# =======================================================
# SUPER()
# =======================================================

# super() permet d'utiliser la méthode du parent
# même après un override

class Car3(Vehicle):

    def demarrer(self):

        print(f"{self.name} prepare son moteur...")

        super().demarrer()

        print(f"{self.name} est maintenant en mouvement")


Mercedes=Car3("Mercedes","Class C","white")

Mercedes.demarrer()

# OUTPUT :
# Mercedes prepare son moteur...
# la voiture Mercedes vient de demarrer VROUM!!!
# Mercedes est maintenant en mouvement


# EXPLICATION :

# super().demarrer()

# veut dire :

# "utilise la méthode demarrer du parent Vehicle"

# Donc :
# 1. Car3 commence sa méthode
# 2. appelle la méthode du parent
# 3. continue ensuite son propre code

#Encapsulation in OOP

class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private ; le fait qu'il yait deux underscore avant le nom de la variable , cela signifie que c'est une variable privée et que l'on ne peut pas y accéder en dehors de la classe , en gros je ne pourrai pas faire c.__max_price pour accéder à la variable max_price , je ne pourrai y accéder que via une méthode de la classe Computer
        
        self._min_price = 500 # protected ; le fait qu'il y ait un underscore avant le nom de la variable , cela signifie que c'est une variable protégée et que l'on peut y accéder en dehors de la classe mais pas dans les classes enfants , je pourrai faire c._min_price pour accéder à la variable min_price mais pas dans une classe enfant de Computer  même si elle est héritée de Computer
    
    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method ; pareil pour cette méthode , je ne pourrai pas l'appeler en dehors de la classe Computer , je ne pourrai l'appeler que via une méthode de la classe Computer
    #cette méthode privée ne sera héritée par aucune classe enfant elle aussi . 


      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()



#======================Les decorateurs 
#Les decorateurs sont des fonctions qui permettent de modifier le comportement d'une autre fonction sans la modifier directement .
#ça se fera en  utilisant un wrapper , qui est une sorte de fontion qui va executer sa logique et dans sa logique , elle utiliseera ce que la fonction décorée fait .et on retournera la valeur du wrapper . 
def func(): 
    print("This is a function") #Comportment basique de la fonction

#je tiens à preciser qu'un decorateur est une fonction comme tout autre hein , c'est juste que son but est de modifier le comportement d'une autre fonction . donc "func" est un paramètre , ça aurait pu s'appeler "x" ou "y" ou n'importe quoi d'autre , c'est juste que par convention on utilise souvent "func" pour désigner la fonction décorée .
def decorator(func):
    def wrapper():

        print("Something is happening before the function is called.")

        func()

        print("Something is happening after the function is called.")

    return wrapper

func() #ça va ecrire : this is a function

#mais si je 'utilise le decorateur en faisantn@decorator avant la fonction , ça va modifier le comportement de la fonction et ça va ecrire :

@decorator
def func():
    print("This is a function")

func()#ça va ecrire :
# Something is happening before the function is called.
# This is a function
# Something is happening after the function is called.


##Decorateurs avec des arguments
#Les décorateurs peuvent aussi prendre des arguments , pour cela on utilise *args et **kwargs dans le wrapper pour pouvoir passer n'importe quel nombre d'arguments à la fonction décorée .

def decorator(func):
    def wrapper(*args, **kwargs):#les args viennent avant les kwargs , c'est une convention , les args sont les arguments positionnels(obligatoire) et les kwargs sont les arguments nommés (optionnels)

        print("Something is happening before the function is called.")

        func(*args, **kwargs)

        print("Something is happening after the function is called.")

    return wrapper

@decorator
def func(name):
    print(f"This is a function and my name is {name}")


#sinon , on developpe le decorateurs en sachant exactement le nombre d'arguments que la fonction décorée prend , mais c'est moins flexible que d'utiliser *args et **kwargs .  dans ce cas de figure on va faire :
def decorator(func):
    def wrapper(name):

        print("Something is happening before the function is called.")

        func(name)

        print("Something is happening after the function is called.")

    return wrapper

@decorator #ce décorateur est intimement lilé à la fonction func , il est fait pour elle , il ne peut pas être utilisé pour une autre fonction qui prend un nombre d'arguments différent de celui de func , c'est pour ça que c'est moins flexible que d'utiliser *args et **kwargs .
def func(name):
    print(f"This is a function and my name is {name}")


#=====Exemple de code avec decorateur ayant des arguments inconnus
def cap_decorator(func):
    def wrapper(*args, **kwargs):
        args = [arg.capitalize() for arg in args] #il a juste fais de smodifs sur les args , des modifs globales , pas des trucs hyper spécialisée vu qu'on ne peut pas specifier

        #ce qui compte , c'est le comportement du decorateur au tour de la fonction décorée , n'est ce pas ? , le decorateur doit faire quelque chose avant et après la fonction décorée , c'est ça qui fait que c'est un decorateur , le fait de faire des modifs sur les arguments ou pas , c'est juste une question de ce que l'on veut faire avec le decorateur , mais ce qui fait que c'est un decorateur , c'est le fait qu'il fasse quelque chose avant et après la fonction décorée .

        
        func(*args, **kwargs)
    return wrapper

@cap_decorator
def describe_me(first_name, last_name, favourite_activity):
    print("I am {} {} and I love {}".format(first_name, last_name, favourite_activity))

@cap_decorator
def describe_my_family(father_name, mother_name, brother_name, sister_name):
    print("The name of my father is", father_name)
    print("The name of my mother is", mother_name)
    print("The name of my brother is", brother_name)
    print("The name of my sister is", sister_name)

describe_me("john", "ricotta", "coding")
describe_my_family("John","Valentina","mario","luigi")


#================================CREER SES PROPRES MODULES =========
#Un module est un fichier python qui contient des fonctions , des classes , des variables , etc ... que l'on peut réutiliser dans d'autres fichiers python en les important .

#On peut developper un module en créant un fichier python et en y mettant du code , puis on peut importer ce module dans un autre fichier python pour utiliser le code qu'il contient .

#souvent on le range dans un dossier pour mieux s'organiser , et on peut importer le module en utilisant le nom du dossier suivi du nom du fichier sans l'extension .py

#ainsi , si j'ai un fichier python qui s'appelle "my_module.py" dans un dossier qui s'appelle "my_folder" , je peux l'importer dans un autre fichier python en faisant , dans ce dossier ,j'aurai un fichier python qui s'appelle __init__.py pour que python considère que c'est un package , et dans ce fichier _init__.py je peux importer les modules que je veux rendre accessibles depuis le package , par exemple si j'ai un module qui s'appelle "my_module.py" dans le dossier "my_folder" , je peux faire dans le fichier _init__.py du dossier "my_folder" :
from .my_module import * #le point avant le nom du module signifie que je veux importer le module qui se trouve dans le même dossier que le fichier _init__.py , et le * signifie que je veux importer tout ce qui se trouve dans le module my_module.py

#ou je peux spécifier les fonctions ou les classes que je veux importer depuis le module my_module.py en faisant :
from .my_module import my_function, MyClass #ici je ne veux importer que la fonction
