import cv2
import os
print(os.getcwd())

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    r, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # change minsize based on application. It can be bigger than the default
    # 30,30 for a webcam, plus the bigger the minsize, the faster the whole
    # thing runs!
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,
    minSize=(200,200), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
#cv2.waitKey(0)

capture.release()
cv2.destroyAllWindows()