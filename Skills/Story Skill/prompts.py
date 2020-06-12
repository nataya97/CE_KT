import random

values = random.randint(0,5)
num = 0;

RANDOM_NUMBER = 0
SELECTED_GENRE = ""

def randomNumb():
    RANDOM_NUMBER += 1
    return RANDOM_NUMBER

GENRES = ["romance", "drama", "horror", "sci-fi", "dystopia"]
GET_AFFIRMATION_MESSAGE = ["That is a very good choice. I am ready, if you are.",
                                   "I could not have picked a better one. I am ready, if you are.",
                                   "What a good choice. I am ready, if you are.",
                                   "Alright, lets get started. I am ready, if you are.",
                                   "Here we go. I am ready, if you are.",
                                   "Alright, alright, alright. I am ready, if you are.",
                                   "Settle in. I am ready, if you are.",
                                   "Cozy up. I am ready, if you are."]
HELP_MESSAGE = "What can I help you with?"
HELP_REPROMPT = "HELP_REPROMPT"
FALLBACK_MESSAGE = "FALLBACK_MESSAGE"
FALLBACK_REPROMPT = "FALLBACK_REPROMPT"
ERROR_MESSAGE = "There was an error..."
STOP_MESSAGE = "I guess, this is where we part ways... bye."
GET_STORY = ["Once upon a time there was a handsome girl called Beth Cox. She was on the way to see her Phil Platt, when she decided to take a short cut through Slipperyham Park.",
                 "It wasn't long before Beth got lost. She looked around, but all she could see were trees. Nervously, she felt into her bag for her favourite toy, Donkey, but Donkey was nowhere to be found! Beth began to panic. She felt sure she had packed Donkey. To make matters worse, she was starting to feel hungry.",
                 "Unexpectedly, she saw a slippery elephant dressed in a green coat disappearing into the trees",
                 "How odd! thought Beth.",
                 "For the want of anything better to do, she decided to follow the peculiarly dressed elephant. Perhaps it could tell him the way out of the forest.",
                 "Eventually, Beth reached a clearing. In the clearing were two houses, one made from red cabbages and one made from sweets.",]

def selectedGenre(genre):
    SELECTED_GENRE = genre
    setStory(SELECTED_GENRE)

def setStory(SELECTED_GENRE):
    if SELECTED_GENRE == "romance":
        print("PRINTING IN ROMANCE")
        SKILL_NAME = "Story Teller"
        STOP_MESSAGE = "I guess, this is where we part ways... bye."
        GET_STORY = ["Once upon a time there was a handsome girl called Beth Cox. She was on the way to see her Phil Platt, when she decided to take a short cut through Slipperyham Park.",
                     "It wasn't long before Beth got lost. She looked around, but all she could see were trees. Nervously, she felt into her bag for her favourite toy, Donkey, but Donkey was nowhere to be found! Beth began to panic. She felt sure she had packed Donkey. To make matters worse, she was starting to feel hungry.",
                     "Unexpectedly, she saw a slippery elephant dressed in a green coat disappearing into the trees",
                     "How odd! thought Beth.",
                     "For the want of anything better to do, she decided to follow the peculiarly dressed elephant. Perhaps it could tell him the way out of the forest.",
                     "Eventually, Beth reached a clearing. In the clearing were two houses, one made from red cabbages and one made from sweets.",]
    elif SELECTED_GENRE == "drama" or SELECTED_GENRE == "DRAMA":
        print("PRINTING IN DRAMA")
        SKILL_NAME = "Story Teller"
        STOP_MESSAGE = "I guess, this is where we part ways... bye."
        GET_STORY = ["Onceeeee upon a time there was a handsome girl called Beth Cox. She was on the way to see her Phil Platt, when she decided to take a short cut through Slipperyham Park.",
                     "Ittttt wasn't long before Beth got lost. She looked around, but all she could see were trees. Nervously, she felt into her bag for her favourite toy, Donkey, but Donkey was nowhere to be found! Beth began to panic. She felt sure she had packed Donkey. To make matters worse, she was starting to feel hungry.",
                     "Unexpectedlyyyy, she saw a slippery elephant dressed in a green coat disappearing into the trees",
                     "How odddddd! thought Beth.",
                     "For the wantrrr of anything better to do, she decided to follow the peculiarly dressed elephant. Perhaps it could tell him the way out of the forest.",
                     "Eventuallyyyy, Beth reached a clearing. In the clearing were two houses, one made from red cabbages and one made from sweets.",]
    else:
        SKILL_NAME = "Story Teller"
        print("PRINTING IN :::")
        STOP_MESSAGE = "I guess, this is where we part ways... bye."
        GET_STORY = ["Onceeeee upon a time there was a handsome girl called Beth Cox. She was on the way to see her Phil Platt, when she decided to take a short cut through Slipperyham Park.",
                     "It wasn't long before Beth got lost. She looked around, but all she could see were trees. Nervously, she felt into her bag for her favourite toy, Donkey, but Donkey was nowhere to be found! Beth began to panic. She felt sure she had packed Donkey. To make matters worse, she was starting to feel hungry.",
                     "Unexpectedlyyyy, she saw a slippery elephant dressed in a green coat disappearing into the trees",
                     "How odddddd! thought Beth.",
                     "For the wantrrr of anything better to do, she decided to follow the peculiarly dressed elephant. Perhaps it could tell him the way out of the forest.",
                     "Eventuallyyyy, Beth reached a clearing. In the clearing were two houses, one made from red cabbages and one made from sweets."]
        
def getStory():
    print(SELECTED_GENRE)
    setStory(SELECTED_GENRE)
    return GET_STORY[RANDOM_NUMBER]

    

        
