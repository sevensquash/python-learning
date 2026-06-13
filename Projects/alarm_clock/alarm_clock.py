import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# import time 
# from datetime import datetime
# import pygame

# def set_alarm(alarm_time):
#     sound_effect = "python_learning/Projects/alarm_clock/sound_effect.mp3"
#     current_time = datetime.now()
#     print("current_time")
#     isrunning = True

#     while isrunning:
#         current_time = datetime.now()
#         print(f"current time: {current_time.strftime("%H:%M:%S")}")
#         if current_time >= alarm_time:
#             print("wake up!")
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_effect)
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 print("Music playing")
#                 time.sleep(1)
#             print("Finsihed")
#             isrunning = False

#         time.sleep(1)

# if __name__ == "__main__":
#     alarm_time = input("Set your alarm clock at(HH:MM:SS): ")
#     alarm_time = datetime.strptime(alarm_time, "%Y-%m-%d %H:%M")
#     set_alarm(alarm_time)

# Practice
import time 
from datetime import datetime 
from pygame import mixer

music_path = "python_learning/Projects/alarm_clock/sound_effect.mp3"

def alarm_clock(set_alarm):

    while True:
        # even zeros have to match so brutal!
        now =  datetime.now().strftime("%I:%M:%S %p")
        if now >= set_alarm:
            print("Wake up!")

            mixer.init()
            mixer.music.load(music_path)
            mixer.music.play()

            print("Alaram sound starts.")
            while mixer.music.get_busy():
                print(now)
                time.sleep(1)
            break
        print(now)
        time.sleep(1)


if __name__ == "__main__":
    now = datetime.now().strftime("%I:%M:%S %p")
    print(now)
    set_alarm = input("Set your alarm at:(HH:MM:SS AM/PM) ")
    print(set_alarm)
    alarm_clock(set_alarm)