import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x600")

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "sqrt", "exp", "M+",
            "M-", "MR", "MC", "M"
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            if button in ["=", "C", "sqrt", "exp", "M+", "M-", "MR", "MC", "M"]:
                tk.Button(self, text=button, padx=20, pady=20, command=action, bg="lightblue").grid(row=row, column=col)
            else:
                tk.Button(self, text=button, padx=20, pady=20, command=action).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.memory = 0

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_display()
        elif char == "=":
            self.calculate_result()
        elif char == "sqrt":
            self.calculate_square_root()
        elif char == "exp":
            self.calculate_exponent()
        elif char == "M+":
            self.memory_add()
        elif char == "M-":
            self.memory_subtract()
        elif char == "MR":
            self.memory_recall()
        elif char == "MC":
            self.memory_clear()
        elif char == "M":
            self.memory_store()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.expression = ""
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
        self.update_display()

    def calculate_square_root(self):
        try:
            result = math.sqrt(float(self.expression))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for square root")
            self.expression = ""
        self.update_display()

    def calculate_exponent(self):
        try:
            base, exp = map(float, self.expression.split(","))
            result = math.pow(base, exp)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for exponentiation")
            self.expression = ""
        self.update_display()

    def memory_add(self):
        try:
            self.memory += float(self.expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for memory addition")
            self.expression = ""

    def memory_subtract(self):
        try:
            self.memory -= float(self.expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for memory subtraction")
            self.expression = ""

    def memory_recall(self):
        self.expression = str(self.memory)
        self.update_display()

    def memory_clear(self):
        self.memory = 0

    def memory_store(self):
        try:
            self.memory = float(self.expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for memory store")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
