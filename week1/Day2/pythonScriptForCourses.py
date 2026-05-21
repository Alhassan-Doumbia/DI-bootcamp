thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_list=['Rick','sanchez']
print("my last name is : ", my_list[1])



sample_dict = { 
  "class":{ 
      "student":{ 
         "name":"Mike",
         "hairColor":"White",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
  }
}
accessing_history=sample_dict['class']['student']['marks']['history']
print(f"the history Mark is{accessing_history}")

#deleting a value in a dict 
def deletingValue():
    try:
        del sample_dict['class']['student']['hairColor']
        print( sample_dict['class']['student']['hairColor'])
    except Exception as e :
        print(f"there is an error of this type {e}")
        
def tryingDictionnaries():
    rick_dict = {
        'first_name':'Rick',
        'last_name':'Sanchez'
    }
    print(rick_dict.items())
    print(rick_dict.keys())
    print(rick_dict.values())
    print(rick_dict.items())
    
# #keys() :The my_dict.keys() method returns a dict_keys of all the keys in my_dict
# # values() : The my_dict.values() method returns a dict_values of all the values in my_dict
# # items() : The my_dict.items() method returns a dict_items of tuples containing the key-value pairs in a dictionary.



def updatingDictionnaries():
    rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
    }
    rick_dict.update({'gun':'portal pistol'})
    print(rick_dict)

# #update() permet de modifier une clé ou ajouter une nouvelle clé ,ainsi si la clé existe , sa valeur est mise à jour , sinon la clé est créée . 
# #Voilà la syntaxe : nom_dictionnaire.update({'clé':'valeur'})

#Loop dictionnaries
my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}
print(my_books.items())

for x,y in my_books.items():
    print("the" + x + "is" + y)
  


#range(start, stop[, step]) : iterator in loops.
#enumerate(iterable) : enumerate each item in the iterable
# L'iterable peut être une liste , un tuple , un dictionnaire , une chaine de caractère . Il nous affiche l'index de chaque élément et énumère les index 

def usingEnumerate():
    for item in enumerate('abcd'):
        print(item)

def usingEnumerateSecond():
    for (index_count, letter) in enumerate('abcd'):
        print('At index {} the= letter is {}'.format(index_count, letter))

def usingBreak():
    word="Leonardo"
    print(len(word))
    for letter in word:
        if letter == "d" :
            break
        print(letter, end='') # end='' renders each letter next to the other


#continue : permet de retourner au debut , lancer l'itération suivante 
def usingContinue():
    for letter in 'Leonardo':
        if letter == 'o':
            continue
        print(letter, end='') # dont execute for 'o' letter
        

#Pass : permet d'abandonner une suite d'instruction selon notre volonté pour eviter des effeurs ou passer des instructions plus vite pour pouvoir le comportement d'un autre bout de code sans impliquer le bout de code précédent 

def usingPass():
    for item in [1,2,3]:
        # comment
        pass # to avoid the error #Pass permet en gros de dire "je sais que je dois faire quelque chose ici , mais je ne veux pas le faire pour l'instant , alors je vais juste passer cette partie de code "
    
    print('Finish the script')
    
    

def Exercise():
    #Implement a loop that asks for user input to add dictionary entries until 'quit' is entered. Display the final dictionary.
    dictionnary={
        'nom':'',
        'age':'',
        'taille': '',
    }
    while True:
        user_name=input("entrez votre nom :")
        user_age= int(input("entrez votre age : "))
        user_heigth=int(input("entrez votre taille"))
        

def Redo():
    dictionnary={
        'nom':'',
        'age':'',
        'taille': '',
    }
    for element in dictionnary:
        value=input(f"vous devez entrer votre {element} :")
        dictionnary.update({element:value})
        
    print(dictionnary)

Redo()






#======================SECTION SUR LES FONCTIONS 

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician=get_formatted_name('jimi', 'hendrix')
print(musician)



def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "FR")


def say_hello_second(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello_second("Rick", "FR")