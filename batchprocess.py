import cv2
import glob

images = glob.glob("images/*.jpg")

for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    print(image)
    cv2.imwrite("resized/resized_"+image[7:],re)
