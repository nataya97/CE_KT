import random

values = random.randint(0,5)
RANDOM_NUMBER = values
valuesYes = random.randint(0,4)
RANDOM_NUMBER_YES = valuesYes

SKILL_NAME = "SKILL_NAME"
MORSE_CODE = "MORSE_CODE"
GET_AFFIRMATION_MESSAGE = ["That is a very good choice. I am ready, if you are",
                           "I could not have picked a better one. I am ready, if you are",
                           "What a good choice. I am ready, if you are",
                           "Alright, lets get started. I am ready, if you are",
                           "Here we go. I am ready, if you are",
                           "Alright, alright, alright. I am ready, if you are",
                           "Settle in. I am ready, if you are",
                           "Cozy up. I am ready, if you are"]

GET_AFFIRMATION_MESSAGE_MORSE = "Sure, tell me up to two words you want me to translate"
HELP_MESSAGE = "I can switch light on and off. Just say: light switch on or off. I can also translate morse code. Just say: text and your text to translate"
HELP_REPROMPT = "What can I help you with?"
FALLBACK_MESSAGE = "The Morse Skill can't help you with that. It can help you with telling stories."
FALLBACK_REPROMPT = "What can I help you with?"
ERROR_MESSAGE = "Something went wrong, I am sorry"
MORE_STORY = ["..Should I keep going?", "I have some more facts fore you, should I continue?", "I know some more interesting tidbits, should I continue?", "I can do more, shall i continue? ", "Some more facts?"]
STOP_MESSAGE = ["I could keep going, but fine. Bye", "OK, bye", "Good bye", "Okeydokey", "It was fun, good bye"]
GET_STORY = ["Morse code is a method used in telecommunication to encode text characters as standardited sequences.",
             "Morse signals are called dots and dashes. Morse code is named for Samuel Morse, an inventor of the telegraph.",
             "The international Morse Code encodes the 26 English letters A through Z and some non-English letters.",
             "The morse code has distinction between upper and lower case letters in morse code.",
             "The duration of a dash is three times the duration of a dot. Each dot or dash within a character is followed by period of signal absence, called space, equal to the dot duration."
             ]