deck = []




def createAcard(name, typec, rarity, attribute, level):
 
    card = {

    }

    card["name"] = name  
    card["typec"] = typec
    card["rarity"] = rarity
    card["level"] = level
    card["attribute"] = attribute 
    

    if card["attribute"] not in ["Dark", "Light", "Fire", "Water", "Wind", "Earth"]:
        attribute = input("Inserted Wrong Card Attribute, Please put it in one of these selections: Dark, Light, Fire, Water, Wind, Earth ")
    deck.append(card)
    
    
for i in range(5): 
    

    name = input("What is your card's name? ")
    typec = input("What is type of card would you like to have? ")
    rarity = input("what is your card's rarity? ")
    level = input("What level is your card?")
    attribute = input("What is your card's attribute?")
    

    createAcard(name, typec, rarity, attribute, level)
    print(deck) 


    if name == "quit":
        break


