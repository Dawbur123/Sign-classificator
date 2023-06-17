import tkinter as tk
from tkinter import filedialog as fd
import os
import image_prediction as pred
from pathlib import Path
import numpy as np
from PIL import Image, ImageTk


def select_file():
    filetypes = (('Image files', '*.jpg'), ('Image files', '*.jpeg'), ('Image files', '*.png'))
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='C:/Users/Asia/Pulpit/STUDIA/TI/semestr4/jpwp/projekt',
        filetypes=filetypes)
    file_path = os.path.abspath(filename)
    return file_path


def update_file_path_label(file_path):
    if os.path.isfile(file_path):
        file_path_label.config(text=file_path)


def open_button_click():
    file_path = select_file()
    update_file_path_label(file_path)


def new_window(result):
    new = tk.Toplevel()
    new.title('sign classificator')
    new.resizable(True, True)
    new.geometry('500x500')
    new.configure(bg='#E5D9E4')
    new.columnconfigure(0, weight=1)
    new.rowconfigure(0, weight=1)
    new.rowconfigure(1, weight=1)

    info_text = result[0]
    info = tk.Label(new, height=1, width=100, text=info_text, font=("Franklin Gothic Medium", 18), bg='#E5D9E4', fg="#33022E")
    info.grid(row=1, column=0)

    newframe = tk.Frame(new, bg='#E5D9E4')
    newframe.grid(row=0, column=0)  # Move the frame to row 1, column 0

    np_array = np.array(result[1])
    photo = Image.fromarray(np.uint8(np_array), 'RGB')
    aspect_ratio = float(photo.width) / float(photo.height)

    new_width = 400  # Target width for resized image
    new_height = int(new_width / aspect_ratio)

    photo = photo.resize((new_width, new_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo)
    label = tk.Label(newframe, image=photo)  # Place the label inside the newframe
    label.image = photo
    label.pack(fill=tk.BOTH, expand=True)

    new.mainloop()


def run_button_click():
    if file_path_label.cget("text") != "":
        file_path = file_path_label.cget("text")
        model_path = os.path.join(Path.cwd(), "Sign_classification_model.h5")
        if os.path.exists(model_path):
            result = pred.load_predict_image(file_path, model_path)
            print(result[0])
            new_window(result)
        else:
            tk.messagebox.showerror("Error", "Model file doesn't exist")


# creating window
root = tk.Tk()
root.title('sign classificator')
root.resizable(False, False)
root.geometry('600x300')
root.eval('tk::PlaceWindow . center')
root.configure(bg='#E5D9E4')

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)

file_path_label = tk.Label(frame, height=1, width=55, text="", bg="#BC64B4",  highlightbackground='#5D0956',
                           highlightcolor='#5D0956', highlightthickness=2, fg="#33022E")
file_path_label.config(justify='left')
file_path_label.grid(row=0, column=0)

open_button = tk.Button(
    frame,
    height=1,
    width=10,
    text='Open a File',
    command=open_button_click,
    bg="#F9EBF8",
    fg="#33022E")
open_button.grid(row=0, column=1)

start_button = tk.Button(frame,
                         height=1,
                         width=10,
                         text='Run',
                         command=run_button_click,
                         bg="#F9EBF8",
                         fg="#33022E")
start_button.grid(row=0, column=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.grid(row=0, column=0)

# starting window
root.mainloop()


