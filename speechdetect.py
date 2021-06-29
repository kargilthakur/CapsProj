import speech_recognition as sr
from tts import corroption
r = sr.Recognizer()
mic = sr.Microphone()
r.dynamic_energy_threshold= False
r.energy_threshold = 400
# sr.Microphone.list_microphone_names()    run this on interpreter it will give list of microphone then add device index in above line as below
# mic = sr.Microphone(device_index=5)

def listening():
    txt = None
    
    while txt is None:
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  
                audio = r.listen(source,phrase_time_limit=4)
                txt = r.recognize_google(audio,language="en-IN")
                
        except sr.WaitTimeoutError as e:
            print("Timeout; {0}".format(e))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))        
            
    return txt


gg = listening()
print(gg)
