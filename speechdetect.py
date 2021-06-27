import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

# sr.Microphone.list_microphone_names()    run this on interpreter it will give list of microphone then add device index in above line as below
#  mic = sr.Microphone(device_index=3)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source,phrase_time_limit=2)
    txt = r.recognize_google(audio)
    print(txt)
