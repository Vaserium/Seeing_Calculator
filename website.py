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

dataToDisplay = pd.read_csv(excel_file)
data = pd.read_csv(excel_file)

seeing = str(round(dataToDisplay['FWHM'][2], 3))
fwhm_display = '<p class="big-font">FWHM: ' + str(seeing)
date_display = '<p class="big-font">Date: ' + dataToDisplay['Date'][2]

st.markdown(fwhm_display, unsafe_allow_html=True)
st.markdown(date_display, unsafe_allow_html=True)

column1, column2 = st.columns((1.5, 1))
image = Image.open('pickering.png')
column1.image(image, caption='Credit: Damian Peach', use_column_width=True)







