import cmd
import textwrap
import sys
import os
import time

screen_width = 100

#Player Setup
class player:
    def __init__(self):
        self.name= ''
        self.location= 'a1'
        self.won= False
        
myPlayer = player()
    
    
####MAP####
'''
Player starts at A1
-------------
|A1|A2|A3|A4|
-------------
|B1|B2|B3|B4|
-------------
|C1|C2|C3|C4|
-------------
'''

NAME = ''
DESCRIPTION = 'description'
UP = 'north'
DOWN = 'south'
LEFT = 'west'
RIGHT = 'east'

###FLAGS###
'''
FLAG00  #Shovel#
FLAG01  #Kate - Neighbor#
FLAG02  #Joseph - Friend 1#
FLAG03  #Chest - 1#
FLAG04  #Joseph - Friend 2#
FLAG05  #Cav - Barista#
FLAG06  #Archie - Sheriff#
FLAG07  #Jean - Bartender#
FLAG08  #Key 1#
FLAG09  #End 1#
FLAG10  #Elm - Librarian#
FLAG11  #Mable - Dean#
FLAG12  #Key 2#
FLAG13  #End 2#
FLAG14  #Key 3#
FLAG15  #End 3#
'''

#Flags Dictionary - Used as conditions in order to be able to go further in the game
flags = {'FLAG00': False, 'FLAG01': False, 'FLAG02': False, 'FLAG03': False, 
         'FLAG04': False, 'FLAG05': False, 'FLAG06': False, 'FLAG07': False, 
         'FLAG08': False, 'FLAG09': False, 'FLAG10': False, 'FLAG11': False, 
         'FLAG12': False, 'FLAG13': False, 'FLAG14': False, 'FLAG15': False}

#Town Map - Denotes the players location and their next destination from said location
town_map = {
    'a0': {
        NAME: "Border",
        DESCRIPTION: "You reached the town border. move any direction to go back home.\n",
        UP: 'a1',
        DOWN: 'a1',
        LEFT: 'a1',
        RIGHT: 'a1',
    },
    'a1': {
        NAME: 'Home',
        DESCRIPTION: "Your simple little apartment. \nIt is quite cheap for a university student like you, and there are a lot of facilities available in the building.\nNot like you'd have time to visit them anyway.\n",
        UP : 'a0',
        DOWN: 'b1',
        LEFT: 'a0',
        RIGHT: 'a2'
    },
    'a2': {
        NAME: "Black Drip Café",
        DESCRIPTION: 'The fragrant aroma envelops you as soon as you enter the room.\n',
        UP: 'a0',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        NAME: "Grand Oak University",
        DESCRIPTION: "Your classes won't be starting anytime soon, so you're free to loiter around.\n",
        UP: 'a0',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        NAME: "Limoné Bar",
        DESCRIPTION: 'Soft jazz music plays in the background. You hear chattering for all around the bar as you took a seat.\n',
        UP: 'a0',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a0',
    },
    'b1': {
        NAME: "Neighbor's House",
        DESCRIPTION: "The exterior reminded you of your old house from across the country. You feel a little homesick the longer you look at it.\n",
        UP : 'a1',
        DOWN: 'c1',
        LEFT: 'a0',
        RIGHT: 'b2'
    },
    'b2': {
        NAME: "Park - West Side",
        DESCRIPTION: 'A spacious park with a huge tree at its center.\n',
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        NAME: "Park - Center",
        DESCRIPTION: 'A spacious park with a huge tree at its center. The oak tree looks even taller up close\n',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        NAME: "Park - East Side",
        DESCRIPTION: 'A spacious park with a huge tree at its center.\n',
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'a0',
    },
    'c1': {
        NAME: 'Store',
        DESCRIPTION: "A tall department store that sells a variety of things. Your parents gave you some money. Perhaps you can go shopping there sometime.\n",
        UP : 'b1',
        DOWN: 'a0',
        LEFT: 'a0',
        RIGHT: 'c2'
    },
    'c2': {
        NAME: "Library",
        DESCRIPTION: 'The library is quiet, but not silent. You can hear some slight sounds when the visitors turn the pages of the book.\n',
        UP: 'b2',
        DOWN: 'a0',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        NAME: "Police Station",
        DESCRIPTION: "It isn't a large building, but you'll know where to go if you need the authorities.\n",
        UP: 'b3',
        DOWN: 'a0',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        NAME: "Old Clock Tower",
        DESCRIPTION: "Apparently it closed down a long time ago, just before you were born.\n",
        UP: 'b4',
        DOWN: 'a0',
        LEFT: 'c3',
        RIGHT: 'a0',
    }
}

###FUNCTIONS###
#Prompt - Prompts the user to submit an input into the game
def prompt():
    print("\n\n========================================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_inputs = ["travel", "move", "go", "walk", "leave", "investigate", "look", "observe", "inspect", "interact", "quit"]
    while action.lower() not in acceptable_inputs:
        print("Please enter a valid action.")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk", "leave"]:
        move(action.lower())
    elif action.lower() in ["investigate", "look", "observe", "inspect", "interact"]:
        investigate(action.lower())
      
      
#Moving Function - Used to find out the players next location after typing north, south, east, or west 
def move(myAction):
	askString = "Where would you like to "+myAction+" to?\n> "
	destination = input(askString)
	if destination == 'north':
		move_dest = town_map[myPlayer.location][UP]
		move_player(move_dest)
	elif destination == 'west':
		move_dest = town_map[myPlayer.location][LEFT]
		move_player(move_dest)
	elif destination == 'east':
		move_dest = town_map[myPlayer.location][RIGHT]
		move_player(move_dest)
	elif destination == 'south':
		move_dest = town_map[myPlayer.location][DOWN]
		move_player(move_dest)
	else:
		print("Invalid direction command, try using north, south, west, or east.\n")
		move(myAction)
  
def move_player(move_dest):
	print("\nYou have moved to the " + move_dest + ".")
	myPlayer.location = move_dest

#Prints current location and description
def print_location():
	print('\n' + ('#' * (4 +len(town_map[myPlayer.location][NAME]))))
	print('# ' + town_map[myPlayer.location][NAME].upper() + ' #')
	print('#' * (4 +len(town_map[myPlayer.location][NAME])))
	print('\n' + (town_map[myPlayer.location][DESCRIPTION]))
 
 
#Investigate function - Controls the text output when the player types "investigate" in the prompt.
#It also uses the flag dictionary, and if you reached a certain flag, a certain event will occur. 
#Likewise, if you haven't reached a certain flag, then said event will not occur, replaced by a generic event.
def investigate(Action):
    if myPlayer.location == 'a0':
        void = ("\n" + "You shouldn't be here. Move anywhere to go back home.")
        for character in void:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
        time.sleep(0.5)
    elif myPlayer.location == 'a1':
        home = ("\n" + "There isn't much to do at home. Let's just get outside.")
        for character in home:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
        time.sleep(0.5)
    elif myPlayer.location == 'a2':
        if flags['FLAG03'] == flags['FLAG04'] == True:
            Café1 = ("\n" + "You walked to the counter and waved at the sole barista.")
            for character in Café1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
            Cav1 = ("\n" + '"Hmmm? Do I know you?"')
            for character in Cav1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(1)
            Cav2 = ("\n" + '"Oh! You must be ' + myPlayer.name+ '! Joseph called about you earlier."')
            for character in Cav2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav3 = ("\n" + '"You can call me Cav. Joseph told me ' + "you'd" + ' like to know more about the chest in the old clock tower?"')
            for character in Cav3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav4 = ("\n" + '"Wow! Hahah! Hearing about that brings back some old memories!"')
            for character in Cav4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav5 = ("\n" + '"I remember me and my friends just screwing around bored to death after doing all there is to do in this damned town."')
            for character in Cav5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav6 = ("\n" + '"So the five of us gathered around some of our things and put them in a box. A sort of time capsule, you know."')
            for character in Cav6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav7 = ("\n" + '"I forgot where we put it though, but it seems like you found it. HAHAHAHA!"')
            for character in Cav7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav8 = ("\n" + '"Sorry if you came here expecting a key... If I couldn' + "'" + 't remember where I kept the chest, that key has left my memory years before you were born, heheh."')
            for character in Cav8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav9 = ("\n" + '"But I think the other fellows might know where to look. You can find Archie in the police station and Jean pretty much lives in the bar."')
            for character in Cav9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav10 = ("\n" + '"Elm and Mable however... those two left town a while back. I barely got to know them. Hope they' + "'" +'re doing well."')
            for character in Cav10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Cav11 = ("\n" + '"Anyway, good luck on your little treasure hunt. If you need anything, you know where to find me."')
            for character in Cav11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            flags['FLAG05'] = True
            
        elif flags['FLAG04'] == flags['FLAG05'] == True and flags['FLAG09'] == False:
            Café2 = ("\n" + "Cav saw you and waved at you with his friendly smile. He gave you a small cup of coffee free of charge. \nYou still don't have the heart to tell him you're more of a tea person.")
            for character in Café2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
                
        elif flags['FLAG04'] == flags['FLAG05'] == False:
            Café3 = ("\n" +"You sat down at the café and tried to order a cup of tea, but unfortunately they don't sell them here. So you settled for a regular cappuccino, which you enjoyed while listening to the ambient music of the café.")
            for character in Café3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
                
    elif myPlayer.location == 'a3':
        if flags['FLAG02']==False:
            Uni1 = ("\n" + "You arrive at Grand Oak University. In class you spot your friend Joseph, who has been living in town before you transfered. The two of you meet and he greets you with a hug.")
            for character in Uni1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
            Jos1 = ("\n" + '"'+str(myPlayer.name) + '! Glad to see you here! I hope the trip here was pleasant."')
            for character in Jos1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos2 = ("\n" + '"You will certainly enjoy this town. It' +"'"+ 's a really nice place to live and settle down."')
            for character in Jos2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos3 = ("\n" + '"It' +"'"+ 's a little far from the city, yes, but it' +"'"+'s very cozy in here. You' +"'"+ 'll love it!"')
            for character in Jos3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos4 = ("\n" + '"But you know the clock tower on the corner of town, next to the police station? To this day it still gives me the creeps. Like there could be some ghost guarding a treasure or something. It' +"'" +'s closed now, but I think you can still go there if you wanna look around."')
            for character in Jos4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos5 = ("\n" + '"Not like anyone wants to anyway, HAHAHA!"')
            for character in Jos5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos6 = ("\n" + '"Oh my, I' + "'" + 'm running late to class. I' +"'"+ 'll catch you around, yeah? See ya!"')
            for character in Jos6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG02'] = True
            
        elif flags['FLAG02'] == flags['FLAG03'] == True:
            Jos7 = ("\n" + '"Oh. My. God."')
            for character in Jos7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.5)
            time.sleep(2)
            Jos8 = ("\n" + '"I can' + "'" +'t believe you actually went there!"')
            for character in Jos8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos9 = ("\n" + '"Hmmm..."')
            for character in Jos9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
            Jos10 = ("\n" + '"A treasure chest you say?"')
            for character in Jos10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos11 = ("\n" + '"I can try calling my dad about it. He' + "'"+ 's lived in this town since he was born. He should know more about it."')
            for character in Jos11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos12 = ("\n" + '"He owns the café next to your apartment. You might' + "'" +'ve already been there, so you can ask my dad about that."')
            for character in Jos12:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jos13 = ("\n" + '"Oh! I' + "'" + 'm late for class! I' + "'"+ 'll see you around, yeah?"')
            for character in Jos13:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG04'] = True

        elif flags['FLAG03'] == flags['FLAG04'] == flags['FLAG10'] == True and flags['FLAG11'] == flags['FLAG13'] == False:
            Uni2 = ("\n" + 'You walked to the Dean' +"'"+ 's office and knocked on the door. A voice from inside allowed you to enter and you opened the door. Inside you see Dean Mable in her desk, looking at some documents. When she saw you enter she looked up and took off her reading glasses.')
            for character in Uni2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
            Mab1 = ("\n" + '"I take it you are ' + str(myPlayer.name) + '. Elm told me about you. Something about a treasure chest, was it?"')
            for character in Mab1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Mab2 = ("\n" + '"Well, you certainly jogged up a memory here. Elm probably told you this but he and I used to live in this town before we moved to the city. I only moved in here 2 years ago, and sure enough Elm was here too, so we reconnected."')
            for character in Mab2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Mab3 = ("\n" + '"I do remember playing with some other kids here. I hope the others are doing well. But yes, I remember making that chest. Elm' +"'"+'s father was a woodworker, you see, and he had an little old chest that was not up to his standards, so he gave it to us children."')
            for character in Mab3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Mab4 = ("\n" + '"We put in some of our treasured items and locked the chest. I recall burying the key under the big oak tree in the park, but as you can see I never really got around to digging it up."')
            for character in Mab4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Mab5 = ("\n" + '"Well, let me know if you need anything else. But don' +"'"+ 't let this treasure hunting hinder your studies, alright?"')
            for character in Mab5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG11'] = True
            
    elif myPlayer.location == 'a4':
        if flags['FLAG05'] == True and flags['FLAG07'] == False:
            Bar1 = ("\n" + "You sat on the stool as the soft jazz tune played in the room. The bartender approached you shortly after finishing another custormer's order.")
            for character in Bar1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean1 = ("\n" + '"What will it be for tonight?')
            for character in Jean1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Bar2 = ("\n" + "...")
            for character in Bar2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(1)
            Jean2 = ("\n" + '"OH! You' +"'re "+ str(myPlayer.name)+ '! Cav called me earlier about you. Sorry I didn'+ "'"+ 't recognize you from the start."')
            for character in Jean2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean3 = ("\n" + '"Cav said you wanted to know about the chest in the clock tower, right? To be honest, all of us forgot about it over time. It' + "'"+ 's been such a long time after all..."')
            for character in Jean3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean4 = ("\n" + '"I remember burying the key together with someone in the park..."')
            for character in Jean4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean5 = ("\n" + '"Wait, who buried the key with me... I just can' + "'" +'t seem to remember who..."')
            for character in Jean5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(2)
            Jean6 = ("\n" + '"..."')
            for character in Jean6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(1)
            Jean7 = ("\n" + '"Oh my lord, MABLE! I wonder how she' + "'"+'s doing!. Hahah!"')
            for character in Jean7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean8 = ("\n" + '"But yeah, Mable and I buried the key near the big oak tree in the park. Talk about letting the girls do all the work."')
            for character in Jean8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean9 = ("\n" + '"Well, it would be nice to see what we put there, heheh."')
            for character in Jean9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Jean10 = ("\n" + '"Anyway, I got a bar to run, so good luck on getting the key! And come over anytime, I'+ "'" + 'll give you a pint for half the price."')
            for character in Jean10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG07'] = True
            
        elif flags['FLAG03'] == flags['FLAG05'] == flags['FLAG07'] == False:
            Bar3 = ("\n" + "You sat down at the bar, enjoying the chatter and the music. However you aren't much of a drinker, so you left shortly after.")
            for character in Bar3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
        elif flags['FLAG07'] == True and flags['FLAG08'] == False:
            Bar4 = ("\n" + 'You took a seat at the bar. Jean saw you and offered to get you a drink, but you weren' + "'" +'t in the mood tonight, so you declined the offer."')
            for character in Bar4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
    
            
    elif myPlayer.location == 'b1':
        if flags['FLAG01'] == False:
            Kate1 = ("\n" + "You knocked on the door to the neighbor's house. Not long after, an old woman opened the door.")
            for character in Kate1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(1)
            Kate2 = ("\n" + '"Hello there. Who might you be?"')
            for character in Kate2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(0.5)
            Kate3 = ("\n" + '...')
            for character in Kate3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(1)
            Kate4 = ("\n" + '"Ahh... So you'+ "'" + 're the new tenant of that apartment. A pleasure to meet you, '+str(myPlayer.name)+'."')
            for character in Kate4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(0.5)
            Kate5 = ("\n" + '"I saw the trucks come over this morning and I prepared a little welcoming gift. Give me a second to fetch it, alright?"')
            for character in Kate5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(0.5)
            Kate6 = ("\n" + '...')
            for character in Kate6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(1)
            Kate7 = ("\n" + '"Here you go! That apartment must be a little bleak without some plants, so I'+"'"+'d like to give you some orchids and a shovel to plant them."')
            for character in Kate7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(0.5)
            Kate8 = ("\n" + '"Do come over if you need anything alright, hun? Even if you need someone to talk to. This old hag has all the time in the world, hehehe."')
            for character in Kate8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(0.5)
            flags['FLAG00'] = True 
            flags['FLAG01'] = True
            
        else:
            Kate9 = ("\n" + "You stop over Kate's house and knocked on the door. She welcomed you in and the two of you have a nice chat.")
            for character in Kate9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
    elif myPlayer.location == 'b2' or myPlayer.location =='b4':
        park_non_center = ("\n" + "You loitered around the park. It was a nice walk, but there wasn't much to do.")
        for character in park_non_center:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)

    elif myPlayer.location == 'b3':
        if flags['FLAG00'] == True:
            Park1 = ("\n" + "You admired the Grand Oak Tree where it stood. It towers over most of the building in the small town. It also emits a nice smell.")
            for character in Park1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Park2 = ("\n" + "You scanned the root area when you find a spot in the tree bark that was skinned. You scanned the area around it and found a strange mound. Excited, you started digging.")
            for character in Park2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Park3 = ("\n" + "With a little shovel, you managed to dig out a small plastic tube, one that seemed like it came out of a surprise toy.")
            for character in Park3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Park4 = ("\n" + "You open the tube and took out a key.")
            for character in Park4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            if (flags['FLAG06'] == True or flags['FLAG07'] == True) and flags['FLAG11'] == False:
                flags['FLAG08'] = True
            elif flags['FLAG06'] == flags['FLAG07'] == False and flags['FLAG10'] == flags['FLAG11'] == True:
                flags['FLAG12'] = True
            elif flags['FLAG05'] == flags['FLAG06'] == flags['FLAG07'] == flags['FLAG10'] == flags['FLAG11'] == True:
                flags['FLAG14'] = True
            elif flags['FLAG06'] == flags['FLAG07'] == flags['FLAG11'] == False:
                Park5 = ("\n" + "You admired the Grand Oak Tree where it stood. It towers over most of the building in the small town. It also emits a nice smell. But there isn't anything else to do.")
                for character in Park5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)
        elif flags['FLAG00'] == False:
            Park6 = ("\n" + "You suddenly have the urge to get a shovel. No reason at all. You can probably get it at Kate's house or in the department store. Who is Kate? I don't know. You should probably go to her house and find out. She lives on the west side of the park.")
            for character in Park6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
    elif myPlayer.location == 'c1':
        if flags['FLAG00'] == True:
            Store1 = ("\n" + "You entered the large department store. You scanned around the store and saw that it contained pretty much anything a household needs, including a shovel.\nFortunately you already have one, so there is no need to visit the store anymore.")
            for character in Store1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)

        elif flags['FLAG00'] == False:
            Store2 = ("\n" + "While looking around the store, you spotted a shovel. You feel the sudden urge to buy said shovel. Ultimately you lost the inner battle and bought the shovel. It is a nice shovel, you thought.")
            for character in Store2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG00'] = True
    
    elif myPlayer.location == 'c2':
        if flags['FLAG03'] == flags['FLAG10'] == False:
            Lib1 = ("\n" + "You entered the library to research more about the treasure chest. You tiptoed over to the librarian in duty and asked him about it.")
            for character in Lib1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Elm1 = ("\n" + '"A book about the clock tower? Sorry, I don'+"'"+'t think we have a book for that. I might know a thing or two about it, though. Is there anything you would like to know in particular?"')
            for character in Elm1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm2 = ("\n" + "...")
            for character in Elm2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(1)
            Elm3 = ("\n" + '"A treasure chest? Hihihi... I certainly do know about that. I was the one who placed it there after all."')
            for character in Elm3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm4 = ("\n" + '"Well, not just me of course. I was with four of my other friends. We played a lot when we were kids, and then decided to make a little keepsake for the future. You know, like a time capsule."')
            for character in Elm4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm5 = ("\n" + '"Now, I myself don'+"'"+'t know where we kept the key, but I think Mable should..."')
            for character in Elm5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm6 = ("\n" + '"Hmm? You don'+"'"+'t know who Mable is? By the look of you I thought you were a student at the university across! Well if you really don'+"'"+'t know, she is one the deans of that university."')
            for character in Elm6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm7 = ("\n" + '"You see, Mable and I moved out of town around the same time, and I didn'+"'"+'t really get the chance to get the other three'+"'"+'s phone numbers. Beside I only met Mable around two years ago when she moved back in."')
            for character in Elm7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm8 = ("\n" + '"Don'+"'"+'t worry. I recall she was one of the two who dug the keys in. As for the other three, well I hope they'+"'"+'re doing okay."')
            for character in Elm8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            Elm9 = ("\n" + '"Anyway, I'+"'"+'ll go give Mable a call. Hope your treasure hunting goes well, and do come back here anytime. Well, when we'+"'"+'re open, of course."')
            for character in Elm9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.075)
            time.sleep(0.5)
            flags['FLAG10'] = True

        elif flags['FLAG10'] == True:
            Lib2 = ("\n" + "You entered the library and saw Elm sitting on the librarian's desk. He spots you and gave you a small wave. You waved back.")
            for character in Lib2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
        elif flags['FLAG03'] == flags['FLAG10'] == False:
            Lib3 = ("\n" + "You entered the library and picked up a random book. It was surprisingly interesting.")
            for character in Lib3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
    elif myPlayer.location == 'c3':
        if flags['FLAG03'] == flags['FLAG05'] == True:
            Pol1 = ("\n" + "You entered the police station and asked for Archie. The receptionist made a call and then directed you to his office.")
            for character in Pol1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Arc1 = ("\n" + '"Well I am glad that we meet under this circumstance and not some other more... '+"'mischievous'"+ ' ones. HAHAHA!')
            for character in Arc1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            Arc2 = ("\n" + '"Ahem.. Anyway I got a call from Cav. He said you need some info on your little quest. Something about a key, perhaps?"')
            for character in Arc2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            Arc3 = ("\n" + '"If this old nugget can remember correctly, Mable and Jean buried the key under the oak tree in the park."')
            for character in Arc3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            Arc4 = ("\n" + '"Gosh.. That brings back memories. I wonder how Elm and Mable are doing, though. Haven'+"'"+'t seen them since they moved outta town."')
            for character in Arc4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            Arc5 = ("\n" + '"Welp, no time to reminisce yet. I got some duties I gotta finish and you got a quest to complete."')
            for character in Arc5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            Arc6 = ("\n" + '"Hope I can see you again, '+str(myPlayer.name)+'. Hopefully without bars separating us. HAHAHAHA!"')
            for character in Arc6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            flags['FLAG06'] = True
            
        elif flags['FLAG05'] == False or flags['FLAG06'] == False:
            Pol2 = ("\n" + "There is no reason for you to be entering the police station, so you decided against it.")
            for character in Pol2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(0.5)
            
    elif myPlayer.location == 'c4':
        if flags['FLAG02'] == True and flags['FLAG03'] == False:
            ct1 = ("\n" + "Your curiosity piqued and you braved through the clock tower. As expected, it is quite empty. No surprise there, though. The building has been abandoned for years.")
            for character in ct1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            ct2 = ("\n" + "You spot something from the corner of your eye. A box; no larger than a milk crate with a decade's worth of dust covering it.")
            for character in ct2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            ct3 = ("\n" + "You walked over to the box and tried to open it, but it is locked.")
            for character in ct3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            ct4 = ("\n" + "Perhaps you could talk to Joseph about this, or maybe research in the library on your own.")
            for character in ct4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG03'] = True
            
        elif flags['FLAG03'] == flags['FLAG05'] == flags['FLAG06'] == flags['FLAG07'] == flags['FLAG08'] == True:
            End1_1 = ("\n" + "With the key you dug out you unlocked the chest. A cloud of dust emerges as the chest opened.\nInside laid a teacup, a watch, a fountain pen, a pair of spectacles, and an ice pick.\n")
            for character in End1_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_2 = ("\n" + '"Oh my, those sure do bring back memories, eh?" a familiar voice sounded from behind. You looked back and saw Cav, Archie, and Jean walking over.')
            for character in End1_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_3 = ("\n" + '"Sorry, I got curious and rang Archie and Jean about you, and sure enough they felt the same. So we came over to check how the chest was holding up, and-"\n"And then sure enough, you opened the chest," Jean said, cutting of Cav.')
            for character in End1_3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_4 = ("\n" + '"My... My... Look at these pieces of junk," Archie chuckled, holding up the watch.')
            for character in End1_4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_5 = ("\n" + '"Heh.. I'+"'"+'ll gladly take those off your hands if you'+"'"+'d like," Cav said, holding the chipped teacup.')
            for character in End1_5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_6 = ("\n" + '"Blech, where did young me even get this?" Jean held up the ice pick with two fingers with disgust, its handle going green from the mold.')
            for character in End1_6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_7 = ("\n" + '"What a shame... I wish we could'+"'"+'ve seen those two again..." Archie said, inspecting the spectacles with his hands.')
            for character in End1_7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_8 = ("\n" + 'He let out a breath and raised his hands, as if holding a shot glass, "Well, Elm and Mable, wherever they are, I sure hope we could one day sit around in the bar and just chat. And of course you too are invited, '+str(myPlayer.name)+'," Archie grabbed you by the hand.')
            for character in End1_8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_9 = ("\n" + '"Heh... if we'+"'"+'re drinking in my bar, drinks are on you," Jean pointed towards Cav, "I hope you still remember the last two tabs I had to cover."')
            for character in End1_9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_10 = ("\n" + '"Hehe... I'+"'"+'ll remember for sure."')
            for character in End1_10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End1_11 = ("\n" + 'The group laughed, and you sighed in relief as your curiosity satiated and your quest finally over.')
            for character in End1_11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Ending1 = ("\n" + "Ending 1\nThere are three endings in this game. Try to get the other two endings.")
            for character in Ending1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG09'] = True
            myPlayer.won = True

        elif flags['FLAG03'] == flags['FLAG10'] == flags['FLAG11'] == flags['FLAG12'] == True:
            End2_1 = ("\n" + "With the key you dug out you unlocked the chest. A cloud of dust emerges as the chest opened.\nInside laid a teacup, a watch, a fountain pen, a pair of spectacles, and an ice pick.\n")
            for character in End2_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_2 = ("\n" + '"I see you managed to opened the chest," a familiar voice sounded from behind. You looked back and saw Elm and Mable walking over.')
            for character in End2_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_3 = ("\n" + '"Mable called back and showed her interest in revisiting old memories, so we thought to see how the chest is holding up," Elm said.\n"And sure enough, here you are, with the chest wide open," Mable continued.')
            for character in End2_3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_4 = ("\n" + '"Have you ever wondered how some of us even got these things as a kid? I mean Archie put in a watch in there," Elm said, playing with the pen.')
            for character in End2_4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_5 = ("\n" + '"One of the world'+"'"+'s greatest mysteries," Mable said, trying on the glasses. "Oh. Mystery solved. He probably stole it."')
            for character in End2_5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_6 = ("\n" + '"Hahaha... Man... If only we could grow up together."')
            for character in End2_6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_7 = ("\n" + '"Yeah... This would be a fun talk between us over some drinks. You can come too, '+str(myPlayer.name)+', if you'+"'"+'d like.')
            for character in End2_7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_8 = ("\n" + '"Is drinking with your student appropriate?" Elm joked.')
            for character in End2_8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_9 = ("\n" + '"When I'+"'"+'m off the clock, anything goes."')
            for character in End2_9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_10 = ("\n" + '"Heh.. if that ever happens you know my number."')
            for character in End2_10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End2_11 = ("\n" + 'The two laughed, and you sighed in relief as your curiosity satiated and your quest finally over.')
            for character in End2_11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Ending2 = ("\n" + "Ending 2\nThere are three endings in this game. Try to get the other two endings.")
            for character in Ending2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            flags['FLAG13'] = True
            myPlayer.won = True
            
        elif flags['FLAG03'] == flags['FLAG05'] == flags['FLAG06'] == flags['FLAG07'] == flags['FLAG10'] == flags['FLAG11'] == flags['FLAG14'] == True:
            End3_1 = ("\n" + "With the key you dug out you unlocked the chest. A cloud of dust emerges as the chest opened.\nInside laid a teacup, a watch, a fountain pen, a pair of spectacles, and an ice pick.\n")
            for character in End3_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_2 = ("\n" + 'Suddenly you hear chatter from outside. You stepped out of the clock tower and saw a familiar group of people.')
            for character in End3_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_3 = ("\n" + '"My oh my, you should'+"'"+'ve told us you were in town!" Jean said, hugging Elm and Mable.')
            for character in End3_3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_4 = ("\n" + '"We have been in town- for the past two years," Elm chuckled, "Besides, we didn'+"'"+'t have your numbers."')
            for character in End3_4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_5 = ("\n" + '"Thats fair. But you guys never thought about visiting other shops? I find it unlikely we never met in two years," Cav said.')
            for character in End3_5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_6 = ("\n" + '"Well, I have a tight schedule, and Elm over here pretty much lives in the library. Funny how none of you never saw him in there," Mable smirked.')
            for character in End3_6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_7 = ("\n" + '"Touché," Archie said, "Say, you guys wanna go for drinks?"')
            for character in End3_7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_8 = ("\n" + '"Oh! Yes! I kept the good stuff just for this occasion," Jean said with glee')
            for character in End3_8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_9 = ("\n" + '"That sounds lovely," Mable replied, "I'+"'"+'ve got nothing to do tonight either.')
            for character in End3_9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_10 = ("\n" + '"Same here," Elm said.')
            for character in End3_10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_11 = ("\n" + '"Cav, don'+"'"+'t think I forgot about your bills."')
            for character in End3_11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_12 = ("\n" + '"Haha, of course Jean! Not even for a moment," Cav nervously said.')
            for character in End3_12:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            End3_13 = ("\n" + "The group laughed as they walk together to Jean's bar, chattering all the way.\nAs for you, you returned to the unlocked chest and closed it.\nPerhaps there will be a better time to open the chest.\nPerhaps there will be a better time to revisit the old memories.\nBut now...\nNow is the time to make some new memories.")
            for character in End3_13:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            Ending3 = ("\n\n" + "THE END")
            for character in Ending3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(1)
            time.sleep(0.5)
            ThankYou = ("\nTHANK YOU FOR PLAYING")
            for character in ThankYou:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.75)
            time.sleep(0.5)
            flags['FLAG15'] = True
            myPlayer.won = True
            
        elif flags['FLAG02'] == False:
            ct5 = ("\n" + "There's nothing to do in the clock tower, so you stopped yourself from entering.")
            for character in ct5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
        elif flags['FLAG02'] == flags['FLAG03'] == True and flags['FLAG08'] == flags['FLAG12'] == flags['FLAG14'] == False:
            ct5 = ("\n" + "You wondered what lies in the chest as you stood by the clock tower.")
            for character in ct5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            
        

        
#Initialize game loop
def game_loop():
    while myPlayer.won is False:
        print_location()
        prompt()
        

#Title Screen
def title_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("quit"):
        sys.exit()	
    while option.lower() not in ['play', 'quit']:
        print("Invalid command, please try again.")
        option = input("> ")
       
#Launches Title Screen     
def title_screen():
    os.system('clear') #Clears terminal
    print('##########################################')
    print('##     Welcome to Grand Oak Town!       ##')
    print('##  Created by Ostein Vittorio Vellim   ##')
    print('##########################################')
    print('                --Play--                  ')
    print('                --Quit--                  ')
    title_selection()

#Sets Up Game
def setup_game():
    os.system('clear')
    Line1 = ('"...Alright that should be everything. You can just go ahead and settle in right now."')
    Line2 = ("\n" + '"If you would please sign here... and write your name in here..."\n')
    #Types out strings by each character individually with a certain amount of delay in between each character
    for character in Line1: 
        sys.stdout.write(character) #Writes the characters
        sys.stdout.flush() #Writes the characters one by one for every character in the string
        time.sleep(0.05) #Adds delay to the command
    for character in Line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myPlayer.name = playerName
    
    Line3 = ("\n" + '"Alright then, '+myPlayer.name+', glad to work with you. Enjoy your new home!\n')
    for character in Line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
        
        
    os.system('clear')
    print("#################################")
    print("#   Welcome to Grand Oak Town   #")
    print("################################\n")
    print("Your home is looking a little barren, but a home's a home\n")
    print("You can move by typing 'move' on the console, and you can 'investigate' by typing 'investigate' in the console.")
    game_loop()

        
title_screen()
