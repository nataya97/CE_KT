#alexaskill.py
import logging
import os
import prompts
import json
import random
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
import time
 
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

values = random.randint(0,4)

RANDOM_NUMBER = values
 
valuesNo = random.randint(0,4)

RANDOM_NUMBER_NO = valuesNo

#ALEXA start
@ask.launch
def launch():
    speech_text = 'Facts about the project'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

#ALXA Skills - Intents
@ask.intent('HelloWorldIntent')
def Facts_Intent():
        speech_text = 'HI! I will give you some facts about the project'
        return question(speech_text).reprompt(speech_text).simple_card(speech_text)
    
@ask.intent('myProjectInfo')
def Facts_Intent():
        speech_text = 'Your project deals with the development of Smart Speakers'
        return question(speech_text).reprompt(speech_text).simple_card(speech_text)
    
@ask.intent('getMembers')
def Facts_Intent(): 
        speech_text = 'the Members of the Project are Nour, natasha and Patrycja'
        return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('MoreInfo')
def Facts_Intent(): 
        speech_text = 'your project is based on Amazon Alex, you will develop skills and create  smart speaker using Raspberry pi '
        return question(speech_text).reprompt(speech_text).simple_card(speech_text)



@ask.intent('AnswerIntentYes')
def AnswerIntentYes():
    speech_text = prompts.GET_STORY[prompts.RANDOM_NUMBER_YES]
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('AnswerIntentNo')
def AnswerIntentNo():
    speech_text = prompts.STOP_MESSAGE[RANDOM_NUMBER_NO]
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('StartMorseIntent')
def MorseStartIntent():
    speech_text = prompts.GET_AFFIRMATION_MESSAGE_MORSE
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)
        
@ask.intent('MorseCodeIntent', mapping = {'morse':'morse','morse':'morse'})
def MorseIntent(morse):
    morse=morse.upper()
    code=textToMorse(morse)
    morseC(code)
    print(code + ' ' + morse)
    return statement('Have you seen it? It is easy! You can try other words. Just say: text and your word')

#DO NO DELETE
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = prompts.HELP_MESSAGE
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