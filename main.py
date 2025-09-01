
import customtkinter as ctk
from functions import fuel_prices, cafe_prices, hesabla_yanacaq, hesabla_cafe, yekun_hesabla

# Əsas Pəncərə
app = ctk.CTk()
app.title("⛽ Fuel Station & ☕ Mini Cafe")
app.geometry("650x450")
app.resizable(False, False)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Yanacaq Frame
frame_fuel = ctk.CTkFrame(app, corner_radius=12)
frame_fuel.grid(row=0, column=0, padx=15, pady=15, sticky="n")

label_fuel = ctk.CTkLabel(frame_fuel, text="⛽ Yanacaq Seçimi", font=("Arial", 16, "bold"))
label_fuel.pack(pady=(10, 5))

fuel_var = ctk.StringVar(value="Petrol")
fuel_menu = ctk.CTkOptionMenu(frame_fuel, values=list(fuel_prices.keys()), variable=fuel_var, width=180)
fuel_menu.pack(pady=5)

label_litr = ctk.CTkLabel(frame_fuel, text="Litrlə daxil edin:", font=("Arial", 13))
label_litr.pack()

entry_litr = ctk.CTkEntry(frame_fuel, placeholder_text="Miqdar (L)", width=150)
entry_litr.pack(pady=5)

fuel_result = ctk.CTkLabel(frame_fuel, text="Qiymət: 0 AZN", font=("Arial", 14, "bold"))
fuel_result.pack(pady=5)

btn_calc_fuel = ctk.CTkButton(frame_fuel, text="Hesabla", width=150,
    command=lambda: hesabla_yanacaq(entry_litr, fuel_var, fuel_result))
btn_calc_fuel.pack(pady=(5, 10))

# Kafe Frame
frame_cafe = ctk.CTkFrame(app, corner_radius=12)
frame_cafe.grid(row=0, column=1, padx=15, pady=15, sticky="n")

label_cafe = ctk.CTkLabel(frame_cafe, text="☕ Mini Cafe", font=("Arial", 16, "bold"))
label_cafe.pack(pady=(10, 5))

cafe_entries = {}
for item, price in cafe_prices.items():
    row = ctk.CTkFrame(frame_cafe)
    row.pack(fill="x", pady=3, padx=10)
    
    lbl = ctk.CTkLabel(row, text=f"{item} - {price:.2f} AZN", font=("Arial", 13))
    lbl.pack(side="left")
    
    ent = ctk.CTkEntry(row, placeholder_text="0", width=50)
    ent.pack(side="right")
    
    cafe_entries[item] = (ent, price)

cafe_result = ctk.CTkLabel(frame_cafe, text="Ümumi: 0 AZN", font=("Arial", 14, "bold"))
cafe_result.pack(pady=5)

btn_calc_cafe = ctk.CTkButton(frame_cafe, text="Hesabla", width=150,
    command=lambda: hesabla_cafe(cafe_entries, cafe_result))
btn_calc_cafe.pack(pady=(5, 10))

# Yekun Frame
frame_total = ctk.CTkFrame(app, corner_radius=12)
frame_total.grid(row=1, column=0, columnspan=2, pady=15)

label_total = ctk.CTkLabel(frame_total, text="💰 Yekun Ödəniş", font=("Arial", 18, "bold"))
label_total.pack(pady=(10, 5))

final_result = ctk.CTkLabel(frame_total, text="0 AZN", font=("Arial", 20, "bold"), text_color="yellow")
final_result.pack()

btn_total = ctk.CTkButton(frame_total, text="Yekun Hesabla", width=200, height=35,
    command=lambda: yekun_hesabla(entry_litr, fuel_var, cafe_entries, final_result))
btn_total.pack(pady=(10, 15))

app.mainloop()