print("Welcome to Treasure Island")

choise = input("You want to cross the road. Type 'left' or 'right': ").lower()
if choise == "left":
    choise == input("You come to a lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()    
    if choise == "wait":
        choise == input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if choise == "red":
            print("It's a room full of fire. Game Over.")
        elif choise == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choise == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    