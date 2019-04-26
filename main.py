import numpy as np
import cv2 as cv
import sys
from collections import namedtuple

print(cv.__version__)


def Main(argc, argv):
    # Acquire command line arguments:
    if argc < 6:
        print(
            "Usage: %s <video file> <vga window x> <vga window y> <vga width> <vga height>\n" % argv[0])
        print(
            "Usage: %s <camera id> <vga window x> <vga window y> <vga width> <vga height>\n" % argv[0])
        print(
            "Usage: %s <image file> <vga window x> <vga window y> <vga width> <vga height>\n" % argv[0])
        return

    VGA = namedtuple('VGA', 'Filename X Y Width Height')
    vga = VGA(argv[1],
              int(argv[2]),
              int(argv[3]),
              int(argv[4]),
              int(argv[5]))

    outputPixelCount = vga.Width * vga.Height

    # OpenCV init
    print("File: %s, Pixels: %d" % (vga.Filename, outputPixelCount))
    capture = cv.VideoCapture(vga.Filename)
    if not capture:
        print("Error reading video file.")
        return

    ProcessImage(vga)
    # Cleanup
    cv.destroyAllWindows()
    if capture:
        capture.release()


def ProcessImage(vga):
    if len(vga) < 5:
        print("Not enough VGA options specified, aborting.")
        return

    # Loads a color image in grayscale.
    img = cv.imread(vga.Filename, 0)

    # Resizes image.
    img = ScaleImage(img, vga.Width, vga.Height, cv.INTER_LINEAR)
    imgWidth, imgHeight = img.shape[:2]

    # Runs Canny edge detection filter over the image and returns it.
    edgesFilename = vga.Filename + " -> Canny Edge Detection"
    edges = cv.Canny(img, vga.Width, vga.Height)

    # Takes a binary image (produced by a threshold function or a Canny edge detection function)
    # then extracts the contours and their hierarchy.
    contoursImageFilename = vga.Filename + " -> Contours"
    contoursImage = GetContours(edges)
    color = (0, 255, 0)  # Green
    # Creates 3-dimensional array (R, G, B) sized like the source image filled with uint8s.
    contours = np.zeros(shape=(imgWidth, imgHeight, 3), dtype=np.uint8)
    cv.drawContours(
        image=contours, contours=contoursImage.Contours, contourIdx=-1, color=color)

    # Display modified images:
    DisplayImage(vga.Filename, img)
    DisplayImage(edgesFilename, edges)
    DisplayImage(contoursImageFilename, contours)


def DisplayImage(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)


def ScaleImage(img, newWidth, newHeight, interpolationMode):
    return cv.resize(img, (newWidth, newHeight), interpolation=interpolationMode)


def GetContours(img):
    contours, hierarchy = cv.findContours(
        img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    ContoursImage = namedtuple('ContoursImage', 'Contours Hierarchy')
    contoursImage = ContoursImage(Contours=contours, Hierarchy=hierarchy)
    return contoursImage


if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    Main(argc, argv)
