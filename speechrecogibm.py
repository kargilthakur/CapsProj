# Required libraries - SpeechRecognition
# pip install SpeechRecognition

import speech_recognition as sr
print(sr.__version__)
audio_file = sr.AudioFile("record.wav")
r = sr.Recognizer()
with audio_file as source:
    audio = r.record(source)
# recognized_speech_ibm = r.recognize_ibm(clean_audio, username="apkikey", password= "your API Key")
print(type(audio))
recognized_speech_ibm = r.recognize_ibm(audio, username="https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/c1300a63-e564-4df8-b0c1-fe9b3a03d1ea", password = "0BkL3RR1nfdbFz6r5MtZMBbHfeChFNcN0HwWk099iT0N")
