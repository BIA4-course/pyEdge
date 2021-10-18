"""
pyEdge: a small utility to detect edges in images
"""

# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.feature import canny
from skimage.filters import sobel, prewitt

# TODO: these should be passed by the user
# if no output filename is passed, it should be generated automatically
input_filename = "test_images/DAPI.png"
output_filename = "DAPI_edges.png"

# Read image
img = imread(input_filename)
# Detect edges
# TODO: user should choose edge detecting algorithm
img_edges = canny(img, sigma=7)

# Display
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].imshow(img, cmap="gray")
ax[1].imshow(img_edges, cmap="gray")

for a in ax:
    a.axis("off")

plt.show()

# Save to file
imsave(fname=output_filename, arr=img_edges)