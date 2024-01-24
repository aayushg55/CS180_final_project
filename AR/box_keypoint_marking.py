
# since this skvideo does not support images yet
import skimage.io
import numpy as np
np.float = np.float64
np.int = np.int_
import skvideo.io
import skvideo.utils
import skvideo.datasets
import matplotlib.pyplot as plt
import time

filename = 'box_vid.mp4'
filename_yuv = "box.yuv"

vid = skvideo.io.vread('/Users/aayushgupta/Desktop/FA23/cs180/CS180_final_project/AR_final_project/box_vid.mp4')
T, M, N, C = vid.shape
vid_rgb = skvideo.io.vread('/Users/aayushgupta/Desktop/FA23/cs180/CS180_final_project/AR_final_project/box.yuv', height=M, width=N)

from matplotlib.widgets import Button

def onpick(event):
    if event.inaxes is not None:
        x, y = event.xdata, event.ydata
        points.append((x, y))
        print(f"Point selected: ({x}, {y})")

def save_points(event):
    np.savetxt("selected_points.txt", points, delimiter=",")
    print(f"Saved {len(points)} points to 'selected_points.txt'")
    plt.close()

img = vid_rgb[0,...]

# Display the image with a specific aspect ratio (adjust the value as needed)
aspect_ratio = 'auto'  
fig, ax = plt.subplots(figsize=(10, 15))
plt.tight_layout()

ax.imshow(img)
ax.set_title('Click to select points')

# Connect the event handler for picking points
fig.canvas.mpl_connect('button_press_event', onpick)

# Create a button to save the points
ax_save_button = plt.axes([0.8, 0.05, 0.1, 0.075])
save_button = Button(ax_save_button, 'Save Points')
save_button.on_clicked(save_points)

# List to store selected points
points = []

plt.show()

