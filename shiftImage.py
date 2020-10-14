import cv2
import numpy as np
from pathlib import Path

counter = 0

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def crop_image(img):
    global counter
    # img = cv2.imread("test/1.jpg", 0)
    x1 = 90
    y1 = 70


    #for calibration of the box size
    # x2 = 1250
    # y2 = 710

    width = x1+1148
    height = y1+636

    #main loop
    while True:
        #create bounding box
        cv2.rectangle(img, (x1, y1), (width, height), 0, 1)

        #show image
        cv2.imshow("image",img)
        k = cv2.waitKey(5)

        #if press ESC stop everything
        if k == 27:
            break

        if k == 97: #a
            x1 -= 1
            width = x1+1148
            img = cv2.imread("test/1.jpg", 0)
            cv2.moveWindow("image", 50, 50)
        if k == 115: #s
            x1 += 1
            width = x1+1148
            img = cv2.imread("test/1.jpg", 0)
            cv2.moveWindow("image", 50, 50)

        if k == 101: #e
            y1 -= 1
            height = y1+636
            img = cv2.imread("test/1.jpg", 0)
            cv2.moveWindow("image", 50, 50)
        if k == 100: #d
            y1 += 1
            height = y1+636
            img = cv2.imread("test/1.jpg", 0)
            cv2.moveWindow("image", 50, 50)


    #for calibration
    #     if k == 107: #k
    #         x2 -= 1
    #         img = cv2.imread("test/1.jpg", 0)
    #         cv2.moveWindow("image", 50, 50)
    #     if k == 108: #l 
    #         x2 += 1
    #         img = cv2.imread("test/1.jpg", 0)
    #         cv2.moveWindow("image", 50, 50)
    # 
    #     if k == 117: #u
    #         y2 -= 1
    #         img = cv2.imread("test/1.jpg", 0)
    #         cv2.moveWindow("image", 50, 50)
    #     if k == 106: #j
    #         y2 += 1
    #         img = cv2.imread("test/1.jpg", 0)
    #         cv2.moveWindow("image", 50, 50)

        if k == 98: #b
            print("x1: ", x1)
            print("x2: ", width)
            print("y1: ", y1)
            print("y2: ", height)

    #for calibration
    #         print("x2: ", x2)
    #         print("y2: ", y2)
    #         crop_img = img[y:y+h, x:x+w]

            crop_img = img[y1:height, x1:width]
            cv2.imwrite(str("cropped/"+str(counter)+".jpg"), crop_img)
            counter += 1
            break

    cv2.destroyAllWindows()

for f in Path("handwriting").iterdir():
    img = cv2.imread(str(f.resolve()), 0)
    crop_image(img)
