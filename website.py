from astropy.io import fits
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import astropy

st.set_page_config(layout="wide", page_title='York Seeing')
row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((3, .2, 0.55, .1))
row0_1.title('York Observatory Seeing Network')
with row0_2:
    st.write('')
row0_2.subheader('Web App by [Toby Avila](https://www.linkedin.com/in/toby-avila-118080208/)')
st.subheader('_Was the data helpful?_')

uploaded_file = st.file_uploader(
    "Upload your fit file(s)", type=["fit", "json"], accept_multiple_files=True
)

if uploaded_file is not None:
    lights = []
    for i in range(len(uploaded_file)):
        name = uploaded_file[i].name
        lights.append(name)

    raw_image_data = {}
    for image_name in lights: raw_image_data[image_name] = fits.getdata(image_name)

    lights_cube = np.stack([raw_image_data[science_frame] for science_frame in lights], axis=0)
    lights_stacked = np.average(lights_cube, axis=0)
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

    if len(np.shape(psf)) == 3:
        psf = psf[0, :, :]

    st.markdown(np.shape(psf))
    result = moments(psf)

    st.markdown(result[3], result[4])

    st.markdown("seeing = " + str((result[3] + result[4]) * 0.5 * 0.0439))

    fig = plt.figure()
    ax = plt.plot(psf)
    plt.show()
