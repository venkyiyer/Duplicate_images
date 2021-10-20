import cv2
import numpy as np
import imutils
import os

images_path = ('./images')
threshold_images_path = ('./Difference')
contents = sorted(os.listdir(images_path))

def draw_color_mask(img, borders, color=(0, 0, 0)):
    h = img.shape[0]
    w = img.shape[1]
    x_min = int(borders[0] * w / 100)
    x_max = w - int(borders[2] * w / 100)
    y_min = int(borders[1] * h / 100)
    y_max = h - int(borders[3] * h / 100)
    img = cv2.rectangle(img, (0, 0), (x_min, h), color, -1)
    img = cv2.rectangle(img, (0, 0), (w, y_min), color, -1)
    img = cv2.rectangle(img, (x_max, 0), (w, h), color, -1)
    img = cv2.rectangle(img, (0, y_max), (w, h), color, -1)
    return img

def preprocess_image_change_detection(img1,img2, gaussian_blur_radius_list=(11,11), black_mask=(5, 10, 5, 0)):
    img1 = cv2.imread(images_path+'/'+img1)
    img2 = cv2.imread(images_path+'/'+img2)
    gray1 = img1.copy()
    gray2 = img2.copy()
    gray1 = cv2.cvtColor(gray1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(gray2, cv2.COLOR_BGR2GRAY)
    if gaussian_blur_radius_list is not None:
        for radius in gaussian_blur_radius_list:
            gray1 = cv2.GaussianBlur(gray1, (radius, radius), 0)
            gray2 = cv2.GaussianBlur(gray2, (radius, radius), 0)
        gray1 = draw_color_mask(gray1, black_mask)
        gray2 = draw_color_mask(gray2, black_mask)
        return gray1, gray2

def compare_frames_change_detection(prev_frame, next_frame, min_contour_area):
    frame_delta = cv2.absdiff(prev_frame, next_frame)
    thresh = cv2.threshold(frame_delta, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    score = 0
    res_cnts = []
    for c in cnts:
        if cv2.contourArea(c) < min_contour_area:
            continue
        res_cnts.append(c)
        score += cv2.contourArea(c)
    cv2.imwrite(threshold_images_path+'/'+img_name1+'_'+img_name2+'_'+str(score)+'.png',thresh)

for img1, img2 in zip(contents[0::1], contents[1::1]):
    img_name1 = img1
    img_name2 = img2
    img1, img2 = preprocess_image_change_detection(img1, img2, gaussian_blur_radius_list=(11,11), black_mask=(5, 10, 5, 0))
    compare_frames_change_detection(img1, img2, 50)



    






    
