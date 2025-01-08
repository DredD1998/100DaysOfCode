print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
your_choice1 = input('You\'re at a crossroad, where do you want to go? Type "right"/"left": ').lower()

if your_choice1 == "right":
    print("You fell in to a hole. Game Over!")

elif your_choice1 == "left":
    your_choice2 = input('You\'ve come to a lake,There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim across.(wait/swim)?: ')
    if your_choice2 == "wait":
        your_choice3 = input("You arrive at the island unharmed.There is house with 3 doors.One red,One blue and One pink.Which colour do you choose(red/blue/pink)?: ")
        if your_choice3 == 'red':
            print("It's a room full of fire. Game Over!")
        elif your_choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        elif your_choice3 == "pink":
            print("You found the treasure. You Win!")

        else:
            print("Not a valid choice!")
            print("You loss!")
            exit()


    elif your_choice2 == "swim":
        print("You got killed by crocodile. Game Over!")
    else:
        print("Not a valid choice!")
        print("You loss!")

        exit()


else:
    print("Not a valid choice!")
    print("You loss!")

    exit()

