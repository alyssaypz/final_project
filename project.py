import random

inventory = ["BOW", "SWORD", "WAND", "BOMB"]

status = ["KNIGHT", "FAIRY", "JESTER", "ROYALTY"]

def adventurer_simulator(enemy_items):
    Player_name = input("WELCOME TO ADVENTURE SIMULATOR! WHAT IS YOUR NAME TRAVELER? ")
    Player_status = input("WHAT IS YOUR STATUS " + str(status) + " TRAVELER?")
    print("AS YOU ARE TRAVELING YOU COME ACROSS MERLIN THE GREAT, HE APPROACHES YOU WITH A QUEST TO DEFEAT THE FOUR GREAT CREATURES WHO HAVE BEEN TERRIFYING THE LANDS. WILL YOU BE THE FIRST TO COME BACK ALIVE? ")

    while True:

        if not enemy_items: 
             
             print("Congrats, you have defeated all the enemies and saved everyones lives!")

             break
        
        enemy = random.choice(list(enemy_items.keys()))
        
        print(enemy, "stands in your way!")

        print("Here is your inventory ", inventory)
        
        player_choice = input("Choose a weapon from your inventory to defeat " + enemy + "! ").upper()
        
        if player_choice in inventory:
            
            if player_choice == enemy_items[enemy]:
                 
                print("Congratulations", Player_name, " THE ", Player_status, ", you have defeated", enemy, ". Prepare for your next foe.")
                
                del enemy_items[enemy]
                
            else: 
                
                print("Your", player_choice, "was no match for ", enemy, ". You died a horrible death.")
                
                print("Game over.")

                break
        else:
            print("Invalid item. Please try another time.")
    

enemy_items1 = {
    "Tito the Troll": "BOMB",
    "Sibyl the Sorcerer": "WAND",
    "Wrangler the Werewolf": "SWORD",
    "Henry the Horseman": "BOW"
}

enemy_items2 = {
    "Tobo the Troll": "WAND",
    "Sibyl the Sorcerer": "SWORD",
    "Wrancor the Werewolf": "BOW",
    "Halphas the Horseman": "BOMB"
}


adventurer_simulator(enemy_items2)