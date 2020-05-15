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

STATUSON = ["on", "switch on", "enable", "power on", "activate", "turn on"] # all values that are defined as synonyms in type
STATUSOFF = ["off", "switch off", "disactivate", "turn off", "disable", "turn off"]


# Nachfolgend sind alle Morse-Zeichen in einem sog. Dictionary definiert
morseCode = {" ":"/","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
 "G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
 "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-",
 "W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---",
 "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..",
 "9":"----.",".":".-.-.-",",":"--..--",":":"---...",";":"-.-.-.","?":"..--..",
 "-":"-....-","(":"-.--.",")":"-.--.-","'":".----.","=":"-...-","+":".-.-.",
 "/":" ","@":".--.-."}

einh=0.080                   # Laenge einer Einheit in Sekunden
dit=einh*1                   # Das Dit ist eine Einheit lang
dah=einh*3                   # Ein Dah ist dreimal so lang wie ein Dit.
pSymbol=einh*1               # Die Pause zwischen zwei gesendeten Symbolen ist ein Dit lang.
pBuchst=einh*2               # Zwischen Buchstaben in einem Wort wird eine Pause von der 
                             # Laenge eines Dah (oder drei Dits) eingeschoben.
pWort=einh*6

led=24

status_=""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led ,GPIO.OUT)

def beep(t):                    # diese Zeile definiert eine Funktion
   GPIO.output(led, GPIO.HIGH)  # LED-Pin auf High (+3.3V) setzen = einschalten
   time.sleep (t)               # t Sekunden warten
   GPIO.output(led, GPIO.LOW)   # LED-Pin auf Low (0V) setzen = ausschalten
   
   
def morseC(symbols):
   for sym in symbols:          # For-Schleife: Gehe alle Zeichen in symbole durch
      if sym == ".":            # Die Einzelzeichen finden sich dann jeweil in sym
         beep (dit)
         time.sleep (pSymbol)          
      elif sym == "-":          # elif ist das Else If in Python 
         beep (dah)
         time.sleep (pSymbol)
      elif sym == " ":
         time.sleep (pBuchst)
      elif sym == "/":
         time.sleep (pWort)
         
def textToMorse(status):
   code = ""
   for bst in status:
      code+= morseCode[bst]+" " # "code += ..." bedeutet das Gleiche wie "code = code + ..."
   return code

@ask.launch
def launch():
    speech_text = 'What would you like to do? Switch light on or off? Or would you rather learn morse code?'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('FactsMorseIntent')
def Facts_Intent():
        speech_text = prompts.GET_STORY[RANDOM_NUMBER] + ' ..' + prompts.MORE_STORY[prompts.RANDOM_NUMBER_YES]
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
    
    
@ask.intent('MorseCodeIntent', mapping = {'morse':'morse', 'morse':'morse'})
def MorseIntent(morse):
    morse=morse.upper()
    code=textToMorse(morse)
    morseC(code)
    return statement('Have you seen it? It is easy! You can try another words. Just say: text and your word')

@ask.intent('LightIntent', mapping = {'status':'status'})
def Gpio_Intent(status):
    if status in STATUSON:
        GPIO.output(24, GPIO.HIGH)
        return statement('Light was turned on')
    elif status in STATUSOFF:
       GPIO.output(24,GPIO.LOW)
       return statement('Light was turned off')
    else:
        return statement('Sorry, this command is not possible!' + ' ' + status)


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