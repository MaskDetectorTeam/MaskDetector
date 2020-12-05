# MaskDetector
## Who are we?
We are Marc Vana, Catalin Gavrila and Mihai Marcu, 3 students currently in 10th at National College "Emil Racovita" Cluj-Napoca. We are very passionate about programming. We want to change the world by making it a better place.

## How can our project help?
We developed a simple Android app which can be used in this pandemic. Using a camera, it detects the people without the masks on and captures them in some photos. The files are upload into a cloud storage and then retrieved by the app. The app shows the photos with the people's name (who appear in it) in a simple but useful way.

The project can be used with surveillance cameras in schools, meeting rooms, or even on street. We can make the world a safer place during this big pandemic by finding the people who don't wear the masks.

## Some tehnical specifications?
Diving into tehnical aspects, the app is made in Android Studio with Kotlin. The project also contains Python files for mask detection, face recognition and upload to cloud storage. Firstly, we run the Python scripts, in the given order: detector, recognizer, uploader. The detector file finds in the camera feed whether there are people who don't wear the mask or not, the recognizer file performs a quick face recognition to find who the people are and the uploader file uploads the captures (with people's names) into Google Firebase. More detailed instructions are made inside the scripts. Secondly, the app retrieves the photos from the cloud storage and shows them in a list, chronologically.



