
# python3 distance_detector.py -f 300 -d 0.51
import numpy as np
import time
import cv2
import tkinter
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face_height", type=int, default=300,
	help="height of the face in pixels")
ap.add_argument("-d", "--distance", type=float, default=0.51,
	help="show warning after if less than that distance in meters")
args = vars(ap.parse_args())

def create_root():
    """Create Tkinter stream (for display a message)"""
    root = tkinter.Tk()
    root.title("Warning!")
    root.resizable(width="false", height="false")
    root.minsize(width=350, height=50)
    root.maxsize(width=350, height=50)
    text_for_message = "Warning! You are too close to the monitor"
    warning_message = tkinter.Text(root)
    warning_message.pack() 
    warning_message.insert(tkinter.END, text_for_message) 
    return root


root = create_root()

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while(True):
    
    _, frame = cap.read()
    last_time = time.time()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    if faces == ():
        root.destroy()
        root = create_root()
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        known_height = args['face_height']
        distance = known_height/h*args['distance']
        if distance < args['distance']:
          
            root.update()
        else:
         
            root.destroy()
            root = create_root()
     
        k=h/4
        text = "Face height: {}".format(k)
        print(k)
        cv2.putText(frame, text, (int(x), int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       
        cv2.putText(frame, "%.2fm" % (distance),
                    (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                    2.0, (0, 255, 0), 3)
   
    cv2.putText(frame, "FPS: %f" % (1.0 / (time.time() - last_time)),
                            (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

   
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


root.destroy()
cap.release()
cv2.destroyAllWindows()