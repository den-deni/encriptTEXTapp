import random
import sqlite3
import string


class EncryptText:
    def __init__(self):
        self.chars = (" " + string.punctuation + string.digits +
                      string.ascii_letters + 'абвгґдеєжзиійклмнопрстуфхцчшщьюя')
        self.chars = list(self.chars)
        self.key = self.chars.copy()
        random.shuffle(self.key)
        self.save_key = ''.join(self.key)
        self.connect = sqlite3.connect("secretkey.db")
        self.cursor = self.connect.cursor()
        self.create_table()

    def encrypt(self, plain_text):
        cipher_text = ""
        for letter in plain_text:
            index = self.chars.index(letter)
            cipher_text += self.key[index]
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ""
        for letter in cipher_text:
            index = self.key.index(letter)
            plain_text += self.chars[index]
        return plain_text

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS db_data_keys(
                id_key  INTEGER PRIMARY KEY AUTOINCREMENT,
                key_ TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connect.commit()

    def write_key(self):
        self.cursor.execute("""
            INSERT INTO db_data_keys(key_)
            VALUES (?)
            """, (self.save_key,))
        self.connect.commit()

    def decrypt_with_key(self, cipher_text, key):
        plain_text = ''
        for letter in cipher_text:
            if letter in key:
                index = key.index(letter)
                plain_text += self.chars[index]
        return plain_text

    def select_key(self):
        self.cursor.execute("SELECT key_ FROM db_data_keys")
        keys = self.cursor.fetchone()
        list_keys = []
        for key in keys:
            list_keys.append(key)
        return list_keys[-1]

    def delete_key(self):
        self.cursor.execute("DROP TABLE IF EXISTS db_data_keys")
        self.connect.commit()

    def closed_db(self):
        self.connect.close()

