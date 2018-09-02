import cv2
import glob

images = glob.glob("images/*.jpg")

for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(100,100))
    cv2.imshow(image,re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
