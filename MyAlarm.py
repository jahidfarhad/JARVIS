import datetime
import time
import winsound
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def alarm(set_time):
    alarm_time = datetime.datetime.strptime(set_time, '%I:%M %p')
    print(f"Done, alarm is set for {set_time}")
    speak(f"Done, alarm is set for {set_time}")
    duration = 15
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=duration)
    while datetime.datetime.now() < end_time:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time.time():
            print("Alarm is running")
            winsound.PlaySound('abc', winsound.SND_LOOP)

        time.sleep(1)


if __name__ == '__main__':
    alarm('10:38 PM')
