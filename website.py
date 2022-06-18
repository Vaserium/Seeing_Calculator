import altair as alt
from PIL import Image
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='York Seeing')
row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((3, .2, 0.95, .1))
row0_1.header('York Observatory Seeing Network')
with row0_2:
    st.write('')
row0_2.subheader('Web App by [Toby Avila](https://www.linkedin.com/in/toby-avila-118080208/)')
# ------------------------------------------------- Displaying all data (just for show and will not actually use data from this)
excel_file = 'sample.csv'
data = pd.read_csv(excel_file)
dataToDisplay = pd.DataFrame(data)

st.subheader("Project Introduction")
st.markdown(
    "This website contains my 2022 co-op investigation into how seeing conditions affect day-to-day observations at Allan I. Carswell Astronomical Observatory. One of the measurements I was interested in was the seeing value. 'Why do you want to measure the seeing value?' Well, this interactive application containing FWHM(Full Width Half Maximum) data allows you to look at measured seeing conditions so you can stay informed on the night each observation was taken!")

st.markdown(
    "For this investigation I used the Pickering scale which is [a scale from 1 to 10 which represents seeing conditions. A rating of 1 is very poor seeing, and a rating of 10 is perfect seeing](https://freestarcharts.com/pickering-scale#:~:text=Pickering%20scale%20The%20scale%20developed%20by%20Harvard%20astronomer,and%20a%20rating%20of%2010%20meaning%20perfect%20seeing.). "
    "Here are some handy definitions for seeing: “Good seeing” is when the stars that are being displayed on your image twinkle very little; “bad seeing” is when they twinkle a lot. "
    "Check the diagram below to see what this might look like in the Pickerings scale.")

image = Image.open('pickering.png')
st.image(image, caption='Credit: Damian Peach (http://www.damianpeach.com/pickering.htm)', width=620)

st.markdown(
    "How are seeing and FWHM related? I used the number of pixels across the width of the star at half its maximum value. The question I wanted to answer with my project is 'what kind of seeing do we get at the Allan I Carswell observatory? See below for the data table and a plot showing all my values. As a reminder, the conversion from the FWHM(arcsec) to the Pickering scale was done using this diagram.")
image1 = Image.open('pickering2.png')
st.image(image1,
         caption='Credit: Kolář J (https://eaae-astronomy.org/images/projects/catch-a-star/2015/18_How_to_measure_seeing.pdf)',
         width=660)

g1, g2 = st.columns((1, 0.75))

image2 = Image.open('Qatar1.png')
g1.image(image2, width=345)

new_title = '<p style="font-family:Courier; color:Orange; font-size: 23px;">FWHM: 11.37972983</p>'
new_title2 = '<p style="font-family:Courier; color:Orange; font-size: 23px;">Pickering = FWHM*0.0439(const)</p>'
g2.markdown(new_title, unsafe_allow_html=True)
g2.markdown(new_title2, unsafe_allow_html=True)

st.subheader("Project Data")
st.markdown(
    "For my project I measured the FWHM of stars in image fields ranging from The North Star to the binary star system of Gamma Leonis. "
    "These sets of data were taken at the Allan I Carswell Observatory 1m telescope. "
    "All 2022 data I took with members of the observatory for this project and previous data was used from the archive. "
    "Here is a picture of our star field for Betelgeuse that contains a FWHM value of 3.66 and a Pickering Scale value of 3.")

g1, g2 = st.columns((1, 0.73))
image = Image.open('Betelgeuse.png')
g1.image(image, caption='Image Credit: Sunna Withers', width=343)

new_title1 = '<p style="font-family:Courier; color:Orange; font-size: 46px;">FWHM: 3.66</p>'
new_title2 = '<p style="font-family:Courier; color:Orange; font-size: 46px;">Pickering Scale: 3</p>'
g2.markdown(new_title1, unsafe_allow_html=True)
g2.markdown(new_title2, unsafe_allow_html=True)

st.subheader("Allan I. Carswell Observatory Seeing and Pickering Scale Data")

st.write(data)

scatter = alt.Chart(dataToDisplay).mark_point(filled=True).encode(
    alt.X('Date'),
    alt.Y('Pickering Scale'),
    alt.Color('Pickering Scale'),
    alt.Size('Pickering Scale'),
    alt.OpacityValue(0.8)).interactive()

scatter2 = alt.Chart(dataToDisplay).mark_point().encode(x='Date', y='Pickering Scale').interactive()

c = alt.layer(scatter)

st.altair_chart(c, use_container_width=True)

st.subheader("Project Conclusions")
st.markdown(
    "Knowing the seeing conditions is important for further assisting astronomers in the practice of observing astronomical objects. Acknowledging these values can prove to be very influential since it will help you perform observing tasks efficiently and to operate well while capturing data because the seeing value tells you how much the atmospheric turbulence, twinkling of stars, and the form of wind affect the amount of “blurring” in the image. The seeing and pickering scale results seek to support the argument that it is meaningful to include seeing value information while observing.")

st.title("Thank You So Much For Checking Out My Web App!")
