##scripts to convert 3-class FRAUAS dataset JSON label to PNG file

import labelme
import matplotlib.pyplot as plt
import glob
import os
from PIL import Image
import numpy as np

folder = 'C:/Users/Abbad/Desktop/Winter21-22/AIS/Project/FRA-UAS-Automation-LAB-main/FRA-UAS-Automation-LAB-main/data/custom/'

print(folder)

for i in range(2):
    f = [os.path.split(file)[-1][:-5] for file in glob.glob(folder+f'{i}/json/*.json')]
 
    f1 = [file for file in glob.glob(folder + f'{i}/rgb/*.jpg')]
    for file in f1:
        name = os.path.split(file)[-1][:-4] 
        json_dir = folder + f'{i}/json/'
        dir = folder + f'{i}/label/'
        print(dir)
        if name in f:
            label_file = labelme.LabelFile(filename=json_dir+name+'.json')
            img = labelme.utils.img_data_to_arr(label_file.imageData)
            class_names = []
            class_name_to_id = {'human':1,'table':2,'chair':3,'robot':4,'backpack':5,'free':6,'patch':7,'sofa':8,'shoe':9,'open_door':10,'close_door':11}
            lbl, _ = labelme.utils.shapes_to_label(
                        img_shape=img.shape,
                        shapes=label_file.shapes,
                        label_name_to_value=class_name_to_id,
                    )
            mask = (lbl!=1)&(lbl!=2) ##since our dataset has only 3 class, we label other classes except free space and human to obstacles.
            lbl[mask] = 0
            Image.fromarray(lbl.astype(np.uint8)).save(dir+name+'.png')
        else:
            zeros = np.zeros((480,640))
            Image.fromarray(zeros.astype(np.uint8)).save(dir+name+'.png') ##images that don't have label will be labellel all 0s