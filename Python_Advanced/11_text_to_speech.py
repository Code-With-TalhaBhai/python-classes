import cowsay
import pyttsx3


engine = pyttsx3.init()
text = input("What you wanna say?")
cowsay.cow(text)

engine.say(text)
engine.runAndWait()



