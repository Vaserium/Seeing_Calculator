import altair as alt
from PIL import Image
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='York Seeing')
st.header('York Observatory Seeing Network')
# ------------------------------------------------- Displaying all data (just for show and will not actually use data from this)
excel_file = 'sample.csv'

latext = r'''
$$ 
halfMax = \frac{min(data) + max(data)}{2} \\
FWHM = i_1 - i_2 + 1 \\
$$
    where i1 is where the data first drops below halfMax, i2 is where the data last rises above halfMax.  
'''

data = pd.read_csv(excel_file)
dataToDisplay = pd.DataFrame(data)

st.subheader("Project Introduction")
st.markdown(
        "This website contains my 2022 co-op investigation into how seeing conditions affect day-to-day observations at Allan I. Carswell Astronomical Observatory. One of the measurements I was interested in was the seeing value. 'Why do you want to measure the seeing value?' Well, this interactive application containing FWHM(Full Width Half Maximum) data allows you to look at measured seeing conditions so you can stay informed on the night each observation was taken!")
st.markdown(
        "How are seeing and FWHM related? I used the number of pixels across the width of the star at half its maximum value, ")
st.write(latext)

st.markdown(
        "For this investigation I used the Pickering scale which is [a scale from 1 to 10 which represents seeing conditions. A rating of 1 is very poor seeing, and a rating of 10 is perfect seeing](https://freestarcharts.com/pickering-scale#:~:text=Pickering%20scale%20The%20scale%20developed%20by%20Harvard%20astronomer,and%20a%20rating%20of%2010%20meaning%20perfect%20seeing.). "
        "Here are some handy definitions for seeing: “Good seeing” is when the stars that are being displayed on your image twinkle very little; “bad seeing” is when they twinkle a lot. "
        "Check the diagram below to see what this might look like in the Pickerings scale.")

image = Image.open('pickering.png')
st.image(image, caption='Credit: Damian Peach (http://www.damianpeach.com/pickering.htm)', width=620)

st.subheader("Project Data")
st.markdown(
    "For my project I measured the FWHM of stars in an image field from Betelgeuse. "
    "These data were taken at the Allan I Carswell Observatory 1m telescope. "
    "All 2022 data I took with members of the observatory for this project and previous data was used from the archive. "
    "Here is a picture of our star field for Betelgeuse that contains a Pickering Scale value of 3 and a FWHM value of 3.66.")

g1, g2 = st.columns((1, 0.43))
image = Image.open('Betelgeuse.png')
g1.image(image, width=420)

g2.title("FWHM: 3.66")
g2.title("Pickering: 3")

st.markdown(
    "The question I wanted to answer with my project is what kind of seeing do we get at the Allan I Carswell observatory, "
    "see below for the data table and a plot showing all my values. As a reminder, the conversion for the Pickering scale was done with this diagram.")

image = Image.open('pickering2.png')
st.image(image, caption='Credit: Kolář J (https://eaae-astronomy.org/images/projects/catch-a-star/2015/18_How_to_measure_seeing.pdf)', width=620)

# g1, g2 = st.columns((1, 2.8))

st.write(data)

a = alt.Chart(dataToDisplay).mark_area(opacity=1).encode(
    x='Date', y='Pickering Scale')

c = alt.layer(a)

st.altair_chart(c, use_container_width=True)
