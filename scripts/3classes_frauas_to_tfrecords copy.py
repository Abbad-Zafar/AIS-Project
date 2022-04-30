##scripts to convert 3-class frauas data to tfrecords

import tensorflow as tf
import glob
import os
import numpy as np
from PIL import Image

def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _float_feature(value):
  """Returns a float_list from a float / double."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def image_example(p_rgb,p_label,p_x,p_y,p_z):
    rgb_string = open(p_rgb, 'rb').read()
    label_string = open(p_label, 'rb').read()
    label = tf.image.decode_png(label_string,dtype = tf.uint8).numpy()
    x_string = open(p_x, 'rb').read()
    y_string = open(p_y, 'rb').read()
    z_string = open(p_z, 'rb').read()
    total_pixel = 480*640
    weight = []
    for i in range(3):
        pixel = np.sum(label==i)
        weight.append(float(pixel)/float(total_pixel)+1e-7)
    weight = (np.median(weight)/np.array(weight)).tolist()
    feature = {
        'rgb': _bytes_feature(rgb_string),
        'label': _bytes_feature(label_string),
        'x': _bytes_feature(x_string),
        'y': _bytes_feature(y_string),
        'z': _bytes_feature(z_string),
        'weight':_float_feature(weight)
    }

    return tf.train.Example(features=tf.train.Features(feature=feature))

##this is a function to sort the names in the right order)
def sorter1(item):
    return int(item[:-5])

rgb = []
label = []
x = []
y = []
z = []


##we divided the dataset into 5 different subfolders corresponding to 5 different setttings
folder = 'C:/Users/Abbad/Desktop/Winter21-22/AIS/Project/FRA-UAS-Automation-LAB-main/FRA-UAS-Automation-LAB-main/data/custom/'
filename = sorted([os.path.split(file)[-1] for file in glob.glob(folder+'0/json/*.json')],key=sorter1)
for i in range(10,len(filename)):
    print( "i = ",i)
    rgb.append(folder+'0/rgb/'+ filename[i][:-5] + '.jpg')
    label.append(folder+'0/label/'+filename[i][:-5]+'.png')
    x.append(folder+'0/x/'+filename[i][:-5]+'.jpg')
    y.append(folder+'0/y/'+filename[i][:-5]+'.jpg')
    z.append(folder+'0/z/'+filename[i][:-5]+'.jpg')
    




    
## create training TFRecords
cnt=0
record_file = folder + 'tfrecords/train_frauas_3classes.tfrecords'
with tf.io.TFRecordWriter(record_file) as writer:
    for p_rgb,p_label,p_x,p_y,p_z in zip(rgb,label,x,y,z):
        cnt+=1
        tf_example = image_example(p_rgb,p_label,p_x,p_y,p_z)
        writer.write(tf_example.SerializeToString())
    writer.close()
print('number of training images: ', cnt)


rgb = []
label = []
x = []
y = []
z = []




filename = sorted([os.path.split(file)[-1] for file in glob.glob(folder+'0/json/*.json')],key=sorter1)
for i in range(0,10):
    print( "i = ",i)
    print( "file = ",folder+'0/rgb/'+filename[i][:-5]+'.jpg')

    rgb.append(folder+'0/rgb/'+filename[i][:-5]+'.jpg')
    label.append(folder+'0/label/'+filename[i][:-5]+'.png')
    x.append(folder+'0/x/'+filename[i][:-5]+'.jpg')
    y.append(folder+'0/y/'+filename[i][:-5]+'.jpg')
    z.append(folder+'0/z/'+filename[i][:-5]+'.jpg')
    

    
##create validation TFRecords
cnt=0
record_file = folder + 'tfrecords/val_frauas_3classes.tfrecords'
with tf.io.TFRecordWriter(record_file) as writer:
    for p_rgb,p_label,p_x,p_y,p_z in zip(rgb,label,x,y,z):
        cnt+=1
        tf_example = image_example(p_rgb,p_label,p_x,p_y,p_z)
        writer.write(tf_example.SerializeToString())
    writer.close()
print('number of validation images: ',cnt)



