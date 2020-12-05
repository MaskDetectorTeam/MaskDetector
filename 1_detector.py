# Read README file first.
'''
Helloooo worldddd!!!
This is a simple mask detector program based on OpenCV and MobileNetV2.

Let's explain a bit how it works, shall we?
(I have put a comment before any important part)
'''

'''
Firstly, we import the standard libraries:
    cv2 -> OpenCV for detection
    keras -> deep learning model: MobileNetV2 & simple function
             to transform an image to a numpy array
    numpy -> any machine learning program has it :D for maths
    time -> counting seconds

So far so good, right?
'''
# Libraries
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import time

'''
Then, we initialize some important variables.
frame_number -> we count the frames, so we can save frame number i as frame_i
last_time_mask -> the last time we found a person without a mask
faceCascade -> xml file which contains the frontal face cascade
model -> !already trained! model (MobileNetV2) saved in a h5 file

Do you think it's getting hard? To be honest, YES.
'''
# Global variables
frame_number = 0
last_time_mask = time.time()
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
model = load_model("mask_detector_model.h5")

'''
After these steps, we are ready to start the webcam feed with OpenCV.
Like in any program with OpenCV, we have a VideoCapture object and then
we loop through every frame until a key is pressed (line 96).
We increase the frame count every time.
Then we detect with cascade.detectMultiScale() on the gray frame all the faces
in that frame. We also keep the RGB frame for further use.
We save all the faces found in faces.

Can you still follow my code?
'''
# Start video feed
video_capture = cv2.VideoCapture(0)
while True:
    frame_number += 1
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    faces_list=[]
    preds=[]
    '''
    Now brace for impact! :D
    
    So we have all the faces found in faces. We iterate through it.
    For each face, we preprocess its frame so it can be fed into MobileNetV2
    model and find if the person has the mask on or not.
    After we find the label, we save a picture of he/she every 2 seconds and
    update the last_time_mask variable. We have the image under frames folder,
    with the name frame_i (where i = frame_number variable).
    Then, we show a rectangle around the face, also writing the label and the
    probability (with red if the person doesn't have a mask, green otherwise).
    All these drawings are made on the original frame, so then we can show
    it back as a video (line 111)
    '''
    # Go through all faces found
    for (x, y, w, h) in faces:
        face_frame = frame[y:y+h,x:x+w]
        face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
        face_frame = cv2.resize(face_frame, (224, 224))
        face_frame = img_to_array(face_frame)
        face_frame = np.expand_dims(face_frame, axis=0)
        face_frame =  preprocess_input(face_frame)
        faces_list.append(face_frame)
        if len(faces_list)>0:
            preds = model.predict(faces_list)
        for pred in preds:
            (mask, withoutMask) = pred
        
        label = "No Mask"
        if mask > withoutMask:
            label = "Mask"
        
        # If the person doesn't have a mask, save a picture of he/she every 2s
        if label == "No Mask":
            end_time = time.time()
            if end_time - last_time_mask >= 2.0:
                cv2.imwrite('frames/frame_' + str(frame_number) + '.png', frame)
                last_time_mask = end_time
        
        # Show results on the frame (label, probability)
        color = (0, 0, 255)
        if label == "Mask":
            color = (0, 255, 0)
        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        cv2.putText(frame, label, (x, y- 10),
                    cv2.FONT_HERSHEY_DUPLEX, 0.45, color, 2)
 
        cv2.rectangle(frame, (x, y), (x + w, y + h),color, 2)
        
    # Show back the frames as a video
    cv2.imshow('Video', frame)
    # Quit if 'Q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
'''
Final step ladies and gentlemen. Are you still with me?

Two simple lines of code here. We release the video and destroy the OpenCV
window.
'''
# End OpenCV
video_capture.release()
cv2.destroyAllWindows()