import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import MyAlarm
import sys
import cv2
import pyautogui
import wikipedia
import pywhatkit
from weather import get_temperature
from sendemail import emailsend
import os
from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_jarvisGUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Jarvis. What can I do for you?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskEcecution()

    def takecommand(self, timeout_limit=300):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        start_time = time.time()
        while True:
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")
                return query
            except Exception as e:
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
                    print("listening...")
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)

    def TaskExecution(self):
        pyautogui.press('esc')
        speak("Verification Successful")
        wish()
        while True:
            self.query = self.takecommand().lower()

            if 'alarm' in self.query:
                speak("please tell me the time to set alarm. For example, 5:30 AM")
                tt = self.takecommand()
                tt = tt.replace("", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)

            elif "what is the weather today" in self.query:
                get_temperature(place='Dhaka')

            elif "temperature" in self.query:
                get_temperature(place='Dhaka')

            elif "send email" in self.query:
                emailsend()

            elif "email" in self.query:
                emailsend()

            if 'open notepad' in self.query:
                npath = 'C:\\Windows\\notepad.exe'
                os.startfile(npath)

            elif 'open command prompt' in self.query:
                os.system('start cmd')

            elif 'open cmd' in self.query:
                os.system('start cmd')

            elif 'play music' in self.query:
                music_dir = 'E:\\Music\\Bangla'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            # elif 'wikipedia' in self.query:
            #     speak('Searching Wikipedia.....')
            #     query = query.replace('wikipedia', '')
            #     results = wikipedia.summary(query, sentences=2)
            #     speak('According to Wikipedia:')
            #     speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open('youtube.com')

            elif 'open facebook' in self.query:
                webbrowser.open('facebook.com')

            elif 'open gmail' in self.query:
                webbrowser.open('gmail.com')

            elif 'open google' in self.query:
                speak('What should I search?')
                cm = takecommand().lower()
                webbrowser.open(f'{cm}')

            # elif 'play song on youtube' in self.query:
            #     speak('What song should I play?')
            #     cm = takecommand().lower()
            #     pywhatkit.playonyt(cm)

            elif "close" in self.query:
                speak("Glad to be at your service. Closing the program. ")
                sys.exit()

            elif "no" in self.query:
                speak("Glad to be at your service. Going back to sleep. ")
                sys.exit()

            speak("Do you have any other work?")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisGUI()
        self.ui.setupUi(self)
        self.Ui.pushButton.clicked.connect(self.startTask)
        self.Ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/Programming/Python/Projects/JARVIS/Interface/pwuXrz.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()


# ===========================================================================================================================================#


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 2
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:

    ret, img = cam.read()

    converted_image = cv2.cvtColor(img,
                                   cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

        if (accuracy < 100):
            id = [id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            TaskExecution()
            cam.release()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
            speak("User authentication failed")
            break

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
