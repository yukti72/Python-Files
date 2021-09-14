import cv2
a=cv2.imread("C:/Users/yukti singh/Desktop/991e59fb6ba1df773552daf9efa76eac.jpg")
b=cv2.resize(a,(0,0),fx=0,fy=0.5)
c=cv2.resize(a,(500,500))
cv2.imshow("image 1",a)
cv2.imshow("image 2",b)
cv2.imshow("image 3",c)
