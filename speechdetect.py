
from tkinter.constants import N
import speech_recognition as sr
from tts import sayagain,NoInternet
r = sr.Recognizer()
mic = sr.Microphone()
r.dynamic_energy_threshold= False
r.energy_threshold = 400
# sr.Microphone.list_microphone_names()    run this on interpreter it will give list of microphone then add device index in above line as below
# mic = sr.Microphone(device_index=5)

def listening():
    txt = None
    l1 = ["withdrawal","Deposit","change pin","balance"]
    while txt  not in l1:
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  
                audio = r.listen(source,phrase_time_limit=2)
                txt = r.recognize_google(audio,language="en-IN")
                
        except sr.WaitTimeoutError as e:
            sayagain()
        except sr.UnknownValueError:
            sayagain()
        except sr.RequestError as e:
            NoInternet()      
            
    return txt

def mounty():
    txt = "gg"
    while not txt.isnumeric():
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  
                audio = r.listen(source,phrase_time_limit=2)
                txt = r.recognize_google(audio,language="en-IN")
                
        except sr.WaitTimeoutError as e:
            sayagain()
        except sr.UnknownValueError:
            sayagain()
        except sr.RequestError as e:
            NoInternet()       
            
    return txt
