import tkinter as tk
from tkinter import filedialog as fd
import os


def select_file():
    filetypes = (('Image files', '*.jpg'), ('Image files', '*.jpeg'), ('Image files', '*.png'))
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    file_path = os.path.abspath(filename)
    return file_path


def update_file_path_label(file_path):
    if os.path.isfile(file_path):
        file_path_label.config(text=file_path)


def open_button_click():
    file_path = select_file()
    update_file_path_label(file_path)


root = tk.Tk()
root.title('numer albumu')
root.resizable(False, False)
root.geometry('600x300')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

file_path_label = tk.Label(root, height=1, width=55, text="")
file_path_label.grid(row=0, column=0)

open_button = tk.Button(
    root,
    height=1,
    width=10,
    text='Open a File',
    command=open_button_click)
open_button.grid(row=0, column=1)

root.mainloop()
