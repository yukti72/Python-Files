import cv2
a=cv2.VideoCapture(0)

while True:
    b,c=a.read()
    c=cv2.flip(c,1)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    cv2.imshow("image 1",c)
cv2.destroyAllWindows()
a.release()

