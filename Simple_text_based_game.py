#TextBased Adventure Game
#By using strings, variables, input/outputs, if/else statements, prints, list and integers.
def text_based_game():
    print("This is a simple text based adventure game created with python.")
    print("First level: you are walking and you see a hole, what do you do")
    print("A : Jump the hole.")
    print("B : Go around.")
    print("C : Go back home.")
    first_level = input("Please enter A,B or C: ")
    if(first_level == "A" or "a"):
        print("You tripped and you fell in the hole it was a long way down, but you landed in water so your okay")
        print("Second level: What do you do? ")
        print("A : Swim.")
        print("B : Try to clam down and think of a way out.")
        print("C : Stay were you are.")
        second_level = input("Please enter A,B or C: ")
        if(second_level == "A" or "a"):
            print("You swim and swim and doesnt end. You swim so long that you get tried.")
        elif(second_level == "B" or "b"):
            print("You think about swimming but you do not know were you are at, so you thing about screaming out for help")
            print("Someone hears you, and they go for help")
        elif(second_level == "C" or "c"):
            print("You're stay were youre at and a dog fulls next to you")
        else:
            print("That was never an option")
    elif(first_level == "B" or "b"):
        print("You walked around the hole, you keep walking and you see a dog.")
        print("Second level: What do you do? ")
        print("A : Pet the dog.")
        print("B : Walk around the dog.")
        print("C : Run away from the dog.")
        #second_level = input("Please enter A,B or C: ")
        #if(second_level == "A" or "a"):
        #elif(second_level == "B" or "b"):  
        #elif(second_level == "C" or "c"):
        #else:
    elif(first_level == "C" or "c"):
        print("Thank you for playing!!")
    else:
        print("That was never an option")
