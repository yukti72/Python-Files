import cv2
a=cv2.imread("C:/Users/yukti singh/Desktop/991e59fb6ba1df773552daf9efa76eac.jpg")
b=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
c=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("image 1",a)
cv2.imshow("image 2",b)
cv2.imshow("image 3",c)

##
