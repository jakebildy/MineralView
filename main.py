import glob
import math
import time
from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk,Image
import pandas as pd
import csv
import os
import random
import numpy as np


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


# The Bounding Box class.
class bounding_box:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def crop_image(self, image, number):
        print("cropping image", number)
        img = Image.open(image)
        s2 = img.crop((self.left, self.top, self.right, self.bottom))
        s2.save("output/" + str(number) + ".png")

# Chops the selected image into the individual grains based on the bounding boxes from the selected CSV file
def chop_image(constraint_name= "Diameter", min_val= 0, max_val=999999):

    popup.destroy()

    if (max_val == ""):
        max_val = 999999

    if (min_val == ""):import glob
import math
import time
from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk,Image
import pandas as pd
import csv
import os
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


# The Bounding Box class.
class bounding_box:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def crop_image(self, image, number):
        print("cropping image", number)
        img = Image.open(image)
        s2 = img.crop((self.left, self.top, self.right, self.bottom))
        s2.save("output/" + str(number) + ".png")

# Chops the selected image into the individual grains based on the bounding boxes from the selected CSV file
def chop_image(constraint_name= "Diameter", min_val= 0, max_val=999999):

    popup.destroy()

    if (max_val == ""):
        max_val = 999999

    if (min_val == ""):
        min_val = 0

    print("TESTING:  ")
    print(max_val)
    print(min_val)

    ##STRINGS FOR FILE PATHS OF PICTURE AND CSV

    start_time = time.time()

    # Save path example: F:/ilastik/testfolder/
    savepath = filedialog.askdirectory(initialdir = "/",title = "Select output directory")+'/'

    ##OPEN EXCEL
    df = pd.read_csv(csvpath)
    df['buffer'] = 20

    ##LISTS FOR BOUNDING BOXES
    bbmin0 = df['Bounding Box Minimum_0'] - df['buffer']
    bbmin1 = df['Bounding Box Minimum_1'] - df['buffer']
    bbmax0 = df['Bounding Box Maximum_0'] + df['buffer']
    bbmax1 = df['Bounding Box Maximum_1'] + df['buffer']
    objnum = df['object_id']

    print(constraint_name)
    constraint = df[constraint_name]

    filename = os.path.join(picpath)
    # imgo = io.imread(filename,plugin='pil')
    image = Image.open(filename)

    ##LOOP FOR CROPPING

    i = 0

    count = 1

    for i in range(len(bbmin0)):

        if bbmin0[i] < 0:
            a = 0
        else:
            a = int(bbmin0[i])

        if bbmin1[i] < 0:
            b = 0
        else:
            b = int(bbmin1[i])

        if bbmax0[i] < 0:
            c = 0
        else:
            c = int(bbmax0[i])

        if bbmax1[i] < 0:
            d = 0
        else:
            d = int(bbmax1[i])

        ##    a = int(bbmin0[i])
        ##    b = int(bbmin1[i])
        ##    c = int(bbmax0[i])s
        ##    d = int(bbmax1[i])

        if (float(constraint[i]) > float(min_val) and float(constraint[i]) < float(max_val)):
            cropped_image = image.crop((bbmin0[i], bbmin1[i], bbmax0[i], bbmax1[i]))

            savefolder = savepath
            savename = savefolder + str(count) + ".tif"
            count+=1
            print(savename)
            savenamefinal = os.path.join(savename)
            # io.imsave(savenamefinal,crop_imgo)
            cropped_image.save(savename)
            # Increase Counter by one
            # i += 1
    print(time.time() - start_time)





def popupmsg():

    global popup
    popup = Tk()
    popup.wm_title("Set Constraints")

    global constraint_name
    constraint_name = ""

    label = ttk.Label(popup, text="Name:", textvariable=constraint_name)
    label.pack(side="top", fill="x", pady=10)
    entry = Entry(popup)
    entry.pack(side="top", fill="x", pady=10)


    label2 = ttk.Label(popup, text="Min Value:")
    label2.pack(side="top", fill="x", pady=10)
    global entry2
    entry2 = Entry(popup)
    entry2.pack(side="top", fill="x", pady=10)

    label3= ttk.Label(popup, text="Max Value:")
    label3.pack(side="top", fill="x", pady=10)
    global entry3
    entry3 = Entry(popup)
    entry3.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(popup, text="Apply", command = lambda: chop_image(constraint_name=entry.get(), min_val=entry2.get(), max_val=entry3.get()))
    B1.pack()

    B2 = ttk.Button(popup, text="Skip", command=chop_image)
    B2.pack()
    popup.mainloop()

# Opens the .csv file generated by Ilastik and uses it to split a second image of the same mineral into
# the individual grains using bounding boxes.
def open_csv():
    print("Open CSV pressed")
    csv_file = filedialog.askopenfile(initialdir="/", title="Select .csv file",filetypes = (("csv files","*.csv"),))
    return csv_file.name


# Opens the source image to be chopped and call the chop image function
def open_source_image(csv):
    image = filedialog.askopenfile(initialdir="/", title="Select image file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("tiff files","*.tiff"),))
    print(image.name)
    global picpath
    picpath = image.name
    global csvpath
    csvpath = csv
    popupmsg()


def run_mineral_segmentation():
    open_source_image(open_csv())

def run_colorize():
    print("running colorize")
    sourcepath = filedialog.askdirectory(initialdir="/", title="Select source folder")
    savepath = filedialog.askdirectory(initialdir="/", title="Select output directory") + '/'

    os.chdir(sourcepath)

    ##FOLDER WITH PICTURES TO BE COLORIZED##
    segimg = '*.tiff'

    segimfnames = glob.glob(segimg)

    print("result: ")
    print(segimfnames)

    for fname in segimfnames:

        print(fname)

        im = Image.open(fname)

        imarray = np.array(im)

        im1 = np.where(imarray == 1, 255, imarray)
        im2 = np.where(imarray == 2, 255, imarray)
        im3 = np.where(imarray == 3, 255, imarray)

        # numpy.set_printoptions(threshold=sys.maxsize)

        stacked_img = np.stack((im1, im2, im3), axis=-1)
        test = Image.fromarray(stacked_img)
        newfname = savepath + fname
        print(newfname)
        test.save(newfname)


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
    global subMenu2
    subMenu2 = Menu(menuBar)
    global subMenu3
    subMenu3 = Menu(menuBar)

    menuBar.add_cascade(label='File', menu=subMenu)
    subMenu.add_command(label='New', command=new)

    menuBar.add_cascade(label='Grain Segmentation', menu=subMenu2)
    subMenu2.add_command(label='Start', command=run_mineral_segmentation)

    menuBar.add_cascade(label='Colorize', menu=subMenu3)
    subMenu3.add_command(label='Choose Folder', command=run_colorize)


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
            old_path = path

            path = glob.glob(mineralview.dir1+"/" + mineralview.position.__str__() + ".*")[0]

            if (old_path != path):
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

            print("PATH 2: ")
            print(path2)

            old_path2 = path2

            # Opens Image 2.
            path2 = glob.glob(mineralview.dir2 + "/" + mineralview.position.__str__() + ".*")[0]

            if (old_path2 != path2):
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
