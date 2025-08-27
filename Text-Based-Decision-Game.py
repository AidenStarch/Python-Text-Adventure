import sys
import time

def dialogue(line):
    sys.stdout.write('\r')
    sys.stdout.flush()
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.035)
    print()

#Function used to increase stats throughout the code
def add_to_stat(stat, increased_by):
    if stat in char_stats:
        char_stats[stat] += increased_by
        print()
        print(f"{stat} increased by {increased_by}! It is now level {char_stats[stat]}!")
        print()
    else:
        print(f"There was an unexpected error found")


#Creates dictionary of stats
char_stats = {
    "mage":0,
    "charisma":0,
    "weapon_wielding":0,
    "archery":0,
}

#Gathers character name from user input
dialogue(f"You awaken feeling dazed and confused.")
dialogue(f"Looking over, you notice a man wearing a black robe and hood.")
dialogue(f"He seems startled at your return to consciousness.")
dialogue(f"Quickly he comes to your side, sits next to your bed, and introduces himself,")
dialogue(f"\"Woah! Woah! Slow down, you've been in a coma for nearly 2 weeks, take it easy.\"")
dialogue(f"He continues,")
dialogue(f"\"What's the last thing you remember? Do you remember your name?\"")

#"dialogue("")" separates input from story
dialogue("")
char_name = input(f"Please enter your name: ")
dialogue("")


#"while True" will force an infinite loop until reaching the break via a viable character name
while True:
    #Ensures the user is giving a viable character name
    if char_name.isalpha():
        break
    else:
        dialogue("")
        char_name = input("Please enter a name using letters")
        dialogue("")

dialogue(f"\"Ah! {char_name}, not a bad name!\"")
dialogue(f"He takes his hands and does a strange circular motion in the air like a wizard.")
dialogue(f"Suddenly a soup appears. ")
dialogue(f"He grabs it out of the air between his hands and gives it to you.")
dialogue(f"\"Eat up\" He says, ")
dialogue(f"\"You must be starving.\" ")
dialogue(f"There's a long pause before his next sentence. ")
dialogue(f"\"Well {char_name}, do you remember what you were good at?")
dialogue(f"Were you an archer, swordsman, mage, or did you just have a silver tongue?\"")

#User input
dialogue("")
class_select = input(f"Please select a class. Archer, swordsman, mage, or silver tongue: ").lower()
dialogue("")

#New loop to get a character class from input
while True:
    #if user input is correct, go to the next step
    if class_select == "archer" or class_select == "archery":
        add_to_stat("archery", 10)
        break
    elif class_select == "swordsman":
        add_to_stat("weapon_wielding", 10)
        break
    elif class_select == "mage":
        add_to_stat("mage", 10)
        break
    elif class_select == "silver tongue" or class_select == "silvertongue":
        add_to_stat("charisma", 10)
        break
    else:
        dialogue("")
        class_select = input("Please input archery, swordsman, mage, or silver tongue.").lower()
        dialogue("")

#Doesn't really matter what the user responds with
dialogue(f"You continue eating your soup as the man talks to you. ")
dialogue(f"\"Well {char_name}, it's nice to meet you.")
dialogue(f" I suppose I should introduce myself.")
dialogue(f" My name is Alfred Stormmaker, I'm the leader of what remains of the Marimbists.")
dialogue(f" We've been fighting off the Ikeals for years, but it doesn't look like things are gonna go our way.")
dialogue(f" Sorry to make this conversation so grim, I figure you'd want to know what's going on.")
dialogue(f" What do you remember anyway?\"")

dialogue("")
char_memory = input(f"Tell Alfred what you remember: ")
dialogue("")

add_to_stat("charisma", 5)

#Continue the story here
if char_stats["charisma"] >= 10:
    dialogue(f"\"It all makes sense now!")
    dialogue(f"I found you with wounds all over your body, you're lucky to be alive {char_name}.\"")
    dialogue(f"As Alfred is talking you hear a strange roaring sound through the walls.")
    dialogue(f"You notice Alfred immediately becomes alert.")
    dialogue(f"He jumps up to go grab something when suddenly-")
    dialogue(f"BOOM!")
    dialogue(f"A dragon crashes it's head through the side of the room.")
    dialogue(f"You fly out of your bed onto the floor.")
    dialogue(f"The dragon roars and speaks in a low gravely voice")
    dialogue(f"\"Where are they! Where is the prisoner!?\"")
else:
    dialogue(f"\"Hmmmm that's very... odd... I found you on the verge of death.")
    dialogue(f"You had wounds and cuts all over you, seems like your story doesn't exactly add up.\"")
    dialogue(f"As Alfred is talking you hear a strange roaring sound through the walls.")
    dialogue(f"You notice Alfred immediately becomes alert.")
    dialogue(f"He jumps up to go grab something when suddenly-")
    dialogue(f"BOOM!")
    dialogue(f"A dragon crashes it's head through the side of the room.")
    dialogue(f"You fly out of your bed onto the floor.")
    dialogue(f"The dragon roars and speaks in a low gravely voice")
    dialogue(f"\"Where are they! Where is the prisoner!?\"")


#This is a GIANT branch of decisions
dialogue("")
char_found = input(f"What do you do? Attack the dragon with a mace, cast a spell at the dragon, talk to the dragon, or rescue Alfred and runaway? ").lower()
dialogue("")


if char_found == "attack the dragon with a mace":
    dialogue(f"You grab a mace off of the wall and swing for the dragon's eye.")
    if char_stats["weapon_wielding"] >= 10:
        add_to_stat("weapon_wielding", 5)
        dialogue(f"It's a direct hit! the dragon groans and yells.")
        dialogue(f"\"AGHHHH! My eye! My eye! What have you done?!\"")
        dialogue(f"The dragon propels its head out of the building and flies away without saying another word.")
        #add what happens here
    else:
        dialogue(f"You attempt to grab a mace off of the wall and swing at the dragon, but you miss.")
        dialogue(f"The dragon throws his head in your direction, sending you flying.")
        dialogue(f"\"Was that really necessary?\" he says. He opens his mouth and unleases fire on your body, killing you instantly.")
        sys.exit()

#Regardless of mage level, the player will advance and increase their skill. Their mage skill is likely to be between 5 and 15
elif char_found == "cast a spell at the dragon":
    add_to_stat("mage", 5)
    dialogue(f"You get on your feet, put your hands together and shout \"Alohamori!\" and throw your hands in the direction of the dragon.")
    if char_stats["mage"] >= 10:
        dialogue(f"A purple ball of light shoots out of your hands and hits the dragon right on its nose.")
        dialogue(f"The dragon seems dazed and confused.")
        dialogue(f"Alfred sprints toward you and grabs your arm \"Lets go! We have to move now!\"")
        dialogue(f"You don't have time to think, so you do as Alfred commands.")
    else:
        dialogue(f"A purple light flickers between your fingers, but it isn't strong enough to do anything.")
        dialogue(f"The dragon speaks, \"I'm not here to hurt anybodu, I know that seems ironic considering I crashed through your building\"")
        dialogue(f"Before the dragon has time to say anything else you hear Alfred shout \"Alohamori!\"")
        dialogue(f"A purple ball of light shoots out of his hands and hits the dragon right on its nose.")
        dialogue(f"The dragon seems dazed and confused.")
        dialogue(f"Alfred sprints toward you and grabs your arm \"Lets go! We have to move now!\"")
        dialogue(f"You don't have time to think, so you do as Alfred commands.")

elif char_found == "talk to the dragon":
    dialogue(f"You stand up and look at the dragon. He speaks out, \"Are you not scared of me puny human?\"")

#While loop to make sure there's a valid input
    while True:
        char_to_dragon = input(f"How do you approach the dragon? Do you make a joke, ask him a question, or tell him to leave? ").lower()
#This whole section is for charisma >= 15
        if char_stats["charisma"] >= 15:
            if char_to_dragon == "make a joke":
                dialogue(f"You approach the dragon.")
                dialogue(f"\"You know, I always expected a dragon to be a lot scarier than this.\" you say.")
                dialogue(f"The dragon makes direct eye contact and says, \"You are one confident human aren't you?\"")
                dialogue(f"He moves in closer to you \"Alohamori!\" Alfred shouts, then suddenly a lightning ball hits the dragon.")
                dialogue(f"The dragon gets knocked unconscious. His head drops to the ground and his body slams into the building.")
                dialogue(f"\"Lets go! Lets go!\" says Alfred. He takes your arm and rushes you down the stairs and outside of the building.")
                add_to_stat("charisma", 5)
                break
            #In this scenario, the player has suspicion that something isn't quite right
            elif char_to_dragon == "ask him a question":
                dialogue(f"\"Who are you? Why are you here?\"")
                dialogue(f"The dragon responds, \"You are a very bold human indeed. Very well, my name is Vloynir III")
                dialogue(f"I'm looking for one of our dragon masters, he was stolen from us.")
                dialogue(f"Wait a second... you kinda look-\" A lightning ball strikes the dragon.")
                dialogue(f"The dragon gets knocked unconscious. His head drops to the ground and his body slams into the building.")
                dialogue(f"\"Lets go! Lets go!\" says Alfred. He takes your arm and rushes you down the stairs and outside of the building.")
                add_to_stat("charisma", 5)
                break

            elif char_to_dragon == "tell him to leave":
                dialogue(f"You approach the dragon.")
                dialogue(f"\"We don't know what you're talking about! Get out of here!\"")
                dialogue(f"The dragon looks confused at your bravery to confront him.")
                dialogue(f"The dragon speaks, \"Everything points towards our dragon master being here. They have to be here!\"")
                dialogue(f"\"Alohamori!\" Alfred yells. A ball of lightning shoots out of his hands and hits the dragon right on his nose.")
                dialogue(f"The dragon gets knocked unconscious. His head drops to the ground and his body slams into the building.")
                dialogue(f"\"Lets go! Lets go!\" says Alfred. He takes your arm and rushes you down the stairs and outside of the building.")
                add_to_stat("charisma", 5)
                break

#Game ends here if you talk to the dragon with a low charisma skill
        else:
            dialogue(f"You stand up to talk to the dragon. Whatever you say, the dragon hates.")
            dialogue(f"He screeches out, \"Rah! Stop talking puny human!\"")
            dialogue(f"He lights the entire room on fire, killing both you and Alfred.")
            sys.exit()

elif char_found == "rescue alfred and runaway":
    dialogue(f"To be continued")

dialogue(f"The rest of the story is still in development. Stay tuned!")
