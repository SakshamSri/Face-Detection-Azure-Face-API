import cv2
import time
import datetime

def run_video_capture():
    print(datetime.datetime.now())    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print(datetime.datetime.now())
    cap = cv2.VideoCapture(0)
    print(datetime.datetime.now())
    frames = 0
    count = 0
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)        
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w+10,y+h+10), (255,255,0), 2)        
            detected_face = img[y:y+h+10, x:x+w+10]
            if frames == 4 :
                status = cv2.imwrite('face_detected' + str(count) + '.jpg', detected_face)
                count = count+1
                frames = -5
                time.sleep(20)
        
        # if flag == 16:
            # flag = 0
            # break
        cv2.imshow('img', img)
        # status = cv2.imwrite('face_detected.jpg', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
        if len(faces) is 0:
            continue
        
        frames = frames + 1
        print(frames)

    # cap.release()
    # cv2.destroyWindow('img')
# cv2.destroyAllWindows()
run_video_capture()