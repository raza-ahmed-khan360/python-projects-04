import time

def countdown_timer(seconds):
    while seconds:
        minutes, secs = divmod(seconds, 60)
        timer = f"{minutes:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!         ")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid integer.")