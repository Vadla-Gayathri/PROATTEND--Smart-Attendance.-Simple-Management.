import streamlit as st


# ============================================================
# HOME PAGE BACKGROUND
# ============================================================

def style_background_home():

    st.markdown("""
        <style>

            /* ==================================================
               MAIN HOME BACKGROUND
               ================================================== */

            .stApp {
                background: #D9D4FF !important;
            }


            /* ==================================================
               STUDENT + TEACHER CARDS
               ================================================== */

            .stApp div[data-testid="stColumn"] {
                padding: 2.5rem !important;
                border-radius: 2.5rem !important;
                min-height: 500px !important;
                box-shadow: 0 12px 30px rgba(23, 37, 84, 0.10) !important;
                position: relative !important;
            }


            /* ==================================================
               STUDENT CARD
               ================================================== */

            .stApp div[data-testid="stColumn"]:first-child {
                background: #E9FAF8 !important;
            }


            /* ==================================================
               TEACHER CARD
               ================================================== */

            .stApp div[data-testid="stColumn"]:last-child {
                background: #FFF3E7 !important;
            }

        </style>
    """, unsafe_allow_html=True)


# ============================================================
# DASHBOARD BACKGROUND
# ============================================================

def style_background_dashboard():

    st.markdown("""
        <style>

            /* Dashboard Background */
            .stApp {
                background: #D9D4FF !important;
            }

        </style>
    """, unsafe_allow_html=True)


# ============================================================
# COMMON APPLICATION STYLE
# ============================================================

def style_base_layout():

    st.markdown("""
        <style>

        /* ==================================================
           GOOGLE FONTS
           ================================================== */

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');

        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


        /* ==================================================
           HIDE STREAMLIT DEFAULT UI
           ================================================== */

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }


        /* ==================================================
           MAIN CONTENT SPACING
           ================================================== */

        .block-container {
            padding-top: 1.5rem !important;
        }


        /* ==================================================
           MAIN HEADINGS
           ================================================== */

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #172554 !important;
        }


        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.4rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #172554 !important;
        }


        /* ==================================================
           OTHER TEXT
           ================================================== */

        h3,
        h4,
        p,
        label {
            font-family: 'Outfit', sans-serif !important;
            color: #172554 !important;
        }
/* ==================================================
   STUDENT / TEACHER CARD HEADING COLORS
   ================================================== */

.stApp div[data-testid="stColumn"]:first-child h1,
.stApp div[data-testid="stColumn"]:first-child h2,
.stApp div[data-testid="stColumn"]:first-child h3 {
    color: #008F8F !important;
}

.stApp div[data-testid="stColumn"]:last-child h1,
.stApp div[data-testid="stColumn"]:last-child h2,
.stApp div[data-testid="stColumn"]:last-child h3 {
    color: #F28C00 !important;
}
/* ==================================================
   HOME PAGE DECORATIVE ACCENTS
   ================================================== */

.stApp div[data-testid="stColumn"]:first-child::before {
    content: "✦";
    position: absolute;
    font-size: 2rem;
    color: #10A6A6;
    margin-left: 85%;
    margin-top: 5px;
}

.stApp div[data-testid="stColumn"]:last-child::before {
    content: "✦";
    position: absolute;
    font-size: 2rem;
    color: #FF9800;
    margin-left: 85%;
    margin-top: 5px;
}

        /* ==================================================
           PRIMARY BUTTON
           Teal
           ================================================== */

        button[kind="primary"] {
            border-radius: 1.5rem !important;
            background-color: #10A6A6 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="primary"] span,
        button[kind="primary"] p {
            color: white !important;
        }


        /* ==================================================
           SECONDARY BUTTON
           Orange
           ================================================== */

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #FF9800 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] span,
        button[kind="secondary"] p {
            color: white !important;
        }


        /* ==================================================
           TERTIARY BUTTON
           Navy
           ================================================== */

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: #172554 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"] span,
        button[kind="tertiary"] p {
            color: white !important;
        }


        /* ==================================================
           BUTTON HOVER EFFECT
           ================================================== */

        button[kind="primary"]:hover,
        button[kind="secondary"]:hover,
        button[kind="tertiary"]:hover {
            transform: scale(1.05) !important;
        }


        /* ==================================================
           INPUT BOXES
           ================================================== */

        input,
        textarea {
            border-radius: 12px !important;
        }


        /* ==================================================
           SELECT BOX
           IMPORTANT:
           Do NOT style the internal selectbox button.
           ================================================== */

        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
        }


        /* Selectbox text */

        div[data-baseweb="select"] {
            font-family: 'Outfit', sans-serif !important;
        }


        div[data-baseweb="select"] span {
            color: #172554 !important;
        }


        /* ==================================================
           DIVIDERS
           ================================================== */

        hr {
            border-color: #C9C3F5 !important;
        }


        /* ==================================================
           LINKS
           ================================================== */

        a {
            color: #7667E8 !important;
        }


        /* ==================================================
           SUCCESS / INFO TEXT
           ================================================== */

        [data-testid="stAlert"] {
            border-radius: 15px !important;
        }

        /* ==================================================
   CAMERA INPUT - TAKE PHOTO BUTTON
   ================================================== */

div[data-testid="stCameraInput"] button {
    background-color: #10A6A6 !important;
    color: white !important;
    border: none !important;
    border-radius: 1.5rem !important;
    padding: 10px 20px !important;
}

div[data-testid="stCameraInput"] button span {
    color: white !important;
}

div[data-testid="stCameraInput"] button:hover {
    background-color: #0D8F8F !important;
    color: white !important;
    transform: scale(1.03) !important;
}


        </style>
    """, unsafe_allow_html=True)