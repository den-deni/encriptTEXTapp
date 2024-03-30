from chifr import EncryptText

import customtkinter as CTk

et = EncryptText()






def open_wind(app):
    window = CTk.CTkToplevel(app)
    window.title("GetKey")
    window.geometry("500x400")
    window.config(background='black')
    entry_id = CTk.CTkEntry(master=window, width=300)
    entry_id.grid(row=0, padx=20)

    key_btn = CTk.CTkButton(master=window, text="ID", width=100)
    key_btn.grid(row=1, column=0)

    get_keys = CTk.CTkEntry(master=window, width=500, height=200)
    get_keys.grid(row=2)
