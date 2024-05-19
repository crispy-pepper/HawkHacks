# Pew Pew Pose: Hawk Hack <br>

## Part 1: Software 
### How does it work? <br>
Pose generator works by taking a camera capture of the screen and processing it with the object <code>Pose</code> from mediapipe. An image is created with a segmentation mask overlay of the human subject. The inside of the subject is rewritten to black while everything else is white. This segmented image is saved as a pose.
#### Libraries used
- cv
- 2mediapipe
- numpy
- os
- win32api <br><br>

The main simulation has 6 "modes": start/calibration page, main menu, turret mode, timed mode, make-pose mode, and the ending page. When ran, the program begins at the start page where the user must align their body parts to a predetermined silohoutte (check pose generator). It uses the <code>Pose</code> object from mediapipe to identify landmarks. Blue lines are drawn to show the users figure. The user passes calibration if all landmarks are within the silohouette. The user is then brought to the main menu where the they use the nose landmark to select from making a custom pose, playing timed mode, playing turret mode, and exiting. Custom poses are made using a slightly modified (changed to fit properly in the while loop) version of <code>Pose_Generator</code> (explained previously).
#### Libraries used
- cv2
- mediapipe
- numpy
- time
- random
- os
- serial
- playsound
- win32api
### Challenges Encountered<br><br>


## Part 2: Hardware
### How does it work?
#### Turret Control
### Materials
- Arduino UNO
- rhvzdhvs
### Challenges Encountered
