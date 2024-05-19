# Must Dance: Hawk Hacks 2024 <br>

## Part 1: Software 
### How does it work? <br>
Pose generator works by taking a camera capture of the screen and processing it with the object <code>Pose</code> from mediapipe. An image is created with a segmentation mask overlay of the human subject. The inside of the subject is rewritten to black while everything else is white. This segmented image is saved as a pose.
#### Libraries used
- cv2
- 2mediapipe
- numpy
- os
- win32api <br><br>

The main simulation has 6 "modes": start/calibration page, main menu, turret mode, timed mode, make-pose mode, and the ending page. When ran, the program begins at the start page where the user must align their body parts to a predetermined silohoutte (check pose generator). It uses the <code>Pose</code> object from mediapipe to identify landmarks. Blue lines are drawn to show the users figure. The user passes calibration if all landmarks are within the silohouette. The user is then brought to the main menu where the they use the nose landmark to select from making a custom pose, playing timed mode, playing turret mode, and exiting.<br>

Custom poses are made using a slightly modified (changed to fit properly in the while loop) version of <code>Pose_Generator</code> (explained previously). This pose is added to Poses folder where the other modes can access the new pose<br>

Timed mode is a mode where the user must match as many positions as they can in 30 seconds. Poses from the pose folder are used as an overlay to show the user what to match to. As a little bit of help, Landmarks turn from red to green as they move from outside to inside the regions of interests. Score is tracked by the number of poses and poses switch when matched correctly. <br>

Turret/lives mode is a mode where users are given 3 seconds to match to a pose. A life is loss for each failed attempt. Once all the lives are used up, you get shot by foam balls. This works very similarly to the Timed mode with a few changes in set up. It is a match when all landmarks are within the regions of interests (displayed as an overlay). "Serial_Communication.py" tells the turret when to fire, details are in hardware. <br>

The end page displays the score and offers a button to return to the main menu.


#### Libraries used
- cv2
- mediapipe
- numpy
- time
- random
- os
- serial
- playsound
- win32api <br><br>
### Challenges Encountered<br><br><br>


## Part 2: Hardware
### How does it work?
#### Turret Control
### Materials
- Arduino UNO
- rhvzdhvs
### Challenges Encountered
