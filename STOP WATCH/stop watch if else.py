import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    
    start_time = time.time()
    
    running = True
    elapsed_time = 0

    while running:
        user_input = input("Press 's' to stop the stopwatch: ")

        if user_input.lower() == 's':
            running = False
        else:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)

    print("\nStopwatch stopped.")
    print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()