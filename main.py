import customtkinter as ctk
from functions import fuel_prices, cafe_prices, update_total

# --- Əsas Pəncərə ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("⛽ Fuel Station & Mini Cafe ☕")
root.geometry("520x650")
root.resizable(False, False)

# --- Header ---
header = ctk.CTkFrame(root, height=80, fg_color="#2ECC71", corner_radius=20)
header.pack(fill="x", pady=10, padx=10)
title = ctk.CTkLabel(header, text="⛽ Fuel Station & Mini Cafe ☕",
                     font=("Arial Rounded MT Bold", 24), text_color="white")
title.place(relx=0.5, rely=0.5, anchor="center")

# --- Content ---
content = ctk.CTkFrame(root, corner_radius=15, fg_color="#34495E")
content.pack(fill="both", expand=True, padx=15, pady=10)

# --- Fuel Station Frame ---
fuel_frame = ctk.CTkFrame(content, corner_radius=15, fg_color="#1ABC9C")
fuel_frame.pack(fill="x", padx=15, pady=10)

ctk.CTkLabel(fuel_frame, text="Fuel Station", font=("Arial", 16, "bold")).pack(anchor="w", padx=10, pady=(10,5))

fuel_type = ctk.StringVar(value="Petrol")
combo_fuel = ctk.CTkComboBox(fuel_frame, values=list(fuel_prices.keys()), variable=fuel_type, width=180)
combo_fuel.pack(padx=10, pady=5)

ctk.CTkLabel(fuel_frame, text="Liters:", font=("Arial", 12)).pack(anchor="w", padx=10)
liters_var = ctk.DoubleVar(value=0)
slider = ctk.CTkSlider(fuel_frame, from_=0, to=100, variable=liters_var, number_of_steps=100)
slider.pack(pady=5, padx=10, fill="x")

liters_label = ctk.CTkLabel(fuel_frame, text="0 Liters", font=("Arial", 12))
liters_label.pack(anchor="w", padx=10, pady=(0,10))

# --- Mini Cafe Frame ---
cafe_frame = ctk.CTkFrame(content, corner_radius=15, fg_color="#E67E22")
cafe_frame.pack(fill="x", padx=15, pady=10)

ctk.CTkLabel(cafe_frame, text="Mini Cafe", font=("Arial", 16, "bold")).pack(anchor="w", padx=10, pady=(10,5))

cafe_widgets = {}
for item in cafe_prices.keys():
    row = ctk.CTkFrame(cafe_frame, fg_color="#F39C12", corner_radius=10)
    row.pack(fill="x", padx=10, pady=5)

    chk_var = ctk.IntVar(value=0)
    chk = ctk.CTkCheckBox(row, text=item, variable=chk_var)
    chk.pack(side="left", padx=10, pady=5)

    spin = ctk.CTkEntry(row, width=50)
    spin.insert(0, "0")
    spin.pack(side="right", padx=10, pady=5)

    cafe_widgets[item] = (chk_var, spin)

# --- Result Frame ---
result_frame = ctk.CTkFrame(root, corner_radius=15, fg_color="#3498DB")
result_frame.pack(fill="x", padx=15, pady=15)

label_result = ctk.CTkLabel(result_frame, text="Total Price: $0.00", font=("Arial", 20, "bold"))
label_result.pack(pady=15)

# --- Trace və Bind ---
liters_var.trace("w", lambda *args: update_total(liters_var, liters_label, fuel_type, cafe_widgets, label_result))
fuel_type.trace("w", lambda *args: update_total(liters_var, liters_label, fuel_type, cafe_widgets, label_result))

for item, (chk_var, spin) in cafe_widgets.items():
    chk_var.trace("w", lambda *args, lv=liters_var, ll=liters_label, ft=fuel_type, cw=cafe_widgets, lr=label_result:
                  update_total(lv, ll, ft, cw, lr))
    spin.bind("<KeyRelease>", lambda e, lv=liters_var, ll=liters_label, ft=fuel_type, cw=cafe_widgets, lr=label_result:
              update_total(lv, ll, ft, cw, lr))

# --- İlk yeniləmə ---
update_total(liters_var, liters_label, fuel_type, cafe_widgets, label_result)

root.mainloop()