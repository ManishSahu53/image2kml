

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

import os
from fnmatch import fnmatch
import pexif,shutil
import numpy as np
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import * 
import simplekml
from plyfile import PlyData, PlyElement
import utm

root = Tk()

location = tkFileDialog.askdirectory(initialdir = "/",title = "Select photos location");
pattern = '*.jpg'
image_list = listdir_fullpath(location);
folders_in_images = list(filter(os.path.isdir, image_list));
no_of_folders = len(folders_in_images);
lat = [];
long = [];
ele = [];
kml = simplekml.Kml()

vertex = np.array([(0,0,0)],dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
vertex_color = np.array([(0,0,0)],dtype=[('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])

for k in range(0,no_of_folders):
    photo_list = [];
    
    directory = str(folders_in_images[k]); 
    kml_name = directory
    print(directory);
    for path, subdirs, files in os.walk(directory):
        for title in files:
            if fnmatch(title, pattern):
                file = path+"\\"+ title;
                f = open(file, 'rb');
                jpeg = pexif.JpegFile.fromFile(file);
                cord= jpeg.get_geo();
                kmlpath = os.path.relpath(file,location);
                pnt = kml.newpoint(description='<img src="' + kmlpath +'" alt="picture" width="400" height="300" align="left" />',coords=[(cord[1],cord[0],cord[2])],altitudemode = "absolute") 
                pnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_square.png"
                utm_cord = utm.from_latlon(cord[0], cord[1])
                vertex =np.append(vertex,np.array([(utm_cord[0], utm_cord[1], cord[2])],dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')]), axis=0)
                vertex_color= np.append(vertex_color,np.array([(0, 255, 0)],dtype=[('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]), axis=0)
    kml.save(os.path.join(directory, '.kml')) 


