import time

def simple_clock():
    running = True
    while running:
        current_time = time.strftime("%H:%M:%S")
        print(current_time, end='\r')  # Print time on the same line
        time.sleep(1)

        if KeyboardInterrupt:
            print("\nClock stopped.")
            running = False

if __name__ == "__main__":
    simple_clock()