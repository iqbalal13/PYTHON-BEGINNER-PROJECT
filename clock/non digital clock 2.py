import time

def simple_clock(duration_in_seconds):
    for _ in range(duration_in_seconds):
        current_time = time.localtime()
        hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

if __name__ == "__main__":
    try:
        duration = 10  # Set the duration of the clock in seconds
        simple_clock(duration)
    except KeyboardInterrupt:
        print("\nClock stopped.")