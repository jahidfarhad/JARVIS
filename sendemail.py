import speech_recognition as sr
import smtplib
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=15, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def commandAgain():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=15, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.replace(" ", "")
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def emailSend():
    while True:
        speak("What is your message?")
        query = command().lower()
        message = query
        email = 'vicer3712@gmail.com'
        password = 'wpov owut lcxg csme'

        speak("Please say the receiver's email address")
        query2 = commandAgain()
        send_to_email = query2

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, send_to_email, message)
        server.quit()

        speak("Email has been sent. Do you want to send another email?")
        response = command().lower()
        if "yes" not in response:
            break
