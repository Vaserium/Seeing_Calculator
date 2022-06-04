import altair as alt
from PIL import Image
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='York Seeing')
st.header('York Observatory Seeing Network')
# ------------------------------------------------- Displaying all data (just for show and will not actually use data from this)
excel_file = 'sample.csv'

data = pd.read_csv(excel_file)
dataToDisplay = pd.DataFrame(data)

row3_1, row3_spacer2 = st.columns((3.2, .1))
with row3_1:
    st.markdown(
        "'Why do you want to measure the seeing value?' Well, this interactive application containing FWHM(Full Width Half Maximum) data allows you to look at measured seeing conditions so you can stay informed on the night each observation was taken!")
    st.markdown("Seeing: “Good seeing” is when the stars that are being displayed on your image twinkle very little; “bad seeing” is when they twinkle a lot. Check the diagram below...")
    st.markdown("Pickering Scale: A scale from 1 to 10 which represents seeing conditions.  A rating of 1 is very poor seeing, and a rating of 10 is perfect seeing.")
    st.markdown("[How to check seeing conditions](https://www.skyatnightmagazine.com/advice/what-is-astronomical-seeing/)")
st.write(data)

a = alt.Chart(dataToDisplay).mark_area(opacity=1).encode(
    x='Date', y='Pickering Scale')

c = alt.layer(a)

st.altair_chart(c, use_container_width=True)

column1, column2 = st.columns((1.5, 1))
image = Image.open('pickering.png')
st.image(image, caption='Credit: Damian Peach', width=620)







