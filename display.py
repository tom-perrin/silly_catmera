### Imports
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.animation import FuncAnimation

import os

# --------------------------------------------------

### Script

# Define global image folder
im_folder = './silly_cats'

# Image displaying function
def im_display(im_name, extension='jpg', mydpi=100):
    '''
    Displays image located at {im_folder}/{im_name}.{ext}
    
    :param im_name: name of the image
    '''
    im_path = os.path.join(im_folder, im_name+'.'+extension)

    # Check image path
    if not os.path.exists(im_path):
        print(f'ERROR: Cannot find file at {os.path.abspath(im_path)}')
    
    else:
        im_data = img.imread(im_path)

        height, width, depth = im_data.shape
        myfigsize = (height/mydpi, width/mydpi)

        plt.rcParams['toolbar'] = 'None' # Remove toolbar
        fig = plt.figure(num='Silly Catmera', figsize=myfigsize, dpi=mydpi)
        
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        im = ax.imshow(im_data, aspect='equal')

        def update(frame):
            im.set_data(im_data)
            return [im]

        ani = FuncAnimation(fig, update, frames=None, interval=50, blit=True)
        plt.show()

# Test
im_name = 'bleh'
im_display(im_name)