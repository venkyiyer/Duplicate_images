# An implementation without any pre-processing of the image. Used canny edge detector to find differences in between frames. 
import cv2
import numpy as np
import os

# path for the images
images_path = ('./images')
threshold_images_path = ('./wp')
contents = sorted(os.listdir(images_path))
duplicates = []

def compare_frames_change_detection(prev_frame, next_frame, min_contour_area):
    
    img_name1 = prev_frame
    img_name2 = next_frame

    prev_frame = cv2.imread(images_path + '/' + prev_frame)
    next_frame = cv2.imread(images_path + '/' + next_frame)
    
    diff_img = cv2.subtract(prev_frame, next_frame)

    _, contours, _= cv2.findContours(cv2.Canny(diff_img, 0, 255), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    blank_image = np.zeros((np.shape(prev_frame)[0], np.shape(prev_frame)[1], 3), np.uint8)
    img_contour = cv2.drawContours(blank_image, contours, -1, (255, 255, 255), 1)

    score = 0
    res_cnts = []
    for c in contours:
        if cv2.contourArea(c) < min_contour_area:
            continue
        res_cnts.append(c) 
        score += cv2.contourArea(c)
    blank_image = np.zeros((np.shape(prev_frame)[0], np.shape(prev_frame)[1], 3), np.uint8)
    img_contour = cv2.drawContours(blank_image, res_cnts, -1, (255, 255, 255), 1)
    #cv2.imwrite(threshold_images_path+'/'+img_name1+'_'+img_name2+'_'+str(score)+'.png',img_contour)


for img1, img2 in zip(contents[0::1], contents[1::1]):
    compare_frames_change_detection(img1, img2, 500)

print('Finished')