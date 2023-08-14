import tkinter as tk
from tkinter import messagebox
from random import randint

# Generate a random number between 1 and 10
random_num: int = randint(1, 10)

chances = 3

def check_guess():
        global chances
        try:
            user_guess = int(entry.get())
        
            if user_guess == random_num:
                result_label.config(text=f"Congratulations! You guessed the correct number = {random_num}.")
                guess_button.config(state=tk.DISABLED) 
            elif user_guess < random_num:
                result_label.config(text="The number is higher")
            else:
                result_label.config(text="The number is lower")
                
            chances -= 1
            clues_label.config(text=f"Chances remaining: {chances}")

            if chances == 0:
                if user_guess == random_num:
                    result_label.config(text=f"Congratulations! You guessed the correct number -> {random_num}.")
                    guess_button.config(state=tk.DISABLED)
                else:
                    result_label.config(text=f"Out of chances. The number was {random_num}.")
                    guess_button.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# Create the main application window
app = tk.Tk()
app.title("Guess the Number")

# Create UI elements
title_label = tk.Label(app, text="Guess the number in the range from 1 to 10.", font=("Helvetica", 16))
instruction_label = tk.Label(app, text="Enter your guess (1-10):")
# cl = tk.Label(app, text=f"Chances remaining: {chances}")
entry = tk.Entry(app)
guess_button = tk.Button(app, text="Guess", command=check_guess)
result_label = tk.Label(app, text="Chances remaining: 3")
clues_label = tk.Label(app, text="")

# Arrange UI elements using grid layout
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
instruction_label.grid(row=1, column=0, padx=10, pady=5)
# cl.grid(row=2, column=0, padx=10, pady=5)
entry.grid(row=1, column=1, padx=10, pady=5)
guess_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
clues_label.grid(row=1, column=1, padx=10, pady=5, rowspan=3)
# to use 'enter' in keyboard
app.bind("<Return>", lambda event: check_guess())


# Start the main event loop
app.mainloop()
