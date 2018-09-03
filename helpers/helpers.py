import numpy as np
import imageio

def image2vector(image):
    # Read image as vector
    vector = imageio.imread(image, pilmode="RGB")
    # Obtain the shape of the vector the same as vector.shape[0],vector.shape[1],vector.shape[2]
    height, width, channels = vector.shape
    v = vector.reshape((height*width, channels))
    return v


image = '../assets/images/koala.jpg'
image2vector(image)
