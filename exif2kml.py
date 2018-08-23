""" exif to kml"""

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

# Importing libraries

import os
from fnmatch import fnmatch
import pexif
import shutil
import numpy as np
import Tkinter
import Tkconstants
import tkFileDialog
from Tkinter import *
import simplekml
from plyfile import PlyData, PlyElement
import utm

# Defining root in Tkinter
root = Tk()

# Asking for photos location 
location = tkFileDialog.askdirectory(
    initialdir="/", title="Select photos location")
    
lat = []
long = []
ele = []
kml = simplekml.Kml()

# looking inside the folder for jpg or JPG file formats
for path, subdirs, files in os.walk(location):
    for title in files:
        fileExt=os.path.splitext(title)[-1]
        if fileExt == '.JPG':
            print(title)
            jpeg = pexif.JpegFile.fromFile(os.path.join(location,title))
            cord = jpeg.get_geo()
            kmlpath = title #os.path.relpath(title, location)
            pnt = kml.newpoint(description='<img src="' + kmlpath + '" alt="picture" width="400" height="300" align="left" />',
                               coords=[(cord[1], cord[0], cord[2])], altitudemode="absolute")
            pnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_square.png"

        elif fileExt == '.jpg':
            print(title)
            jpeg = pexif.JpegFile.fromFile(os.path.join(location,title))
            cord = jpeg.get_geo()
            kmlpath = os.path.relpath(title, location)
            pnt = kml.newpoint(description='<img src="' + kmlpath + '" alt="picture" width="400" height="300" align="left" />',
                               coords=[(cord[1], cord[0], cord[2])], altitudemode="absolute")
            pnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_square.png"
        
        else:
            continue

kml.save(os.path.join(location, os.path.basename(location)+'.kml'))
