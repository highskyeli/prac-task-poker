deck = []




def createAcard(name, typec, rarity, attribute, level):
 
    tries = 5

    while rarity not in ["common", "rare", "ultra-rare"]:
        if tries <= 0:
            print("Wow. It's taken you more than 4 tries to get it right. Wow.")

        rarity = input("Inserted Wrong Card Rarity, Please put it in one of these selections: Common, Rare, Ultra-Rare ")
        tries -= 1
        
    tries = 5


    while attribute not in ["dark", "light", "fire", "water", "wind", "earth"]:
        if tries <= 0:
            print("Wow. It's taken you more than 4 tries to get it right. Wow.")        
        attribute = input("Inserted Wrong Card Attribute, Please put it in one of these selections: Dark, Light, Fire, Water, Wind, Earth ")
        tries -= 1




    card = {

    }

    card["name"] = name  
    card["typec"] = typec
    card["rarity"] = rarity
    card["level"] = level
    card["attribute"] = attribute 

    deck.append(card)
    

    

for i in range(2): 
    

    name = input("What is your card's name? ")
    typec = input("What is type of card would you like to have? An example could be Dragon, Plant, Aqua, Rock; it could be up to your imagination ")
    rarity = input("what is your card's rarity? Choose from Common, Rare, Ultra-Rare ").lower()
    level = input("What level is your card? ")
    attribute = input("What is your card's attribute? Choose from Dark, Light, Fire, Water, Wind, Earth ").lower()
   


    createAcard(name, typec, rarity, attribute, level)
    print(deck) 
