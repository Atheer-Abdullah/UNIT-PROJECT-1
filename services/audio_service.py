# services/audio_service.py
import pyttsx3

def play_audio(text, speed=1):

    engine = pyttsx3.init()

    rate = int(170 * (1/speed))
    engine.setProperty("rate", rate)

    engine.say(text)

    engine.runAndWait()

    engine.stop()