# im2kml
This python program converts image's exif data to kml or ply which can be viewed in gogole earth and cloud compare/ Meshlab. It read coordinate information stored in exif data of image.

# Dependencies
1. numpy
2. pexif (To be installed seperately)
3. simplekml
4. Tkinter
5. plyfile
6. utm

# How to run

1. Clone this repository inside the im2kml folder, using the following command to you can simply download it as zip. 
```
git clone https://gitlab.com/manish.indshine/im2kml.git
cd im2kml
git checkout develop
```
2. Make sure you have python2.7 installed in your system. If not then download it from here [Python2.7](https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi)

    - Once python 2.7 is installed, then set environment path for python 2.7. To do this follow steps given below
        - Right Click "MY PC" and select properties
        - Go to "Advance system settings" option
        - Go to "Advance" tab
        - Click on "Environment variable"
        - From the list given at bottom search "PATH" 
        - Click on edit to add new path as the location where Python2.7 is installed. It is generally in "C:/python27" folder
        - Once added this python path to "PATH" variable, open command prompt and type "python" and press enter to check if python is installed or not.

3. Once installed correctly, you are ready to install dependencies.
    * To install maximum dependencies at once, simply type
        > python -m pip install -r requirements.txt
    * To install pexif, which read and write exif data to images, download pexif from this link as zip [pexif](https://github.com/mcbridejc/pexif.git) and extract it or if you have git then clone it using following link
        ```
        git clone https://github.com/mcbridejc/pexif.git
        ```
    * After download or cloning, open cmd and change directory to folder where it is downloaded or cloned. To change change directory see **Point 6**
    * After changing directory to folder where it is downloaded (you must a setup.py file inside it), type 
        ```
        python setup.py build
        python setup.py install
        ```
            
4. Dependencies list is given above, to install them open cmd and type 
    > python -m pip install utm
5. This will install utm library in python. Similarly install all the other required libraries.
6. Once all the libraries are installed, you are ready to run im2kml program. Open cmd and go to folder where **im2kml.py** is downloaded.
7. Copy its location and open command prompt (cmd). To go to the folder for example -  **D:/python** , type in cmd as follows
    ```
    cd D:/python
    D: (press enter)
    ```
8. This will change your cmd directory to *D:/python*
9. Now type as given below and press enter
    > python *im2kml.py*
10. A file dialog box will appear. For example - If images are kept in *D:/UAV_images/Day1*. Then select *D:/UAV* folder
11. This will scan all the folder present inside UAVimages kept in that folder and extract coordinate information from them.
12. A kml file with same name as the folder will be created. Open this kml file to view images and image's location. 

