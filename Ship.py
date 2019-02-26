class Ship(object): # the basic way every class is started with
    def __init__ (self):
        self.game = {} # empty, because otherwise the commands the player gives won't work
        self.description = "\0"
#we will make a dictionary, which will have the names,directions, description  of the places we need to go during the game
#we are naming each place as numbers (1,2,3,4,5,6,7,8,9,10), because it is easier for us to recognize them.
    Map = {
    1 :  {"name" : "Cockpit", #the name of the actual place
          "desc" : "You start from here. You can see all the flashing lights on the main control board. ¬ OHH SO MANY LIGHTS! SO BEAUTIFUL AND SHINY! ¬ ", # the description for it
          "north" : 2, #each room has direction that they can go it does this easily as they are numbered 
          "east": 3, #so if i was to input north it would ee that it would go to number 2 so itll then look at room 2s data
          },
    2 : {"name" : "Hanger",
        "south" : 1,
        "east" : 4,
        "north" : 6,
        "west" : 8,
        "desc" : " ¬ after the crash this place looks trashed. But the debris seems to be out the way so you can go into the other parts of the ship. Hahaha! ¬",
        "item" : "Blue Slime", #each room except the first(cockpit) and the last(airlock) have items in them
        },
    3 : {"name" : "Air Lock",
        "desc" : "I am at the airlock. I guess this is where i was told to go once i had the materials",
        "west" : 1,
        "north" : 4,
        "win" : "you win", #you'll only get the 'win' if you have all items first
        },
    4 : { "name" : "Armory",
        "south" : 3,
        "west" : 2,
        "north" : 5,
        "desc" : " The armory so many weapons but no explosive. Damn it!",
        "item" : "a Fuse",
        },
    5 : {"name" : "Bunk Rooms",
        "south" : 4,
        "west" : 6,
        "desc" : "The Bunk room where you would normally sleep. ¬The other bunks havent been used in a while",
        "item" : "Red Slime",
        },
    6 : {"name" : "Engine Room",
        "east" : 5,
        "south" : 2,
        "west"  : 7,
        "desc" : "You are in the engine Room ¬ the engine has fully cooled now. ¬",
        "item" : "Yellow Slime",
        },
    7 : {"name" : "Science Lab",
        "east" : 6,
        "west" : 10,
        "south" : 8,
        "desc" : "The science lab`. ¬ SCIENCE! ¬ ",
        "item" : "Yellow liquid",
        },
    8 : {"name" : "Living Quarter",
        "east" : 2,
        "north" : 7,
        "west" : 9,
        "desc" : "The living quarters You have fond memories of this room. ¬",
        "item" : "a Lighter",
        },
    9 : {"name" : "Utility Lab",
        "east" : 8,
        "north" : 10,
        "desc" : "The utility lab people have lots of work to do after this",
        "item" : "a Blow Torch",
    },
    10 : {"name" : "Servicing Module",
         "east" : 7,
         "south" : 9,
         "desc" : "The servicing Module is quite dark ¬ I've only been here a few times ¬",
         "item" : "Putty",
    },
    }
    def getship(self): #the same as the players name
        return self.Ship.Map
#we classify the Air Lock
class Air_Lock(object):
    def __init__ (self):
        self.Name = {}
        # Items
