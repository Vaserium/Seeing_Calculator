from astropy.io import fits
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(layout="wide", page_title='York Seeing')
row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((3, .2, 0.55, .1))
row0_1.title('York Observatory Seeing Network')
with row0_2:
    st.write('')
# ------------------------------------------------- Displaying all data (just for show and will not actually use data from this)
excel_file = 'sample.csv'

st.markdown("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)

today = date.today()
d1 = today.strftime("%d/%m/%Y")

dataToDisplay = pd.read_csv(excel_file)
data = pd.read_csv(excel_file)

seeing = str(round(dataToDisplay['FWHM'][1], 3))
fwhm_display = '<p class="big-font">FWHM: ' + str(seeing)
date_display = '<p class="big-font">Date: ' + d1

st.markdown(fwhm_display, unsafe_allow_html=True)
st.markdown(date_display, unsafe_allow_html=True)
