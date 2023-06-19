import zad2
import zad1
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('numer albumu')
root.resizable(False, False)
root.geometry('600x300')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

info_text = zad2.pred_label
info = tk.Label(root, height=1, width=100, text=info_text,)
info.grid(row=1, column=0)

img = zad1.zad1(r"data\pl_Test\0\000DK2PNLBPO9CUA-C122-F4.jpg")
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.grid(row=0, column=0)

root.mainloop()

