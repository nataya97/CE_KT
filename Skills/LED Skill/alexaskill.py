import logging
import os
import subprocess

from date_skill import demo
from datetime import datetime

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

#launch ALEXA
@ask.launch
def launch():
    speech_text = 'Hi! What can I do for you today?'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('TimeIntent')
def time_intent():
    demo()
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    
    return statement('The time and date is ' + dt_string)

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can switch light on or you could switch it off!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
    
if __name__ == "__main__":
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
