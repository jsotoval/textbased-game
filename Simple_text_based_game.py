#TextBased Adventure Game
#By using strings, variables, input/outputs, if/else statements, prints, list and integers.
import random
import time
def text_based_game():
    time.sleep(2)
    two_items = 2
    list_of_items = [] 
    print("We are on a party cruises that hits a terrible storm. ")
    print(" The ship takes in water. ")
    print(" Everyone is screaming and panicking.")
    print(" The ship brings to sink, so you start to panic too.")
    print(" You want to find all your family and friends but because of all the chaos. ")
    print(" You can not see more than five feet in front of us.")
    print("\n 1: Go back to the room, to see if anyone is there.")
    print(" 2: Go to the highest place on the ship to spot if you can see someone. ")
    print(" 3: Panic and run around and hope you find someone you know. ")
    print(" 4: Stay where you are at and hope someone finds you. ")
    first_option = input("Please enter option 1, 2, 3, 4: ")
    if(first_option == "1"):
        print("Going back to your room, you do not find anybody.")
        print("But you can get 2 things from your room before you must leave and find everyone else before the ship sinks.")
        while two_items > 0: 
            print("\n a: Grab your bag but cannot remember what you put inside of it earlier.")
            print(" b: A bag of mix nuts.")
            print(" c: Hand pump water filter system, your sister brought you at a survivor store last year.")
            print(" d: A piece of gum.")
            item_picked = input("Please enter option a, b, c, d: ")
            if(item_picked == "A" or "a"):
                print("You picked your bag.")
                list_of_items.append("Bag")
            elif(item_picked == "B" or "b"):
                print("you pick the bag of mix nuts.")
                list_of_items.append("Mix nuts")
            elif(item_picked == "C" or "c"):
                print("You picked the hand pump water filter.")
                list_of_items.append("Water filter")
            elif(item_picked == "D" or "d"):
                print("You picked the piece of gum.")
                list_of_items.append("Piece of gum")
            else:
                print("That was never an option")
                break
            two_items = two_items - 1
            print(list_of_items)
    elif(first_option == "2"):
       print("You around up to the stern side of the ship.")
       print("You look down, but you cannot see anything but people running around and panicking.")
       print("You do not see anyone you know.")
       print("But someone bumps into you and they drop their purses.")
       print("But they don’t go back to pick it up.")
       print("You don’t know what is within the purse but a cell phone might be in side of it.")
       print("\na: Pick up the purse, go back to were you were. ")
       print("\nb: Leave the purse, go back to were you were. ")
       pick_up_purse = input("Please enter option a, b")
       if(pick_up_purse == a):
           print("You picked up the purse.")
           list_of_items.append("Purse")
       elif(pick_up_purse == b):
           print("You left the purse.")
       else:
            print("That was never an option")
    elif(first_option == "3"):
        print("Thank you for playing!!")
    else:
        print("That was never an option")
