from PIL import Image
import png
import sys
from printy import printy
from progress.spinner import Spinner

grain_pixels = []
total_pixels = []


# ARGUMENTS
from_photo = False


if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if (arg == "--photo"):
            from_photo = True


def crop_grains(input, output, x, y):

    print("[", end='')
    printy("🔥[oB]MineralView@", end='')
    print("]", end='')
    printy(" [g]selecting grain:@ [wB]" + input + "@")

    global spinner
    spinner = Spinner('Selecting from [' + str(x) + ", " + str(y) + "]")



    sys.setrecursionlimit(10 ** 6)

    image = Image.open(input)

    global image_rgb
    image_rgb = image.convert("RGB")



    global height
    height = image.height

    global width
    width = image.width

    global coords
    coords = [None] * (width+2)
    for i in range(width+2):
        coords[i] = [True] * (height+2)

    find_boundary_initial(x, y)

    # export to png output

    p = convert_array(width, height)
    #print(p.__str__())
    f = open(output, 'wb')

    w = png.Writer(width, height, greyscale=False, transparent=(0,0,0))
    w.write(f, p)

    print('', end="\r")
    print("[", end='')
    printy("🔥[oB]MineralView@", end='')
    print("]", end='')
    printy(" [g]outputted grain:@ [wB]" + output + "@")





def is_valid_color(x, y):

    # Checks that the pixel doesn't already exist
    if (x < width and x >= 0 and y < height and y >= 0):
        r,g,b = image_rgb.getpixel((x, y))

        if (r < 100):
            return True

        else:
            return False

    else:
        return False




def find_boundary_initial(x, y):

    if (x < width and x >= 0 and y < height and y >= 0):

        if (from_photo) :
            r, g, b = photo_rgb.getpixel((x, y))
        else:
            r, g, b = image_rgb.getpixel((x, y))

        grain_pixels.__add__([x, y, r, g, b])


        if is_valid_color(x+1, y):
            find_boundary2(x+1, y, 0, 1)

        if is_valid_color(x, y+1):
            find_boundary(x, y+1, 1, 1)

        if is_valid_color(x - 1, y):
            find_boundary(x - 1, y, 2, 1)

        if is_valid_color(x, y-1):
            find_boundary(x, y-1, 3, 1)


def find_boundary(x, y, d, rec):

    if (x < width and x >= 0 and y < height and y >= 0):

        if (from_photo):
            r, g, b = photo_rgb.getpixel((x, y))
        else:
            r, g, b = image_rgb.getpixel((x, y))

        if (x < coords.__len__()):
            if (y < coords[x].__len__()):
                if (coords[x][y] != None):

                    grain_pixels.append([x, y, r, g, b])

                    coords[x][y] = None

                  # for debugging
                  #  print(x, y)
                  #  print("~~~~~~~~~")


                    if d != 1:
                        if is_valid_color(x - 1, y):
                            find_boundary(x - 1, y, 0, rec+1)

                    if d != 2:
                        if is_valid_color(x, y+1):
                            find_boundary(x, y+1, 3, rec+1)

                    if d != 3:
                        if is_valid_color(x, y-1):
                            find_boundary(x, y-1, 2, rec+1)



def find_boundary2(x, y, d, rec):

    if (x < width and x >= 0 and y < height and y >= 0):

        if (from_photo):
            r, g, b = photo_rgb.getpixel((x, y))
        else:
            r, g, b = image_rgb.getpixel((x, y))

        if(x < coords.__len__()):
            if (y < coords[x].__len__()):
                if (coords[x][y] != None):
                    spinner.next()
                    grain_pixels.append([x, y, r, g, b])

                    coords[x][y] = None

                    # for debugging
                    #  print(x, y)
                    #  print("~~~~~~~~~")

                    if d != 0:
                        if is_valid_color(x+1, y):
                            find_boundary2(x+1, y, 1,  rec+1)

                    if d != 2:
                        if is_valid_color(x, y+1):
                            find_boundary2(x, y+1, 3, rec+1)

                    if d != 3:
                        if is_valid_color(x, y-1):
                            find_boundary2(x, y-1, 2, rec+1)




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


if from_photo:
    print("[", end='')
    printy("🔥[oB]MineralView@", end='')
    print("]", end='')
    printy(" [w]Enter the grain photo path: @", end='')
    global photo_val
    photo_val = input("")


print("[", end='')
printy("🔥[oB]MineralView@", end='')
print("]", end='')
printy(" [w]Enter the colorized image path: @", end='')
input_val = input("")

print("[", end='')
printy("🔥[oB]MineralView@", end='')
print("]", end='')
printy(" [w]Enter the output path: @", end='')
output_val = input("")

print("[", end='')
printy("🔥[oB]MineralView@", end='')
print("]", end='')
printy(" [w]Enter the center coords separated by a comma: @", end='')
center_coords = input("")

if from_photo:
    photo_image = Image.open(photo_val)
    global photo_rgb
    photo_rgb = photo_image.convert("RGB")

crop_grains(input_val, output_val, int(center_coords.split(",")[0]), int(center_coords.split(",")[1]))
