import requests
from bs4 import BeautifulSoup
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_temperature(place):
    while True:
        search = f"temperature in {place} today"
        r = requests.get(f"https://www.google.com/search?q={search}", verify=False)

        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current {search} is {temp}")
        print(f"current {search} is {temp}")
        break
