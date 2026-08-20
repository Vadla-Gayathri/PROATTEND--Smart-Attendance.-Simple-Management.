import streamlit as st


def footer_home():
    st.markdown("""
        <div style="display:flex; gap:6px; align-items:center; justify-content:center; margin-top:2rem">
            <p style="font-weight:500; color:white;">
                © 2026 SnapClass · Developed by Gayathri Vadla
            </p>
        </div>
    """, unsafe_allow_html=True)
