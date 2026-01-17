### Imports

import matplotlib.pyplot as plt

# --------------------------------------------------

### Script

def setup_window(w, h, mydpi=100):
    '''
    Sets the window up to display the silly cat images

    :param w: width of displayed image
    :param h: height of displayed image
    :param dpi: DPI of the screen on which the image is displayed
    '''
    plt.rcParams['toolbar'] = 'None' # Remove toolbar
    fig = plt.figure(num='Silly Catmera', figsize=(w/mydpi, h/mydpi), dpi=mydpi)
    
    # Left subplot : camera
    ax_cam = fig.add_axes([0, 0, 0.5, 1])
    ax_cam.axis('off')
    im_cam = ax_cam.imshow([[0]], aspect='equal')

    # Right subplot : silly cat
    ax_cat = fig.add_axes([0.5, 0, 0.5, 1])
    ax_cat.axis('off')
    im_cat = ax_cat.imshow([[0]], aspect='equal')
    return fig, im_cam, im_cat