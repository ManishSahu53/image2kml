""" exif to kml"""
# just make sure that Python 3 code runs fine with 2.7+ too ~98% of the time :)
from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import os
from fnmatch import fnmatch
import exifread
import Tkinter
import Tkconstants
import tkFileDialog
from Tkinter import *
import simplekml
import sys


# Get in fraction
def eval_frac(value):
    try:
        return float(value.num) / float(value.den)
    except ZeroDivisionError:
        return None


# Get in decimal format system
def gps_to_decimal(values, reference):
    sign = 1 if reference in 'NE' else -1
    degrees = eval_frac(values[0])
    minutes = eval_frac(values[1])
    seconds = eval_frac(values[2])
    return sign*(degrees + minutes / 60 + seconds / 3600)


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


# Extracting metadata
def get_geo(file):
    try:
        jpeg = open(file, 'rb')
    except:
        if os.path.isfile(file):
            print('File %s not readable' % (file))
        else:
            print('File %s not found')
        sys.exit()

    tags = exifread.process_file(jpeg, details=False)
    ref_lat = tags['GPS GPSLatitudeRef'].values
    ref_long = tags['GPS GPSLongitudeRef'].values
    lat = gps_to_decimal(tags["GPS GPSLatitude"].values, ref_lat)
    long = gps_to_decimal(tags["GPS GPSLongitude"].values, ref_long)
    ele = eval_frac(tags["GPS GPSAltitude"].values[0])
    return lat, long, ele


# Defining root in Tkinter
root = Tk()

# Asking for photos location
location = tkFileDialog.askdirectory(
    initialdir="/", title="Select photos location")

kml = simplekml.Kml()

# looking inside the folder for jpg or JPG file formats
for path, subdirs, files in os.walk(location):
    for title in files:
        fileExt = os.path.splitext(title)[-1]
        if fileExt.lower() == '.jpg':
            print(title)
            lat, long, ele = get_geo(os.path.join(location, title))
            kmlpath = title  # os.path.relpath(title, location)
            pnt = kml.newpoint(description='<img src="' + kmlpath + '" alt="picture" width="400" height="300" align="left" />',
                               coords=[(long, lat, ele)], altitudemode="absolute")
            pnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_square.png"
        else:
            continue

kml.save(os.path.join(location, os.path.basename(location)+'.kml'))
