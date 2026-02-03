print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.\nYor're at a cross road. Where do you want to go?")
print("     Type \"left\" or \"right\"")

if input() in ("left", "Left"):
    print("You have come to a lake. There is an island in the middle of the lake. What would you choose \"wait\" to wait for a boat. or \"swim\" to swim acroos.")
    if input() in ('wait', 'Wait'):
        print("You arrive at the island unharmed. There is a house with 3 colour doors: Red or Blue or Yellow,  which door do you choose?")
        final_choice = input()
        if final_choice in ('Red', 'red'):
            print("It's a room full of fire and you got burned by fire. Game over")
        elif final_choice in ('Blue', 'blue'):
            print("You entered a room full of beasts. Gamer over")
        elif final_choice in ('Yellow', 'yellow'):
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("You got attcked by an angry trout. Game Over.")
else:
    print("You fell inot a hole, Game over")
