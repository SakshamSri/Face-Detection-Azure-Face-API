import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    flag = 0
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)        
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        detected_face = img[y:y+h, x:x+w]
        status = cv2.imwrite('face_detected.jpg', detected_face)
        flag = 1
        break
        # for(ex, ey, ew, eh) in eyes:
    if flag == 1:
        break
    cv2.imshow('img', img)
    # status = cv2.imwrite('face_detected.jpg', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
# cv2.destroyAllWindows()