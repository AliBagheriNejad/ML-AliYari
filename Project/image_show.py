import cv2
import os
import tqdm
import numpy as np
import matplotlib.pyplot as plt

# path = r'G:\Masters\Term 2\Machine Learning\Project\HH-modified\Source'
path = r'G:\Masters\Term 2\Machine Learning\Project\HH-modified\Target'

# Files
names = os.listdir(path)

# Modify loop
for i in tqdm.tqdm(range(len(names))):

    im_path = os.path.join(path,names[i])
    image = cv2.imread(im_path)
    # Resize
    image_modified = image[70:820,200:1000,:]
    cv2.imwrite(im_path, image_modified)
