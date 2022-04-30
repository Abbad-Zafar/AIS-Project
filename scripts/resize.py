from PIL import Image
import os, sys

path = "C:/Users/Abbad/Desktop/Winter21-22/AIS/Project/FRA-UAS-Automation-LAB-main/FRA-UAS-Automation-LAB-main/data/New_json/5/z/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,480), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()