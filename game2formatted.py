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
        print ('Hello there human,')
        print ('....')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print ('Human')
        time.sleep(1)
        print ('..')
        time.sleep(1)  # NOTE: this is the intro
        print ('\nTell Me!')
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
        chapter = 1
        ch1 = str(input('would you like to run? [y/n]: '))
        if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
            print ('You spring up from the table and run out the door, not looking back')
            time.sleep(2)
            print("...")
            time.sleep(2)
            print ('lights start to flash around the ship')
            time.sleep(1)
            print ('...')
            escape = 1
            turn = 1
            if ch1 in ['n', 'N', 'No', 'NO', 'no']:
                print ('You stay laying on the table awaiting your fate')
                time.sleep(2)
                escape = 0
                turn = 1
            else:
                print("\nI don't understand, please try again\n")

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
                                    print ('You killed the alien!')
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
                                    chapter_2
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
                                chapter_2
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
                                        chapter_2
                                        time.sleep(2)

                                        if ch4 in ['n', 'N', 'No', 'NO', 'no']:
                                            print ('You choose not to fight the alien.')
                                            time.sleep(1)
                                            print ('As you turn away, it ambushes you and disintergrates you!!!')
                                            playagain()

    def chapter_2(inventory):
        print("after finding the corpse of the woman, you see")
        time.sleep(1)
        print("there is a sort of alien map with parts of the ship,")
        time.sleep(1)
        print("with where you are, which seems to be the holding cells")
        time.sleep(1)
        print('\nwhoooosh')
        time.sleep(1)
        print('....')
        time.sleep(1)
    def start(inventory):
        print('an elevator opens up in the room your in')
        print('\n[-MAIN ELEVATOR-]')
        print('\n1.) deck 1 - Holding deck')
        print('2.) deck 2 - Maintenance')
        print('3.) deck 3 - Cargo Hold - Airlock')
        print('4.) deck 4 - Docking Port')
        print('5.) deck 5 - Helm')
        print('6.) deck 6 - Observation\n')

        cmdlist = ['1', '2', '3', '4', '5', '6',]
        cmd = cmdlist

        if cmd == '1':
            game(inventory)
        elif cmd == '2':
            print('\n- DECK 2 - MAINTENANCE LOCKED -')
            time.sleep(2)
            chapter_2(inventory)
        elif cmd == '3':
            cargo_hold(inventory)
        elif cmd == '4':
            if 'Docking Port keycard' in inventory:
                print('\n- Docking Port - Docking Port LOCKED -')
                time.sleep(2)
                docking_port(inventory)
            elif cmd == '5':
                helm(inventory)
            elif cmd == '6':
                print('\n- DECK 6 - OBSERVATION LOCKED -')
                time.sleep(2)
            observatory(inventory)
        else:
            observatory(inventory)

    def cargo_hold(inventory):
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('''\nYou enter the Cargo Hold,
            two militarised aliens with big laser guns
            unload a barrage of laser fire at you.
            Their fire is very accurate
            and you take a direct hit to your lungs and heart''')
        print('\n[-CARGO HOLD - AIRLOCK-]')
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print("you have died")
        playagain
        exit(0)

    def observatory(inventory):
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('''\nThe observatory is filled with debris. There
            is laser scoring everywhere and there are corpses everywhere, human and alien.
            In the corner there is an injured human still alive but close to death.
            You can try to talk to him\n''')
        print('[-Observatory-]')
        print('\n1.) talk to human')
        print('2.) Return to Main Elevator')

        cmdlist = ['1', '2']
        cmd = cmdlist

        if cmd == '1':
            'docking_port_keycard'(inventory)
        elif cmd == '2':
            start(inventory)

    def docking_port(inventory):
        time.sleep(1)
        print("....")
        time.sleep(1)

    def helm(inventory):
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('''\nYou enter the helm where all navigation takes place.
            A bigger alien Enemy which looks in Command is posted here.
            This alien is extremely powerfull.''')
        print('\n[-Helm-]')
        print('\n1.) Attack the Alien')
        print('2.) Retreat to Main Elevator')
        cmdlist = ['1', '2']
        cmd = cmdlist

        if cmd == '1':
            print('\n....')
            time.sleep(1)
            print('\n....')
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                  Fighting...                  ")
            print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
            print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print_alien()
            fight_enemy('BIG-ALIEN', 5, 8, 4, 20)
            time.sleep(2)
            if cmd == '2':
                print('''\nThe bigger alien is now alert and has you locked
                on. You try to retreat back to the elevator but its to late..''')
                print('....')
                time.sleep(1)
                print('....')
                time.sleep(1)
                print('\nGAME OVER\n')
                exit(0)

    chapter_1()

def playagain():
    if playagain == ['y', 'Y', 'Yes', 'YES', 'yes']:
        game()
        if playagain in ['n', 'N', 'No', 'NO', 'no']:
            print("Thank you for playing, hope you enjoyed the adventure!")
            exit()

game()