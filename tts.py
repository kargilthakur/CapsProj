import pyttsx3

engine = pyttsx3.init()
# engine.setProperty('voice', 'english_rp+f4')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.75)
voices = engine.getProperty('voices')
#for voice in voices:
engine.setProperty('voice', voice_id)
engine.say("Hello, I am robot")
engine.runAndWait()
#9,22 31 37 43 64