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

print("You arrived at the Treasure Island by falling from a plane. You fell exactly on a crossroads. Where would you like to go?")
choice = input(""" Type "left" or "right"\n""")
if choice == "right":
    print("You fall into a hole. Game over.")
else:
    print("You arrived at a giant lake. Do you want to swim to the other side or wait for a boat at the pier?")
    choice = input(""" Type "swim" or "wait"\n""")
    if choice == "swim":
        print("You were attacked by a trout. Game over.")
    else:
        print("You crossed the lake, walked a mile and reached an abandoned house. You open the door and enter the house, in front of you there are 3 colored doors. Which color you choose?")
        choice = input(""" Type "red" or "yellow" or "blue"\n""")
        if choice == "red":
            print("You were burned by fire. Game over.")
        elif choice == "yellow":
            print("You opened the door and reached the treasure chest full of gold! Congratulations, you won!")
        elif choice == "blue":
            print("You were eaten by beasts. Game over.")
        else:
            print("This color does not exist. Game over.")
