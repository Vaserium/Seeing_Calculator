import altair as alt
from PIL import Image
from astropy.io import fits
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(layout="wide", page_title='York Seeing')
st.header('York Observatory Seeing Network')
# ------------------------------------------------- Displaying all data (just for show and will not actually use data from this)
excel_file = 'sample.csv'

st.markdown("""
<style>
.big-font {
    font-size:65px !important;
}
</style>
""", unsafe_allow_html=True)

today = date.today()
d1 = today.strftime("%d/%m/%Y")

data = pd.read_csv(excel_file)
dataToDisplay = pd.DataFrame(data)

seeing = str(round(data['FWHM'][2], 3))
row3_1, row3_spacer2 = st.columns((3.2, .1))
with row3_1:
    st.markdown(
        "Hello there! Why are dark sky's so important? Why do you want to measure the FWHM. Well, this interactive application containing FWHM data allows you to measure seeing conditions on the night each observation was taken!")
    st.markdown(
        "You can find the source code in the [York Observatory Seeing Network GitHub Repository](https://github.com/Vaserium/Seeing_Calculator/blob/main/website.py)")

st.write(data)

a = alt.Chart(dataToDisplay).mark_area(opacity=1).encode(
    x='Date', y='FWHM')

c = alt.layer(a)

st.altair_chart(c, use_container_width=True)

column1, column2 = st.columns((1.5, 1))
image = Image.open('pickering.png')
st.image(image, caption='Credit: Damian Peach', width=520)







