import tkinter as tk
from time import strftime




def set_custom_time():
    global custom_time
    input_time = entry.get()
    
    if validate_input(input_time):
        custom_time = input_time
        entry.delete(0, tk.END)
        time()
    else:
        error_label.config(text="Invalid input. Please use HH:MM format.", fg="red")

def validate_input(input_time):
    try:
        # Check if the input can be converted to a valid time format
        valid_time = tk.StringVar()
        valid_time.set(input_time)
        entry.config(validate="key", validatecommand=(valid_time, '%P'))
        return True
    except tk.TclError:
        return False

def update_watch():
    time()
    root.after(1000, update_watch)

def time():
    current_time = custom_time if custom_time else strftime('%H:%M:%S %p')
    lbl.config(text=current_time)

    # Extract the hour part to check if it's daytime or nighttime
    current_hour = int(current_time.split(':')[0])

    # Define a list of colors to cycle through
    all_colors = ['lightblue', 'lightgreen', 'lightyellow', 'black', 'darkblue', 'darkpurple']

    # Use a modulo operation to cycle through the list of colors
    color_index = current_hour % len(all_colors)

    # Set the background and foreground colors based on the time of day
    lbl.config(background=all_colors[color_index], foreground='black' if 6 <= current_hour < 18 else 'white')

root = tk.Tk()
root.title("Digital Watch")

custom_time = None

entry = tk.Entry(root, font=('calibri', 20))
entry.pack(pady=10)

set_button = tk.Button(root, text="Set Custom Time", command=set_custom_time)
set_button.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')

update_watch()
root.mainloop()