import glob, json, os, shutil
from pascal_voc_writer import *

voc_folder_name = 'CanistersSynthetic'
dataset = 'synth'
json_path_pattern = 'cansynth/2019*/*/*/*.json' #'not_can/*/*.json'

"""
Hierarchy:
Data Directory
-> images
--> image0.png
--> image1.png
--> imageN.png
-> labels
--> labels0.txt
--> labels1.txt
--> labelsN.txt

In other words labels folder should be located next to the image folder in the same directory named "labels".
"""

if not os.path.exists(voc_folder_name):
    os.mkdir(voc_folder_name)

for subfolder in ['Annotations', 'JPEGImages', 'labels', 'ImageSets', 'ImageSets/Main']:
    if not os.path.exists(os.path.join(voc_folder_name, subfolder)):
        os.mkdir(os.path.join(voc_folder_name, subfolder))

image_index = 0
image_set = open(os.path.join(voc_folder_name, 'ImageSets', 'Main', 'triplecanister_{}'.format(dataset)), 'w')
list_file = open('{}.txt'.format(dataset), 'w')

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for file in glob.glob(json_path_pattern):
    print(file)
    with open(file) as json_file:
        data = json.load(json_file)
        image_path = file.split('/')
        image_path[-1] = image_path[-1].split('.')[0] + '.png'
        image_path[-2] = 'img'
        image_path = os.path.join(*image_path)
        image_name = str(image_index).zfill(5)
        image_set.write(image_name+'\n')
        new_image_path = '{}/JPEGImages/{}.jpg'.format(voc_folder_name, image_name)
        list_file.write(new_image_path+'\n')
        image_index += 1
        try:
            shutil.copy(image_path, new_image_path)
        except:
            print('error', image_path, new_image_path)
        
        label_txt = open('{}/labels/{}.txt'.format(voc_folder_name, image_name), 'w')
        w = data["size"]["width"]
        h = data["size"]["height"]
        writer = Writer(new_image_path, w, h)
        for detBox in data['objects']:
            if detBox['bitmap'] == None and detBox['classTitle'] == 'canister-general-bbox':
                p1, p2 = detBox['points']['exterior']
                x1, y1 = p1
                x2, y2 = p2
                x_min = min(x1, x2)
                x_max = max(x1, x2)
                y_min = min(y1, y2)
                y_max = max(y1, y2)
                writer.addObject('canister', x_min, y_min, x_max, y_max)
                bb = convert((int(w), int(h)), [float(a) for a in [x_min, x_max, y_min, y_max]])
                label_txt.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
        
        writer.save('{}/Annotations/{}.xml'.format(voc_folder_name, image_name))
        label_txt.close()
        
list_file.close()        
image_set.close()
                