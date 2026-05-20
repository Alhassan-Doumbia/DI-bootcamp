#Challenge 1
#Challenge 1 :letter index dictionnary
#Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

def letterIndexDict():
    letterDict={}
    
    try:
        user_word=input("enter a word :")
        
        for letter in user_word:
            letterDict.update({letter:[]})
            
        keysArray=letterDict.keys()
        
        for (index_count,letter) in enumerate(user_word):
            if(letter in keysArray):
                letterDict[f"{letter}"].append(index_count)
                
        print(letterDict)
        
    except ValueError:
        print("enter a character chain")
        
    except Exception as e:
        print(f"an error occured : {e}")

#======================Divider========================================

# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.
# 1. Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:

# You need to clean the dollar sign and the commas using python. Don’t hard code it.
# 3. Determining Affordable Items:

# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.

def affordableItems(moneyInWallet=300):
    items_purchase = {
        "Water": "$1",
        "Bread": "$3",
        "TV": "$1,000",
        "Fertilizer": "$20"
    }
    
    wallet = f"${moneyInWallet}"
    
    # Clean wallet value
    wallet = wallet.replace("$", "")
    wallet = wallet.replace(",", "")
    wallet = int(wallet)
    
    # Clean prices inside the dictionary
    for item_name in items_purchase:
    
        cleaned_price = items_purchase[item_name].replace("$", "")
        cleaned_price = cleaned_price.replace(",", "")
    #les strings étant immuable , lorsqu'on fait des modification sur des chaines avec Replace , c'est comme s'il creait une nouvelle chaine de caractère , qu'il faut donc stocker d'où le nouvelle variable cleaned_price
        items_purchase[item_name] = int(cleaned_price)
    
    print(items_purchase)
    
    basket = []
    
    # Add affordable items to basket
    for item_name in items_purchase:
    
        item_price = items_purchase[item_name]
    
        if item_price <= wallet:
            basket.append(item_name)
            wallet -= item_price
    
    # Final result
    if len(basket) == 0:
        print("Nothing")
    
    else:
        arranged_list = sorted(basket)
        print(arranged_list)


user_money=input("how much money do you have in your wallet :")
affordableItems(user_money)
