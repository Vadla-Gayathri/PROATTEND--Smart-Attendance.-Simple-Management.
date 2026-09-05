import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#F8FAF8; border-left:8px solid #7667E8; padding:25px; border-radius:20px; border:1px solid #D9D4FF; margin-bottom:20px;">
        <h3 style="margin:0; color:#172554; font-size:1.5rem;">{name}</h3>
        <p style="color:#475569; margin:10px 0;">
            Code :
            <span style="background:#EDEAFF; color:#7667E8; padding:2px 8px; border-radius:5px;">
                {code}
            </span>
            | Section : {section}
        </p>
    """

    if stats:
        html += """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """

        for icon, label, value in stats:
            html += f'<div style="background:#E8F7F5; color:#172554; padding:5px 12px; border-radius:12px; font-size:0.9rem;">{icon} <b style="color:#172554;">{value}</b> <span style="color:#334155;">{label}</span></div>'

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()