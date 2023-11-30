from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import glob

root = Tk()
root.title("Image Viewer")
root.geometry("800x600")
root.configure(bg="black")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))

all_files = []

current_file_index = 0
#open the folder
def open_directory():
    global all_files
    global current_file_index
    folder_path = filedialog.askdirectory(initialdir=os.getcwd())
    if folder_path:
        all_files = sorted(glob.glob(os.path.join(folder_path, '*')))
        current_file_index = 1
#The next image button
def next_image():
    global all_files
    global current_file_index
    if all_files and current_file_index < len(all_files):
        img_path = all_files[current_file_index]
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img
        current_file_index += 1
#Previous image button
def previous_image():
    global all_files
    global current_file_index
    if all_files and current_file_index > 0:
        current_file_index -= 1
        img_path = all_files[current_file_index]
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img
#the frame on which the image will be shown
frame = Frame(root, height=500, width=1900, borderwidth=10,relief=tk.RIDGE,bg="#808080")
frame.pack_propagate(False)
frame.pack(fill=tk.BOTH, expand=True)

lbl = Label(frame,bg="#808080")
lbl.pack()
#Open folder buttom
open_button = Button(root, text="Open Directory", font=("copper", 15),relief=tk.RAISED,bg="#BFDAF7",command=open_directory)
open_button.pack()
#Next image button
next_button = Button(root, text="Next", font=("copper", 15),bg="#BFDAF7",command=next_image)
next_button.pack(side=RIGHT)
#Previous image button
previous_button = Button(root, text="Back", font=("copper", 15),bg="#BFDAF7",command=previous_image)
previous_button.pack(side=LEFT)

root.mainloop()
