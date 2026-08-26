import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/VYxP8hD7/logo-png.png"

    st.markdown(f"""<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:10px; margin-top:5px">

<img src="{logo_url}" style="width:125px; height:95px; object-fit:contain; margin-bottom:5px;">

<h1 style="text-align:center; color:#172554; margin:0; font-family:'Climate Crisis', sans-serif; font-size:4rem; line-height:0.9;">
Pro<br>Attend
</h1>

<p style="text-align:center; color:#4B4F8A; font-family:'Outfit', sans-serif; font-size:1.15rem; margin-top:18px;">
Smart Attendance. Simple Management.
</p>

</div>""", unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/VYxP8hD7/logo-png.png"

    st.markdown(f"""<div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:25px;">

<img src="{logo_url}" style="width:85px; height:85px; object-fit:contain;">

<h2 style="text-align:left; color:#172554; margin:0; font-family:'Climate Crisis', sans-serif; line-height:0.9;">
Pro<br>Attend
</h2>

</div>""", unsafe_allow_html=True)