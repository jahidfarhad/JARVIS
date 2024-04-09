import pyttsx3
import speech_recognition as sr
import sys
from weather import get_temperature
from sendemail import emailSend
import time
import cv2
import pyautogui
import wikipedia
import pywhatkit
import os
import random
import webbrowser
import datetime
import MyAlarm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand(timeout_limit=200):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8, phrase_time_limit=7)
    start_time = time.time()
    while True:
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            return query
        except Exception:
            pass
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout_limit:
            print("Timeout limit reached. Exiting...")
            speak("Timeout limit reached. Exiting...")
            return "none"
        else:
            print("No input received. Please give an order...")
            speak("No input received. Please give an order...")
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=8, phrase_time_limit=7)


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 < hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. What can I do for you?")


def TaskExecution():
    # pyautogui.press('esc')
    # speak("Verification Successful")
    wish()
    while True:
        query = takeCommand().lower()

        if 'alarm' in query:
            speak("Please tell me the time to set alarm. For example, 5:30 AM")
            tt = takeCommand()
            tt = tt.replace("", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            MyAlarm.alarm(tt)

        elif 'weather' in query:
            get_temperature(place='Dhaka')

        elif 'temperature' in query:
            get_temperature(place='Dhaka')

        elif 'send email' in query:
            emailSend()

        if 'open notepad' in query:
            path = 'C:\\Windows\\notepad.exe'
            os.startfile(path)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open cmd' in query:
            os.system('start cmd')

        elif 'play music' in query:
            music_dir = 'E:\\Music\\The Weeknd'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'open google' in query:
            speak('What should I search?')
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia:')
            speak(results)

        elif 'play song on youtube' in query:
            speak('What song should I play?')
            cm = takeCommand().lower()
            pywhatkit.playonyt(cm)

        elif 'close' in query:
            speak("Glad to be at your service...")
            sys.exit()

        elif 'no' in query:
            speak("Glad to be at your service...")
            sys.exit()

        elif 'exit' in query:
            speak("Glad to be at your service...")
            sys.exit()

        speak("Do you have any other work?")


TaskExecution()

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer/trainer.yml')
# cascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascadePath)
#
# font = cv2.FONT_HERSHEY_SIMPLEX
#
# id = 2
# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cam.set(3, 640)
# cam.set(4, 480)
#
# minW = 0.1 * cam.get(3)
# minH = 0.1 * cam.get(4)
#
# while True:
#
#     ret, img = cam.read()
#
#     converted_image = cv2.cvtColor(img,
#                                    cv2.COLOR_BGR2GRAY)
#
#     faces = faceCascade.detectMultiScale(
#         converted_image,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(int(minW), int(minH)),
#     )
#
#     for (x, y, w, h) in faces:
#
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])
#
#         if accuracy < 100:
#             id = [id]
#             accuracy = "  {0}%".format(round(100 - accuracy))
#             TaskExecution()
#             cam.release()
#
#         else:
#             id = "unknown"
#             accuracy = "  {0}%".format(round(100 - accuracy))
#             speak("User authentication failed")
#             break
#
#         cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#         cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
#
#     cv2.imshow('camera', img)
#
#     k = cv2.waitKey(1) & 0xff
#     if k == 27:
#         break
#
# print("Thanks for using this program, have a good day.")
# cam.release()
# cv2.destroyAllWindows()
