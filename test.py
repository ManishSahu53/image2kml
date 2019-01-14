""" exif to kml"""

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def eval_frac(value):
    try:
        return float(value.num) / float(value.den)
    except ZeroDivisionError:
        return None


def gps_to_decimal(values, reference):
    sign = 1 if reference in 'NE' else -1
    degrees = eval_frac(values[0])
    minutes = eval_frac(values[1])
    seconds = eval_frac(values[2])
    return sign*(degrees + minutes / 60 + seconds / 3600)


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

import exifread

location = '/home/indshine-2/Downloads/testing/solar/1.JPG'
#jpeg = pexif.JpegFile.fromFile(location)

# Open image file for reading (binary mode)
f = open(location, 'rb')

# Return Exif tags
tags = exifread.process_file(f, details=False)
ref_lat = tags['GPS GPSLatitudeRef'].values
ref_long = tags['GPS GPSLongitudeRef'].values
lat = gps_to_decimal(tags["GPS GPSLatitude"].values, ref_lat)
long = gps_to_decimal(tags["GPS GPSLongitude"].values, ref_long)
ele = eval_frac(tags["GPS GPSAltitude"].values[0])
