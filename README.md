# Must Dance: Hawk Hacks 2024 <br>
Check out our demo at [https://www.youtube.com/watch?v=fZ9sNM9EYOQ](url)!

## Part 1: Software 
### How does it work? <br>
Pose generator works by taking a camera capture of the screen and processing it with the object <code>Pose</code> from mediapipe. An image is created with a segmentation mask overlay of the human subject. The inside of the subject is rewritten to black while everything else is white. This segmented image is saved as a pose.
#### Libraries used
- cv2
- mediapipe
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
### Challenges Encountered
1. Landmark coordinates out of range
    1. Landmarks are supposed to be a decimal number from 0 to 1. However we were getting negative numbers and numbers greater than 1, so we experienced many issues with range
    2. When landmarks are off screen, mediapipe has an approximation of where they are leading to results that do not fit the postcondition

2. Serial communication
    1. When trying to get our Arduino circuit and Python program to communicate through USB, we ran into many errors where the port was busy or connected improperly
    2. When we were first trying to send signal from the Python program to the Arduino program, the signal sent improperly as we needed to add a delay after opening the serial port to properly send signals

These are just two examples as we had *way* too many bugs and issues

<br><br><br>

## Part 2: Hardware
### How does it work?
#### Turret Control
### Materials
- Cardboard
- 1x 3D printer
- 1x DC motor
- 1x 9V battery
- 1x Keyestudio 8x8 Dot Matrix
- Foam golf balls
- Wires (M-M, M-F)
- 1x Arduino UNO board
- 1x Sunfounder Clutch Gear Servo
- 1x Songle relay circuit
- 1x Elegoo breadboard
### Challenges Encountered
1. Designing a mechanism to effectively store and launch balls.
    1. Proper DC motor selection and postioning on the barrel, taking into consideration the number of motors to use, maintaining a steady connection with the ball, and optimizing the spin of the ball for travel time.
    2. Loading up multiple balls within the system; designing a mechanism to both push balls into the barrel, and allowing the next one in.
    3. Pushing balls into the barrel with the servo. Had many issues with snugly fitting balls within the barrel, while still being wide enough to not cause jamming.

2. Issues with electrical wiring.
    1. Powering motors with adequate supply of voltage, seperate from the servo motor. Another circuit system was made, while still being connected to the same breadboard/Arduino board.
    2. Implementing a relay module into the circuit, which allows a signal to be sent from the Arduino to power on the DC motor. 
Overall issues with sorting out breadboard connections; many wires led to a confusing and unorganized wire system.
