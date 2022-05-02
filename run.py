import matplotlib.pyplot as plt
import os
import numpy as np
import glob
import astropy
from astropy.io import fits

# file_dir = os.path.dirname(os.getcwd()) + '/Sample-images'
lights = []

arr = os.listdir()

## function to plot an image cube
## for this code a "cube" means a stack of image data arrays

for file in glob.glob("*.fit" or "*.fits" or "*.FIT" or "*.FITS"):
    lights.append(file)

raw_image_data = {}
for image_name in lights: raw_image_data[image_name] = fits.getdata(image_name)

lights_cube = np.stack([raw_image_data[science_frame] for science_frame in lights], axis=0)
lights_stacked = np.average(lights_cube, axis=0)


if len(lights_stacked.shape) == 3:
    lights_stacked = lights_stacked[0, :, :]

hdu = fits.PrimaryHDU(lights_stacked)
hdu.writeto('lights_stacked.fits', overwrite=True)
file_name = 'lights_stacked.fits'

def moments(data):
    """Returns (height, x, y, width_x, width_y)
	the gaussian parameters of a 2D distribution by calculating its
	moments """
    total = data.sum()
    X, Y = np.indices(data.shape)
    x = (X * data).sum() / total
    y = (Y * data).sum() / total
    col = data[:, int(y)]
    width_x = np.sqrt(np.abs((np.arange(col.size) - y) ** 2 * col).sum() / col.sum())
    row = data[int(x), :]
    width_y = np.sqrt(np.abs((np.arange(row.size) - x) ** 2 * row).sum() / row.sum())
    height = data.max()
    print(width_x, width_y, height)
    return height, x, y, width_x, width_y


data = fits.open(file_name)
image = data[0].data
psf = image
print(np.shape(psf))
result = moments(psf)

print(result[3], result[4])

print("seeing = ", (result[3] + result[4]) / 2.0 * 0.0439)

fig = plt.figure()
ax = plt.plot(psf)
plt.show()
