from tkinter import *
from PIL import ImageTk, Image
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

#img = ImageTk.PhotoImage(Image.open("Header.png"))

label = Label(root, image=img)
label.grid(row=0,column=0,columnspan=2)
text = Label(root, text="Yes")
text.grid(row=2,column=0,columnspan=2)
generate_lab = Label(root,text=" ")
generate_lab.grid(row=4,column=0)

update_screen = Button(root, text="Update",command=update_image)
update_screen.grid(row=1,column=0)
revert_screen = Button(root, text="Revert",command=revert_image)
revert_screen.grid(row=1,column=1)
generate_button = Button(root,text="Generate",command=generate)
generate_button.grid(row=3,column=0)

root.mainloop()