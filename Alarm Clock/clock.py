from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    elapsed_time = 0

    print(CLEAR)
    while elapsed_time < seconds:
        time.sleep(1)
        elapsed_time += 1

        time_left = seconds - elapsed_time
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")


minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
