import tkinter as tk
from tkinter import ttk, messagebox

def calculate_amount_by_distance(distance, unit):
    if unit == "km":
        return distance * 0.5
    else:
        return distance * 0.0005

def calculate_amount_by_time(time, unit):
    if unit == "hours":
        return time * 20
    else:
        return time * 0.3333

def apply_discount(amount, code):
    discounts = {"Tec5": 0.05, "Tec15": 0.15, "TecFirstTry": 0.50}
    return amount * (1 - discounts.get(code, 0))

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Travel Calculator")
        master.geometry("300x300")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.distance_frame = ttk.Frame(self.notebook)
        self.time_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.distance_frame, text="Distance")
        self.notebook.add(self.time_frame, text="Time")

        self.setup_distance_frame()
        self.setup_time_frame()

    def setup_distance_frame(self):
        ttk.Label(self.distance_frame, text="Distance:").grid(row=0, column=0, padx=5, pady=5)
        self.distance_entry = ttk.Entry(self.distance_frame)
        self.distance_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.distance_frame, text="Unit:").grid(row=1, column=0, padx=5, pady=5)
        self.distance_unit = ttk.Combobox(self.distance_frame, values=["km", "meters"])
        self.distance_unit.grid(row=1, column=1, padx=5, pady=5)
        self.distance_unit.set("km")

        ttk.Label(self.distance_frame, text="Discount Code:").grid(row=2, column=0, padx=5, pady=5)
        self.distance_discount = ttk.Entry(self.distance_frame)
        self.distance_discount.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.distance_frame, text="Calculate", command=self.calculate_distance).grid(row=3, column=0, columnspan=2, pady=10)

    def setup_time_frame(self):
        ttk.Label(self.time_frame, text="Time:").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.time_frame)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.time_frame, text="Unit:").grid(row=1, column=0, padx=5, pady=5)
        self.time_unit = ttk.Combobox(self.time_frame, values=["hours", "minutes"])
        self.time_unit.grid(row=1, column=1, padx=5, pady=5)
        self.time_unit.set("hours")

        ttk.Label(self.time_frame, text="Discount Code:").grid(row=2, column=0, padx=5, pady=5)
        self.time_discount = ttk.Entry(self.time_frame)
        self.time_discount.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.time_frame, text="Calculate", command=self.calculate_time).grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_distance(self):
        try:
            distance = float(self.distance_entry.get())
            unit = self.distance_unit.get()
            discount_code = self.distance_discount.get()

            amount = calculate_amount_by_distance(distance, unit)
            final_amount = apply_discount(amount, discount_code)

            messagebox.showinfo("Result", f"Calculated amount: {final_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def calculate_time(self):
        try:
            time = float(self.time_entry.get())
            unit = self.time_unit.get()
            discount_code = self.time_discount.get()

            amount = calculate_amount_by_time(time, unit)
            final_amount = apply_discount(amount, discount_code)

            messagebox.showinfo("Result", f"Calculated amount: {final_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()