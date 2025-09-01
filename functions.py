
from tkinter import messagebox

# Qiymətlər
fuel_prices = {"Petrol": 2.0, "Diesel": 1.8, "Gas": 1.2}
cafe_prices = {"Coffee ☕": 3.0, "Sandwich 🥪": 5.0, "Cake 🍰": 4.0, "Juice 🧃": 2.5}

def hesabla_yanacaq(entry_litr, fuel_var, fuel_result):
    try:
        litr = float(entry_litr.get())
        secilmis = fuel_var.get()
        total = litr * fuel_prices[secilmis]
        fuel_result.configure(text=f"Qiymət: {total:.2f} AZN")
    except ValueError:
        messagebox.showerror("Xəta", "Zəhmət olmasa düzgün litr daxil edin!")

def hesabla_cafe(cafe_entries, cafe_result):
    total = 0
    for item, (ent, price) in cafe_entries.items():
        try:
            miqdar = int(ent.get()) if ent.get() else 0
            total += miqdar * price
        except ValueError:
            messagebox.showerror("Xəta", f"{item} üçün düzgün rəqəm daxil edin!")
            return
    cafe_result.configure(text=f"Ümumi: {total:.2f} AZN")

def yekun_hesabla(entry_litr, fuel_var, cafe_entries, final_result):
    try:
        litr = float(entry_litr.get()) if entry_litr.get() else 0
        secilmis = fuel_var.get()
        total_fuel = litr * fuel_prices[secilmis]
    except ValueError:
        total_fuel = 0
    
    total_cafe = 0
    for item, (ent, price) in cafe_entries.items():
        try:
            miqdar = int(ent.get()) if ent.get() else 0
            total_cafe += miqdar * price
        except ValueError:
            pass
    
    yekun = total_fuel + total_cafe
    final_result.configure(text=f"{yekun:.2f} AZN")