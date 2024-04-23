deck = []




def createAcard(name, typec, rarity, attribute, level):
 
    card = {

    }

    card["name"] = name  
    card["typec"] = typec
    card["rarity"] = rarity
    card["level"] = level
    card["attribute"] = attribute 

    deck.append(card)
    

    

for i in range(5): 
    

    name = input("What is your card's name? ")
    typec = input("What is type of card would you like to have? ")
    rarity = input("what is your card's rarity? ")

    tries = 5

    while rarity not in ["Common", "Rare", "Ultra-Rare"]:
        if tries <= 0:
            print("Wow. It's taken you more than 4 tries to get it right. Wow.")

        rarity = input("Inserted Wrong Card Rarity, Please put it in one of these selections: Common, Rare, Ultra-Rare ")
        tries -= 1
        
    tries = 5

    level = input("What level is your card?")

    attribute = input("What is your card's attribute?")

    while attribute not in ["Dark", "Light", "Fire", "Water", "Wind", "Earth"]:
        if tries <= 0:
            print("Wow. It's taken you more than 4 tries to get it right. Wow.")        
        attribute = input("Inserted Wrong Card Attribute, Please put it in one of these selections: Dark, Light, Fire, Water, Wind, Earth ")
        tries -= 1
   


    createAcard(name, typec, rarity, attribute, level)
    print(deck) 
