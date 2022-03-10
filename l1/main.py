#!/usr/bin/env python3
from caesar import Caesar
from provenzano import Provenzano
import tkinter as tk

from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

window = Tk()
window.title("Szyfr Cezara - Krzysztof Krzyżaniak")
# window.geometry('640x480')
Label(window, text="Input").grid(columnspan=2)
txt = Text(window, width=64, height=8)
txt.grid(row=1, columnspan=2)

Label(window, text="Output").grid(row=2, columnspan=2)
txt2 = Text(window, width=64, height=8)
txt2.grid(row=3, columnspan=2)


def encrypt():
    c = Caesar(int(key_entry.get()), {
        'alpha': alpha.get(),
        'numeric': number.get(),
        'polish': polish.get()

    })
    txt2.delete("1.0", tk.END)
    txt2.insert('end-1c', c.encrypt(txt.get("1.0", "end-1c")))

def decrypt():
    c = Caesar(int(key_entry.get()), {
        'alpha': alpha.get(),
        'numeric': number.get(),
        'polish': polish.get()

    })
    txt2.delete("1.0", tk.END)
    txt2.insert('end-1c', c.decrypt(txt.get("1.0", "end-1c")))

def pencrypt():
    p = Provenzano()
    txt2.delete("1.0", tk.END)
    txt2.insert('end-1c', p.encrypt(txt.get("1.0", "end-1c")))

def pdecrypt():
    p = Provenzano()
    txt2.delete("1.0", tk.END)
    txt2.insert('end-1c', p.decrypt(txt.get("1.0", "end-1c")))

def atbash():
    p = Caesar(0)
    txt2.delete("1.0", tk.END)
    txt2.insert('end-1c', p.atbash(txt.get("1.0", "end-1c")))

def load_from_file():
    file_path = askopenfile(mode='r')
    if file_path is not None:
        with file_path as f:
            txt.delete("1.0", tk.END)
            txt.insert('end-1c', str(f.read()))

def save_to_file():
    file = asksaveasfile(mode='w', defaultextension=".txt")
    if file is not None:
        with file as f:
            f.write(txt2.get("1.0", "end-1c"))
            f.close()



load_from_file_btn = Button(window, text="Load from file", command=load_from_file)
load_from_file_btn.grid(column=0, row=0)

save_to_file_btn = Button(window, text="Save", command=save_to_file)
save_to_file_btn.grid(column=0, row=2)

encrypt_btn = Button(window, text="Encrypt", command=encrypt)
encrypt_btn.grid(column=0, row=4)
decrypt_btn = Button(window, text="Decrypt", command=decrypt)
decrypt_btn.grid(column=1, row=4)

pencrypt_btn = Button(window, text="Provenzano encrypt", command=pencrypt)
pencrypt_btn.grid(column=0, row=5)
pdecrypt_btn = Button(window, text="Provenzano decrypt", command=pdecrypt)
pdecrypt_btn.grid(column=1, row=5)
alpha = IntVar()
number = IntVar()
polish = IntVar()



atbash_encrypt_btn = Button(window, text="Atbash encrypt", command=atbash)
atbash_encrypt_btn.grid(column=0, row=6)
atbash_decrypt_btn = Button(window, text="Atbash decrypt", command=atbash)
atbash_decrypt_btn.grid(column=1, row=6)

alpha_btn = Checkbutton(window, text="[A-z]", variable=alpha)
alpha_btn.select()
alpha_btn.grid(column=0, row=7)
number_btn = Checkbutton(window, text="[0-9]", variable=number)
number_btn.grid(column=1, row=7)
number_btn.select()
polish_btn = Checkbutton(window, text="polskie znaki", variable=polish)
polish_btn.grid(column=0, row=8)
Label(window, text="Shift:").grid(column=1, row=8)
key_entry = Entry(window, width=3)
key_entry.insert(0, '13')
key_entry.grid(column=1, row=9)

window.mainloop()
