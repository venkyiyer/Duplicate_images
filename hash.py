# A demo example to understand how hash works when the images have lighting changes. 
import os
import imagehash
from PIL import Image

images_path = ('./images')
contents = sorted(os.listdir(images_path))
duplicates = []

def file_hash(img1, img2):
        
        return (imagehash.average_hash(Image.open(images_path+'/'+img1)), (imagehash.average_hash(Image.open(images_path+'/'+img2))))

for img1, img2 in zip(contents[0::1], contents[1::1]):
    illum_prev_img1, illum_next_img2 = file_hash('c23-1616780130983.png', 'c23-1616780473745.png')
    normal_img1, normal_img2 = file_hash('c23-1616689078329.png', 'c23-1616689120916.png')
    print(illum_prev_img1)
    print(illum_prev_img1)
    print(normal_img1)
    print(normal_img2)
    exit()
    