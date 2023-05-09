from PIL import Image

# load image from file
im = Image.open("IMG_6711.jpg")

# print out some basic data
print("Image dimensions: ", im.size)
print("Image format: ", im.format)
print("Image mode: ", im.mode)

# show image
im.show()

# iterate through the pixels and display them
width, height = im.size

# use a double FOR loop to iterate through 2D data

# walk through the width (x-axis) first
for x in range(0, width):

    # walk through the height (y-axis) second
    for y in range(0, height):
        colors = im.getpixel((x, y))

        if im.mode == "RGB":
            # unpack colors since tuple
            red, green, blue = colors
            # print("RBG values at ", (x, y), " are ", (red, green, blue))

# so now we can iterate through colors...can we adjust them?
# attempt no. 1; remove all red from the image
# walk through the width (x-axis) first
for x in range(0, width):

    # walk through the height (y-axis) second
    for y in range(0, height):
        loc = (x, y)

        red, green, blue = im.getpixel(loc)

        new_color = (green, blue, red)

        im.putpixel(loc, new_color)

        # if red > 235 and green > 235 and blue > 235:
        #    new_color = (0, 0, 0)
        #    im.putpixel(loc, new_color)
        # new_color = (0, green, blue)
        # im.putpixel(loc, new_color)

# display modified image
im.show()
