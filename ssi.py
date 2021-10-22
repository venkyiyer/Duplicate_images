from skimage.measure import compare_ssim
import os
import cv2
import imutils

images_path = ('./images')
contents = sorted(os.listdir(images_path))
threshold_images_path = ('./ssidiff')

for img1, img2 in zip(contents[0::1], contents[1::1]):
    img_name1 = img1
    img_name2 = img2
    img1 = cv2.imread(images_path+'/'+img1)
    img2 = cv2.imread(images_path+'/'+img2)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, difference = compare_ssim(gray1, gray2, full= True)
    diff = (difference * 255).astype("uint8")
    print("SSIM: {}".format(score))
    thresh = cv2.threshold(diff, 100, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img1,(x, y),(x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite(threshold_images_path+'/'+img_name1+'_'+img_name2+'_'+str(score)+'.png',diff)
