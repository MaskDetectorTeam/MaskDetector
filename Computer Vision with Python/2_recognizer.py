'''
Do you think that was all? Hahaha!

You can't get rid of me that fast.

Now let's start the journey of recognition... together.
'''

'''
We import the libraries. You already know some of them, right?
    pickle -> save/load the image encodings into/from a file in binary mode
'''
# Importing the libraries
import face_recognition
import cv2
import numpy as np
import os
import pickle

'''
Global variables, important. The dictionary keys are the names of people we
have taken pictures of, while their values are their pictures encoded.
A person has more than one picture.

In the comments is a code which should be run only the first time we create
the people's faces 'database'. It writes down in the encodings.txt all
encodings with names.

If it is not the first time, we just load them back. It saves a lot of time.
You can print the 3 variables out and you will see what they are containing.
(make sure lines 58-64 were run before checking the variables)
'''
# Encodings
all_face_encodings = {}
known_face_encodings = []
known_face_names = []

'''
# If it is the first time
for image in os.listdir('images'):
    current_image = face_recognition.load_image_file("images/" + image)
    image_class = image.split('_')[0].upper() + ' ' + image.split('_')[1].upper()
    all_face_encodings[image_class] = []
for image in os.listdir('images'):
    try:
        current_image = face_recognition.load_image_file("images/" + image)
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        image_class = image.split('_')[0].upper() + ' ' + image.split('_')[1].upper()
        all_face_encodings[image_class].append(current_image_encoded)
        print('Done: ' + image)
    except:
        print('Image ' + image + " does not contain faces.")

with open('encodings.txt', 'wb') as f:
    pickle.dump(all_face_encodings, f)
'''

with open('encodings.txt', 'rb') as f:
    all_face_encodings = pickle.load(f)

for key, values in all_face_encodings.items():
    for value in values:
        known_face_encodings.append(value)
        known_face_names.append(key)


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

'''
For each file we downloaded before in the detection step (main 'for' loop),
we resize it and then we find all faces in it. For each face, we compare it
to all know faces to find which person/people is/are in it (first 'for' loop).
In the second 'for' loop we draw the results for each face found in the
current file. We simply draw a rectangle with a name. I kept the red color
because the person/people does/do not have masks on.
'''
for path in os.listdir('frames'):
    frame = cv2.imread('frames/' + path)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "UNKNOWN"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    '''
    Final step here. Whoa, this wasn't that hard, was it?
    
    I save the files in the 'firebase' folder with a strict name format.
    Let's say we have a file which contains N faces in it and for every face
    we know who the person is. The file will be saved as:
        firstname1_lastname1__firstname2_lastname2__...__firstnameN_lastnameN.png
    You can see some examples in the 'firebase' folder.
    '''
    file_name = ""
    for name in face_names:
        file_name = file_name + "__" + name.split(' ')[0] + '_' + name.split(' ')[1]
    file_name = file_name[2:]
    cv2.imwrite('firebase/' + file_name + '.png', frame)
    print('Done: ' + 'frames/' + path)


    