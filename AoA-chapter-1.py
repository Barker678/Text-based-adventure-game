import time
import random

class WEAPONS(object):
    def __init__(self):
        self.WEAPONS = {
        'Fist': (3,8),
        'stick': (4,9),
        'pulse_baton': (5,10),
        'alien_blaster': (5,12),
        }
        self.current_weapon = WEAPONS['Fist']

    def add_WEAPONS(self,name, weapon):
        self.WEAPONS[name] = weapon
        print ('You have picked up {} to your inventory').format(name.upper())

    def __str__(self):
        for WEAPONS in self.WEAPONS.values():
            print ('\t'.join([str(x)for x in [WEAPONS.name]]))
            if not WEAPONS.inventory:
                print ('You Have Nothing!')

def game():
    
    def print_alien():
        time.sleep(2)
        print("    dMMMb._              .adOOOOOOOOOba.              _,dMMMb_ ")
        print("  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb")
        print("  V      ~MMb          dOOOOOOOOOOOOOOOOOb          dM~      V")
        print("           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'         ")
        print("            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'          ")
        print("       __     `YMMM| OP'~0OOOOOOOOOOO0~`YO |MMMP'     __     ")
        print("     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb    ")
        print("  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._")
        print(" <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>")
        print("              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'            ")
        print("      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa    ")
        print("    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb. ")
        print("   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.")
        print("   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM")
        print("   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP")
        print("    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM' ")
        print("      `'                  `OObNNNNNdOO'                   `'   ")
        print("                            `~OOOOO~'                          ")

    def fight_enemy(enemy_name, min_enemy_damage, max_enemy_damage, min_player_damage, max_player_damage):
        enemy_damage_dealt = random.randint(min_enemy_damage, max_enemy_damage)
        player_damage_dealt = random.randint(min_player_damage, max_player_damage)

        if enemy_damage_dealt > player_damage_dealt:
            print("Uh-oh! You died!")
        elif enemy_damage_dealt < player_damage_dealt:
            print("You killed the {enemy_name}".format(enemy_name=enemy_name))
        else:
            print("You walk away unscathed, but the {enemy_name} still lives.".format(enemy_name=enemy_name))
        
        
    def chapter_1():
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('Welcome to the Army of Aliens!')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        time.sleep(2)
        print ('Hello human,')
        print ('....')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print ('Human')
        time.sleep(1)
        print ('...')
        time.sleep(1)  # NOTE: this is the intro
        print ('\nAnswer Me!')
        time.sleep(1)
        print ('...')
        print ('\nWakey wakey')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print ('....')
        print ('\ngrr, I will go see other humans')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print('''You Wake up on what looks to be a dissection table,''')
        print('''and from the sound of it, You Are On an Alien Vessel''')
        time.sleep(3)
        print("...")
        time.sleep(2)
        print ('Before you can fully take in your surroundings a slimy')
        print ('and disgusting alien walks in and stares at you,')
        time.sleep(2)
        print ('You feel the urge to run')
        time.sleep(1)                   
        chapter = 1                                                                         # NOTE: in chapter 1 the player will mostly answer yes or no questions with there being different things happen throughout
        ch1 = str(input('What Would You like to Do?'))                                  # NOTE: this will change throughout the game; chapter 2 has more things to do as i feel like chapter 1 opens the story of where the player is and
        if ch1 in ['run', 'Run', 'RUN', 'forward']:                                          # NOTE: what they should be doing, i will make some changes so that the player has more choices in chapter 1
            print ('You spring up from the table and run out the door, not looking back')
            time.sleep(2)
            print("...")
            time.sleep(2)
            print ('lights start to flash around the ship')
            time.sleep(1)
            print ('...')
            escape = 1
            turn = 1
            if ch1 in ['nothing', 'Nothing','NOTHING', 'STAY' 'Stay', 'stay', 'die', 'Die', 'DIE']:
                print ('You stay laying on the table awaiting your fate')
                time.sleep(2)
                escape = 0
                turn = 1
            if ch1 in ['talk', 'Talk', 'alien', 'Alien', 'ALIEN']:
                print("You try to communicate with the Alien, as you do it turns round and shrieks")
                time.sleep(1)
                print("You think its best to keep quiet")
                escape = 0
                turn = 1
                shriek = 1
            else:
                print("I don't understand, please try again")

            if turn == 1:
                if escape == 1:
                    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                        print ('As you run down some corridors you start to slow down')
                        ch2 = str(input('Would you like to look around? [y/n]: '))
                        time.sleep(2)
                        if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                            loot1 = int(random.randint(3, 10))
                            nloot1 = int(random.randint(1, 10))
                            nloot2 = int(random.randint(2, 10))
                        if loot1 > nloot1:
                            print ('As you look around you find a nothing')
                            loot1 = int(random.randint(3, 10))
                            nloot1 = int(random.randint(1, 10))
                            ch10 = 1
                        elif loot1 < 5:
                            print ('As you look around you find a prodding stick')
                            current_weapon = ["stick"]
                            ch10 = 1
                            loot1 = int(random.randint(3, 10))
                            nloot2 = int(random.randint(2, 10))
                        else:
                            print ('You find a plasma pistol!')
                            current_weapon = ["alien_blaster"]
                            ch10 = 1

                        if ch10 == 1:
                            print ('After looking around you notice you are at a deadend')
                            time.sleep(2)
                            print ('you hear thuds coming from the long corridor you came from')
                            time.sleep(2)
                            ch5 = str(input('Would you like to wait and fight? [y/n]: '))
                            time.sleep(2)
                            if ch5 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                print ('You wait for the thudding to get closer')
                                time.sleep(2)
                                print ('The alien walks pass the doorway')
                                ch6 = str(input('Would you like to fight the Alien? [y/n]: '))
                                if ch6 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                    time.sleep(2)
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print ("                  Fighting...                  ")
                                    print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                    print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print_alien()
                                    fight_enemy('ALIEN', 3, 6, 1, 15)
                                    time.sleep(2)
                                    print ('The alien turns into a puddle of goo on the floor')
                                    print ('you find nothing in the goo')
                                    time.sleep(2)

                        if ch2 in ['n', 'N', 'No', 'NO', 'no']:
                            print ('After looking around you notice you are at a deadend')
                            time.sleep(2)
                            print ('you hear thuds coming from the long corridor you came from')
                            time.sleep(2)
                            ch5 = str(input('Would you like to wait and fight? [y/n]: '))
                            time.sleep(2)
                            if ch5 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                print ('You wait for the thudding to get closer')
                                time.sleep(2)
                                print ('The alien walks pass the doorway')
                                ch6 = str(input('Would you like to fight the Alien? [y/n]: '))
                                if ch6 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                    time.sleep(2)
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print ("                  Fighting...                  ")
                                    print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                    print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print_alien()
                                    fight_enemy('ALIEN', 3, 6, 1, 15)
                                    time.sleep(2)
                                    print ('You killed the alien!')
                                    print ('You find the corpse of a woman with drills in the side of her head')
                                    print ('But you do find a Pulse Baton...ey')
                                    current_weapon = ["pulse_baton"]
                                    time.sleep(2)

                                if ch5 in ['n', 'N', 'No', 'NO', 'no']:
                                    print ('You choose not to fight the alien.')
                                    time.sleep(1)
                                    print ('The alien totally misses you and walks straight past!')
                                    if escape ==  2:
                                        print ('you hear what seems to be drills coming from the room next to the one your in')
                                        ch7 = str(input('Would you like to investigate? [y/n]: '))
                                        time.sleep(2)
                                        if escape < 2:
                                            print("The alien hears you from behind,")
                                            print ("he grabs you by the neck and your mind slowly goes black")
                                            playagain()

                if escape == 0:
                    if turn == 1:
                        if ch1 in ['n', 'N', 'No', 'NO', 'no']:
                            print ('you hear what seems to be drills coming from the room next to the one your in')
                            ch3 = str(input('Would you like to investigate? [y/n]: '))
                            if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                time.sleep(2)
                                print ('You get up slowly and peer into the room next door')
                                time.sleep(2)
                                print ('An Alien stares directly at you')
                                ch4 = str(input('Would you like to fight the Alien? [y/n]: '))
                            if ch4 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                time.sleep(2)
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print ("                  Fighting...                  ")
                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print_alien()
                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                time.sleep(2)
                                print ('You killed the alien!')
                                print ('You find the corpse of a woman with drills in the side of her head')
                                print ('But you do find a Pulse Baton...ey')
                                current_weapon = ["pulse_baton"]
                            else:
                                print("\nI don't understand, please try again\n")



                                if ch7 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                    print ('You get up slowly and peer into the room next door')
                                    time.sleep(2)
                                    print ('An Alien stares directly at you')
                                    ch4 = str(input('Would you like to fight the Alien? [y/n]: '))
                                    if ch4 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                                        time.sleep(2)
                                        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print ("                  Fighting...                  ")
                                        print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                        print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print_alien()
                                        fight_enemy('ALIEN', 3, 6, 1, 15)
                                        time.sleep(2)
                                        print ('You killed the alien!')
                                        print ('You find the corpse of a woman with drills in the side of her head')
                                        print ('But you do find a Pulse Baton...ey')
                                        current_weapon = ["pulse_baton"]
                                        time.sleep(2)

                                        if ch4 in ['n', 'N', 'No', 'NO', 'no']:
                                            print ('You choose not to fight the alien.')
                                            time.sleep(1)
                                            print ('As you turn away, it ambushes you and disintergrates you!!!')
                                            playagain()


    chapter_1()

def playagain():
    if playagain == ['y', 'Y', 'Yes', 'YES', 'yes']:
        game()
        if playagain in ['n', 'N', 'No', 'NO', 'no']:
            print("Thank you for playing, hope you enjoyed the adventure!")
            print(""".     .       .  .   . .   .   . .    +  .
.     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
 """)
            exit()

game()