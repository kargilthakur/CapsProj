# Required libraries - SpeechRecognition
# pip install SpeechRecognition

import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
print(sr.__version__)
audio_file = sr.AudioFile("audiosamples/12000amount.wav")
r = sr.Recognizer()
with audio_file as source:
    audio = r.record(source)
# recognized_speech_ibm = r.recognize_ibm(clean_audio, username="apkikey", password= "your API Key")
print(type(audio))
recognized_speech_google = r.recognize_google(audio)
print(recognized_speech_google)
print(type(recognized_speech_google))
engine.say(recognized_speech_google)
engine.runAndWait()
