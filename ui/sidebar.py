"""
sidebar.py — Styled sidebar navigation for the Multiple Disease Prediction app.
"""

import base64
import os
import streamlit as st
from streamlit_option_menu import option_menu


# Navigation pages — must match the keys used in app.py
PAGES = [
    "Disease Prediction",
    "Diabetes Prediction",
    "Heart disease Prediction",
    "Parkison Prediction",
    "Liver prediction",
    "Hepatitis prediction",
    "Lung Cancer Prediction",
    "Chronic Kidney prediction",
    "Breast Cancer Prediction",
]

ICONS = [
    "search",
    "droplet-half",
    "heart-pulse",
    "person-standing",
    "activity",
    "virus",
    "lungs",
    "shield-plus",
    "gender-female",
]


def _logo_b64() -> str:
    for path in ["logo1.png", "logo.png", "Frontend/logo1.png", "Frontend/logo.png"]:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return ""


def render_sidebar() -> str:
    """
    Render the styled sidebar navigation.
    Returns the name of the currently selected page.
    """
    logo = _logo_b64()

    with st.sidebar:
        # ── Brand header ──────────────────────────────────────────────────────
        if logo:
            st.markdown(f"""
            <div style="
                display:flex; align-items:center; gap:12px;
                padding: 20px 16px 14px 16px;
                border-bottom: 1px solid #1C1C1C;
                margin-bottom: 4px;
            ">
                <img src="data:image/png;base64,{logo}"
                     style="width:34px;height:34px;object-fit:contain;
                            border:none !important;border-radius:0 !important;" />
                <div>
                    <div style="font-size:13px;font-weight:700;
                                color:#F2F2F2;line-height:1.2;
                                font-family:'Inter',sans-serif;">
                        Disease Predict
                    </div>
                    <div style="font-size:10px;color:#5A5A5A;
                                font-family:'Inter',sans-serif;letter-spacing:0.3px;">
                        AI Medical Analysis
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="padding:20px 16px 14px;border-bottom:1px solid #1C1C1C;margin-bottom:4px;">
                <div style="font-size:14px;font-weight:700;color:#F2F2F2;
                            font-family:'Inter',sans-serif;">🏥 Disease Predict</div>
                <div style="font-size:10px;color:#5A5A5A;
                            font-family:'Inter',sans-serif;margin-top:2px;">
                    AI Medical Analysis
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Nav menu ──────────────────────────────────────────────────────────
        selected = option_menu(
            menu_title=None,
            options=PAGES,
            icons=ICONS,
            default_index=0,
            styles={
                "container": {
                    "padding": "8px 8px",
                    "background-color": "transparent",
                },
                "icon": {
                    "color": "#5A5A5A",
                    "font-size": "13px",
                },
                "nav-link": {
                    "font-size": "13px",
                    "color": "#9A9A9A",
                    "font-weight": "400",
                    "font-family": "'Inter', 'Segoe UI', sans-serif",
                    "border-radius": "8px",
                    "padding": "9px 14px",
                    "margin": "1px 0",
                    "--hover-color": "#1C1C1C",
                    "transition": "all 0.15s ease",
                },
                "nav-link-selected": {
                    "background-color": "#8B1E2D",
                    "color": "#FFFFFF",
                    "font-weight": "600",
                    "border-radius": "8px",
                },
            },
        )

        # ── Back to home ──────────────────────────────────────────────────────
        st.markdown(
            '<div style="margin-top:12px;padding-top:12px;border-top:1px solid #1C1C1C;">',
            unsafe_allow_html=True,
        )
        if st.button("← Back to Home", key="btn_home", use_container_width=True):
            st.session_state.page = "hero"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Footer ────────────────────────────────────────────────────────────
        st.markdown("""
        <div style="margin-top:auto;padding:16px 16px 0;
                    border-top:1px solid #1C1C1C;margin-top:24px;">
            <div style="font-size:10px;color:#2E2E2E;text-align:center;
                        font-family:'Inter',sans-serif;letter-spacing:0.5px;">
                Multiple Disease Prediction v1.0
            </div>
        </div>
        """, unsafe_allow_html=True)

    return selected
