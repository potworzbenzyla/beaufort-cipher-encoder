from tkinter import *

def encryptor(plain_text, keyword):
    cipher_text = ''
    keyword_index = 0
    for char in plain_text:
        if char.isalpha():
            char_num = ord(char.upper()) - 65
            keyword_num = ord(keyword[keyword_index % len(keyword)].upper()) - 65
            cipher_num = (keyword_num - char_num) % 26
            cipher_char = chr(cipher_num + 65)
            cipher_text += cipher_char
            keyword_index += 1
        else:
            cipher_text += char
    return cipher_text

def decryptor(cipher_text, keyword):
    plain_text = ''
    keyword_index = 0
    for char in cipher_text:
        if char.isalpha():
            cipher_num = ord(char.upper()) - 65
            keyword_num = ord(keyword[keyword_index % len(keyword)].upper()) - 65
            plain_num = (keyword_num - cipher_num) % 26
            plain_char = chr(plain_num + 65)
            plain_text += plain_char
            keyword_index += 1
        else:
            plain_text += char
    return plain_text

def encrypt_text():
    keyword = keyword_entry.get()
    plain_text = input_text.get("1.0", END).strip()
    cipher_text = encryptor(plain_text, keyword)
    output_text.delete("1.0", END)
    output_text.insert("1.0", cipher_text)

def decrypt_text():
    keyword = keyword_entry.get()
    cipher_text = input_text.get("1.0", END).strip()
    plain_text = decryptor(cipher_text, keyword)
    output_text.delete("1.0", END)
    output_text.insert("1.0", plain_text)

root = Tk()
root.title("Szyfr Beauforta")

keyword_label = Label(root, text="Slowo kluczowe: ")
keyword_label.pack()
keyword_entry = Entry(root)
keyword_entry.pack()

input_label = Label(root, text="Tekst: ")
input_label.pack()
input_text = Text(root, height=10)
input_text.pack()

encrypt_button = Button(root, text="Szyfrowanie", command=encrypt_text)
encrypt_button.pack()

decrypt_button = Button(root, text="Deszyfrowanie", command=decrypt_text)
decrypt_button.pack()

output_label = Label(root, text="Wynik:")
output_label.pack()
output_text = Text(root, height=10)
output_text.pack()

root.mainloop()
