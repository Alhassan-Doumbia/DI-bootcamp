class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Woof!')

    def get_info(self):
        return f'{self.name} is {self.age} years old.'

class Dogo():
    def __init__(self, name, age):
        #Le init est ce qu'on appel un constructeur , c'est une méthode spéciale qui est automatiquement appelée lors de la création d'une instance de la classe. Elle est utilisée pour initialiser les attributs de l'objet avec des valeurs spécifiques.  ainsi ,si je met un print dans le init , il s'affichera à chaque fois que je créer une instance de la classe .
        print('Creating a new dog...')
        self.name = name
        #self est un mot-clé qui fait référence à l'instance actuelle de la classe. Il est utilisé pour accéder aux attributs et méthodes de l'objet à l'intérieur de la classe. En utilisant self, vous pouvez différencier les variables d'instance des variables locales dans les méthodes de la classe. en gros quand je vais utiliser self pour une variable , ca sera une variable propre à chaque instance de la classe , et je pourrai y accéder à travers les méthodes de la classe en utilisant self.variable_name et 

        #ça sera différent des variables par exemple dans une méthode qui ne sont pas précédées de self et qui sont des variables locales à cette méthode .

        #donc à chaque fois que je veux creer une variable propre à la classe ( donc aux instances de la classe ) , je dois utiliser self.variable_name pour la créer et y accéder à travers les méthodes de la classe .

Rick = Dog('Rick', 5)
print(Rick.name)#va afficher "Rick", pour acceder aux variable d'instance on utilise le nom de l'instance suivi d'un point et du nom de la variable d'instance .
print(Rick.age) #va afficher 5


#Creation des methtond 

class Doggo():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Creating a new doggo...")
    def bark(self):
        #à chaque fois que je cree une fonction / méthode dans une classe , je dois mettre self comme premier paramètre de la fonction , pour pouvoir accéder aux variables d'instance à travers cette méthode .
        print('Woof!')
    #il ya aussi ce qu'on appel les class méthode , qu'on ecrit avec le cdecorateur @classmethod et qui prennent cls comme premier paramètre au lieu de self , et qui sont utilisées pour accéder aux variables de classe ( variables partagées entre toutes les instances de la classe ) et pour créer des méthodes qui sont liées à la classe plutôt qu'à une instance spécifique de la classe . c'est bizarre mais en fros c'est des fonctions qui ne sont pas influencés par variable d'instance , elle font juste leur truc quoi .


scooby = Doggo('Scooby', 3)
#je peux ajouter une variable à scooby qui sera propre à lui et qui n'affectera pas les autres instances de la classe Doggo , par exemple :
scooby.breed = 'Great Dane'

#breed n'appartient pas à la classe Doggo , c'est une variable d'instance qui appartient uniquement à l'instance scooby , donc si je crée une autre instance de la classe Doggo , elle n'aura pas la variable breed et ne pourra pas y accéder . Par exemple :
shaggy = Doggo('Shaggy', 4)
#si je fais print shaggy.breed , ça va me donner une erreur car breed n'existe pas pour l'instance shaggy , elle n'existe que pour l'instance scooby .

#L'instance/l'objet en dehors de la classe a sa vie propre , elle peut avoir des variables d'instance qui lui sont propres et qui n'affectent pas les autres instances de la classe . Par exemple , scooby a la variable breed qui lui est propre et qui n'affecte pas shaggy ou d'autres instances de la classe Doggo .

#==========================EXAMPLE OF CLASS CODE ==========================
class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


#=========================================

class cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
    def __str__(self):
        return f" la marque est{self.brand} le modèle est {self.model}"
    #la méthode __str__ est une méthode spéciale qui permet en gros d'rafficherpar défaut une certaine chaine de caractère lorsqu'on fait print(l'objet) , elle est utilisée pour fournir une représentation lisible de l'objet lorsqu'on l'affiche ou qu'on le convertit en chaîne de caractères. En définissant la méthode __str__, vous pouvez personnaliser la façon dont l'objet est représenté sous forme de chaîne de caractères, ce qui peut être utile pour le débogage ou pour fournir des informations sur l'objet de manière plus conviviale.

my_car = cars("Toyota", "Corolla")
print(my_car) # sans la méthode __str__ , ça va afficher quelque chose comme <__main__.cars object at 0x7f8b8c8d9e50> , mais avec la méthode __str__ , ça va afficher "la marque est Toyota le modèle est Corolla" , c'est plus lisible et plus informatif que l'affichage par défaut de l'objet .