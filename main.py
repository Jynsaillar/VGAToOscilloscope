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


def ProcessImage(vga):
    if len(vga) < 5:
        print("Not enough VGA options specified, aborting.")
        return

    # Loads a color image in grayscale.
    img = cv.imread(vga.Filename, 0)

    # Resizes image.
    img = ScaleImage(img, vga.Width, vga.Height, cv.INTER_LINEAR)
    
    # Runs Canny edge detection filter over the image and returns it.
    edgesFilename = vga.Filename + " -> Canny Edge Detection"
    edges = cv.Canny(img, vga.Width, vga.Height)

    # Display modified images:
    DisplayImage(vga.Filename, img)
    DisplayImage(edgesFilename, edges)


def DisplayImage(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)


def ScaleImage(img, newWidth, newHeight, interpolationMode):
    return cv.resize(img, (newWidth, newHeight), interpolation = interpolationMode)


if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    Main(argc, argv)
