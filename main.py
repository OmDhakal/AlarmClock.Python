#Python Alarm Clock
import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm-clock-90867.mp3"
    is_alarm_ringing = True

    while is_alarm_ringing:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time) 

        if current_time == alarm_time:
            print("WAKE UP!")

            is_alarm_ringing = False

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()


            while pygame.mixer.music.get_busy():
                time.sleep(1)




        
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in (HH:MM:SS) format: ")
    set_alarm(alarm_time)
















