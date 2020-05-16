import random
import time

list_of_items = [] 

def intro():
    _age = random.randint(21, 24)
    _drinks = random.randint(2, 5)
    _hour = random.randint(1, 12)
    _minutes = random.randint(10, 59)
    time.sleep(1)
    print("For your " + str(_age) + " birthday, your family and friends buy a ticket for a party cruise for the weekend.")
    print("The first day of the cruise was amazing, you had the best time of your life.")
    print("The best part of the cruise is having time to spend time with your family and friends.")
    print("You have " + str(_drinks) + " drinks. Everything goes blink.")
    print("You wake up at " + str(_hour) + ":" + str(_minutes) + " a.m. the next moring to a rocking ship.")
    print("You look out the window, and there is a huge storm heading the ships way.")
    print("You think its weird that none of your family and friends are there with you. But you shrug it off.")
    print("You are a bit hungey, so you look at the menu and there is a few places you can go eat on the ship.")
    print(" ")
    menu()

def menu():
    time.sleep(1)
    print("You have three options for food.")
    print("\n A: a tradition tapas meal.")
    print(" B: Churros with chocolate.")
    print(" C: Fish and chips.")
    print(" ")
    _food = input("What would you like to eat? Your three options are: ")
    while _food != "A" or "a" and _food != "B" or "b" and _food != "C" or "c":
        if(_food == "A" or "a"):
            print("You head to the seafood restaurant.")
            print(" ")
            panic()
        elif(_food == "B" or "b"):
            print("You head to the mecican restaurant.")
            print(" ")
            panic()
        elif(_food == "C" or "c"):
            print("You head to the burger shop.")
            print(" ")
            panic()

def panic():    
    time.sleep(2)
    print("While you are walking to the restaurant, it begins to rain.")
    print("The ship starts to rock back and forth.")
    print("Then the ship takes in water.")
    print("Storm finally caught up the the cruise.")
    print("Everyone around you starts to scream and panick.")
    print("The ship brings to sink slowly almost like it hit something, so you start to panic too.")
    print("You want to find all your family and friends but because of all the chaos.")
    print("You can not see more than five feet in front of you.")
    print("You come up with four ideas: ")
    panic1()
    
def panic1():    
    print("\n A: Go back to the room, to see if anyone is there.")
    print(" B: Go to the highest place on the ship to spot if you can see someone. ")
    print(" C: Panic and run around and hope you find someone you know. ")
    print(" D: Stay where you are at and hope someone finds you. ")
    print(" ")
    _ideas = input("Which option do you want to go with: ")
    while _ideas != "A" or "a" and _ideas != "B" or "b" and _ideas != "C" or "c" and _ideas != "D" or "d":
        if(_ideas == "A" or "a"):
            print("Going back to your room, you do not find anybody.")
            print("But you can get 2 things from your room before you must leave and find everyone else before the ship sinks.")
            room()
        elif(_ideas == "B" or "b"):
            print("You around up to the stern side of the ship.")
            print("You look down, but you cannot see anything but people running around and panicking.")
            print("You do not see anyone you know.")
            print("But someone bumps into you and they drop their purses.")
            print("But they don’t go back to pick it up.")
            print("You don’t know what is within the purse but a cell phone might be in side of it.")
            stern_side()
        elif(_ideas == "C" or "c"):
            print("Thank you for playing!!")
        elif(_ideas == "D" or "d"):
             print("That was never an option")

def panic2():    
    print(" A: Go to the highest place on the ship to spot if you can see someone. ")
    print(" B: Panic and run around and hope you find someone you know. ")
    print(" C: Stay where you are at and hope someone finds you. ")
    _ideas = input("Which option do you want to go with: ")
    while _ideas != "A" or "a" and _ideas != "B" or "b" and _ideas != "C" or "c" and _ideas != "D" or "d":
        if(_ideas == "A" or "a"):
            print("You around up to the stern side of the ship.")
            print("You look down, but you cannot see anything but people running around and panicking.")
            print("You do not see anyone you know.")
            print("But someone bumps into you and they drop their purses.")
            print("But they don’t go back to pick it up.")
            print("You don’t know what is within the purse but a cell phone might be in side of it.")
            stern_side()
        elif(_ideas == "B" or "b"):
            print("Thank you for playing!!")
        elif(_ideas == "C" or "c"):
            print("That was never an option")

def panic3():    
    print("\n A: Go back to the room, to see if anyone is there.")
    print(" B: Panic and run around and hope you find someone you know. ")
    print(" C: Stay where you are at and hope someone finds you. ")
    _ideas = input("Which option do you want to go with: ")
    while _ideas != "A" or "a" and _ideas != "B" or "b" and _ideas != "C" or "c" and _ideas != "D" or "d":
        if(_ideas == "A" or "a"):
            print("Going back to your room, you do not find anybody.")
            print("But you can get 2 things from your room before you must leave and find everyone else before the ship sinks.")
            room()
        elif(_ideas == "B" or "b"):
            print("Thank you for playing!!")
        elif(_ideas == "C" or "c"):
             print("That was never an option")   
         
def room():
    time.sleep(2)
    two_items = 2
    while two_items > 0: 
        print("\n A: Grab your bag but cannot remember what you put inside of it earlier.")
        print(" B: A bag of mix nuts.")
        print(" C: Hand pump water filter system, your sister brought you at a survivor store last year.")
        print(" D: A piece of gum.")
        print(" ")
        item_picked = input("Please enter option: ")
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
        two_items = two_items - 1
    panic2()
    
def stern_side(): 
    print("\na: Pick up the purse, go back to were you were. ")
    print("\nb: Leave the purse, go back to were you were. ")
    pick_up_purse = input("Please enter option a, b")
    while pick_up_purse != "A" or "a" and pick_up_purse != "B" or "b":
        if(pick_up_purse == a):
            print("You picked up the purse.")
            list_of_items.append("Purse")
            panic3()
        elif(pick_up_purse == b):
            print("You left the purse.")
            panic3()
            
play_again = "yes"
while play_again == "Yes" or "yes" or "Y" or "y":
    intro()
    list_of_items = [] 
    play_again = input("Do you want to play again? (Yes or Y or yes or y to continue a new game)")
  
        
