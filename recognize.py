import pyttsx3
import speech_recognition as sr
from ohbot import *

def recognize():
    
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 32504.85796527251
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as mic:
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()

    if text == "hello":
        say("Please talk now", "en")
        wait(1)
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 32504.85796527251
        recognizer.dynamic_energy_threshold = True
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(text)
            return text
