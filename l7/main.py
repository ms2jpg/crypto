import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from PIL import Image, ImageTk
from stegano import Stegano
window = Tk()
window.title("Steganografia - Krzysztof Krzyżaniak")
image = None
stegano = None
Label(window, text="Program pozwala na na ukrycie danych w pliku typu BMP. Payload może zawierać").grid(columnspan=2)


def load_image():
    file_path = askopenfile(mode='r')
    if file_path is not None:
        global image
        global stegano
        image = ImageTk.PhotoImage(file=file_path.name)
        image_label = Label(window, image=image)
        # image_label.pack()
        image_label.grid(row=2, columnspan=2)

        stegano = Stegano(file_path.name)
        # messagebox.showinfo('Informacja', 'Maksymalny rozmiar wiadomości to {} bajtów!'.format(stegano.max_message_size))
        # with file_path as f:
        #     print(f.read())

def hide_message():
    global stegano
    if stegano is None:
        return
    file_path = askopenfile(mode='r')
    if file_path is not None:
        with open(file_path.name, 'rb') as f:
            payload = f.read()
        if len(payload) > stegano.max_message_size:
            messagebox.showerror('Za duży rozmiar pliku', 'Maksymlany rozmiar ukrywanego pliku to {} bajtów!', stegano.max_message_size)
            return
        stegano.embed_message(payload)
        filename_to_save = asksaveasfile(mode='w', defaultextension='.bmp')
        if filename_to_save is not None:
            stegano.save_image(filename_to_save.name)

def show_message():
    global stegano
    if stegano is None:
        return
    payload = stegano.get_message()
    filename_to_save = asksaveasfile(mode='w')
    if filename_to_save is not None:
        with open(filename_to_save.name, mode='wb') as f:
            f.write(payload)

load_image_btn = Button(window, text="Load image", command=load_image)
load_image_btn.grid(column=0, row=1, columnspan=2)

hide_message_btn = Button(window, text="Hide message", command=hide_message)
hide_message_btn.grid(column=0, row=3)

show_message_btn = Button(window, text="Show message", command=show_message)
show_message_btn.grid(column=1, row=3)

window.mainloop()