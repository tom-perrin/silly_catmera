### Imports

from display import setup_window
from capture import get_camera, grab_frame
from silly_cater import CAT_MAP, cat_picker

import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.animation import FuncAnimation

import os

# --------------------------------------------------

### Script

# Global image folder
im_folder = './silly_cats'
extension = 'jpg'
side = 512 # image side, assuming all are squares

# Setup capture, figure and animation interval
cap = get_camera()
fig, cam_handle, cat_handle = setup_window(2*side, side)
interval = 20 # corresponds to 50 FPS

# Dictionary of loaded images
loaded_cats = {}


def update(frame_count):
    '''
    Animation function running every interval.
    
    :param frame_count: current frame number
    '''
    rgb_frame = grab_frame(cap)

    if rgb_frame is not None:
        # Update camera
        cam_handle.set_data(rgb_frame)

        # Update cat
        im_name = cat_picker(rgb_frame)

        if im_name not in loaded_cats:
            im_path = os.path.join(im_folder, f'{im_name}.{extension}')
            if os.path.exists(im_path):
                loaded_cats[im_name] = img.imread(im_path)
        
        cat_handle.set_data(loaded_cats[im_name])
    
    return [cam_handle, cat_handle]


# Start animation
ani = FuncAnimation(fig, update, interval=interval, blit=True, cache_frame_data=False)
plt.show()

# Cleanup when closing window
cap.release()