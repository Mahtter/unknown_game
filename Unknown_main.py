###########################################################################################
# Name: Matthew Blanchard
# Date: 3/28/24
# Description: Enhanced rendition of the Rooms Adventure Game - Unknown 

#This game functions to help you learn a new language by turning key game elements into the new target language.

#(To win you must grab the key, chalice, book, and painting and reach the south door of the Hall to escape. 
#The route to take it north then either east or west, then secret, then either east or west again, then south two times.)

#Change log: 
#-Added start screen with appropriate text
#-Added chase entity to chase you. When you run into entity, games ends.
#-Added end room. Once you reach this room, you win and game is over.
#-Added more items and better descriptions.
#-Must type "open inventory" to see your inventory
#-To see exits and grabbables, you must look around. Enterable text/controls are CAPITALIZED
#-Included a translation script so the user can learn a new language as they play. The language and frequency of translation chan be changed in code.
#-Changed images to fit the narrative and game design better
#-Changed code structure to be highly modular so adding rooms and changing rooms is easy to do without changing the game design or function.
#-Added sound effects for player interactions and game events
###########################################################################################

from tkinter import *
from TranslationProgram import *
from minigame import *
import pygame

# Load sound effects
pygame.init()
door = pygame.mixer.Sound("sounds/door.wav")
caught = pygame.mixer.Sound("sounds/caught.wav")
pickup = pygame.mixer.Sound("sounds/pickup.wav")
rain = pygame.mixer.Sound("sounds/rain.wav")
secret = pygame.mixer.Sound("sounds/secret.wav")
thunder = pygame.mixer.Sound("sounds/thunder.wav")
footsteps = pygame.mixer.Sound("sounds/footsteps.wav")

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	#changed to provide less information requiring the player to think
	def __str__(self):
		# first, the room name
		s = "You are in the {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		return s
#object
# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent, something = str, start = None, game = None, counter = None):
		# call the constructor in the superclass
		Frame.__init__(self, parent)
		self.soemthing = something
		self.start = start
		self.game = game
		self.counter = counter
	@property	
	def something(self):
		return self._something

	@something.setter
	def something(self, value):
		self._something = value

	@property	
	def start(self):
		return self._start

	@start.setter
	def start(self, value):
		self._start = value

	@property	
	def game(self):
		return self._game

	@game.setter
	def game(self, value):
		self._game = value
		
	@property	
	def counter(self):
		return self._counter

	@counter.setter
	def counter(self, value):
		self._counter = value

	# creates the rooms
	def createRooms(self):
		# r1 through r4 are the four rooms in the mansion
		# currentRoom is the room the player is currently in (which
		# can be one of r1 through r4)
		
		# create the rooms and give them meaningful names and an
		# image in the current directory
		r0 = Room("Beginning", "images/start.png")
		r1 = Room("Hall", "images/hall.png")
		r2 = Room("Ballroom", "images/ballroom.png")
		r3 = Room("Study", "images/study.png")
		r4 = Room("Lounge", "images/lounge.png")
		r5 = Room("End", "images/end.png")
		
		# add exits to room 1
		r1.addExit("north", r2)
		r1.addExit("south",r5)
		# add grabbables to room 1
		r1.addGrabbable("key")
		r1.addGrabbable("wallet")
		r1.addGrabbable("shrub")
		# add items to room 1
		r1.addItem("planter", "The planter looks old, but the SHRUB in it looks well maintained")
		r1.addItem("dresser", "It looks brand new compared to the rest of the room. Odd. There is a WALLET and a KEY on it.")
		r1.addItem("doors", "There is a door to the NORTH and SOUTH.")

		# add exits to room 2
		r2.addExit("west", r3)
		r2.addExit("east", r4)
		r2.addExit("south", r1)
		r2.addGrabbable("chalice")
		r2.addGrabbable("pillow")
		r2.addGrabbable("musicsheets")
		# add items to room 2
		r2.addItem("couch", "There is a thick layer of dust on the couch, but not on the PILLOW.")
		r2.addItem("piano", "It looks aged and worn. Almost as if no has played it in a while. Yet there are MUSICSHEETS on the piano and the chair is pulled out.")
		r2.addItem("rug", "The rug is free of dust and looks new...apart from the stains on the rug. An empty CHALICE lies upsidedown.")
		r2.addItem("doors","there is a door to the WEST, EAST, and SOUTH.")

		# add exits to room 3
		r3.addExit("east", r2)
		r3.addExit("secrettunnel",r4)
		# add grabbables to room 3
		r3.addGrabbable("watch")
		r3.addGrabbable("painting")
		r3.addGrabbable("lamp")
		# add items to room 3
		r3.addItem("chair", "There is a chair by the door. It looks like someone recently sat in it not long ago. There is a creepy looking PAINTING next to the chair.")
		r3.addItem("nightstand", "The nightstand is unusually enlongated. It's paint is peeling. There is an ancient looking LAMP on it.")
		r3.addItem("dresser", "The dresser looks old. There is a gold WATCH on it.")
		r3.addItem("wall", "There is an indentation on the wall. Behind it, some sort of SECRETTUNNEL.")
		r3.addItem("doors","There is a door to the EAST.")

		# add exits to room 4
		r4.addExit("west", r2)
		r4.addExit("secrettunnel", r3)
		# add grabbables to room 4
		r4.addGrabbable("trophy")
		r4.addGrabbable("book")
		# add items to room 4
		r4.addItem("bookshelf", "The bookshelf is nearly empty and there is a fine layer of dust on the shelves, but not on the books.There is a BOOK laying on top the bookshelf.")
		r4.addItem("armchair", "There are two arm chairs, booth look worn but recently used. On one chair lies a TROPHY of some sort.")
		r4.addItem("wall", "There is an indentation on the wall. Behind it, some sort of SECRETTUNNEL.")
		# set room 1 as the current room at the beginning of the
		# gameGame.
		#set win room and start room
		Game.start = r0
		Game.game = r1
		Game.currentRoom = Game.start
		# initialize the player's inventory
		Game.inventory = []
		
		
	# sets up the GUI
	def setupGUI(self):
		#organize the GUI
		self.pack(fill=BOTH, expand=1)
		# setup the player input at the bottom of the GUI
		# the widget is a Tkinter Entry
		# set its background to white and bind the return key to the
		# function process in the class
		# push it to the bottom of the GUI and let it fill
		# horizontally
		# give it focus so the player doesn't have to click on it
		Game.player_input = Entry(self, bg="white")
		Game.player_input.bind("<Return>", self.process)
		Game.player_input.pack(side=BOTTOM, fill=X)
		Game.player_input.focus()

		# setup the image to the left of the GUI
		# the widget is a Tkinter Label
		# don't let the image control the widget's size
		img = None
		Game.image = Label(self, width=int(WIDTH / 2), image=img)
		Game.image.image = img
		Game.image.pack(side=LEFT, fill=Y)
		Game.image.pack_propagate(False)

		# setup the text to the right of the GUI
		# first, the frame in which the text will be placed
		text_frame = Frame(self, width=WIDTH / 2)
		# the widget is a Tkinter Text
		# disable it by default
		# don't let the widget control the frame's size
		Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
		Game.text.pack(fill=Y, expand=1)
		text_frame.pack(side=RIGHT, fill=Y)
		text_frame.pack_propagate(False)

	# sets the current room image
	def setRoomImage(self):
			if (Game.currentRoom == None):
				# if dead, set the void image
				Game.img = PhotoImage(file="images/something.png")
			else:
				# otherwise grab the image for the current room
				Game.img = PhotoImage(file=Game.currentRoom.image)
			# display the image on the left of the GUI
			Game.image.config(image=Game.img)
			Game.image.image = Game.img

	# sets the status displayed on the right of the GUI
	def setStatus(self, status):
		# enable the text widget, clear it, set it, and disabled it
		Game.text.config(state=NORMAL)
		Game.text.delete("1.0", END)
		if (Game.currentRoom == None):
			# if dead, let the player know
			Game.text.insert(END, "Something has caught you.\n")
		elif Game.currentRoom == Game.start:
			rain.play(-1) #play start rain sound
			#intro text
			Game.text.insert(END, """They say that SOMETHING is better than NOTHING. \nBut is that really the true? 
					\nWhat if that SOMETHING is worse than NOTHING? \nThen NOTHING is surely better than SOMETHING \nright?
					\nYet you seek SOMETHING so that you are not left \nwith NOTHING knowing that that SOMETHING might be worse than NOTHING.
					\nSo the question becomes which should you fear \nmore...SOMETHING...or...NOTHING?
					\n\nSOMETHING is chasing you. Use your wits and logic to escape alive before you get \ncaught by SOMETHING
					\nBe careful, the noise you make may alert SOMETHING.
					\n\nType \"start game\" to escape.""")
		else:
			# otherwise, display the appropriate status
			#made hints not as obvious
			possible_actions=("""Hints:\nYou can type:\ngo direction \ndirection -> check \"item\"
					  \nlook item \nitem -> check \"You see\"
					  \ntake grabbable \ngrabbable -> check \"item\"""")
			Game.text.insert(END, str(Game.currentRoom) + "\n\n" 
					+ status+"\n\n\n"+possible_actions)
			
			Game.text.config(state=DISABLED)

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):
		# grab the player's input from the input at the bottom of
		# the GUI
		action = Game.player_input.get()
		# set the user's input to lowercase to make it easier to
		# compare the verb and noun to known values
		action = action.lower()
		# set a default response
		response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."
		# exit the game if the player wants to leave (supports quit,
		# exit, and bye)
		if (action == "quit" or action == "exit" or action == "bye"\
			or action == "sionara!"):
			exit(0)

		# the player is dead if the player is cought by something
		if (Game.currentRoom == None):
			# clear the player's input
			Game.player_input.delete(0, END)
			return
		
		# split the user input into words (words are separated by
		# spaces) and store the words in a list
		words = action.split()

		# the game only understands two word inputs
		if (len(words) == 2):
			# isolate the verb and noun
			verb = words[0]
			noun = words[1]

		# the verb is: go
		if (verb == "go"):
			# set a default response
			response = "Invalid exit."

		# check for valid exits in the current room
		if (noun in Game.currentRoom.exits):
			# if one is found, change the current room to
			# the one that is associated with the
			# specified exit
			new_room = Game.currentRoom.exits[noun]#sets the new room to be the room accociated with the exit location
			if noun == "south" and Game.currentRoom.name == "Hall":#check player for win condition
				if all(item in Game.inventory for item in ["key","book","chalice","painting"]): #You must find these items to escape.
					Game.currentRoom = new_room #if condition is met, player is allowed to proceed to winning room
					thunder.play(-1) #play end game sound
					response = "It is over. Nothing is chasing you now."#win message
				else:
					response = "It is locked."#prevent player from entering win room before completing objectives
			elif new_room.name == Game.something or Game.counter <= 0:#check if player is in the same room as something
				caught.play() #play caught sound
				Game.currentRoom = None #if caught set current rome to None to end the game in a dead state
			else:
				sroom = Game.currentRoom.name #set something room to current room
				Game.currentRoom = new_room #change current room to the new room
				Game.something = sroom #set something room to previous current room
				# set the response (success)
				response = "Room changed."
				Game.counter += 5
				if noun == "secrettunnel":
					secret.play() #play going into secret tunnel sound
				else:
					door.play() #play door open/close sound

		# the verb is: look
		elif (verb == "look"):
			# set a default response
			response = "I don't see that item."

			# check for valid items in the current room
			if (noun in Game.currentRoom.items):
				# if one is found, set the response to the
				# item's description
				Game.counter -= 2
				footsteps.play()
				response = Game.currentRoom.items[noun]

		# the verb is: take
		elif (verb == "take"):
			# set a default response
			response = "I don't see that item."

			# check for valid grabbable items in the current
			# room
			for grabbable in Game.currentRoom.grabbables:
				# a valid grabbable item is found
				if (noun == grabbable):
					# add the grabbable item to the player's
					# inventory
	 				
					Game.counter -= 1
					pickup.play() #play pickup sound
					Game.inventory.append(grabbable)
					# remove the grabbable item from the
					# room
					Game.currentRoom.delGrabbable(grabbable)
					# set the response (success)
					response = "Item grabbed."
					# no need to check any more grabbable
					# items
					break
		#open inventory on command, otherwise hidden/closed
		elif (verb == "open") and (noun == "inventory"):
			response = str(Game.inventory) 
		
		elif verb == "start" and noun == "game":
			rain.stop() #stop rain sound
			Game.currentRoom = Game.game
			Game.counter = 10
			response = " "

		if Game.counter == 0:#check if soething is near player from the sound
			caught.play() #play caught sound
			Game.currentRoom = None #if caught set current rome to None to end the game in a dead state

		# display the response on the right of the GUI
		# display the room's image on the left of the GUI
		# clear the player's input
		t = translate(response,1,10)#1=words in sentences; 0=whole sentences;;last number indicates frequency from 1-n
		self.setStatus(t)
		self.setRoomImage()
		Game.player_input.delete(0, END)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 1000
HEIGHT = 800

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()