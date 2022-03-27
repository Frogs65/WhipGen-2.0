from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

root = Tk()
root.title("Main Menu")

#Images must be global for these methods to work properly.
img = ImageTk.PhotoImage(Image.open("Important.png"))
img2 = ImageTk.PhotoImage(Image.open("Header.png"))

sample = ["Ok", "Yuh", "What", "Esketit"]

#Must be done for images. If an image is not global, you must add the commented lines.
def whip_gen_gui():
    #img2 = ImageTk.PhotoImage(Image.open("Important.png"))
    #label.configure(image=img2)
    #label.image = img2

    #label["image"] = img2

    forget_main_menu()

    whip_image.grid(row=0,column=0,columnspan=2)
    gen_whip.grid(row=2,column=0)
    gen_double.grid(row=2,column=1)
    main_menu_whip.grid(row=3,column=1)
    text_display.grid(row=1,column=0,columnspan=2)

def forget_whip_gen():
    whip_image.grid_forget()
    gen_whip.grid_forget()
    gen_double.grid_forget()
    main_menu_whip.grid_forget()
    text_display.grid_forget()

def main_menu_gui():
    forget_whip_gen()

    menu_image.grid(row=0,column=0,columnspan=2)
    version.grid(row=1,column=0,columnspan=2)
    whip_gen.grid(row=2,column=0,sticky=NW)
    rap_gen.grid(row=2,column=1)
    credit.grid(row=3,column=0)
    patch_notes.grid(row=3,column=1)
    quit_button.grid(row=4,column=1)
    b.grid(row=4,column=0)

    #text["text"] = "In Development"
    #label["image"] = img

def forget_main_menu():
    menu_image.grid_forget()
    version.grid_forget()
    whip_gen.grid_forget()
    rap_gen.grid_forget()
    credit.grid_forget()
    patch_notes.grid_forget()
    quit_button.grid_forget()
    b.grid_forget()

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
    #text = box.get()
    #add_whips(text)
    #box.delete(0,len(text))
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

#ALL OF THE WIDGETS FOR EACH GUI

#Main Menu widgets
menu_image = Label(root, image=img)
version = Label(root, text="In Development")
whip_gen = Button(root,text="Whip Generator",command=whip_gen_gui,height=3,width=20)
rap_gen = Button(root,text="Rap Generator",command=revert_image,height=3,width=20)
credit = Button(root,text="Credits",command=generate,height=3,width=20)
patch_notes = Button(root,text="Patch Notes",command=grab_input,height=3,width=20)
quit_button = Button(root,text="Quit",command=root.quit,height=3,width=20)
b = Button(root,text="TBD",height=3,width=20)

#Whip Generator widgets
whip_image = Label(root,image=img2)
gen_whip = Button(root,text="Generate Whip",height=5,width=35)
gen_double = Button(root,text="Generate Double Whip",height=5,width=35)
main_menu_whip = Button(root,text="Main Menu",command=main_menu_gui,height=5,width=35)
text_display = Label(root,text="Test Text",bg="#00a2e8",width=71,height=2)




#img = ImageTk.PhotoImage(Image.open("Header.png"))

#label = Label(root, image=img)
#label.grid(row=0,column=0,columnspan=2)
#text = Label(root, text="In Development")
#text.grid(row=1,column=0,columnspan=2)

#whip_gen = Button(root,text="Whip Generator",command=whip_gen_gui,height=3,width=20)
#whip_gen.grid(row=2,column=0,sticky=NW)
#rap_gen = Button(root,text="Rap Generator",command=revert_image,height=3,width=20)
#rap_gen.grid(row=2,column=1)
#credit = Button(root,text="Credits",command=generate,height=3,width=20)
#credit.grid(row=3,column=0)
#patch_notes = Button(root,text="Patch Notes",command=grab_input,height=3,width=20)
#patch_notes.grid(row=3,column=1)
#quit_button = Button(root,text="Quit",command=root.quit,height=3,width=20)
#quit_button.grid(row=4,column=1)
#b = Button(root,text="TBD",height=3,width=20)
#b.grid(row=4,column=0)

main_menu_gui()

root.mainloop()