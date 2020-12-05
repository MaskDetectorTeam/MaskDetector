# MaskDetector
## Who are we?
We are Marc Vana, Catalin Gavrila and Mihai Marcu, 3 students currently in the 10th grade at National College "Emil Racovita" Cluj-Napoca. We are very passionated by programming. We want to change the world by making it a better place.

## How can our project help?
We developed a simple Android app which can be used in this pandemic. Using a camera, it detects the people without the masks on and captures them in some photos. The files are uploaded to a cloud storage and then retrieved by the app. The app shows the photos with the people's name (who appear in it) in a simple but useful way.

The project can be used with surveillance cameras in schools, meeting rooms, or even on the street. We can make the world a safer place during this big pandemic by finding the people who don't wear the masks.

## Some tehnical specifications?
Diving into tehnical aspects, the app is made in Android Studio using Kotlin. The project also contains Python files for mask detection, face recognition and upload to cloud storage. Firstly, we run the Python scripts. The detector file finds in the camera feed whether there are people who don't wear the mask or not, the recognizer file performs a quick face recognition to find who the people are and the uploader file uploads the captures (with people's names) into Google Firebase. More detailed instructions are made inside the scripts. Secondly, the app retrieves the photos from the cloud storage and shows them in a list, chronologically.

## Instructions on how to run
Firstly, you need to run the Python scripts in this order:
    -> 1_detector.py (will open the primary video input from your PC/laptop and will start recording whether you have a mask or not; press 'q' to terminate)
    -> 2_recognizer.py (will perform face recognition on the frames saved previously with you (without the mask) with simple logs in the console and save them in another folder)
    -> 3_uploader.py (will upload the recognized faces previously saved on Firebase with simple logs in the console)
After this, you can refresh the android app and the photos saved on Firebase by the python scripts will successfully show in the app's list.



