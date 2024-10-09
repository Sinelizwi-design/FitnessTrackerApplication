import tkinter as tk
from tkinter import messagebox

# Unified function to handle saving fitness data
def save_fitness_data(data):
    try:
        with open('FitnessData.txt', 'a') as file:
            file.write(f"{data}\n")
    except Exception as e:
        print(f"Failed to save data: {e}")

# Function to handle saving fitness goal and focus areas
def save_fitness_goal_and_focus(goal, selected_focus_areas):
    if selected_focus_areas:
        data = f"Goal: {goal}\nFocus Areas: {', '.join(selected_focus_areas)}\n"  # Format for better readability
        save_fitness_data(data)
        messagebox.showinfo("Success", "Fitness goal and focus areas saved successfully!")

# Function to handle goal selection and navigate to focus area selection
def select_focus_area(goal):
    def save_focus():
        selected_focus_areas = [focus_var.get() for focus_var, checkbox in focus_checkboxes if checkbox.get() == 1]
        if selected_focus_areas:
            save_fitness_goal_and_focus(goal, selected_focus_areas)
            reset_to_goal_screen()
        else:
            messagebox.showwarning("Input Error", "Please select at least one focus area.")

    # Clear current window
    for widget in root.winfo_children():
        widget.destroy()

    # Show selected goal
    tk.Label(root, text=f"Selected Goal: {goal}", font=("Helvetica", 24, "bold"), fg="#333").pack(pady=20)

    # Focus area options (multiple selection with checkboxes)
    tk.Label(root, text="Select Your Focus Areas", font=("Helvetica", 20), fg="#444").pack(pady=10)

    focus_checkboxes = []
    focus_areas = ['Legs', 'Back', 'Shoulders', 'Arms', 'Abs', 'Butt', 'Chest', 'Full Body']

    for area in focus_areas:
        focus_var = tk.StringVar(value=area)
        checkbox = tk.IntVar()
        cb = tk.Checkbutton(root, text=area, variable=checkbox, font=("Helvetica", 18))
        cb.pack(anchor='w', padx=50, pady=5)
        focus_checkboxes.append((focus_var, checkbox))

    tk.Button(root, text="Save", command=save_focus, font=("Helvetica", 18), width=20, height=2, bg="#ff6f61", fg="white").pack(pady=20)
    tk.Button(root, text="Back", command=reset_to_goal_screen, font=("Helvetica", 18), width=20, height=2, bg="#ffa500", fg="white").pack()

# Function to display goal selection screen
def reset_to_goal_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Your Fitness Goal", font=("Helvetica", 28, "bold"), fg="#333").pack(pady=30)

    tk.Button(root, text="Weight Loss", command=lambda: select_focus_area("Weight Loss"), font=("Helvetica", 20), width=30, height=3, bg="#34c759", fg="white").pack(pady=15)
    tk.Button(root, text="Muscle Gain", command=lambda: select_focus_area("Muscle Gain"), font=("Helvetica", 20), width=30, height=3, bg="#5ac8fa", fg="white").pack(pady=15)
    tk.Button(root, text="Body Shape", command=lambda: select_focus_area("Body Shape"), font=("Helvetica", 20), width=30, height=3, bg="#ff3b30", fg="white").pack(pady=15)

# Main application window
root = tk.Tk()
root.title("Goal and Focus")
root.geometry("800x600")

reset_to_goal_screen()

root.mainloop()
