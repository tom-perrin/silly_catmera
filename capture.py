### Imports 

import cv2

# --------------------------------------------------

### Script

def get_camera():
    '''
    Creates a video capture object associated to the camera
    '''
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    return cap


def grab_frame(cap):
    '''
    Returns the current frame from video capture as RGB image.
    
    :param cap: video capture object associated to the camera
    '''
    ret, frame = cap.read()
    if not ret:
        return None
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return rgb_frame

# --------------------------------------------------

### Test

# grab_frame(get_camera())