print(r'''
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at a cross road. Where do you want to go?\n'
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. In the middle of the lake there is a small island.\n'
                    'Would you like to swim across or wait for a boat?\n'
                    'Type "wait" or "swim".\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. '
                        'There is a house in front of you with 3 doors. One red,'
                        'one yellow and one blue.\n'
                        'Which color do you choose?\n ').lower()
        if choice3 == "red":
            print("You open the door and a big flame scoops you up and pulls you inside.\n"
                  "You burn to death.\n"
                  "Game Over")
        elif choice3 == "yellow":
            print("You win!")
        elif choice3 == "blue":
            print("You open the door and a giant grabs you and eats you.\n"
                  "Game Over")
        else:
            print("Game Over")
    else:
        print("You get into the water and a giant trout eats you.\n"
              "Game Over")
else:
    print("You fall into a hole. Game Over")
  
