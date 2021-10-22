import hashlib
import imagehash
import os
import numpy as np
import cv2
from PIL import Image

# images_path = ('./images')
# contents = sorted(os.listdir('/home/venkys/Duplicate_images/images'))
# duplicates = []
# hash_keys = dict()

# #for img1, img2 in  zip(contents[0::1], contents[1::1]):
# #    print(img1)
# #    print(img2)
# img1 = ih.whash(Image.open(images_path+'/'+'c23-1616689163591.png'))
# img2 = ih.whash(Image.open('/home/venkys/Duplicate_images/DifferenceGB/'))
# print(img2)
# print(img2)
# exit()

# if filehash not in hash_keys: 
#     hash_keys[filehash] = index
# else:
#     duplicates.append((index,filename))
#     print(duplicates)

#hash_keys[filehash]



def file_hash(filepath):
        
        return print(imagehash.average_hash(Image.open(filepath)))

file_hash('/home/venkys/Duplicate_images/images/c23-1616689078329.png')
file_hash('/home/venkys/Duplicate_images/images/c23-1616689120916.png')


# #if os.path.isfile(images_path+'/'+filename):
#     with open('/home/venkys/Duplicate_images/images/c23-1616692132577.png', 'rb') as f:
#     #filehash = hashlib.md5(f.read()).hexdigest()
    #print(filehash)
    #exit()
# if filehash not in hash_keys: 
#     hash_keys[filehash] = index
# else:
#     duplicates.append((index,hash_keys[filehash]))

# print(duplicates)


