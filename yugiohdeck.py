deck = []




def createAcard(name, typec, rarity, attribute, level):
 
    card = {

    }

    card["name"] = name  
    card["typec"] = typec
    card["rarity"] = rarity
    card["attribute"] = attribute 
    card["level"] = level

    if card["typec"] not in ["Link", "Effect", "Spell", "XYZ", "Dragon"]:
        type = input("Inserted Wrong Card Type, Please put it in one of these selections: Link, Effect, Spell, XYZ, and Dragon.")
    deck.append(card)

    if card["attribute"] not in ["Dark", "Light", "Fire", "Water", "Wind", "Earth"]:
        attribute = input("Inserted Wrong Card Attribute, Please put it in one fo these selections: Dark, Light, Fire, Water, Wind, Earth")
    deck.append(card)

    if card["rarity"] not in ["Common", "Silver", "Gold"]:
        rarity = input("Inserted Wrong Card Attribute, Please put it in one fo these selections: Dark, Light, Fire, Water, Wind, Earth")
    deck.append(card)

for i in range(5): 
    

    name = input("What is your card's name? ")
    typec = input("What is type of card would you like to have? ")
    rarity = input("what is your card's rarity? ")
    attribute = input("What is your card's attribute?")
    level = input("What level is your card?")

    createAcard(name, typec, rarity, attribute, level)
    print(deck) 


    if name == "quit":
        break


