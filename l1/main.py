#!/usr/bin/env python3
from caesar import Caesar
from provenzano import Provenzano
import tkinter as tk

from tkinter import *

window = Tk()
window.title("Szyfr cezara")
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
        'number': number.get(),
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

alpha_btn = Checkbutton(window, text="[A-z]", variable=alpha)
alpha_btn.select()
alpha_btn.grid(column=0, row=6)
number_btn = Checkbutton(window, text="[0-9]", variable=number)
number_btn.grid(column=1, row=6)
number_btn.select()
polish_btn = Checkbutton(window, text="polskie znaki", variable=polish)
polish_btn.grid(column=0, row=7)
Label(window, text="Shift:").grid(column=1, row=7)
key_entry = Entry(window, width=3)
key_entry.insert(0, '13')
key_entry.grid(column=1, row=8)

window.mainloop()
