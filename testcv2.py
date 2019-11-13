import cv2
import time
import datetime
import os
import uploaderHelperFunctions as UHF

last_person = []
last_time = None
def run_video_capture():
    print(datetime.datetime.now())    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print(datetime.datetime.now())
    cap = cv2.VideoCapture(0)
    print(datetime.datetime.now())
    frames = -2
    count = 0
    FLAG = True
    while FLAG:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)        
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w+35,y+h+35), (255,255,0), 2)        
            # detected_face = img[y:y+h+35, x:x+w+35]
            if frames == 8:
                name = 'face_detected' + str(count) + '.jpg'
                status = cv2.imwrite(name, img)
                det_face = str(os.path.abspath(name))
                print(det_face)
                frames = -4
                # time.sleep(5)
                try:
                    UHF.testImage(det_face,last_person, last_time)
                    FLAG = False
                    break
                    print('hehe')
                except:
                    print('error in testImage()')
                # time.sleep(0.5)
                count = count+1
                
                # time.sleep(1)
        
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
#run_video_capture()