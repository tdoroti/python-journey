print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
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
  
