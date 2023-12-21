import time

def simple_clock():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(current_time, end='\r')  # Print time on the same line
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    simple_clock()