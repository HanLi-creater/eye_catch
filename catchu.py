import cv2

mim = cv2.VideoCapture(0)

while True:
    ret,frame = mim.read()

    if ret:
        gry = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        eye_cascade = cv2.CascadeClassifier('righteyes.xml')
        eye_rect = eye_cascade.detectMultiScale(gry,1.5,8)

        for (x,y,w,h) in eye_rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'AMaTeLaSi',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)

        cv2.imshow('frame',frame)
        cv2.waitKey(1)
    else:
        break

    if cv2.waitKey(1) == ord('q'):
        break

