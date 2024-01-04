import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    
    start_time = time.time()
    
    elapsed_time = 0

    for _ in range(10000):  # Adjust the range based on your desired maximum iterations
        user_input = input("Press 's' to stop the stopwatch: ")

        if user_input.lower() == 's':
            break
        else:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)

    print("\nStopwatch stopped.")
    print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()