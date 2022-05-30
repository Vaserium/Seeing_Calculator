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
        "'Why do you want to measure the seeing value?' you might ask. Well, this interactive application containing FWHM(Full Width Half Maximum) data allows you to look at measured seeing conditions so you can stay informed on the night each observation was taken!")
    st.markdown("Seeing: “Good seeing” is when the stars that are being displayed on your image twinkle very little; “bad seeing” is when they twinkle a lot. Check the diagram below...")
    st.markdown(
        "You can find the source code in the [York Observatory Seeing Network GitHub Repository](https://github.com/Vaserium/Seeing_Calculator/blob/main/website.py)")

st.write(data)

a = alt.Chart(dataToDisplay).mark_area(opacity=1).encode(
    x='Date', y='FWHM')

c = alt.layer(a)

st.altair_chart(c, use_container_width=True)

column1, column2 = st.columns((1.5, 1))
image = Image.open('pickering.png')
st.image(image, caption='Credit: Damian Peach', width=620)







