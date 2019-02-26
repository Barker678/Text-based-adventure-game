from Player import Player
from Ship import Ship
from Items import Item
class Game():
    #we define the player and the Ship as empty
    def __init__ (self):
        self.player = Player()
        self.Ship = Ship()
        self.win = ["Blue Slime", "Red Slime", "Yellow Slime", "Yellow liquid", "a Fuse", "a Lighter", "a Blow Torch", "Putty"]
        # a list [] which helps the "Air-Lock" counting the number of the items we have in the inventory
    def intro(self):
        # We introduce the player to the cockpit and there task or game.
        print("Hello Pilot! I am the on board computer! Are you hurt that was a hard landing... well thats good")
        # Ask for player Name
        print("Can I know your name?")
        # store player name in player class
        playername = input(">")
        self.player.setname(playername)
        # print name from player class
        print ("Good. Well hello " + self.player.getname() + ". what you'll need to do now is simple. You just have to collect 8 items from the ship that'll melt the door to get outside")
        print ("If you do that, you will have survived, Start from here - the cockpit. Good luck!")

    # putting a function that gives the player possible directions for each place they go
    def give_directions (self):
        print("Where would you like to go " + self.player.getname() + "?")
        print ("The possible directions are:")
        print ("north")
        print ("south")
        print ("east")
        print ("west")
    # define game loop with a while loop
    def game_loop(self):  # we add the actions in the game, without the "game_loop" the game shouldn't work.
        self.intro()
        currentLocation = 1 #we start from the cockpit
        while True:
            self.give_directions()
            # ask the player to input a string
            playerinput = input (">") #before the player writes- this will appear before the text
            if playerinput.isalpha(): #This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.
                if playerinput in self.Ship.Map[currentLocation]:
                    currentLocation = self.Ship.Map[currentLocation][playerinput]
                    if "item" in self.Ship.Map[currentLocation]: #item part. Everytime the player goes to a place, they receive only ONE item
                        print("You received !\n") # the text that appears everytime the player gets an item
                        print(str(self.Ship.Map[currentLocation]["item"]))
                        self.player.addItem(self.Ship.Map[currentLocation]["item"]) # adds item to inventory
                        del self.Ship.Map[currentLocation]["item"] # only ONE item from a place. when the player goes to the same place, they don't receive anything
                    if "win" in self.Ship.Map[currentLocation]: #the air-lock checks if the player has 8 item in their inventory
                        print("Hmm, let me check!\n")
                        if len(self.player.inventory) == len(self.win): #if the player receive all the needed items in their inventory(list), they will win
                            print("You have all the items! Great! lets make some explosive! Boom! \n") #ending
                            #ending screen/picture
                            def main():

                                f = open("testtxt.txt", "r")
                                if f.mode == "r":
                                    contents = f.read()
                                    print(contents)

                            if __name__=="__main__":
                                main()
                            break
                        else: # if not, the ship will tell them that they need to search for more items
                            print("Unfortunatelly, you haven't collected all the items to escape")
                # if player input equals direction - north, south, west, east - move to that place(direction)
                    if playerinput == "north":
                        print ("You moved to " + self.Ship.Map[currentLocation]["name"])
                        print("" + self.Ship.Map[currentLocation]["desc"])
                    elif playerinput == "east":
                        print ("You moved to " + self.Ship.Map[currentLocation]["name"])
                        print(self.Ship.Map[currentLocation]["desc"])
                    elif playerinput == "south":
                        print ("You moved to " + self.Ship.Map[currentLocation]["name"])
                        print(self.Ship.Map[currentLocation]["desc"])
                    elif playerinput == "west":
                        print ("You moved to " + self.Ship.Map[currentLocation]["name"])
                        print(self.Ship.Map[currentLocation]["desc"])
                elif playerinput == "quit":
                    print ("So Your Giving up... well.. It's your life... Powering off... Fair well!")
                    break
                elif playerinput == "inventory":
                    print("My inventory: ")
                    for item in self.player.inventory:
                        print(item)
                else:
                    print("You can't go that way\n")
            else:
                print("Invalid Input.\n")
                continue

    # TODO: Evaluate player input

gameinstance = Game() #important for the game- it starts because of this code
gameinstance.game_loop() # we add the game_loop to be played.
