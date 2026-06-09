#Exercise 1 
birthdays = {
    "Alice": "1998/05/12",
    "Bob": "2000/08/21",
    "Charlie": "1995/03/15",
    "David": "1999/11/30",
    "Emma": "2001/07/09"
}

print("Bienvenue !")
print("Vous pouvez rechercher les anniversaires des personnes de la liste.")

name = input("Entrez un nom : ")

birthday = birthdays[name]

print(f"L'anniversaire de {name} est le {birthday}.")



#Exercise 2
birthdays = {
    "Alice": "1998/05/12",
    "Bob": "2000/08/21",
    "Charlie": "1995/03/15",
    "David": "1999/11/30",
    "Emma": "2001/07/09"
}

print("Bienvenue !")
print("Voici les personnes disponibles :")

for person in birthdays:
    print(person)

name = input("\nEntrez un nom : ")

if name in birthdays:
    print(f"L'anniversaire de {name} est le {birthdays[name]}.")
else:
    print(f"Désolé, nous n'avons pas l'information d'anniversaire pour {name}.")


#Exercise 3 
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Entrez votre nom : ")

if user_name in names:
    index = names.index(user_name)
    print(f"Premier index trouvé : {index}")
else:
    print("Nom introuvable.")



#Exercice 4
import random


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    throws = 0

    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()

        throws += 1

        if dice1 == dice2:
            return throws


def main():
    results = []

    for i in range(100):
        result = throw_until_doubles()
        results.append(result)

    total_throws = sum(results)
    average = total_throws / len(results)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average:.2f}")


main()


