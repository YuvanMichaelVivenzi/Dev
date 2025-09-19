import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to show expressions.
        self.expression = ""
        self.entry = tk.Entry(self.root, textvariable="", font="Arial 18", bd=0, bg="#eee", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)
        
        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.root, text=button, font="Arial 15", command=cmd, bd=0).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def click(self, item):
        if item == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif item == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            self.expression += str(item)
            self.entry.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
