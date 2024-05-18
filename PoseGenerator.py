import cv2
import mediapipe as mp
import urllib.request
import numpy as np
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import PyQt5
#from PIL import img
from IPython.display import Video
import nb_helpers
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

w = 1920
h = 1080

numPoses = 0

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

while True: 

    ret,frame = cap.read() # return a single frame in variable `frame`

    # Create a MediaPipe `Pose` object
    with mp_pose.Pose(static_image_mode=True, 
            model_complexity=2,
                    enable_segmentation=True) as pose:
            
        # Read the file in and get dims
        #image = cv2.imread(frame)
        #display(image)

        # Convert the BGR image to RGB and then process with the `Pose` object.
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
    # Copy the image
    segmented_image = frame.copy()

    # Probability threshold in [0, 1] that says how "tight" to make the segmentation. Greater value => tighter.
    tightness = .3

    # Stack the segmentation mask for 3 RGB channels, and then create a filter for which pixels to keep

    if np.stack((results.segmentation_mask,) * 3, axis=-1).any() == None: 
        continue

    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > tightness

    # Creates a black background image
    bg_image = np.zeros(frame.shape, dtype=np.uint8)
    figure = np.zeros(frame.shape, dtype=np.uint8)

    # Can change the color of this background by specifying (0-255) RGB values. We choose green-screen green.
    bg_image[:] = [0, 0, 0]
    figure[:] = [255, 255, 255]

    # For every pixel location, display the corresponding pixel from the original imgae if the condition in our filter is met (i.e. the probability of being part of the object is above the inclusiogn threshold), or else display corresponding pixel from the background array (i.e. green)
    segmented_image = np.where(condition, figure, bg_image)
    
    cv2.imshow("pose", segmented_image)

    if cv2.waitKey(1) & 0xFF == ord('q'): #save on pressing 'y' 

        if numPoses < 10: 
            numPoses += 1

            filename = f"pose{numPoses}.jpg"

            cv2.imwrite(filename, segmented_image)

        else: 
            cv2.destroyAllWindows()
            break