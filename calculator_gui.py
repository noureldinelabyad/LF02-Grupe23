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
        master.title("Scouter Calculator")
        master.geometry("400x350")
        master.configure(bg='#b4cfd3')

        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('TFrame', background='#57b6d3')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 14))
        self.style.configure('TButton', font=('Arial', 14, 'bold'), background='#b4cfd3', foreground='black')
        self.style.map('TButton', background=[('active', '#4CAF50')])
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', padding=[10, 5], font=('Arial', 10, 'bold'))

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both", padx=20, pady=20)

        

        notebook_width = 360  # Width of the notebook
        notebook_height = 310  # Height of the notebook
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        position_top = int(screen_height / 2 - notebook_height / 2)
        position_right = int(screen_width / 2 - notebook_width / 2)
        master.geometry(f"{notebook_width}x{notebook_height}+{position_right}+{position_top}")


        self.distance_frame = ttk.Frame(self.notebook, padding=20)
        self.time_frame = ttk.Frame(self.notebook, padding=20)

        self.notebook.add(self.distance_frame, text="Distance")
        self.notebook.add(self.time_frame, text="Time")

        self.setup_distance_frame()
        self.setup_time_frame()

    def setup_distance_frame(self):
        ttk.Label(self.distance_frame, text="Distance:").grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.distance_entry = ttk.Entry(self.distance_frame, width=20, style='TEntry')
        self.distance_entry.grid(row=0, column=1, padx=5, pady=10)

        ttk.Label(self.distance_frame, text="Unit:").grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.distance_unit = ttk.Combobox(self.distance_frame, values=["km", "meters"], width=18, style='TCombobox')
        self.distance_unit.grid(row=1, column=1, padx=5, pady=10)
        self.distance_unit.set("km")

        ttk.Label(self.distance_frame, text="Discount Code:").grid(row=2, column=0, padx=5, pady=10, sticky='w')
        self.distance_discount = ttk.Entry(self.distance_frame, width=20, style='TEntry')
        self.distance_discount.grid(row=2, column=1, padx=5, pady=10)

        ttk.Button(self.distance_frame, text="Calculate", command=self.calculate_distance).grid(row=3, column=0, columnspan=2, pady=20)

    def setup_time_frame(self):
        ttk.Label(self.time_frame, text="Time:").grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.time_entry = ttk.Entry(self.time_frame, width=20, style='TEntry')
        self.time_entry.grid(row=0, column=1, padx=5, pady=10)

        ttk.Label(self.time_frame, text="Unit:").grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.time_unit = ttk.Combobox(self.time_frame, values=["hours", "minutes"], width=18, style='TCombobox')
        self.time_unit.grid(row=1, column=1, padx=5, pady=10)
        self.time_unit.set("hours")

        ttk.Label(self.time_frame, text="Discount Code:").grid(row=2, column=0, padx=5, pady=10, sticky='w')
        self.time_discount = ttk.Entry(self.time_frame, width=20, style='TEntry')
        self.time_discount.grid(row=2, column=1, padx=5, pady=10)

        ttk.Button(self.time_frame, text="Calculate", command=self.calculate_time).grid(row=3, column=0, columnspan=2, pady=20)

    def calculate_distance(self):
        try:
            distance = float(self.distance_entry.get())
            unit = self.distance_unit.get()
            discount_code = self.distance_discount.get()

            amount = calculate_amount_by_distance(distance, unit)
            final_amount = apply_discount(amount, discount_code)

            messagebox.showinfo("Result", f"Calculated amount: €{final_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def calculate_time(self):
        try:
            time = float(self.time_entry.get().replace(',', '.'))
            unit = self.time_unit.get()
            discount_code = self.time_discount.get()

            amount = calculate_amount_by_time(time, unit)
            final_amount = apply_discount(amount, discount_code)

            messagebox.showinfo("Result", f"Calculated amount: €{final_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()