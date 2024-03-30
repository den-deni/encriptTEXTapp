import customtkinter as CTk
from PIL import Image

from chifr import EncryptText


et = EncryptText()


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Text encoder")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("static/photo33.png"), size=(500, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo, fg_color="transparent")
        self.logo_label.grid(row=0, column=0, sticky='nsew')

        self.crypt_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.crypt_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_text = CTk.CTkEntry(master=self.crypt_frame, width=300)
        self.entry_text.grid(row=0, column=0, padx=(0, 20))

        self.btn_crypt = CTk.CTkButton(master=self.crypt_frame, text="Encrypt", width=100, command=self.encrypt_text)
        self.btn_crypt.grid(row=0, column=1)

        self.decrypt_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.decrypt_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.entry_decrypt_text = CTk.CTkEntry(master=self.decrypt_frame, width=300)
        self.entry_decrypt_text.grid(row=1, column=0)

        self.btn_decrypt = CTk.CTkButton(master=self.decrypt_frame, text="Decrypt", width=100,
                                         command=self.decrypt_text)
        self.btn_decrypt.grid(row=1, column=1, padx=20)

        self.get_key_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.get_key_frame.grid(row=3, padx=20, pady=10, sticky="nsew")

        self.entry_get_key = CTk.CTkEntry(master=self.get_key_frame, width=300)
        self.entry_get_key.grid(row=0, column=0)

        self.get_key_btn = CTk.CTkButton(master=self.get_key_frame, text="GetKey", width=100,
                                         command=self.getkey)
        self.get_key_btn.grid(row=0, column=1, padx=20)

        self.entry_key_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.entry_key_frame.grid(row=4, padx=20, pady=10, sticky="nsew")

        self.entry_key = CTk.CTkEntry(master=self.entry_key_frame, width=300)
        self.entry_key.grid(row=0, column=0)

        self.entry_key_btn = CTk.CTkButton(master=self.entry_key_frame, text="EnterKey", width=100,
                                           command=self.entry_keys)
        self.entry_key_btn.grid(row=0, column=1, padx=20)

        self.result_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.result_frame.grid(row=5, padx=20, pady=10, sticky="nsew")

        self.entry_result = CTk.CTkEntry(master=self.result_frame, width=425)
        self.entry_result.grid(row=0)

        self.save_key_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.save_key_frame.grid(row=6, padx=20, pady=10, sticky="nsew")

        self.save_key_btn = CTk.CTkButton(master=self.save_key_frame, text="SaveKey", width=100,
                                          command=self.save_keys)
        self.save_key_btn.grid(row=0, column=0)

        self.select_btn = CTk.CTkButton(master=self.save_key_frame, text='DeleteKey', width=100,
                                        command=self.delete_keys)
        self.select_btn.grid(row=0, column=1, padx=20)

    def encrypt_text(self):
        plain_text = self.entry_text.get()
        self.entry_result.delete(0, 'end')
        self.entry_result.insert('end', et.encrypt(plain_text=plain_text))

    def decrypt_text(self):
        cipher_text = self.entry_decrypt_text.get()
        self.entry_result.delete(0, 'end')
        self.entry_result.insert('end', et.decrypt(cipher_text))

    def entry_keys(self):
        try:
            master_key = self.entry_key.get()
            cipher_text = self.entry_decrypt_text.get()
            decrypt_text = et.decrypt_with_key(cipher_text, master_key)
            self.entry_result.delete(0, 'end')
            self.entry_result.insert('end', decrypt_text)
        except TypeError:
            self.entry_result.get()

    def getkey(self):
        try:
            key_values = et.select_key()
            self.entry_get_key.delete(0, 'end')
            self.entry_get_key.insert(0, key_values)
        except Exception as e:
            text_error = 'Not key in db'
            self.entry_get_key.insert(0, f'{e}' + text_error)

    @staticmethod
    def save_keys():
        et.write_key()

    @staticmethod
    def delete_keys():
        et.delete_key()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    et.closed_db()
