from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

root = Tk()
root.title("A DYDX Co Program")

#Images must be global for these methods to work properly.
img = ImageTk.PhotoImage(Image.open("Important.png"))
img2 = ImageTk.PhotoImage(Image.open("Header.png"))
img3 = ImageTk.PhotoImage(Image.open("Rap.png"))

sample = ["Ok", "Yuh", "What", "Esketit"]

#If an image is not global, you must add the commented lines.
#img2 = ImageTk.PhotoImage(Image.open("Important.png"))
#label.configure(image=img2)
#label.image = img2

def whip_gen_gui():
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

def rap_gen_gui():
    forget_main_menu()

    rap_image.grid(row=0,column=0,columnspan=2)
    rap_display.grid(row=1,column=0,columnspan=2)
    gen_rap.grid(row=2,column=0)
    main_menu_rap.grid(row=2,column=1)

def forget_rap_gen():
    rap_image.grid_forget()
    rap_display.grid_forget()
    gen_rap.grid_forget()
    main_menu_rap.grid_forget()

def main_menu_gui():
    forget_whip_gen()
    forget_rap_gen()

    menu_image.grid(row=0,column=0,columnspan=2)
    version.grid(row=1,column=0,columnspan=2)
    whip_gen.grid(row=2,column=0,sticky=NW)
    rap_gen.grid(row=2,column=1)
    func_gen.grid(row=3,column=0)
    patch_notes.grid(row=3,column=1)
    quit_button.grid(row=4,column=1)
    credit.grid(row=4,column=0)


def forget_main_menu():
    menu_image.grid_forget()
    version.grid_forget()
    whip_gen.grid_forget()
    rap_gen.grid_forget()
    func_gen.grid_forget()
    patch_notes.grid_forget()
    quit_button.grid_forget()
    credit.grid_forget()

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
rap_gen = Button(root,text="Rap Generator",command=rap_gen_gui,height=3,width=20)
func_gen = Button(root,text="Function Generator (WIP)",height=3,width=20)
patch_notes = Button(root,text="Patch Notes",command=grab_input,height=3,width=20)
quit_button = Button(root,text="Quit",command=root.quit,height=3,width=20)
credit = Button(root,text="Credits",height=3,width=20)

#Whip Generator widgets
whip_image = Label(root,image=img2)
gen_whip = Button(root,text="Generate Whip",height=5,width=35)
gen_double = Button(root,text="Generate Double Whip",height=5,width=35)
main_menu_whip = Button(root,text="Main Menu",command=main_menu_gui,height=5,width=35)
text_display = Label(root,text="Test Text",bg="#00a2e8",width=71,height=2)

#Rap Generator widgets
rap_image = Label(root,image=img3)
gen_rap = Button(root,text="Generate Rap",height=5,width=35)
main_menu_rap = Button(root,text="Main Menu",command=main_menu_gui,height=5,width=35)
rap_display = Label(root,text="Test Text",bg="#22b14c",width=71,height=2)


main_menu_gui()

root.mainloop()