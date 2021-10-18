"""
pyEdge: a small utility to detect edges in images
"""

# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.feature import canny
from skimage.filters import sobel, prewitt
import sys
import argparse as ap

# Create a parser for command line arguments
parser = ap.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="The input filename")
parser.add_argument("-o", "--output", required=False, help="The output filename. If not specified, _edges is appended to the input filename.")

# This creates a dictionary of the parameters
# e.g. {"input": "filename.jpg", "output": "filename_edges.jpg"}
params = vars(parser.parse_args())

input_filename = params['input']

if params['output'] is None:
    input_split = input_filename.split(".")   
    output_filename = input_split[0] + "_edges." + input_split[1]
    print(f"No output file specified, automatically saving to {output_filename}")
else:
    output_filename = params['output']

def plot_results(img, img_edges, cmap="gray"):
    """Plots the results of edge detection

    Args:
        img (np.array): The original image
        img_edges (np.array): The detected edges
        cmap (str, optional): The colourmap. Defaults to "gray".

    Returns: nothing
    """
    # Display
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax[0].imshow(img, cmap=cmap)
    ax[1].imshow(img_edges, cmap=cmap)

    for a in ax:
        a.axis("off")

    plt.show()

def detect_edges(img, method="canny"):
    """Detect edges in an image

    Args:
        img (np.array): The image
        method (str, optional): The edge-detecting algorithm. Defaults to "canny".
    
    Returns (np.array): The edges of the image
    """

    if method == "canny":        
        return canny(img, sigma=7)
    elif method == "prewitt":
        return prewitt(img)
    elif method == "sobel":
        return sobel(img)
    else:
        sys.exit(f"{method} is an unsupported edge-detecting method!")

# Read image
img = imread(input_filename)
# Detect edges
# TODO: user should choose edge detecting algorithm
img_edges = detect_edges(img, "sobel")

plot_results(img, img_edges)

# Save to file
imsave(fname=output_filename, arr=img_edges)