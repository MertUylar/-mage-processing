import cv2
thres=0.5
#img= cv2.imread("lena.png")
cap =cv2.VideoCapture("MOT17-04-DPM.mp4")
cap.set(3,640)
cap.set(4,480)
classNames=[]
classFile='coco.names'
with open (classFile,'rt')as f:
    classNames=f.read().rstrip('\n').split('\n')
print(classNames)
configPath ='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath='frozen_inference_graph.pb'

net=cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.8/127)
net.setInputMean((127.5,127.5,127.5) )
net.setInputSwapRB(True)
while True :
    success,img=cap.read()
    classIds,confs,bbox=net.detect(img,confThreshold=thres)
    print(classIds,bbox)

    if len(classIds) !=0:
        for classIds, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classIds-1].upper(),(box[0]+10,box[1]+38),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img, str(confidence),(box[0] +150, box[1] + 38),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    cv2.imshow('Output',img)
    cv2.waitKey(1)



