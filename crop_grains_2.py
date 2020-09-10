import os
import platform
import time
import pandas as pd

from PIL import Image
import png
import sys
import glob
import numpy as np

global grain_pixels
global total_pixels

grain_pixels = []
total_pixels = []


# Chops the selected image into the individual grains based on the bounding boxes from the selected CSV file
def chop_image(photo_val, csv_path, savepath, constraint_name= "Diameter", min_val= 180, max_val=999999):

    if (max_val == ""):
        max_val = 999999

    if (min_val == ""):
        min_val = 0


    ##OPEN EXCEL
    df = pd.read_csv(csv_path)
    df['buffer'] = 20

    ##LISTS FOR BOUNDING BOXES
    bbmin0 = df['Bounding Box Minimum_0'] - df['buffer']
    bbmin1 = df['Bounding Box Minimum_1'] - df['buffer']
    bbmax0 = df['Bounding Box Maximum_0'] + df['buffer']
    bbmax1 = df['Bounding Box Maximum_1'] + df['buffer']
    objnum = df['object_id']

    print(constraint_name)
    constraint = df[constraint_name]

    filename = os.path.join(photo_val)
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
            savename = savefolder + str(df["object_id"][i]) + ".tif"
            count+=1
            print(savename)
            savenamefinal = os.path.join(savename)
            # io.imsave(savenamefinal,crop_imgo)
            cropped_image.save(savename)
            # Increase Counter by one
            # i += 1


def crop_grains(input, output, photo_in, x, y):

    grain_pixels.clear()
    total_pixels.clear()

    sys.setrecursionlimit(10 ** 6)

    image = Image.open(input)
    photo = Image.open(photo_in)

    global image_rgb
    image_rgb = image.convert("RGB")

    global photo_rgb
    photo_rgb = photo.convert("RGB")


    global height
    height = image.height

    global width
    width = image.width

    global coords
    coords = [None] * (width+2)
    for i in range(width+2):
        coords[i] = [True] * (height+2)

    # if (is_black(width//2, height//2)):
    #     print("black on left and top")
    #     floodfill(x-20, y-20)
    #
    # elif (is_black(width//2, 0)):
    #     print("black on top")
    #     floodfill(x, y-20)
    #
    # elif (is_black(0, height//2)):
    #     print("black on left side")
    #     floodfill(x-20, y)
    #
    # else:

    if is_valid_color(x, y):
        floodfill(x, y)
    else:

        r = 1

        while not (is_valid_color(x+r, y+r) or is_valid_color(x-r, y-r) or is_valid_color(x+r, y-r) or is_valid_color(x-r, y+r)):
            r+=1

        if is_valid_color(x+r, y+r):
            floodfill(x+r, y+r)
        elif is_valid_color(x-r, y-r):
            floodfill(x-r, y-r)
        elif is_valid_color(x+r, y-r):
            floodfill(x+r, y-r)
        elif is_valid_color(x - r, y + r):
            floodfill(x - r, y + r)




    print("found pixels: " + grain_pixels.__len__().__str__())



    # export to png output

    p = convert_array(width, height)
    #print(p.__str__())
    f = open(output, 'wb')

    w = png.Writer(width, height, greyscale=False, transparent=(0,0,0))
    w.write(f, p)



def is_black(x, y):
    r, g, b = image_rgb.getpixel((x, y))

    if (r < 10 and g < 10 and b < 10):
        return True
    else:
        return False


def is_valid_color(x, y):

    # Checks that the pixel doesn't already exist
    if (x < width and x >= 0 and y < height and y >= 0):
        r,g,b = image_rgb.getpixel((x, y))

        if (g > 100):
            return True

        else:
            return False

    else:
        return False



def floodfill(x, y):

    # assume surface is a 2D image and surface[x][y] is the color at x, y.

    theStack = [ (x, y) ]
    while (len(theStack) > 0):

        x, y = theStack.pop()

        if (x == width):
            continue
        if (x == -1):
            continue
        if (y == -1):
            continue
        if (y == height):
            continue


        if not is_valid_color(x, y):
            continue

        if (x < coords.__len__()):
            if (y < coords[x].__len__()):
                if (coords[x][y] != None):

                    r, g, b = photo_rgb.getpixel((x, y))

                    grain_pixels.append([x, y, r, g, b])

                    coords[x][y] = None

                    theStack.append((x + 1, y))  # right
                    theStack.append((x - 1, y))  # left
                    theStack.append((x, y + 1))  # down
                    theStack.append((x, y - 1))  # up


#
# def find_boundary_initial(x, y, coords):
#
#     theStack = [(x, y)]
#
#     if (x < width and x >= 0 and y < height and y >= 0):
#
#         r, g, b = photo_rgb.getpixel((x, y))
#
#
#         grain_pixels.__add__([x, y, r, g, b])
#
#
#         if is_valid_color(x+1, y):
#             find_boundary(x+1, y, 0, 1, coords)
#
#         if is_valid_color(x, y+1):
#             find_boundary(x, y+1, 1, 1, coords)
#
#         if is_valid_color(x - 1, y):
#             find_boundary(x - 1, y, 2, 1, coords)
#
#         if is_valid_color(x, y-1):
#             find_boundary(x, y-1, 3, 1, coords)
#
#
# def find_boundary(x, y, d, rec, coords):
#
#     if (x < width and x >= 0 and y < height and y >= 0):
#
#         r, g, b = photo_rgb.getpixel((x, y))
#
#         if (x < coords.__len__()):
#             if (y < coords[x].__len__()):
#                 if (coords[x][y] != None):
#
#                     grain_pixels.append([x, y, r, g, b])
#
#                     coords[x][y] = None
#
#                   # for debugging
#                   #  print(x, y)
#                   #  print("~~~~~~~~~")
#
#                     if d != 0:
#                         if is_valid_color(x + 1, y):
#                             find_boundary(x + 1, y, 1, rec + 1, coords)
#
#                     if d != 1:
#                         if is_valid_color(x - 1, y):
#                             find_boundary(x - 1, y, 0, rec+1, coords)
#
#                     if d != 2:
#                         if is_valid_color(x, y+1):
#                             find_boundary(x, y+1, 3, rec+1, coords)
#
#                     if d != 3:
#                         if is_valid_color(x, y-1):
#                             find_boundary(x, y-1, 2, rec+1, coords)


def convert_array(width, height):


    # create an array of size WIDTH x HEIGHT

    result = [None] * height
    for i in range(height):
        result[i] = [0] * width * 3

    #print(result.__str__())

    # insert the grain_pixels


    for i in range(grain_pixels.__len__()):
        pixel = grain_pixels[i]

        row = result[pixel[1]]

        row[pixel[0]*3] = pixel[2]
        row[pixel[0]*3+1] = pixel[3]
        row[pixel[0]*3+2] = pixel[4]

    return result



def run_colorize():
    print("running colorize")

    ##FOLDER WITH PICTURES TO BE COLORIZED##
    sourcepath = "output/chopped_tiff/"
    savepath = "../../output/colorized/"

    os.chdir(sourcepath)

    segimg = '*.tif'

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

