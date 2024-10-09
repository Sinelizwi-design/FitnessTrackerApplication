import tkinter as tk
from tkinter import messagebox

# Unified function to handle saving fitness data
def save_fitness_data(data):
    try:
        with open('FitnessData.txt', 'a') as file:
            file.write(f"{data}\n")
    except Exception as e:
        print(f"Failed to save data: {e}")

def save_fitness_level(fitness_level):
    data = f"Fitness Level: {fitness_level}\n"  # Format for better readability
    save_fitness_data(data)

def open_workout_schedule(fitness_level):
    root.destroy()
    
    workout_window = tk.Tk()
    workout_window.title("Workout Schedule")
    workout_window.attributes('-fullscreen', True)
    workout_window.configure(bg="#f0f8ff")

    schedule_label = tk.Label(workout_window, text=f"Workout Schedule for {fitness_level}", 
                              font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#4682b4")
    schedule_label.pack(pady=30)

    info_label = tk.Label(workout_window, text="This is where the workout schedule will be displayed.", 
                          font=("Helvetica", 24), bg="#f0f8ff", fg="#000000")
    info_label.pack(pady=20)

    back_button = tk.Button(workout_window, text="Back", font=("Helvetica", 18), bg="#4682b4", fg="white", command=workout_window.destroy)
    back_button.pack(pady=20)

    workout_window.mainloop()

def select_fitness_level(level):
    fitness_label.config(text="")
    save_fitness_level(level)  # Save the fitness level
    messagebox.showinfo("Success", f"Fitness Level '{level}' saved successfully!")  # Show success message
    open_workout_schedule(level)

def go_back():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("User Experience")
root.attributes('-fullscreen', True)
root.configure(bg="#f0f8ff")

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=50)

heading_label = tk.Label(frame, text="Select Your Workout Level", font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#4682b4")
heading_label.pack(pady=10)

beginner_button = tk.Button(frame, text="Beginner", font=("Helvetica", 18), bg="#7fff00", width=15, command=lambda: select_fitness_level("Beginner"))
beginner_button.pack(pady=20)

intermediate_button = tk.Button(frame, text="Intermediate", font=("Helvetica", 18), bg="#ff8c00", width=15, command=lambda: select_fitness_level("Intermediate"))
intermediate_button.pack(pady=20)

advanced_button = tk.Button(frame, text="Advanced", font=("Helvetica", 18), bg="#ff6347", width=15, command=lambda: select_fitness_level("Advanced"))
advanced_button.pack(pady=20)

fitness_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#f0f8ff", fg="#000000")
fitness_label.pack(pady=30)

back_button = tk.Button(root, text="Back", font=("Helvetica", 18), bg="#4682b4", fg="white", command=go_back)
back_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", go_back)

root.mainloop()
