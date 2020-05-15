import logging
import os
import prompts
import json
import random

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'You called for a story? Do you want to start one?'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('Amazon.StopIntent')
def noIntent():
    speech_text = 'Well then.... bye?'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('StartStoryIntent')
def startStoryIntent():
    speech_text = 'Sure, let us start a story. What genre would you like?'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GenreIntent', mapping =  {'genre':'genre'})
def genreIntent(genre):
    if genre in prompts.GENRES:
        speech_text = prompts.GET_AFFIRMATION_MESSAGE[prompts.RANDOM_NUMBER]
        return question(speech_text).reprompt(speech_text).simple_card(speech_text)
    speech_text = "I'm sorry that is not a valid genre. Please try again." + " " + str(genre)
   
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('ReadingIntent')
def readingIntent():
    speech_text = prompts.GET_STORY[prompts.RANDOM_NUMBER]
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

#continueIntent
#repeatIntent
#switchGenreIntent
    
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)