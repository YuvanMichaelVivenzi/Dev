import tkinter as tk

def click_button(char):
    # Update the display with the clicked button's value
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def calculate_result():
    try:
        # Calculate the result of the expression in the display
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        # Handle any errors (like division by zero)
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear_entry():
    # Clear the display
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#F8F8FF")

# Entry widget for displaying calculations and results
entry = tk.Entry(root, width=40, borderwidth=5, font=("Helvetica", 16), bg="#FFFFFF", relief='flat', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="news")

# Define buttons for digits 0-9
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Layout the buttons in a grid
row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=15, font=("Helvetica", 14), bg="#E0E0E0", borderwidth=0, relief='flat',
                     command=lambda b=button: click_button(b) if b != '=' else calculate_result(),
                     activebackground="#D0D0D0")
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="news")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button to clear the display
clear_btn = tk.Button(root, text="Clear", padx=16.5, pady=15, font=("Helvetica", 14), bg="#E0E0E0", borderwidth=0, relief='flat',
                       activebackground="#D0D0D0",
                       command=clear_entry)
clear_btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="news")

# Configure grid to make buttons resize nicely
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.grid_rowconfigure(0, weight=0)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
