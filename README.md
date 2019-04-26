# VGAToOscilloscope
Python scripts to display an image or video on a VGA port for viewing them on an oscilloscope (preferably analog) in XY-Mode.  
Written in Python2.7 using conda for virtual environments.  
Will probably be moved to Python3 later on.  
Mainly uses the Python integration of [OpenCV](https://anaconda.org/conda-forge/opencv) (which is mandatory to function).  
Python tutorials for OpenCV may be found on the [official OpenCV page](https://docs.opencv.org/4.1.0/d6/d00/tutorial_py_root.html).  
A fair warning:  
The Python documentation for OpenCV is, mildly put, lacking.  
Make good use of the search function and Google.

## How To Use:
Launch `main.py` with Python2.7, it expects 5 additional parameters:  
`<path to image file>` `<VGA window size X>` `<VGA window size Y>` `<VGA width>` `<VGA height>`  

### Example
`>python27 main.py "/home/myuser/images/picture.jpg" 1920 1080 200 200`
