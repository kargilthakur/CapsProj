import pyttsx3
from beepy import beep  # pip install beepy
engine = pyttsx3.init()
# engine.setProperty('voice', 'english_rp+f4')
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.75)
engine.setProperty('hindi',b'\x05hi' )

def welcome():
    engine.say("WELCOME TO BANK OF INDIA")
    engine.runAndWait()
    
def enter_pin():
    engine.say("ENTER YOUR 4 DIGIT PIN")
    engine.runAndWait()

def incorrect_pin():
    engine.say("You have entered incorrect pin! TRY AGAIN")
    engine.runAndWait()

def Options():
    engine.say("say the option number after hearing beep")
    engine.say("say one for cash withdrawal")
    engine.say("say two for cash deposit")
    engine.say("say three for changing pin")
    engine.say("Say four for Balance Enquiry")
    engine.runAndWait()
    beep(sound=4)

def canform(a):
    a = a-1 
    li = ["transaction successful collect money from dispenser","transaction successful Your money is deposited","transaction successful Your PIN is changed","transaction successful Please collect enquiry receipt"]
    engine.say(li[a])
    engine.runAndWait()

def middle(k):
    k = k-1
    gg = [" please enter the amount to be withdrawn","place the cash in the deposit machine","Enter the new Pin","Your current balance is"]
    engine.say(gg[k])
    engine.runAndWait()
