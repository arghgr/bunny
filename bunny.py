import random
global bunny_pissed
global has_carrot
global has_popcorn
global has_gun # used in the Lame Room; if True, can shoot Woody Allen to get to the Awesum Room.
global rev_on # used in the Backwards Room; if True, reverses all text.
global count # counts number of times an action occurs before it changes. Can only be used once per room.
bunny_pissed = False
has_carrot = False
has_popcorn = False
has_gun = False
rev_on = True
count = 0

def bunny_actions(next, status):
# Defines the default actions you can do to the bunny in any room.
	global bunny_pissed
	global has_carrot
	global has_popcorn

	if "carrot" in next or "bunny" in next:
		if "give" in next or "return" in next or "feed" in next:
			if has_carrot and not bunny_pissed:
				print "The bunny gives you your carrot back."
				print "It doesn't need one right now."
				print "It's grooming itself by rubbing its fuzzy little purple paws on its face."
				print "Aww."
			elif has_carrot and bunny_pissed:
				print "You hand the bunny the carrot in your pocket."
				print "The bunny seems less pissed with you now."
				print "It takes the carrot and gives it a cautious nibble."
				has_carrot = False
				bunny_pissed = False
			else:
				print "What are you trying to do? You don't have any carrots."
		elif "take" in next or "get" in next or next == "carrot":
			if not bunny_pissed:
				print "You take the carrot from the bunny's hutch."
				print "The bunny looks pissed."
				has_carrot = True
				bunny_pissed = True
			else:
				dead("The bunny's pissed and rips your face off.")
		else:
			if "bunny" in next:
				if next == "bunny" or "examine" in next or "look" in next:
					print "%s" % status
				elif "kick" in next:
					dead("You kicked a fucking bunny.\nSeriously?\nIt grows fangs and sinks its teeth into your hand.")
				elif "fuck" in next:
					dead("You really just tried to fuck the bunny.\nIt fucks you with a knife instead.\nAsshole.")
				else:
					if not bunny_pissed:
						print "Your nonspecific attempts at interacting with the bunny have pissed it off."
						print "I'd leave the bunny alone if I were you."
						bunny_pissed = True
					else:
						dead("The bunny's pissed and rips your face off.")
			else:
				print "You mumble gibberish and piss your pants."
	else:
		print "You mumble gibberish and piss your pants."

def awesum_room_prompt():
	print "You're in a green room with giant cardboard letters on the wall:"
	print "AWESUM ROOM"
	print "Below that is a hole that looks like it might fit a carrot."

def awesum_room():
	global bunny_pissed
	global has_carrot

	awesum_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "carrot" in next:
			if has_carrot:
				print "You take the limp carrot out of your pocket and jam it into the hole in the wall."
				print "A door to the outside world magically appears around it."
				print "The carrot was the key!"
				print "You turn the brass doorknob underneath the hole and push the door open."
				print "Sunlight floods the room."
				print "The purple bunny hops past your feet and into the grass beyond."
				print "\nTHE END\n"
				exit()
			else:
				print "You don't have any carrots on you."
				print "Too bad."
				print "The bunny tugs on your pant leg, urging you to follow it."
				print "From the way its stomach is grumbling, it probably wants to go look for carrots."
		elif "bunny" in next:
			bunny_actions(next, "The bunny is doing the Macarena.")
		elif "hole" in next:
			print "You stick your finger into the hole in the wall."
			print "That was a bad idea."
			print "Your finger's stuck in the hole now."
			print "It takes a few tries to yank it back out."
			print "Now your finger is red and swollen."
			print "The bunny's munching on a carrot."
		elif "look" in next or "examine" in next:
			awesum_room_prompt()
			print "The bunny's at your feet, sniffing around."
		else:
			print "You mumble gibberish and piss your pants."

def lame_room_prompt():
	print "You emerge into an apartment with a large open window that overlooks the Manhttan skyline."
	print "There's a wooden chair in the center of the room."
	print "Fucking Woody Allen is sitting in it, looking agitated."
	print "Fuck!"
	print "You're stuck in a room with fucking Woody Allen."
	print "He's going on about some stupid inane shit again."

woody_allen_quotes = [
	"\"Um, I shot a moose once,\" Woody Allen says.",
	"\"I didn't mean to break it to you that way.\"",
	"\"I shot a moose.\"",
	"\"I was hunting in upstate New York in the woods.\"",
	"\"I tied the moose onto the fender of my car, and I drove back home.\"",
	"\"But I didn't realize that the bullet had not penetrated the moose.\"",
	"\"But it just creased its scalp, knocking it unconscious.\"",
	"You're only half-listening to Woody now because you've just caught a glimpse of a revolver on the floor behind his chair.",
	"\"I'm driving home along the highway, and I'm going through a tunnel...\"",
	"\"The moose woke up.\"",
	"\"So I'm driving with a live moose on my fender.\"",
	"\"The moose is signaling for a turn.\"",
	"\"And there's a law in New York State against driving with a conscious moose...\""
]

def woody_allen():
	global count
	if count < len(woody_allen_quotes):
		print "%s" % woody_allen_quotes[count]
		count += 1

def lame_room():
	global has_popcorn
	global has_gun
	global count
	count = 0

	lame_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "popcorn" in next:
			if has_popcorn:
				print "You take your bag of popcorn and throw it Woody Allen's face."
				print "\"That's for Midnight in Paris!\" you yell."
				print "Woody Allen sighs and picks popcorn out of his hair."
				print "He's heard all this before."
				print "And he's still a multi-bajillionaire, while you're some no-name schmuck."
				has_popcorn = False
			else:
				print "You wish you had a bag of popcorn to throw at Woody Allen's face."
				print "Maybe you can go get some at the movie theater and come back here."
				print "In the meantime, I guess you have to just keep talking to him."
		elif "shoot" in next or "kill" in next:
			if has_gun:
				print "You shrug, lift the gun, aim for Woody Allen's head, and pull the trigger."
				print "You startle yourself with the loud BANG!"
				print "Holy shit! You just shot Woody Allen!"
				print "Before you can see the hole you made in his skull, the floor of the entire apartment opens up like a trapdoor beneath you."
				print "You fall into the abyss.\n"
				count = 0
				awesum_room()
			else:
				print "You imagine yourself taking out this annoying facsimile of Woody Allen."
				print "Unfortunately, you have nothing in your possession that can do that."
				print "Yet."
		elif "revolver" in next or "gun" in next:
			if has_gun:
				print "You examine the revolver in your hand."
				print "It's a classic old western .45, shiny and silver with a wooden handle."
				print "Engraved in a fancy script across the barrel are the following words:"
				print "KILL WOODY ALLEN"
			else:
				print "As Woody rambles on, you walk around his chair and calmly pick up the gun behind him."
				has_gun = True
		elif "talk" in next or "woody" in next:
			if count < len(woody_allen_quotes):
				woody_allen()
			else:
				print "Oh good, Woody's gotten quiet."
				print "Oh, wait, no, he's just really old and forgot what he was talking about."
				print "Dammit!"
				print "You have to get us out of here."
				count = 0
		elif "look" in next or "room" in next or "examine" in next:
			print "The tube slide is behind you."
			print "There's a gray conveyor belt on the ceiling."
			print "Fucking Woody Allen is sitting in a chair in the middle of the room."
		elif "slide" in next:
			print "You climb into the slide and hurtle back down to the mooR sdrawkcaB."
			print "!eeeehW\n"
			backwards_room()
		elif "belt" in next:
			print "You jump onto the conveyor belt on the ceiling and surprisingly stick onto it."
			print "It seems like gravity's pull on the ceiling is the same as its pull on the floor."
			print "The conveyor belt whisks you off to a room with no lights."
			print "It loses its grip on you and you go flying through the air.\n"
			tentacle_room()
		elif "bunny" in next:
			print "The bunny is nowhere to be found."
			print "It's probably getting its groove on in the Backwards Room next door."
		elif "exit" in next or "get out" in next:
			print "I suppose I should tell you that there's a way to get to the AWESUM ROOM from here."
			print "It involves some violence."
		elif next == "help":
			if has_popcorn:
				print "You can LOOK AROUND, TALK TO WOODY ALLEN, THROW POPCORN AT WOODY ALLEN'S FACE, or REPEAT.\nOr piss your pants."
			else:
				print "You can LOOK AROUND, TALK TO WOODY ALLEN, or REPEAT.\nOr piss your pants."
		elif next == "repeat" or next == "again":
			lame_room_prompt()
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and piss your pants."

def tentacle_room_prompt():
	print "You fall into the darkness with a loud thud."
	print "There's a FUCKING HUGE TERRIFYING MONSTER lying in a pit in front of you."
	print "It has maybe twenty purplish-red gyrating tentacles but I'm trying not to count."
	print "Good luck, buddy."

def tentacle_room():
	global bunny_pissed
	global has_carrot

	tentacle_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "exit" in next or "back" in next or "get out" in next:
			print "Are you kidding me? That hole you came through is way too far up."
		elif next == "ask":
			print "Ask what? Who? Me?"
			print "ASK THE FUCKING BUNNY COZ I AIN'T GOT NO ANSWERS FOR YOU."
			print "The ridiculous tentacular monster turns one of its giant yellow eyes on you."
		elif "bunny" in next:
			if "ask" in next:
				if bunny_pissed:
					dead("You're fucked, man. The bunny doesn't wanna help you.\nYou die wrapped in a tentacle, screaming for your life.")
				elif not bunny_pissed and has_carrot:
					print "The bunny stares at you, then grudgingly hops a path through the monster's tentacularness."
					print "You follow it, then give it a carrot for saving your pathetic ass.\n"
					has_carrot = False
					riddle_room()
				else:
					print "The bunny stares at you, then grudgingly hops a path through the monster's tentacularness."
					print "You follow it safely through to the other side of the room."
					print "You're alive, but the bunny is now hungry and pissed at your stupid ass."
					print "Give it a carrot for its trouble next time."
					print "It's the least you can do."
					print "Jerk.\n"
					bunny_pissed = True
					riddle_room()
			else:
				print "The purple bunny hops to your side, amused."
				print "Maybe you should try asking it for help."
				if bunny_pissed: print "Or don't, you're fucked anyway. It doesn't like you."
		elif "repeat" in next or "again" in next:
			print "Srsly, I have to repeat myself? You are so fucked."
			tentacle_room_prompt()
		elif "look" in next or "examine" in next:
			print "Your eyes adjust to the darkness and you look around the dungeon-like room, heart pounding."
			print "A few feet away, the giant monster is waving its tentacles around blindly, looking for a tasty snack."
		elif next == "help":
			print "How the fuck should I know? You're the one who got yourself into this shit!"
			print "Why don't you ask the fucking bunny with the smug fucking look on its face?"
		elif next == "fuck this":
			exit()
		else:
			dead("You fail to be coherent.\nThe purple bunny hops away as the monster finds you and stuffs you into its big, gaping mouth.")

def bunny_room_prompt():
	print "The bunny hops away and leads you to its house."
	print "It doesn't seem to like being touched."
	print "The little hutch is nice and grassy, but too small for you."
	print "There is a carrot near the entrance."

def bunny_room():
	global bunny_pissed
	global has_carrot

	bunny_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "hutch" in next or "house" in next:
			print "You stick your head into the bunny's hutch."
			print "It smells kind of green and earthy."
		elif next == "repeat" or next == "again":
			bunny_room_prompt()
		elif next == "help":
			if not has_carrot:
				print "You can PET BUNNY, KICK BUNNY, TAKE CARROT, LEAVE ROOM, or REPEAT.\nOr piss your pants."
			else:
				print "You can PET BUNNY, KICK BUNNY, GIVE CARROT, LEAVE ROOM, or REPEAT.\nOr piss your pants."
		elif "leave" in next or "exit" in next or "back" in next:
			print "You leave the bunny's house and backtrack the way you came."
			print "The bunny follows you, its footfalls nearly silent on the carpet.\n"
			start()
		elif next == "fuck this":
			exit()
		else:
			bunny_actions(next, "The bunny is twitching its little pink nose nervously, as bunnies are wont to do.")

def intermission_prompt():
	print "The word \"INTERMISSION\" scrolls across the black screen in white Helvetica."
	print "Calm elevator music fills the room."
	print "There's an exit near the big screen, and a door in the back that leads to the lobby."

def intermission():
	intermission_prompt()

	while True:
		next = raw_input("> ").lower()

		if "exit" in next:
			print "You head over to the exit by the big screen and open the door."
			print "It unceremoniously deposits you into nothingness.\n"
			backwards_room()
		elif "lobby" in next:
			print "You walk briskly up the aisle and make a beeline for the door.\n"
			lobby()
		elif next == "door":
			print "Which door? There's the exit door and the lobby door."
		elif "screen" in next:
			print "You sit in one of the red velvet chairs and watch the big screen for a minute."
			print "It flickers between the scrolling \"INTERMISSION\" and a test pattern."
		elif "music" in next:
			print "You strain your ears to hear exactly what song is playing."
			print "After a few minutes, you surmise that it might be the original Pure Moods album."
		elif next == "intermission":
			print "Oh good, you can read what's on the screen."
			print "Wait, how have you been reading this whole thing then?"
			print "What the shit?"
		elif "repeat" in next or "again" in next:
			print "You wake up alone in a large movie theater."
			intermission_prompt()
		elif next == "help":
			print "You can find an EXIT or visit the LOBBY, or REPEAT.\nOr take a nap."
		elif "back" in next:
			print "Dude you can't go back, you don't even know how the fuck you got here."
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and slip into microsleep."

def lobby_prompt():
	print "In the lobby, the tuxedo-clad snack counter robot is giving away snacks for free."
	print "There's also a restroom by the counter."

def lobby():
	global has_carrot
	global has_popcorn

	lobby_prompt()

	while True:
		next = raw_input("> ").lower()

		if "snack" in next:
			if has_carrot and not has_popcorn:
				print "The tuxedo-clad snack robot hands you a box of popcorn."
				has_popcorn = True
			elif not has_carrot:
				print "The tuxedo-clad snack robot hands you a carrot."
				has_carrot = True
			else:
				print "Your hands are pretty full."
				print "The tuxedo-clad snack robot gives you stinkeye."
				print "He has a soda cup with googly eyes on it for a face."
		elif "restroom" in next or "bathroom" in next or "piss" in next or "poop" in next:
			print "Oh good, you manage to relieve yourself in a toilet."
			print "Maybe you won't piss your pants anymore."
		elif "exit" in next or next == "get out" or next == "way out":
			print "You wander around the lobby until you find another exit."
			print "As soon as you step through it, lasers rip you apart."
			print "Don't worry, they neatly reassemble you in a minute.\n"
			riddle_room()
		elif "back" in next or "theater" in next:
			print "You head back into the dark theater."
			intermission()
		elif "repeat" in next or "again" in next:
			lobby()
		elif next == "help":
			print "You can TAKE A PISS, GET A SNACK, GO BACK to the theater, find the EXIT, or REPEAT."
			print "Or take a nap."
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and slip into microsleep."

def deep_space_prompt():
	print "You are now hurtling through deep space."
	print "Oh my God, it's full of stars!"
	print "The purple bunny followed you and is floating off with a piece of celery."
	print "There is a small moon embedded in the pink planet below."

def deep_space():
	global bunny_pissed
	global has_carrot

	deep_space_prompt()

	while True:
		next = raw_input("> ").lower()

		if "moon" in next:
			print "You crash land on the moon and lose consciousness.\n"
			intermission()
		elif "planet" in next:
			print "You navigate yourself to the pink planet."
			pink_planet()
		elif "repeat" in next or "again" in next:
			deep_space_prompt()
		elif "bunny" in next:
			print "The bunny slowly kicks its way out of your reach."
		elif "celery" in next:
			if not bunny_pissed:
				print "You make a grab for the celery that the purple bunny is holding."
				print "The bunny punches you in the face and disappears."
				print "Good thing it was in a good mood this time."
			else:
				dead("You make a grab for the bunny's celery.\nShouldn't have pissed that bunny off.\nIt eats you alive.")
		elif next == "help":
			print "You can VISIT MOON, VISIT PINK PLANET, GRAB ROPE, or REPEAT.\nOr piss your pants."
		elif "rope" in next or "back" in next:
			print "You grab on to the rope and slide back down to where you started."
			start()
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and piss your pants."

def pink_planet_prompt():
	print "It's a neon pink that only gets more garish as you come closer."
	print "There is a bulbous silver rocket on its surface."
	print "The embedded moon is now a few days' journey away."
	print "The bunny finishes its celery and glances at you curiously."

def pink_planet():
	global bunny_pissed
	global has_carrot
	global has_popcorn

	pink_planet_prompt()

	while True:
		next = raw_input("> ").lower()

		if "rocket" in next:
			print "You enter the rocket."
			print "Its lighted control panel is pretty straightforward."
			print "You pilot it to the nearest star."
			print "It slingshots you very suddenly to your destination.\n"
			backwards_room()
		elif "moon" in next:
			if not has_carrot and not has_popcorn:
				dead("You run out of food on the way to the moon and starve.\nThe bunny eats you for sustenance.")
			else:
				print "During your three-day journey to the moon, you get really hungry."
				if has_carrot:
					print "Good thing that carrot manages to tide you over."
				else:
					print "Good thing that popcorn manages to tide you over."
				print "You still black out before you get there, though.\n"
				print "You wake up alone in a large movie theater."
				has_carrot = False
				intermission()
		elif "bunny" in next:
			if bunny_pissed and has_carrot:
				print "The bunny flinches away from you."
				print "It's still hungry, though, so it goes for the carrot in your hand."
				print "Stop pissing the bunny off."
				has_carrot = False
			elif bunny_pissed and not has_carrot:
				dead("The bunny's still hungry, so it lunges for you.")
			else:
				print "The bunny flinches and does a half-hop to get the hell away from you."
				print "You really should have learned by now.\nSTOP FUCKING WITH THE BUNNY."
				bunny_pissed = True
		elif "repeat" in next or "again" in next:
			pink_planet_prompt()
		elif next == "help":
			print "You can ENTER ROCKET, VISIT MOON, attempt to chill with the BUNNY, or REPEAT.\nOr piss your pants."
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and piss your pants."

def reverse_reverse(string):
	# This function reverses any string of text you pass into it if rev_on is True.
	global rev_on

	if rev_on == True:
		revtext = string[::-1]
		print revtext
	else:
		print string

def backwards_room_prompt():
	reverse_reverse("You are now in a large bedroom that's been wallpapered a garish orange paisley.")
	reverse_reverse("Everything is ass backwards.")
	reverse_reverse("Miscegenation is still illegal here.")
	reverse_reverse("The purple bunny is in the middle of the room, doing the Cha Cha Slide.")

def backwards_room():
	global bunny_pissed
	global rev_on
	rev_on = True

	backwards_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "help" in next or "flip" in next or "reverse" in next or "look" in next or "examine" in next or "dance" in next or "slide" in next or "cha " in next or "exit" in next or "bunny" in next or "spin" in next or "handstand" in next:
			reverse_reverse("Nope, you have to type by the rules.")
		elif "esrever" in next or "drawkcab" in next or "pilf" in next or "nips" in next or "dnatsdnah" in next:
			if rev_on == True:
				rev_on = False
				print "Everything spins around and the room reorients itself."
				print "You throw up a little but are otherwise fine."
				print "But it's just your perception that's been un-reversed."
				print "You still have to interact with everything around you backwards."
			else:
				print "Everything spins around and the room reorients itself."
				reverse_reverse("You throw up a little but are otherwise fine.")
				reverse_reverse("Everything is backwards again.")
		elif "kool" in next or "enimaxe" in next:
			reverse_reverse("You examine the paisley very closely as you make your way across the room.")
			reverse_reverse("In a far corner, there's an opening in the wallpaper big enough for a kid half your size.")
			reverse_reverse("It looks like the exit to one of those indoor tube slides.")
		elif "ecnad" in next:
			reverse_reverse("You hop in next to the bunny.")
			reverse_reverse("The two of you boogie down.")
			if not bunny_pissed:
				reverse_reverse("The bunny's long ears twitch in time to the music.")
			else:
				reverse_reverse("I think the bunny is starting to like you.")
				bunny_pissed = False
		elif "ynnub" in next:
			reverse_reverse("The bunny's gotten wise to you. It hops out of reach.")
		elif "edils" in next:
			reverse_reverse("You climb into the slide and run up its spiraling length.")
			print "You get dizzy as things spin back into their proper place.\n"
			lame_room()
		elif next == "repeat" or next == "taeper":
			backwards_room_prompt()
		elif "pleh" in next:
			if rev_on == True:
				reverse_reverse("You can DANCE with the BUNNY, LOOK around, do a HANDSTAND, or REPEAT.")
				reverse_reverse("Or piss your pants.")
			else:
				print "You can ECNAD with the YNNUB, KOOL around, do a DNATSDNAH, or TAEPER.\nOr piss your pants."
		elif next == "fuck this":
			exit()
		else:
			reverse_reverse("You mumble incoherently and piss your pants.")

# A list of riddles for the riddle_room().
riddles = [
	["tiny","red","Pop","Aldous Huxley","one"],
	["big","orange","Six","a Tyrannosaurus rex","two"],
	["enormous","yellow","Squish","Nelson Mandela","three"],
	["large","green","Uh-uh","your mom","four"],
	["small","blue","Cicero","an anthropomorphized white daisy","five"],
	["bunny-sized","indigo","Lipschitz","a blinged-out showgirl","six"],
	["miniscule","violet","He had it comin'","ex-prime minister Yukio Hatoyama","seven"]
]

def riddle_maker():
	ridnum = random.randint(0,6) #.__str__()
	rid_list = riddles[ridnum]
	size = rid_list[0]
	color = rid_list[1]
	question = rid_list[2]
	hologram = rid_list[3]
	answer = rid_list[4]

	print "You walk up to a %s %s question mark and push it into the wall." % (size, color)
	print "It projects a hologram of %s onto the floor at your feet." % hologram
	print "In a big, booming voice that fills the room, it asks you this question:"
	print '"%s"' % question

	while True:
		next = raw_input("> ").lower()

		if answer in next:
			print '"YOU GOT IT!"'
			print "The hologram dances around happily and waves a magic wand."
			print "A door appears on the wall opposite you, setting many colorful question marks on fire in the process."
			print "You stride across the room and pull open the door triumphantly.\n"
			awesum_room()
		elif next == "fuck this":
			exit()
		else:
			print '"That\'s the wrong answer," booms the hologram as it fuzzes out and disappears.'
			print "You only get one shot at answering each question? That's bullshit."
			print "Well, try another question."
			print "Maybe you'll get back to this one later."
			return

def riddle_room_prompt():
	print "You find yourself in a tie-dye-colored room filled with rainbow-colored question marks."
	print "Your eyes water from the visual assault."

def riddle_room():

	riddle_room_prompt()

	while True:
		next = raw_input("> ").lower()

		if "bunny" in next:
			print "Oh! The bunny's little white cotton tail disappears into a cupboard in the floor."
			print "I think there's another way out of here."
		elif "question" in next:
			riddle_maker()
		elif "button" in next:
			if "push" in next:
				print "Against your better judgment, you push the little red button."
				print "You feel air rushing past you."
				print "Whoosh!"
				print "A hurricane-like current sweeps you out through the window."
				print "You're driven up like a rocket through the sky.\n"
				deep_space()
			else:
				print "You walk up to the little red button and peer at it closely."
				print "It looks like a stereotypical little red button."
				print "Not the fat kind that has a depression for your thumb, but narrower."
		elif "look" in next or "room" in next or "examine" in next:
			print "As you look around, you notice that the technicolor question marks can be pushed into the wall."
			print "There's a little red button on the other side of the room, built into the dot of a blue interrobang."
			print "The purple bunny sniffs around. Its bright, shiny coat looks right at home here."
		elif next == "help":
			print "You can LOOK AROUND or examine one of the many QUESTIONs on the walls."
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and piss your pants."

def dead(why):
	print why
	print "\nWTF why did you do that.\nBoom.\nYou're dead now.\n"
	print "Back to square one? Y/N"

	while True:
		next = raw_input("> ").lower()

		if next == "yes" or next == "y" or next == "sure" or next == "ok" or next == "okay" or next == "fine":
			global bunny_pissed
			global has_carrot
			global has_popcorn
			global has_gun
			global rev_on
			global count
			bunny_pissed = False
			has_carrot = False
			has_popcorn = False
			has_gun = False
			rev_on = True
			count = 0
			print "\n"
			start()
		elif next == "no" or next == "nope" or next == "n" or "fuck" in next:
			exit()
		else:
			print "Wat?"

def start_prompt():
	print "You're in a small white room."
	print "There are no windows but it's very bright."
	print "There's a rope that leads to the ceiling and a hole in the floor."
	print "A little purple bunny is nibbling on a banana behind you."

def start():
	start_prompt()

	while True:
		next = raw_input("> ").lower()

		if next == "up" or next == "go up" or "ceiling" in next or "rope" in next:
			print "You climb the rope and are whisked upward. \n"
			deep_space()
		elif "down" in next or "hole" in next or "floor" in next:
			tentacle_room()
		elif "bunny" in next:
			if "kick" in next:
				dead("You kicked the fucking bunny.\nSeriously?\nIt grows fangs and sinks its teeth into your hand.")
			elif "fuck" in next:
				dead("You really just tried to fuck the bunny.\nIt fucks you with a knife instead.\nAsshole.")
			else:
				bunny_room()
		elif "repeat" in next or "again" in next:
			start_prompt()
		elif next == "help":
			print "You can CLIMB ROPE, JUMP INTO HOLE, PET BUNNY, KICK BUNNY, or REPEAT.\nOr piss your pants."
		elif next == "fuck this":
			exit()
		else:
			print "You mumble gibberish and piss your pants."
			print "Ask me for HELP to see some of the stuff you can do."

start()