class Player(object): #we create a Player class that affects the inventory of the player, the players name and given direction to the player.
    def __init__ (self):
        self.Player = Player
        self.Name = "" #empty - for the players name
        self.inventory = [] #we define the inventory/we need it for the items
    def getname (self):
        return self.Name
    def setname (self, newname): #the name of the player will be the same in the whole game
        self.Name = newname
    def givedirections (self): #the directions of the game
        print ("Type the direction you want to walk.")
        print ("north")
        print("south")
        print ("east")
        print ("west")

    # when we go to a certain place, we add a item to the inventory
    def addItem (self, itemtoadd):
        # check to see if player already has item
        if itemtoadd in self.inventory:
            print ("There is nothing else in this room that can help.")
        else:
            # add item to player inventory
             self.inventory.append(itemtoadd)
             print(self.inventory)
