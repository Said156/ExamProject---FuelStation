import customtkinter as ctk

# Qiymətlər
fuel_prices = {"Petrol": 2.0, "Diesel": 1.8, "Gas": 1.2}
cafe_prices = {"Coffee ☕": 3.0, "Sandwich 🥪": 5.0, "Cake 🍰": 4.0, "Juice 🧃": 2.5}

def update_total(liters_var, liters_label, fuel_type, cafe_widgets, label_result):
    """Total qiyməti yeniləyir"""
    total = 0

    # Yanacaq
    liters = liters_var.get()
    liters_label.configure(text=f"{liters:.0f} Liters")
    fuel = fuel_type.get()
    if fuel in fuel_prices:
        total += liters * fuel_prices[fuel]

    # Mini Cafe
    for item, (chk_var, spin) in cafe_widgets.items():
        if chk_var.get() == 1:
            try:
                count = int(spin.get())
            except ValueError:
                count = 0
            total += count * cafe_prices[item]

    label_result.configure(text=f"Total Price: ${total:.2f}")