
import cv2
a=cv2.VideoCapture(0)
data=cv2.CascadeClassifier("C:/Users/yukti singh/Desktop/TechieNest/Haarcascade files/haarcascade_frontalface_default.xml")

while True:
    b,c=a.read()
    c=cv2.flip(c,1)
    gray=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
    faces=data.detectMultiScale(gray)
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(c,(x,y),(x+w,y+h),(0,255,200),2)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    cv2.imshow("image 1",c)
cv2.destroyAllWindows()
a.release()
