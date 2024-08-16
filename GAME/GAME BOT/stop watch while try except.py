import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    
    start_time = time.time()
    
    elapsed_time = 0
    max_iterations = 10000  # Adjust the maximum number of iterations based on your preference
    iteration = 0

    while iteration < max_iterations:
        try:
            user_input = input("Press 's' to stop the stopwatch: ")

            if user_input.lower() == 's':
                break
            else:
                elapsed_time = time.time() - start_time
                print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
                time.sleep(0.1)

            iteration += 1
        except KeyboardInterrupt:
            print("\nStopwatch interrupted.")
            break

    print("\nStopwatch stopped.")
    print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()