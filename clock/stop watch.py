import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped. Elapsed time: {:.2f} seconds.".format(self.elapsed_time))

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset.")

if __name__ == "__main__":
    stopwatch = Stopwatch()

    while True:
        print("\nStopwatch Menu:")
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            stopwatch.start()
        elif choice == '2':
            stopwatch.stop()
        elif choice == '3':
            stopwatch.reset()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")