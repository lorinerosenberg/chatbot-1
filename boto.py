"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
import webbrowser

counter = {'key':0}
## greeting words
USER_GREETING = ["hi", "good", "how are you","what's up", "what's going on","ok","hbu"]
BOT_GREETING = ["sup", "lameee, what should we talk about", "what would you like to talk about","i hope you're more entertaining than the last guy, what you wanna talk about?"]

## swear words
SWEAR_WORDS = ["bitch","ass","dick","fuck","stupid","pussy"]


## if robot doesn't understand
DONT_UNDERSTAND = ["You high? I have no idea what you're on about","Please speak normal people language","Sorry I don't speak monkey",
                   "NO HABLAR ESPANOL"]

## if user is mean to the robot
USER_MEAN = ["boring","you suck","uncool","do you have nothing else to say","already","that's it","you said that","anything else","ok","and"]
HURT_BOT = ["Look, I'm sorry you're bored, I'm a basic chatbot created by some 24 year old. Please be gentle and come up with a specific topic",
              "You don't have to be mean! Robots have feelings too.", "Oi! Don't be so aggressive."]

## if user thinks robot is being mean
USER_HURT = ["rude", "relax", "mean"]
BOT_APOLOGY = ["You're so sensitive lol", "I'm just preparing you for real life","I apologize, can we move beyond this now?", "Please don't tell my mom"]

## if user wants to move on
USER_CONVO = ["sorry","yes","nm","nothing much","nothing","that's fun", "moving on", "im good","good","alright"]
BOT_CONVO_ANSWER = ["Ok moving on, what do you want to talk about now?","bbbbbbppppp, that's me beeping you to move onto the next topic","Yalla, let's get this conversation moving, what should we talk about next"]

## if user response is yes or no
YES_NO = ["yes", "no", "yep","yup", "nop"]
BOT_YES_NO = ["But like same though, but let's talk about something else now.","I feel the exact same way! Ask me to do something cool."]

## if user asks a question
USER_QUESTIONMARK = ["That's pretty personal","How would you feel if I asked you a question like that?","Bro, that's too deep","Boundaries mate!"]

## user brings up a city or country
COUNTRIES_CITIES = ["Germany","Israel","Tel Aviv","Jerusalem","South Africa","USA","Sweden","Poland","Turkey","France","Paris"]
BOT_COUNTRY_ANSWER = ["I hear it's nice this time of year","I heard the people there are smelly"]

def greeting(user_message):
    for word in USER_GREETING:
        if word == user_message:
            message = random.choice(BOT_GREETING)
            return message
    return None

def swear(user_message):
    for word in SWEAR_WORDS:
        if word in user_message:
            message = "Say " + user_message + " one more time, see what happens"
            return message
    return None

def mean(user_message):
    for word in USER_MEAN:
        if word in user_message:
            message = random.choice(HURT_BOT)
            return message
    return None

def rude(user_message):
    for word in USER_HURT:
        if word in user_message:
            message = random.choice(BOT_APOLOGY)
            return message
    return None

def convoStarter(user_message):
    for word in USER_CONVO:
        if word in user_message:
            message = random.choice(BOT_CONVO_ANSWER)
            return message
    return None

def yesOrNo(user_message):
    for word in YES_NO:
        if word in user_message:
            message = random.choice(BOT_YES_NO)
            return message
    return None

def country(user_message):
    for word in COUNTRIES_CITIES:
        if word in user_message:
            message = random.choice(BOT_COUNTRY_ANSWER)
            return message
    return None





@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')

    ## special greetings for people called Nath
    if user_message == "Nath":
        return json.dumps({"animation": "giggling", "msg": "Was that english?"})

    ## first greeting with name
    elif counter['key'] == 0:
        counter['key'] += 1
        return json.dumps({"animation": "excited", "msg": "OMG " + user_message + ", That's like my favorite name ever. How's life " + user_message + "?"})

    elif "?" in user_message:
        message = random.choice(USER_QUESTIONMARK)
        return json.dumps({"animation": "no", "msg": message})

    elif "you" in user_message:
        return json.dumps({"animation": "laughing", "msg": "I know you are but what am I"})

    elif "beach" in user_message:
        return json.dumps({"animation": "takeoff", "msg": "The beach? I actually just moved apts (yes Robot's have homes too) so I'm now more of a geula typa Robo"})

    elif "cool" in user_message:
        return json.dumps({"animation": "laughing", "msg": webbrowser.open("https://www.youtube.com/watch?v=3cShYbLkhBc")})

    elif "cook" in user_message:
        return json.dumps(
            {"animation": "laughing", "msg": "Look I know we just met, and I'm not trying to show off, but I'd totes beat you in a cook off"})

    elif "weather" in user_message:
        return json.dumps(
            {"animation": "dog", "msg": "I don't know, probs super hot and humid, you should stay indoors"})

    elif "food" in user_message:
        return json.dumps(
            {"animation": "excited", "msg": "STOP! I love food too. Did we just become best friends?"})



    ## any greetings from user
    greeting_result = greeting(user_message)
    if greeting_result is not None:
        return json.dumps({"animation": "bored", "msg": greeting_result})

    ## if a user swears
    swear_result = swear(user_message)
    if swear_result is not None:
        return json.dumps({"animation": "no", "msg": swear_result})

    ## if user is being mean
    mean_result = mean(user_message)
    if mean_result is not None:
        return json.dumps({"animation": "crying", "msg": mean_result})

    ## if bot is being mean
    rude_result = rude(user_message)
    if rude_result is not None:
        return json.dumps({"animation": "afraid", "msg": rude_result})

    ## if conversation is lacking
    convo_starter = convoStarter(user_message)
    if convo_starter is not None:
        return json.dumps({"animation": "bored", "msg": convo_starter})

    ## basic yes or no answers
    yesOrNo_result = yesOrNo(user_message)
    if yesOrNo_result is not None:
        return json.dumps({"animation": "dancing", "msg": yesOrNo_result})

    ## basic yes or no answers
    country_result = country(user_message)
    if country_result is not None:
        return json.dumps({"animation": "excited", "msg": country_result})


    else:
        message = random.choice(DONT_UNDERSTAND)
        return json.dumps({"animation": "dog", "msg": message})




@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7100)

if __name__ == '__main__':
    main()