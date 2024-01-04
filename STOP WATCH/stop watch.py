import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    
    start_time = time.time()
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass  # Stop the stopwatch when the user presses Ctrl+C

    print("\nStopwatch stopped.")
    print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()