# main.pyw - MyMoney App Main Codes

import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import customtkinter as ctk
import json
import platform
import sys
import random
import subprocess
import webbrowser
from time import sleep
import shutil
from PIL import Image, ImageTk
import threading

"""
Notlar :
Analiz sonuçlarında filtre kısmına eklencekler :
- Kar Analiz
- Son 5 Veri Analizi
- Tarih Aralığı Analizi
- Son 2 Veri Analiz
"""

# Modules
import modules.create_files as create_files_module
import modules.getdata as getdata_module
import modules.user_currency_date as save_currency_saves
import modules.currency_updater_bot as currency_updater_bot
import modules.version_control as version_control_module

def app():
#-[LANGUAGE]------------------------------------------------------
    def LanguageSync(type="Main"):
        global lang_flag

        with open("app/settings.json", "r", encoding="utf-8") as f:
            configure = json.load(f)

        language = configure["language"]

        if language == "tr":
            lang_flag = "Turkish"
        elif language == "en":
            lang_flag = "English"
        else:
            lang_flag = "English"

        if type == "Main":
            if language == "tr":
                doviz_button.configure(text="Döviz")
                gelir_gider_button.configure(text="Para Kayıt")
                analiz_button.configure(text="Analiz")
                ayarlar_button.configure(text="Ayarlar")
                title_label.configure(text=f"Merhaba, {configure['user']['name']}")
                version_label.configure(text=f"Sürüm {configure['version']}")
            else:
                doviz_button.configure(text="Currency")
                gelir_gider_button.configure(text="Money Record")
                analiz_button.configure(text="Analysis")
                ayarlar_button.configure(text="Settings")
                title_label.configure(text=f"Hi, {configure['user']['name']}")
                version_label.configure(text=f"Version {configure['version']}")

        elif type == "Settings":
            if language == "tr":
                enter.configure(text="Kaydet")
                rename_button.configure(text="İsmi Değiştir")
                title_label_settings.configure(text="Ayarlar")
                version_label_settings.configure(text=f"Sürüm {configure['version']}")
                currency_label.configure(text="Para Birimi")
                theme_label.configure(text="Tema")
                language_label.configure(text="Dil")
                root_settings.title("MyMoney - Ayarlar")
                auto_refresh_box.configure(text="Oto Yenileme")
            else:
                enter.configure(text="Save")
                rename_button.configure(text="Change Name")
                title_label_settings.configure(text="Settings")
                version_label_settings.configure(text=f"Version {configure['version']}")
                currency_label.configure(text="Currency")
                theme_label.configure(text="Theme")
                language_label.configure(text="Language")
                root_settings.title("MyMoney - Settings")
                auto_refresh_box.configure(text="Auto Refresh")
        elif type == "Rename":
            if language == "tr":
                enter.configure(text="Giriş")
                title_label_rename.configure(text="İsmi Değiştir")
                name_label.configure(text="İsim")
                surname_label.configure(text="Soyisim")
                root_settings_rename.title("MyMoney - İsim Değiştir")

            else:
                root_settings_rename.title("MyMoney - Change Name")
                enter.configure(text="Enter")
                title_label_rename.configure(text="Change Name")
                name_label.configure(text="Name")
                surname_label.configure(text="Surname")
        elif type == "Doviz":
            if language == "tr":
                title_label_doviz.configure(text="Döviz")
                root_doviz.title("MyMoney - Döviz")
                reset.configure(text="YENİLE")
                hesapmakinesi.configure(text="HESAP MAKİNESİ")
            else:
                title_label_doviz.configure(text="Currency")
                root_doviz.title("MyMoney - Currency")
                reset.configure(text="RESET")
                hesapmakinesi.configure(text="CALCULATOR")
        elif type == "Calculator":
            if language == "tr":
                root_calc.title("Hesap Makinesi")
            else:
                root_calc.title("Calculator")
        elif type == "Gelir Gider":
            if language == "tr":
                root_gg.title("MyMoney - Para Kayıt")
                title_gg.configure(text="Para Kayıt")
                available_money.configure(placeholder_text="Para değer giriniz...")
                available_money_currency.set("Para Türü.")
                available_money_currency_to.set("Çevirilecek.")
                save_names_entry.configure(placeholder_text="Kayıt adını giriniz...")
                saves_save.configure(text="Kaydet")
                all_saves.configure(text="Tüm Kayıtlar")
                currency_update.configure(text="Kurları Güncelle")
            else:
                root_gg.title("MyMoney - Money Record")
                title_gg.configure(text="Money Record")
                available_money.configure(placeholder_text="Enter money value...")
                available_money_currency.set("Currency.")
                available_money_currency_to.set("To Convert.")
                save_names_entry.configure(placeholder_text="Enter save name...")
                saves_save.configure(text="Save")
                all_saves.configure(text="All Saves")
                currency_update.configure(text="Update Currency")
        elif type == "Tüm Kayıtlar":
            if language == "tr":
                root_oas.title("MyMoney - Tüm Para Kayıtları")
                title_oas.configure(text="Tüm Para Kayıtları")
                open_save.configure(text="Kayıdı Aç")
            else:
                root_oas.title("MyMoney - All Money Records")
                title_oas.configure(text="All Money Records")
                open_save.configure(text="Open Save")
        elif type == "Kayıt Detayları":
            if language == "tr":
                root_osd.title(f"MyMoney - Kayıt Detayları [{selected_save_file}]")
                title_osd.configure(text="Kayıt Detayları")
                delete_button.configure(text="Kayıdı Sil")
                reload_button.configure(text="Yenile")

                info_label.configure(text=f"Kayıt Adı : {selected_save_file}\n\nPara Türü : {data['currency']}\n\nÇevrilecek Para Türü : {data['to']}\n\nMevcut Para : {data['first_money']} {data['currency']}\n\nKayıt Tarihi : {data['first_import_date']}")

                note_label.configure(text="*Analiz için 'Ana Menü' alanından 'Analiz' sekmesine giriniz.")
            else:
                root_osd.title(f"MyMoney - Save Details [{selected_save_file}]")
                title_osd.configure(text="Save Details")
                delete_button.configure(text="Delete Save")
                reload_button.configure(text="Reload")
                info_label.configure(text=f"Save Name : {selected_save_file}\n\nCurrency : {data['currency']}\n\nCurrency To Convert : {data['to']}\n\nAvailable Money : {data['first_money']} {data['currency']}\n\nSave Date : {data['first_import_date']}")
                note_label.configure(text="*For analysis, go to the 'Analysis' section from the 'Main Menu' area.")
        
        elif type == "Analiz":
            if language == "tr":
                pass
            else:
                pass

        elif type == "Analiz Sonuçları":
            if language == "tr":
                pass
            else:
                pass

        else:
            pass
#---------------------------------------------------------------------
            
    def doviz_function():
        global root_doviz, title_label_doviz, currency_label_1, background_1, background_2, background_3, reset, hesapmakinesi, date_label

        def SyncCurrency():
            reset.configure(state="disabled")
            hesapmakinesi.configure(state="disabled")

            date_label.configure(text="Loading...")
            root.update()

            with open("app/settings.json", "r", encoding="utf-8") as f:
                configure = json.load(f)

            _currency = configure["currency"]

            if _currency == "TRY":
                try:
                    root.update()
                    title_1.configure(text="USD")
                    title_2.configure(text="EUR")
                    title_3.configure(text="GBP")

                    currency_label_1.configure(text=f"Loading...")
                    currency_label_2.configure(text=f"Loading...")
                    currency_label_3.configure(text=f"Loading...")

                    root.update()

                    root.update()
                    data_usdtotry = getdata_module.get_currency_data("USD=TRY")
                    currency_label_1.configure(text=f"1 USD\n{round(data_usdtotry, 2)} TRY")
                    root.update()
                    data_eurtotry = getdata_module.get_currency_data("EUR=TRY")
                    currency_label_2.configure(text=f"1 EUR\n{round(data_eurtotry, 2)} TRY")
                    root.update()
                    data_gbptotry = getdata_module.get_currency_data("GBP=TRY")
                    currency_label_3.configure(text=f"1 GBP\n{round(data_gbptotry, 2)} TRY")
                    root.update()
                    reset.configure(state="normal")
                    hesapmakinesi.configure(state="normal")

                except Exception as e:
                    root_doviz.attributes("-topmost",False)
                    reset.configure(state="normal")
                    hesapmakinesi.configure(state="normal")
                    messagebox.showerror("Currency Error",f"An error occurred while loading the exchange rate! Please try again. {e}")
                    currency_label_1.configure(text=f"NO DATA")
                    currency_label_2.configure(text=f"NO DATA")
                    currency_label_3.configure(text=f"NO DATA")

                    root_doviz.focus()

                    root.update()

            else:
                try:
                    root.update()
                    title_1.configure(text="TRY")
                    title_2.configure(text="EUR")
                    title_3.configure(text="GBP")

                    currency_label_1.configure(text=f"Loading...")
                    currency_label_2.configure(text=f"Loading...")
                    currency_label_3.configure(text=f"Loading...")

                    root.update()

                    root.update()
                    data_trytousd = getdata_module.get_currency_data(f"TRY=USD")
                    currency_label_1.configure(text=f"1 TRY\n{round(data_trytousd, 2)} USD")
                    root.update()
                    data_eurtousd = getdata_module.get_currency_data(f"EUR=USD")
                    currency_label_2.configure(text=f"1 EUR\n{round(data_eurtousd, 2)} USD")
                    root.update()
                    data_gbptousd = getdata_module.get_currency_data(f"GBP=USD")
                    currency_label_3.configure(text=f"1 GBP\n{round(data_gbptousd, 2)} USD")
                    root.update()
                    reset.configure(state="normal")
                    hesapmakinesi.configure(state="normal")

                except Exception as e:
                    reset.configure(state="normal")
                    hesapmakinesi.configure(state="normal")
                    messagebox.showerror("Currency Error","An error occurred while loading the exchange rate! Please try again.")

        def hesapmakinesi_function():
            global expression, root_calc

            root_calc = ctk.CTkToplevel()
            root_calc.title("Hesap Makinesi")
            root_calc.geometry("300x400")
            root_calc.resizable(False, False)

            expression = ""

            def button_click(value):
                global expression

                if value == "C":
                    expression = ""
                elif value == "=":
                    try:
                        expression = str(eval(expression))
                    except:
                        expression = "Hata"
                else:
                    expression += str(value)
                entry.delete(0, "end")
                entry.insert(0, expression)

            entry = ctk.CTkEntry(root_calc, justify="right", font=("Arial", 24), width=280)
            entry.pack(pady=10)

            frame = ctk.CTkFrame(root_calc)
            frame.pack(expand=True, fill="both")

            buttons = [
                ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
                ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
                ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
                ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
                ("=", 5, 0)
            ]

            for (text, row, col) in buttons:
                btn = ctk.CTkButton(frame, text=text, width=60, height=50,
                                    command=lambda t=text: button_click(t))
                btn.grid(row=row, column=col, padx=5, pady=5)

            LanguageSync("Calculator")

            root.mainloop()

        def time_date():
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            time = datetime.datetime.now().strftime("%H:%M:%S")

            if lang_flag == "Turkish":
                month_list_turkish = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
                text_date = f"{day} {month_list_turkish[month - 1]} - {time}"

                root.update()
                date_label.configure(text=text_date)
                root.update()

            elif lang_flag == "English":
                month_list_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                text_date = f"{day} {month_list_english[month - 1]} - {time}"

                root.update()
                date_label.configure(text=text_date)
                root.update()

            root_doviz.after(500, time_date)

        def auto_refresh_function_doviz():
            with open("app/settings.json","r",encoding="utf-8") as f:
                configure_doviz_auto_refresh = json.load(f)
            
            auto_refresh_flag = configure_doviz_auto_refresh["auto_refresh"]

            if bool(auto_refresh_flag) == True:
                root_doviz.update()
                SyncCurrency()
                root_doviz.update()
            else:
                pass

            root_doviz.after(120000, auto_refresh_function_doviz)

        with open("app/settings.json","r",encoding="utf-8") as f:
            name_config = json.load(f)

        name_surname = str(name_config["user"]["name"] +" "+ name_config["user"]["surname"])

        root_doviz = ctk.CTkToplevel()
        root_doviz.title("MyMoney - Currency")
        root_doviz.geometry("600x400")
        root_doviz.resizable(False, False)
        root_doviz.attributes("-topmost", True)

        x = (root_doviz.winfo_screenwidth() - 600) // 2
        y = (root_doviz.winfo_screenheight() - 500) // 2
        root_doviz.geometry(f"+{x}+{y}")

        title_label_doviz = ctk.CTkLabel(root_doviz, text="Currency", font=ctk.CTkFont(size=25, weight="bold"))
        title_label_doviz.pack(pady=10)

        background_1 = ctk.CTkFrame(root_doviz, width=140, height=160, fg_color="#1A1A1A")
        background_1.pack(pady=10)
        background_1.place(x=50, y=70)

        background_2 = ctk.CTkFrame(root_doviz, width=140, height=160, fg_color="#1A1A1A")
        background_2.pack(pady=10)
        background_2.place(x=220, y=70)

        background_3 = ctk.CTkFrame(root_doviz, width=140, height=160, fg_color="#1A1A1A")
        background_3.pack(pady=10)
        background_3.place(x=400, y=70)

        title_1 = ctk.CTkLabel(root_doviz, text="USD", font=ctk.CTkFont(size=20, weight="bold"), bg_color="#1A1A1A")
        title_1.pack()
        title_1.place(x=100, y=80)

        title_2 = ctk.CTkLabel(root_doviz, text="EUR", font=ctk.CTkFont(size=20, weight="bold"), bg_color="#1A1A1A")
        title_2.pack()
        title_2.place(x=270, y=80)

        title_3 = ctk.CTkLabel(root_doviz, text="GBP", font=ctk.CTkFont(size=20, weight="bold"), bg_color="#1A1A1A")
        title_3.pack()
        title_3.place(x=450, y=80)

        currency_label_1 = ctk.CTkLabel(root_doviz, text=f"No Data", font=ctk.CTkFont(size=18), bg_color="#1A1A1A")
        currency_label_1.pack()
        currency_label_1.place(x=80, y=140)

        currency_label_2 = ctk.CTkLabel(root_doviz, text=f"No Data", font=ctk.CTkFont(size=18), bg_color="#1A1A1A")
        currency_label_2.pack()
        currency_label_2.place(x=250, y=140)

        currency_label_3 = ctk.CTkLabel(root_doviz, text=f"No Data", font=ctk.CTkFont(size=18), bg_color="#1A1A1A")
        currency_label_3.pack()
        currency_label_3.place(x=430, y=140)

        with open("app/settings.json", "r",encoding="utf-8") as f:
            config = json.load(f)
        
        _theme = config["theme"]

        _system_data_theme = ctk.get_appearance_mode()

        if str(_theme) == "light" or str(_system_data_theme) == "Light":
            background_1.configure(fg_color="#D2D2D2")
            background_2.configure(fg_color="#D2D2D2")
            background_3.configure(fg_color="#D2D2D2")

            title_1.configure(bg_color="#D2D2D2")
            title_2.configure(fg_color="#D2D2D2")
            title_3.configure(fg_color="#D2D2D2")

            currency_label_1.configure(fg_color="#D2D2D2")
            currency_label_2.configure(fg_color="#D2D2D2")
            currency_label_3.configure(fg_color="#D2D2D2")

        reset = ctk.CTkButton(root_doviz, text="RESET", font=("century gothic",16,"bold"), command=SyncCurrency, fg_color="#ffb700", hover_color="#7e5b01")
        reset.pack()
        reset.place(x=220, y=250)
        reset.configure(state="normal")

        hesapmakinesi = ctk.CTkButton(root_doviz, text="HESAP MAKİNESİ", font=("century gothic",16,"bold"), command=hesapmakinesi_function)
        hesapmakinesi.pack()
        hesapmakinesi.place(x=220, y=310)
        hesapmakinesi.configure(state="normal")

        date_label = ctk.CTkLabel(root_doviz, text=f"Loading...", font=("century gothic",14,"bold"))
        date_label.pack()
        date_label.place(x=10, y=370)

        name_surname_label = ctk.CTkLabel(root_doviz, text=f"{name_surname}", font=("century gothic",15,"bold"))
        name_surname_label.pack()
        name_surname_label.place(x=440, y=370)

        LanguageSync("Doviz")
        SyncCurrency()

        time_date()

        auto_refresh_function_doviz()

        root_doviz.attributes("-topmost", True)
        root_doviz.focus()

        root_doviz.mainloop()
        
    def gelir_gider_function():
        global root_gg, title_gg, available_money, available_money_currency, available_money_currency_to, save_names_entry, saves_save, all_saves, currency_update, update_currency
        def open_all_saves():
            global root_oas, liste, open_save, money_data_list, root_osd, title_oas, open_save
            def load_saves_List():
                for i in os.listdir(os.path.abspath("app/saves")):
                    liste.insert(tk.END, f"{i}")
                    root_oas.update()

            def on_select_list(event=None):
                selection = liste.curselection()

                if selection:
                    open_save.configure(state="normal")
                else:
                    open_save.configure(state="disabled")

            def open_save_data():
                global selected_save_file, money_data_list, root_osd, delete_button, reload_button, note_label, title_osd, info_label, data
                def load_save_currency_data():
                    money_data_list.delete(0, tk.END)

                    save_path = os.path.abspath(f"app/saves/{selected_save_file}")
                    txt_files = []

                    for files in os.listdir(save_path):
                        if files.endswith(".txt"):
                            txt_files.append(files)

                    with open(f"app/saves/{selected_save_file}/{txt_files[0]}","r",encoding="utf-8") as f:
                        lines = f.readlines()

                        for line in lines:
                            money_data_list.insert(tk.END, line.strip())
                            root_osd.update()
                            money_data_list.yview(tk.END)
                            sleep(0.05)

                def delete_save():
                    root_osd.attributes("-topmost", False)
                    if messagebox.askyesno("Warning","Are you sure you want to delete this record? This action cannot be undone!"):
                        shutil.rmtree(f"app/saves/{selected_save_file}")
                        messagebox.showinfo("Successful","The record has been successfully deleted.")
                        root_osd.destroy()
                        root_oas.destroy()
                        root_gg.attributes("-topmost", True)
                    else:
                        pass

                secili_index = liste.curselection()
                selected_save_file = liste.get(secili_index[0])

                with open(f"app/saves/{selected_save_file}/data-info.json","r" ,encoding="utf-8") as f:
                    data = json.load(f)

                root_osd = ctk.CTkToplevel(root_gg)
                root_osd.title(f"MyMoney - Kayıt Detayları [{selected_save_file}]")
                root_osd.resizable(False, False)
                root_osd.geometry("650x400")
                root_oas.attributes("-topmost",False)
                root_osd.attributes("-topmost", True)

                x=(root.winfo_screenwidth() - 650) // 2
                y=(root.winfo_screenheight() - 400) // 2
                root_osd.geometry(f"+{x}+{y}")

                title_osd = ctk.CTkLabel(root_osd, text="Kayıt Detayları", font=ctk.CTkFont(size=25, weight="bold"))
                title_osd.pack(pady=10)

                info_label = ctk.CTkLabel(root_osd, text=f"Kayıt Adı : {selected_save_file}\n\nPara Türü : {data['currency']}\n\nÇevrilecek Para Türü : {data['to']}\n\nMevcut Para : {data['first_money']} {data['currency']}\n\nKayıt Tarihi : {data['first_import_date']}", font=("century gothic",16,"bold"), justify="left")
                info_label.pack()
                info_label.place(x=20, y=70)

                money_data_list = tk.Listbox(root_osd, width=29, height=13, border=0, justify="left", borderwidth=0,relief="flat",activestyle="none",  selectbackground="black",selectforeground="orange", font=("Century Gothic",12,"bold"))
                money_data_list.pack()
                money_data_list.place(x=360, y=50)

                load_save_currency_data()

                delete_button = ctk.CTkButton(root_osd, text="Kayıdı Sil", font=("century gothic",13,"bold"), command=delete_save, fg_color="#ff0000", hover_color="#7e0000")
                delete_button.pack()
                delete_button.place(x=100, y=280)

                reload_button = ctk.CTkButton(root_osd, text="Yenile", font=("century gothic",13,"bold"), command=load_save_currency_data)
                reload_button.pack()
                reload_button.place(x=100, y=320)

                note_label = ctk.CTkLabel(root_osd, text="*Analiz için 'Ana Menü' alanından 'Analiz' sekmesine giriniz.", font=("century gothic",13,"italic"))
                note_label.pack()
                note_label.place(x=20, y=370)

                LanguageSync("Kayıt Detayları")

                root_osd.mainloop()

            with open("app/settings.json")as f:
                config = json.load(f)

            root_oas = ctk.CTkToplevel()
            root_oas.title("MyMoney - Tüm Para Kayıtları")
            root_oas.resizable(False, False)
            root_oas.attributes("-topmost", True)
            root_gg.attributes("-topmost",False)
            root_oas.geometry("400x500")

            x = (root.winfo_screenwidth() - 400) // 2
            y = (root.winfo_screenheight() - 500) // 2

            root_oas.geometry(f"+{x}+{y}")

            title_oas = ctk.CTkLabel(root_oas, text="Tüm Para Kayıtları", font=ctk.CTkFont(size=25, weight="bold"))
            title_oas.pack(pady=10)

            liste = tk.Listbox(root_oas, width=35, height=14, border=0, justify="center", borderwidth=0,relief="flat",activestyle="none",  selectbackground="black",selectforeground="orange", font=("Century Gothic",14,"bold"))
            liste.pack(pady=10)
            liste.bind("<<ListboxSelect>>", on_select_list)

            open_save = ctk.CTkButton(root_oas, text="Kayıdı Aç", font=("century gothic",17,"bold"), command=open_save_data)
            open_save.pack(pady=10)
            open_save.configure(state="disabled")

            load_saves_List()

            LanguageSync("Tüm Kayıtlar")

            root_oas.mainloop()

        def save():
            if available_money_currency.get().upper().strip() == "" or available_money_currency_to.get().upper().strip() == "" or save_names_entry.get().lower().strip() == "" or available_money.get().lower().strip() == "":
                root_gg.attributes("-topmost", False)
                messagebox.showerror("Error","Do not leave entries blank!")
                root_gg.attributes("-topmost", True)
            else:
                    try:
                        money = float(available_money.get().strip())
                    except:
                        root_gg.attributes("-topmost", False)
                        messagebox.showerror("Error","Please enter a numeric value.")
                        root_gg.attributes("-topmost", True)
                        return

                    save_name = save_names_entry.get().lower().strip()
                    currency_save = available_money_currency.get().upper().strip()
                    currency_save_to = str(available_money_currency_to.get().upper().strip())

                    save_currency_saves.save_currency_saves(file_name=str(save_name), currency=currency_save, currency_to=currency_save_to,available_money=float(money))
                    currency_updater_bot.start_currency_update()

                    root_gg.attributes("-topmost", False)
                    messagebox.showinfo("Successful","Your registration has been saved successfully!")
                    root_gg.attributes("-topmost", True)

                    available_money.delete(0, tk.END)
                    available_money_currency.set("Para Türü.")
                    available_money_currency_to.set("Çevirilecek.")
                    save_names_entry.delete(0, tk.END)

        def update_currency():
            currency_updater_bot.start_currency_update()
            root_gg.attributes("-topmost", False)
            messagebox.showinfo("Successful","All currencies have been updated successfully!")
            root_gg.attributes("-topmost", True)

        root_gg = ctk.CTkToplevel()
        root_gg.resizable(False, False)
        root_gg.title("MyMoney - Para Kayıt")
        root_gg.geometry("500x400")
        root_gg.attributes("-topmost", True)

        x = (root.winfo_screenwidth() - 500) // 2
        y = (root.winfo_screenheight() - 400) // 2

        root_gg.geometry(f"+{x}+{y}")
        
        title_gg = ctk.CTkLabel(root_gg, text="Para Kayıt", font=ctk.CTkFont(size=25, weight="bold"))
        title_gg.pack(pady=10)

        available_money = ctk.CTkEntry(root_gg, placeholder_text="Para değer giriniz...", width=170)
        available_money.pack(pady=10)

        available_money_currency = ctk.CTkComboBox(root_gg, values=("USD","TRY","EUR","GBP"))
        available_money_currency.pack(pady=10)
        available_money_currency.set("Para Türü.")

        available_money_currency_to = ctk.CTkComboBox(root_gg, values=("USD","TRY","EUR","GBP"))
        available_money_currency_to.pack(pady=10)
        available_money_currency_to.set("Çevirilecek.")

        save_names_entry = ctk.CTkEntry(root_gg, placeholder_text="Kayıt adını giriniz...", width=170)
        save_names_entry.pack(pady=10)

        saves_save = ctk.CTkButton(root_gg, text="Kaydet", font=("century gothic",13,"bold"), command=save)
        saves_save.pack(pady=15)

        all_saves = ctk.CTkButton(root_gg, text="Tüm Kayıtlar", font=("century gothic",13,"bold"), command=open_all_saves)
        all_saves.pack(pady=10)

        currency_update = ctk.CTkButton(root_gg, text="Kurları Güncelle", font=("century gothic",13,"bold"), command=update_currency, fg_color="#ffb700", hover_color="#7e5b01")
        currency_update.pack(pady=10)

        LanguageSync("Gelir Gider")

        root_gg.mainloop()

    def analiz_function():
        def start_analysis():
            def load_analysis_data():
                with open(f"app/saves/{save_file}/data-info.json","r",encoding="utf-8") as f:
                    data_analysis = json.load(f)

                for i in os.listdir(os.path.abspath(f"app/saves/{save_file}")):
                    if i.endswith(".txt"):
                        with open(f"app/saves/{save_file}/{i}","r",encoding="utf-8") as f:
                            lines = f.readlines()

                            for line in lines:
                                money_data_list_analysis.insert(tk.END, line.strip())
                                root_analysis_result.update()
                                money_data_list_analysis.yview(tk.END)
                                sleep(0.05)

            def reload_analysis_data():
                money_data_list_analysis.delete(0, tk.END)
                load_analysis_data()

            def report_screen():
                def report_generate():
                    pass
                pass

            def grafik_analizi():
                with open(f"app/saves/{save_file}/data-info.json","r",encoding="utf-8") as f:
                    data_analysis = json.load(f)

                for i in os.listdir(os.path.abspath(f"app/saves/{save_file}")):
                    if i.endswith(".txt"):
                        with open(f"app/saves/{save_file}/{i}","r",encoding="utf-8") as f:
                            money_list = []
                            for i in f.readlines():
                                money = str(i).strip().split("-")
                                money_list.append(money[0].strip().split(" ")[0])

                                print(money_list)

            def machine_learning_analysis_screen():
                def machine_learning_process():
                    pass
                pass

            def insert_filte():
                filter_type = analysis_filter_combobox.get()

                # ▲, ▼

                if filter_type == "Son 5 Analiz":
                    pass
                elif filter_type == "Kar Analiz":
                    with open(f"app/saves/{save_file}/data-info.json","r",encoding="utf-8") as f:
                        data_analysis = json.load(f)

                    first_data_money = money_data_list_analysis.get(0).split("-")[0].strip().split(" ")[0]
                    last_data_money = money_data_list_analysis.get(tk.END).split("-")[0].strip().split(" ")[0]

                    money_data = float(getdata_module.get_currency_data(f"{data_analysis['currency']}={data_analysis['to']}"))
                    root_analysis_result.update()

                    first_data = float(first_data_money) / money_data
                    last_data = float(last_data_money) / money_data
                
                    first_data = first_data_money * int(money_data)
                    last_data = last_data_money * int(money_data)

                    if first_data < last_data:
                        info_label_analysis.configure(text=f"▲ {round((last_data - first_data),2)} {data_analysis['to']}")
                        root_analysis_result.update()
                    elif first_data > last_data:
                        info_label_analysis.configure(text=f"▼ {round((first_data - last_data),2)} {data_analysis['to']}")
                        root_analysis_result.update()
                    else:
                        info_label_analysis.configure(text=f"NOTR (0 {data_analysis['to']})")
                        root_analysis_result.update()
                
                elif filter_type == "Son 2 Analiz":
                    pass
                else:
                    root_analysis_result.attributes("-topmost", False)
                    messagebox.showerror("Error","Please select a filter type.")
                    root_analysis_result.attributes("-topmost", True)
                    return
        
            analysis_type = analyze_type_combobox.get()
            save_file = saves_combobox.get()

            if not analysis_type == "Gelir-Gider Grafik":
                root_analysis.attributes("-topmost", False)
                messagebox.showerror("Error","Please select an analysis type.")
                root_analysis.attributes("-topmost", True)
                return
            elif save_file == "Kayıt Seçiniz." or save_file == "" or save_file not in os.listdir(os.path.abspath("app/saves")):
                root_analysis.attributes("-topmost", False)
                messagebox.showerror("Error","Please select a save file.")
                root_analysis.attributes("-topmost", True)
                return
            else:
                root_analysis_result = ctk.CTkToplevel()
                root_analysis_result.title("MyMoney - Analiz Sonuçları")
                root_analysis_result.geometry("600x400")
                root_analysis_result.resizable(False, False)
                root_analysis.attributes("-topmost",False)
                root_analysis_result.attributes("-topmost", True)

                x = (root_analysis_result.winfo_screenwidth() - 600) // 2
                y = (root_analysis_result.winfo_screenheight() - 400) // 2

                root_analysis_result.geometry(f"+{x}+{y}")

                title_label_analysis_result = ctk.CTkLabel(root_analysis_result, text="Analiz Sonuçları", font=ctk.CTkFont(size=21, weight="bold"))
                title_label_analysis_result.pack(pady=10)

                money_data_list_analysis = tk.Listbox(root_analysis_result, width=27, height=15, border=0, justify="left", borderwidth=0,relief="flat",activestyle="none",  selectbackground="black",selectforeground="orange", font=("Century Gothic",12,"bold"))
                money_data_list_analysis.pack()
                money_data_list_analysis.place(x=20, y=50)

                reload_button_analysis = ctk.CTkButton(root_analysis_result, text="Yenile", font=("century gothic",13,"bold"), command=reload_analysis_data)
                reload_button_analysis.pack()
                reload_button_analysis.place(x=70, y=360)

                load_analysis_data()

                info_label_analysis = ctk.CTkLabel(root_analysis_result, text=f"ANALYSIS RESULT", font=("century gothic",25,"bold"), justify="left")
                info_label_analysis.pack()
                info_label_analysis.place(x=330, y=50)

                analysis_filter_combobox = ctk.CTkComboBox(root_analysis_result, values=("Son 5 Analiz","Kâr Analiz","Son 2 Analiz"), width=150)
                analysis_filter_combobox.pack()
                analysis_filter_combobox.place(x=280, y=90)
                analysis_filter_combobox.set("Analizi Filtrele")

                insert_filter_button = ctk.CTkButton(root_analysis_result, text="Filtrele", font=("century gothic",13,"bold"), fg_color="#ed0000", hover_color="#7e0101", command=insert_filte)
                insert_filter_button.pack()
                insert_filter_button.place(x=440, y=90)

                grafik_analiz_button = ctk.CTkButton(root_analysis_result, text="Grafik Analiz", font=("century gothic",13,"bold"), command=grafik_analizi)
                grafik_analiz_button.pack()
                grafik_analiz_button.place(x=360, y=150)

                machine_learning_button = ctk.CTkButton(root_analysis_result, text="Makine Analizi", font=("century gothic",13,"bold"))
                machine_learning_button.pack()
                machine_learning_button.place(x=360, y=210)

                rapor_button = ctk.CTkButton(root_analysis_result, text="Rapor Oluştur", font=("century gothic",13,"bold"))
                rapor_button.pack()
                rapor_button.place(x=360, y=270)

                LanguageSync("Analiz Sonuçları")

                root_analysis_result.mainloop()

        root_analysis = ctk.CTkToplevel()
        root_analysis.title("MyMoney - Analiz")
        root_analysis.geometry("400x300")
        root_analysis.resizable(False, False)
        root_analysis.attributes("-topmost", True)

        x = (root_analysis.winfo_screenwidth() - 400) // 2
        y = (root_analysis.winfo_screenheight() - 300) // 2
        root_analysis.geometry(f"+{x}+{y}")

        title_label_analysis = ctk.CTkLabel(root_analysis, text="Analiz", font=ctk.CTkFont(size=25, weight="bold"))
        title_label_analysis.pack(pady=10)

        saves_combobox = ctk.CTkComboBox(root_analysis, values=os.listdir(os.path.abspath("app/saves")), width=200)
        saves_combobox.pack(pady=20)
        saves_combobox.set("Kayıt Seçiniz.")

        analyze_type_combobox = ctk.CTkComboBox(root_analysis, values=["Gelir-Gider Grafik"], width=200)
        analyze_type_combobox.pack(pady=13)

        analyze_button = ctk.CTkButton(root_analysis, text="Analiz Et", font=("century gothic",13,"bold"), width=100, command=start_analysis)
        analyze_button.pack(pady=20)

        LanguageSync("Analiz")

        root_analysis.mainloop()

    def ayarlar_function():
        global root_settings, theme_combobox, language_combobox, currency_combobox, enter, rename_button, title_label_settings, version_label_settings, currency_label, theme_label, language_label, auto_refresh_box

        def rename_function():
            global title_label_rename, root_settings_rename, name_entry, surname_entry, enter, name_label, surname_label

            def save_name(name, surname): 

                if name_entry.get() == "" or surname_entry.get() == "":
                    messagebox.showerror("Error", "Name and Surname cannot be empty.")
                else:
                    with open("app/settings.json", "r", encoding="utf-8") as f:
                        configure = json.load(f)
                    configure["user"]["name"] = name
                    configure["user"]["surname"] = surname
                    with open("app/settings.json", "w", encoding="utf-8") as f:
                        json.dump(configure, f, indent=4)
                        root_settings_rename.attributes("-topmost", False)
                    messagebox.showinfo("Success", "Name and Surname changed successfully.")
                    root_settings_rename.destroy()
                    root_settings.attributes("-topmost", True)

            root_settings_rename = ctk.CTkToplevel()
            root_settings_rename.title("MyMoney - Change Name")
            root_settings_rename.geometry("400x300")
            root_settings_rename.resizable(False, False)

            root_settings.attributes("-topmost", False)
            root_settings_rename.attributes("-topmost", True)

            with open("app/settings.json", "r", encoding="utf-8") as f:
                configure_name_surname = json.load(f)

            x = (root_settings_rename.winfo_screenwidth() - 400) // 2
            y = (root_settings_rename.winfo_screenheight() - 300) // 2
            root_settings_rename.geometry(f"+{x}+{y}")

            title_label_rename = ctk.CTkLabel(root_settings_rename, text="Change Name", font=ctk.CTkFont(size=20, weight="bold"))
            title_label_rename.pack(pady=10)

            name_label = ctk.CTkLabel(root_settings_rename, text="Name", font=("Century Gothic", 16,"bold"))
            name_label.pack()

            name_entry = ctk.CTkEntry(root_settings_rename, font=ctk.CTkFont(size=14))
            name_entry.pack(pady=10)
            name_entry.insert(0, configure_name_surname["user"]["name"])

            surname_label = ctk.CTkLabel(root_settings_rename, text="Surname", font=("Century Gothic", 16,"bold"))
            surname_label.pack()

            surname_entry = ctk.CTkEntry(root_settings_rename, font=ctk.CTkFont(size=14))
            surname_entry.pack(pady=10)
            surname_entry.insert(0, configure_name_surname["user"]["surname"])

            enter = ctk.CTkButton(root_settings_rename, text="Enter", font=("Century Gothic",14,"bold"), width=100, command=lambda: save_name(name_entry.get(), surname_entry.get()))
            enter.pack(pady=10)

            LanguageSync("Rename")

            root_settings_rename.mainloop()

        def save_settings():
            try:
                with open("app/settings.json", "r", encoding="utf-8") as f:
                    configure = json.load(f)

                theme = theme_combobox.get().lower()
                language = "en" if language_combobox.get() == "English" else "tr"
                currency = currency_combobox.get()
                configure["theme"] = theme
                configure["language"] = language
                configure["currency"] = currency

                with open("app/settings.json", "w", encoding="utf-8") as f:
                    json.dump(configure, f, indent=4)

                root_settings.destroy()
                messagebox.showinfo("Success", "All your settings will be saved, but the app will close and you will need to reopen it.")

                sleep(0.5)

                exe_path = sys.executable
                args = [exe_path] + sys.argv

                subprocess.Popen(args)

                sys.exit()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving settings: {e}")
                return

        def checkbox_auto_refresh_function():
            with open("app/settings.json","r",encoding="utf-8") as f:
                configure_refresh = json.load(f)
            
            if tik_deger.get() == True:
                configure_refresh["auto_refresh"] = True
            else:
                configure_refresh["auto_refresh"] = False

            with open("app/settings.json","w",encoding="utf-8") as f:
                json.dump(configure_refresh, f, indent=4)

        root_settings = ctk.CTkToplevel()
        root_settings.title("MyMoney - Settings")
        root_settings.geometry("500x470")
        root_settings.resizable(False, False)
        root_settings.attributes("-topmost", True)

        x = (root_settings.winfo_screenwidth() - 500) // 2
        y = (root_settings.winfo_screenheight() - 400) // 2
        root_settings.geometry(f"+{x}+{y}")

        title_label_settings = ctk.CTkLabel(root_settings, text="Settings", font=ctk.CTkFont(size=25, weight="bold"))
        title_label_settings.pack(pady=10)

        theme_label = ctk.CTkLabel(root_settings, text="Theme", font=("Century Gothic", 16,"bold"))
        theme_label.pack()

        theme_combobox = ctk.CTkComboBox(root_settings, values=["Light", "Dark", "System"], font=ctk.CTkFont(size=14))
        theme_combobox.set(configure["theme"].capitalize())
        theme_combobox.pack(pady=10)

        language_label = ctk.CTkLabel(root_settings, text="Language", font=("Century Gothic", 16,"bold"))
        language_label.pack()

        language_combobox = ctk.CTkComboBox(root_settings, values=["English", "Turkish"], font=ctk.CTkFont(size=14))
        language_combobox.set("English" if configure["language"] == "en" else "Turkish")
        language_combobox.pack(pady=10)

        currency_label = ctk.CTkLabel(root_settings, text="Currency", font=("Century Gothic", 16,"bold"))
        currency_label.pack()

        currency_combobox = ctk.CTkComboBox(root_settings, values=["USD", "TRY"], font=ctk.CTkFont(size=14))
        currency_combobox.set(configure["currency"])
        currency_combobox.pack(pady=10)

        tik_deger = ctk.BooleanVar()

        auto_refresh_box = ctk.CTkCheckBox(root_settings, text="Auto Refresh", variable=tik_deger, command=checkbox_auto_refresh_function, font=("Century Gothic",14,"bold"))
        auto_refresh_box.pack(pady=10)

        if configure["auto_refresh"] == True:
            tik_deger.set(1)
            root_settings.update()
        else:
            tik_deger.set(0)
            root_settings.update()

        rename_button = ctk.CTkButton(root_settings, text="Change Name", font=("Century Gothic",14,"bold"), width=150, command=rename_function, fg_color="#E60000", hover_color="#862302")
        rename_button.pack(pady=5)

        enter = ctk.CTkButton(root_settings, text="Save", font=("Century Gothic",14,"bold"), width=100, command=save_settings)
        enter.pack(pady=10)

        github_link = ctk.CTkLabel(root_settings, text="GitHub Link", font=("Century Gothic",14,"underline"), text_color="white", cursor="hand2")
        github_link.pack(pady=5)
        github_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/TheKeops/MyMoney"))
        
        _system_data_theme = ctk.get_appearance_mode()

        if _system_data_theme == "Light" or configure["theme"] == "light":
            github_link.configure(text_color="black")
        else:
            github_link.configure(text_color="white")

        version_label_settings = ctk.CTkLabel(root_settings, text=f"Version {configure['version']}", font=("Century Gothic",14))
        version_label_settings.pack(side="bottom", pady=5)

        LanguageSync("Settings")

        root_settings.mainloop()

    with open("app/settings.json", "r", encoding="utf-8") as f:
        configure = json.load(f)

    ctk.set_appearance_mode(configure["theme"])
    ctk.set_default_color_theme("blue")

    if configure["user"]["name"] == "None" or configure["user"]["surname"] == "None" or configure["user"]["name"] == "" or configure["user"]["surname"] == "":
        configure["user"]["name"] = f"user{random.randint(1000,9999)}"
        configure["user"]["surname"] = "default"

        with open("app/settings.json", "w", encoding="utf-8") as f:
            json.dump(configure, f, indent=4)
    else:
        pass

    root = ctk.CTk()
    root.title("MyMoney")
    root.geometry("400x300")
    root.resizable(False, False)
    root.focus()

    x = (root.winfo_screenwidth() - 400) // 2
    y = (root.winfo_screenheight() - 300) // 2

    root.geometry(f"+{x}+{y}")

    title_label = ctk.CTkLabel(root, text=f"Hi, {configure['user']['name']}", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=10)

    doviz_button = ctk.CTkButton(root, text="Currency", font=("Century Gothic",18,"bold"), fg_color="#DD9E00", hover_color="#A49100", width=250, command=doviz_function)
    doviz_button.pack(pady=10)

    gelir_gider_button = ctk.CTkButton(root, text="Income-Expense Tracking", font=("Century Gothic",18,"bold"), fg_color="#DD0000", hover_color="#A40000", width=250, command=gelir_gider_function)
    gelir_gider_button.pack(pady=10)

    analiz_button = ctk.CTkButton(root, text="Analysis", font=("Century Gothic",18,"bold"), width=250, command=analiz_function)
    analiz_button.pack(pady=10)

    ayarlar_button = ctk.CTkButton(root, text="Settings", font=("Century Gothic",18,"bold"), fg_color="#434343", hover_color="#858585", width=250, command=ayarlar_function)
    ayarlar_button.pack(pady=10)

    version_label = ctk.CTkLabel(root, text=f"Version {configure['version']}", font=("Century Gothic",14))
    version_label.pack(side="bottom", pady=5)

    LanguageSync()

    root.mainloop()

def network_check():
        try:
            import requests
            response = requests.get("https://www.google.com", timeout=5)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False
        
def splash_screen():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("500x400")
    splash.attributes("-topmost", True)

    x = (splash.winfo_screenwidth() - 500) // 2
    y = (splash.winfo_screenheight() - 400) // 2

    splash.geometry(f"+{x}+{y}")

    try:
        img_path = os.path.abspath("img/mymoney_loading_img.png")
        img = Image.open(img_path).resize((500, 400))
        photo = ImageTk.PhotoImage(img)
        tk.Label(splash, image=photo).pack(expand=True)
    except:
        tk.Label(splash, text="MyMoney Uygulaması Yükleniyor...", font=("Arial", 16)).pack(expand=True)

    def start_app():
        splash.update()
        currency_updater_bot.start_currency_update()
        splash.update()
        splash.destroy()
        app()

    splash.update()
    splash.after(2000, start_app)
    splash.update()

    splash.mainloop()

if __name__ == "__main__":
    platform_name = platform.system()
    if platform_name == "Windows":
        create_files_module.create_and_insert_default_settings()
        network_check_value = network_check()
        if network_check_value == False:
            messagebox.showwarning("No Internet Connection", "No internet connection detected. Some features may not work properly.")
        else:
            _version_control_flag = version_control_module.check_for_updates()

            if _version_control_flag == False: 
                messagebox.showinfo("Update Available", "A new version of the application is available. Please update to the latest version.")
            else:
                splash_screen()
    else:
        messagebox.showerror("Unsupported OS", "This application only supports Windows.")
        exit(1)
