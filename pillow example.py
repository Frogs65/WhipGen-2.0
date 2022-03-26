from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

root = Tk()

#Images must be global for these methods to work properly.
img = ImageTk.PhotoImage(Image.open("Header.png"))
img2 = ImageTk.PhotoImage(Image.open("Important.png"))

sample = ["Ok", "Yuh", "What", "Esketit"]

#Must be done for images. If an image is not global, you must add the commented lines.
def update_image():
    #img2 = ImageTk.PhotoImage(Image.open("Important.png"))
    #label.configure(image=img2)
    #label.image = img2
    label["image"] = img2
    update_text()

#Can be used for text updates.
def update_text():
    text["text"] = "No"

#Can be reverted back easily because img is global.
def revert_image():
    label["image"] = img
    revert_text()

def revert_text():
    text["text"] = "Yes"

def generate():
    outcome = random.choice(sample)
    generate_lab["text"] = outcome

def grab_input():
    text = box.get()
    #add_whips(text)
    box.delete(0,len(text))
    messagebox.showinfo("Success!", "Whip succesfully added")

def add_whips(your_addition):
    file = open("Whips.txt", "r")
    temp = []
    for line in file:
        temp = line.split(",")
    file.close()
    second = open("Whips.txt","a")
    if len(temp) == 0:
        second.write(your_addition)
    else:
        second.write("," + your_addition)
    second.close()

#img = ImageTk.PhotoImage(Image.open("Header.png"))

label = Label(root, image=img)
label.grid(row=0,column=0,columnspan=2)
text = Label(root, text="Yes")
text.grid(row=2,column=0,columnspan=2)
generate_lab = Label(root,text=" ")
generate_lab.grid(row=4,column=0)
box = Entry(root)
box.grid(row=5,column=0)

update_screen = Button(root, text="Update",command=update_image)
update_screen.grid(row=1,column=0)
revert_screen = Button(root, text="Revert",command=revert_image)
revert_screen.grid(row=1,column=1)
generate_button = Button(root,text="Generate",command=generate)
generate_button.grid(row=3,column=0)
entry_button = Button(root,text="Enter",command=grab_input)
entry_button.grid(row=5,column=1)

root.mainloop()