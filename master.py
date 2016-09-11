from random import *
from tkinter import *


root = Tk()

#~~~Here are the global variables~~~
version_number = "0.0.1"
screen_width = root.winfo_screenwidth()
print (screen_width)
screen_height = root.winfo_screenheight()
print(screen_height)
oj = "#FAA551"
coal = "#474441"
font_adjust=13
font_size="-size %s" % (font_adjust)
larger_font_size ="-size %s" % (int(font_adjust) + 1)


#~~~Create basic tkinter layout for main menu~~~

root.title("Photon %s" % (version_number))
root.geometry("%s" % ((str(int(screen_width * .9))) + "x" + "%s" % (str(int(screen_height * .8)))))
root.pack_propagate(0)

logo = PhotoImage(file='photon.gif')

#placeholder chills on the left, no bg color
placeholder = Frame(root, width=(int(.15 * int(screen_width * .9))))
placeholder.pack(fill=Y, side=LEFT)

#menu holding frame
menu_frame = Frame(root)
menu_frame.pack(fill=Y, side=LEFT)

#orange stylistic stuff
bgflush = Frame(root, width=(int(.15 * int(screen_width * .9))), bg=oj)
bgflush.pack(fill=(BOTH), side=RIGHT)

logo_label = Label(menu_frame, image=logo)
logo_label.pack(side=TOP, pady=10, padx=150)

choices_label = Label(menu_frame, text="Welcome to Photon Learnware! Please choose your core subject", font=font_size)
choices_label.pack(side=TOP, pady=25)

def dindu():
    pass

select_bio = Button(menu_frame, text="Biology", font=larger_font_size, bg=coal, fg="white", command=dindu, width=15)
select_bio.pack(pady = 10)

select_chem = Button(menu_frame, text="Chemistry", font=larger_font_size, bg=coal, fg="white", command=dindu, width=15)
select_chem.pack(pady = 10)

select_phys = Button(menu_frame, text="Physics", font=larger_font_size, bg=coal, fg="white", command=dindu, width=15)
select_phys.pack(pady = 10)

info_label = Label(menu_frame, text="For personal use only. Copyright Brian L. Wilson © 2016")
info_label.pack(side=BOTTOM)

root.mainloop()

