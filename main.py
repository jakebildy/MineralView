import glob
import math
import time
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

import random



# The colors used for the application's theme.
darkish = '#%02x%02x%02x' % (29, 30, 38)
whitish = '#%02x%02x%02x' % (214, 216, 218)
code_green = '#%02x%02x%02x' % (80, 200, 70)
code_green_light = '#%02x%02x%02x' % (170, 200, 150)
code_dark = '#%02x%02x%02x' % (23, 24, 30)


# Refreshes the application.
def new():
    print("new pressed")
    mineralview.state = -1

# Go back to the previous image.
def back():
    if (mineralview.position > 0):
        mineralview.position-=1

# Go to the next image.
def next():
    if (mineralview.position < mineralview.count1-1):
        mineralview.position+=1

# Select the first directory..
def select_folder1():
    dir1 = Label(text="                                                                  ",
                 font='Helvetica 12 bold', bg=darkish, fg=code_green)
    dir1.grid(row=4, column=4, columnspan=2, )
    directory =  filedialog.askdirectory(initialdir = "/",title = "Select directory 1")
    print(directory)
    mineralview.count1 = glob.glob(directory+"/*").__len__()
    mineralview.dir1 =directory

# Select the second directory.
def select_folder2():
    dir2 = Label(text="                                                                  ",
                 font='Helvetica 12 bold', bg=darkish, fg=code_green)
    dir2.grid(row=4, column=1, columnspan=2, )
    directory =  filedialog.askdirectory(initialdir = "/",title = "Select directory 2")
    print(directory)
    mineralview.count2 = glob.glob(directory + "/*").__len__()
    mineralview.dir2 = directory


# Starts the program. Called on refresh and on initial startup.
def start_program():
    global root
    root = Tk()
    root.minsize(width=600, height=700)
    root.configure(bg=darkish)
    w = Label(root, text="MineralView", font='Helvetica 30 bold', bg=darkish, fg=whitish).grid(row=0, column=2,
                                                                                               columnspan=3, padx=10)
    w2 = Label(root, text="", bg=darkish).grid(row=2, column=0)
    absorptive_title = Label(text="\nDirectory 2", font='Helvetica 18 bold', bg=darkish, fg=whitish)
    absorptive_title.grid(row=1, columnspan=2, column=4)

    reflective_title = Label(text="\nDirectory 1", font='Helvetica 18 bold', bg=darkish, fg=whitish)
    reflective_title.grid(row=1, columnspan=2, column=1)

    global absorptive_frame
    absorptive_frame = Frame(root, width=300, height=300, bg=code_dark)
    absorptive_frame.grid(row=3, column=4, columnspan=2, sticky='e', padx=20)

    global reflective_frame
    reflective_frame = Frame(root, width=300, height=300, bg=code_dark)
    reflective_frame.grid(row=3, column=1, columnspan=2, sticky='e', padx=20)

    global back_button
    back_button = Button(text="Back", relief='flat', highlightthickness=0, command=back)
    back_button.grid(row=6, column=2, pady=20)

    global next_button
    next_button = Button(text="Next", relief='flat', highlightthickness=0, command=next)
    next_button.grid(row=6, column=4, pady=20)

    global select_absorptive
    select_absorptive = Button(text="Select Folder", font='Helvetica 18 bold', command=select_folder1, fg=darkish)
    select_absorptive.grid(row=3, column=4, columnspan=2)

    global select_reflective
    select_reflective = Button(text="Select Folder", font='Helvetica 18 bold', command=select_folder2, fg=darkish)
    select_reflective.grid(row=3, column=1, columnspan=2)

    root.title("MineralView")

    top = root.winfo_toplevel()
    global menuBar
    menuBar = Menu(top)
    top['menu'] = menuBar
    global subMenu
    subMenu = Menu(menuBar)

    menuBar.add_cascade(label='File', menu=subMenu)
    subMenu.add_command(label='New', command=new)


start_program()

# Holds key global variables
class mineralview:
    position = 1
    state = 0
    count1 = -2
    count2 = -1
    position_label = Label()
    dir1 = ""
    dir2 = ""



# The main running method.
def running():

    prev_selection = 1
    panel = Label()
    panel2 = Label()
    path = ""
    path2 = ""
    pathlabel1 = Label()
    pathlabel2 = Label()

    select_reflective.lift()
    select_absorptive.lift()

    while mineralview.state != -1:
        time.sleep(0.1)

        if (prev_selection != mineralview.position):
            prev_selection = mineralview.position
            panel.pack_forget()
            panel2.pack_forget()
            reflective_frame.lift()
            absorptive_frame.lift()
            pathlabel1 = Label(text="                                                ",
                               font='Helvetica 12 bold', bg=darkish, fg=code_green)
            pathlabel1.grid(row=5, column=4, columnspan=2, )

            pathlabel2 = Label(text="                                                ",
                               font='Helvetica 12 bold', bg=darkish, fg=code_green)
            pathlabel2.grid(row=5, column=1, columnspan=2, )


        # Checks that both directories have been selected. If they have different numbers of images, select the lowest number.
        if (mineralview.count1 > 0 and mineralview.count2 > 0) :
            if mineralview.count1 > mineralview.count2:
                mineralview.count1 = mineralview.count2
            else:
                mineralview.count2 = mineralview.count1


        if (mineralview.count1 == mineralview.count2) :
            mineralview.position_label = Label(text="\nSelect folders with the same number of images",
                                               font='Helvetica 12 bold', bg=darkish, fg=darkish)
            mineralview.position_label.grid(row=6, column=2, pady=20, columnspan=3)

            mineralview.position_label = Label(text="\n" + str(mineralview.position) + "/" + str(mineralview.count1), font='Helvetica 18 bold', bg=darkish, fg=whitish)
            mineralview.position_label.grid(row=6, column=3, pady=20)

            back_button.lift()
            next_button.lift()

            absorptive_title = Label(text="\nDirectory 2", font='Helvetica 18 bold', bg=darkish, fg=darkish)
            absorptive_title.grid(row=1, columnspan=2, column=4)

            reflective_title = Label(text="\nDirectory 1", font='Helvetica 18 bold', bg=darkish, fg=darkish)
            reflective_title.grid(row=1, columnspan=2, column=1)


            dir1split = mineralview.dir1.split("/")

            absorptive_title = Label(text="\n" + dir1split[dir1split.__len__() - 1], font='Helvetica 18 bold',
                                     bg=darkish, fg=whitish)
            absorptive_title.grid(row=1, columnspan=2, column=4)

            dir2split = mineralview.dir2.split("/")

            reflective_title = Label(text="\n" + dir2split[dir2split.__len__() - 1], font='Helvetica 18 bold',
                                     bg=darkish, fg=whitish)
            reflective_title.grid(row=1, columnspan=2, column=1)

            # Opens Image 1.
            print(mineralview.position)
            path = glob.glob(mineralview.dir1+"/" + mineralview.position.__str__() + ".*")[0]
            file = Image.open(path)
            aspect = (file.width/file.height)

            # Handles image scaling.
            if aspect > 1 :
                # width is bigger
                img = ImageTk.PhotoImage(Image.open(path).resize((300, (math.floor(300 * 1/aspect))), Image.ANTIALIAS))
            elif aspect < 1 :
                # height is bigger
                img = ImageTk.PhotoImage(Image.open(path).resize((math.floor(300 * aspect), 300), Image.ANTIALIAS))
            else :
                img = ImageTk.PhotoImage(Image.open(path).resize((300, 300), Image.ANTIALIAS))

            panel = Label(root, image=img, borderwidth=0)
            panel.photo = img
            panel.grid(row=3, column=4, columnspan=2,)
            panel.lift()

            # Opens Image 2.
            path2 = glob.glob(mineralview.dir2 + "/" + mineralview.position.__str__() + ".*")[0]

            file2 = Image.open(path2)
            aspect2 = (file2.width / file2.height)

            # Handles image scaling.
            if aspect2 > 1:
                # width is bigger
                img2 = ImageTk.PhotoImage(
                    Image.open(path2).resize((300, (math.floor(300 * 1 / aspect2))), Image.ANTIALIAS))
            elif aspect2 < 1:
                # height is bigger
                img2 = ImageTk.PhotoImage(Image.open(path2).resize((math.floor(300 * aspect2), 300), Image.ANTIALIAS))
            else:
                img2 = ImageTk.PhotoImage(Image.open(path2).resize((300, 300), Image.ANTIALIAS))


            panel2 = Label(root, image=img2, borderwidth=0)
            panel2.photo = img2
            panel2.grid(row=3, column=1, columnspan=2,)
            panel2.lift()

        else:
            mineralview.position_label = Label(text="\nSelect folders with the same number of images",
                             font='Helvetica 12 bold', bg=darkish, fg=whitish)
            mineralview.position_label.grid(row=6, column=2, pady=20, columnspan=3)

        dir1 = Label(text=mineralview.dir1,
                                           font='Helvetica 12 bold', bg=darkish, fg=whitish)
        dir1.grid(row=4, column=4, columnspan=2, )

        dir2 = Label(text=mineralview.dir2,
                     font='Helvetica 12 bold', bg=darkish, fg=whitish)
        dir2.grid(row=4, column=1, columnspan=2, )

        pathlabel1 = Label(text=path.replace(mineralview.dir1, ""),
                     font='Helvetica 12 bold', bg=darkish, fg=code_green)
        pathlabel1.grid(row=5, column=4, columnspan=2, )

        pathlabel2 = Label(text=path2.replace(mineralview.dir2, ""),
                     font='Helvetica 12 bold', bg=darkish, fg=code_green)
        pathlabel2.grid(row=5, column=1, columnspan=2, )


        root.update_idletasks()
        root.update()

    # This runs when the program refreshes.
    if mineralview.state == -1:
        mineralview.state = 0
        mineralview.count1 = -2
        mineralview.count2 = -1
        mineralview.position = 0
        mineralview.dir1 = ""
        mineralview.dir2 = ""
        root.destroy()
        start_program()
        running()






running()



