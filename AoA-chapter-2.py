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

class player(object):
    def __init__(self):
        self.health = {
            'health': (16)
        }

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
            and you take a direct hit to your lungs''')
        print("you take 3 damage")
        player.health - 3
        print('''
                           .-.      .-.
                     _..--'`;;`-..-';;'`--.._
                   .';,    _   `;;'   _    ,;`.
                  ;;'  `;;' `;.`;;'.;' `;;'  `;;
                 .;;._.;'`;.   `;;'   .;'`;._.;;.
               ;'      '`;;`   `;;'   ';;'`      `;
              ;:     .:.  `;;. `--' .;;'  .:.     :;
               ;.   .:|:.     `;;;;'     .:|:.   .;
                `;  `:|:'    .;;'`;;.    `:|:'  ;'
                 `;. `:'  .;;'.::::.`;;.  `:' .;'
                   `;._.;;' .:`::::':. `;;._.;'
              .::::. `::   (:._.::._.:)   ::' .::::.
         .:::::'  `::.`:_.--.`:::::. .--._:'.::'  `:::::.
       .::'     `:MJP `::-.:::"""":::.-::' PJM`::      `::.
     .::'      .::'      | /.^^^..^^^.\ |      `::        `:.
     :::      .:'::.     \( `;;;..;;;' )/     .::::       :::
     ::  :  .:':.  `::.   \            /   .::'  .:     .  ::
     :  ::  .   :     `::.              .::'     :  :   ::  :
    .:  :    `.::.       `:.          .:'       .::.'    :  :.
   ::  :  :   : :::.       `:.      .:'       .::: :   :  :  ::
   ::  :        :' `:.       :.    .:       .:' `:        :  ::
   :::     :   ::    `:.      :.  .:      .:'    ::   :     :::
   ' :       :::'      :.      `::'      .:      `:::       : `''')
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

        chapter_2()

def playagain():
    if playagain == ['y', 'Y', 'Yes', 'YES', 'yes']:
        chapter_2()
        if playagain in ['n', 'N', 'No', 'NO', 'no']:
            print("Thank you for playing, hope you enjoyed the adventure!")
            exit()

game()