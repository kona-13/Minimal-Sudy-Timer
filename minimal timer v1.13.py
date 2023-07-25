#Smaller version of the timer with built in pomodoro timer for studying
__author__ = 'kona-13'

import time
import datetime
import winsound
import os


print("Minimal timer w/ pomodoro timer")
print("Slapped together by Steven (kona-13)")


#Big overhaul - trying to add more features to this!
def startup():
    print("1.) Start")
    print("2.) Start with pomodoro timer (45 mins)")
    print("3.) Start with pomodoro timer (50 mins)")
    print("4.) Exit")
    choice_input = input('>>')

    if choice_input == "1":
        while True:

            h = input("Enter the time in hours: ")
            m = input("Enter the time in minutes: ")
            s = input("Enter the time in seconds: ")
            countdown(int(h), int(m), int(s))
            total_s = 0

            if total_s == 0:
                repeat = input("Start again? y/n ")

                if repeat.lower() != "n":
                    startup()

                elif repeat.lower() != 'y':
                    print("Thanks for your time! (get it its a timer pun haha!)")
                    break
    elif choice_input == "2":
        fixed_time45()
        
    elif choice_input == "3":
        fixed_time50()
        
    elif choice_input == "4":
        exit()
    else:
        print("Invalid choice, try again.")
        startup()

def fixed_time45():
    while True:
        h = 0
        m = 45
        s = 0
        countdown(int(h), int(m), int(s))
        total_s = 0

        if total_s == 0:
            print("Break time:")
            h = 0
            m = 15
            s = 0

            countdown(int(h), int(m), int(s))


            fixed_time45()

def fixed_time50():
    while True:
        h = 0
        m = 50
        s = 0
        countdown(int(h), int(m), int(s))
        total_s = 0

        if total_s == 0:
            print("Break time:")
            h = 0
            m = 10
            s = 0

            countdown(int(h), int(m), int(s))

            fixed_time50()

def countdown(h, m, s):
    total_s = h * 3600 + m * 60 + s

    while total_s > 0:

        timer = datetime.timedelta(seconds = total_s)

        print(timer, end="\r")

        time.sleep(1)

        total_s -= 1

    while total_s == 0:
        print("Time is up!")
        sounds()
        total_s = -1

def sounds():
    ringtone_sound = 'ringtone.wav' #Default ringtone
    winsound.PlaySound(ringtone_sound, winsound.SND_FILENAME)

startup()
