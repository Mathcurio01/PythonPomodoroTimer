import time
import sys

def pomodoro_timer(work_duration, break_duration):
    print("Start working!")
    countdown(work_duration * 60)

    print(f"Take a break for {break_duration} minutes.")
    countdown(break_duration * 60)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

work_duration = 25  # 25 minutes of work
break_duration = 5   # 5 minutes break

pomodoro_timer(work_duration, break_duration)