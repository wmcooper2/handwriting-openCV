import cv2
import numpy as np
#start position for y coordinate
img = cv2.imread("test/1.jpg", 0)
x1 = 90
x2 = 1250
y1 = 70
y2 = 710
counter = 1

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

#main loop
while True:
    #show image
    cv2.imshow("image",img)
    k = cv2.waitKey(5)

    #if press ESC stop everything
    if k == 27:
        break

    # rotate
    if k == 103: #g
        y2 -= 1
        img = rotate_image(img, -0.1)
        cv2.moveWindow("image", 50, 50)
    if k == 104: #h
        y2 += 1
        img = rotate_image(img, 0.1)
        cv2.moveWindow("image", 50, 50)

    if k == 115: #s
        cv2.imwrite(str("rotated/"+str(counter)+".jpg"), img)

        

cv2.destroyAllWindows()
