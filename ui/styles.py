"""
styles.py — Global CSS for the Multiple Disease Prediction app.
Injected once via inject_css() at app startup.
"""

from ui import theme


def get_global_css() -> str:
    """Return the complete CSS string for the entire application."""
    return f"""
/* ══════════════════════════════════════════════
   GOOGLE FONTS
   ══════════════════════════════════════════════ */
@import url('{theme.GOOGLE_FONTS}');

/* ══════════════════════════════════════════════
   GLOBAL RESET & BASE
   ══════════════════════════════════════════════ */
*, *::before, *::after {{
    box-sizing: border-box;
}}

html, body, .stApp {{
    background-color: {theme.BG_PRIMARY} !important;
    font-family: {theme.FONT_FAMILY} !important;
    color: {theme.TEXT_PRIMARY} !important;
    -webkit-font-smoothing: antialiased;
}}

/* Hide Streamlit branding */
#MainMenu {{ visibility: hidden; }}
footer    {{ visibility: hidden; }}
header    {{ visibility: hidden; }}
.css-1rs6os {{ visibility: hidden; }}
.viewerBadge_container__1QSob {{ display: none !important; }}
[data-testid="stToolbar"] {{ visibility: hidden; }}
[data-testid="stDecoration"] {{ visibility: hidden; }}

/* ══════════════════════════════════════════════
   MAIN CONTENT AREA
   ══════════════════════════════════════════════ */
.block-container {{
    padding: 2rem 2.5rem 4rem 2.5rem !important;
    max-width: 1280px !important;
}}

/* ══════════════════════════════════════════════
   SIDEBAR
   ══════════════════════════════════════════════ */
[data-testid="stSidebar"] {{
    background-color: {theme.BG_SIDEBAR} !important;
    border-right: 1px solid {theme.BORDER} !important;
}}

[data-testid="stSidebar"] > div:first-child {{
    padding-top: 0 !important;
}}

[data-testid="stSidebar"]::-webkit-scrollbar {{ width: 3px; }}
[data-testid="stSidebar"]::-webkit-scrollbar-track {{ background: {theme.BG_SIDEBAR}; }}
[data-testid="stSidebar"]::-webkit-scrollbar-thumb {{
    background: {theme.WINE_RED};
    border-radius: 2px;
}}

/* ══════════════════════════════════════════════
   BUTTONS — ALL VARIANTS
   ══════════════════════════════════════════════ */
.stButton > button {{
    background-color: {theme.WINE_RED} !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: {theme.RADIUS_MD} !important;
    padding: 12px 24px !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2px !important;
    line-height: 1.4 !important;
    transition: background-color 0.18s ease, box-shadow 0.18s ease, transform 0.12s ease !important;
    cursor: pointer !important;
    width: 100% !important;
    min-height: 46px !important;
    box-shadow: {theme.SHADOW_WINE} !important;
}}

.stButton > button:hover {{
    background-color: {theme.WINE_RED_HOVER} !important;
    box-shadow: 0 6px 20px rgba(139, 30, 45, 0.4) !important;
    transform: translateY(-1px) !important;
}}

.stButton > button:active {{
    background-color: {theme.WINE_RED_ACTIVE} !important;
    box-shadow: none !important;
    transform: translateY(0) !important;
}}

.stButton > button:focus:not(:active) {{
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(139, 30, 45, 0.25) !important;
}}

/* Secondary / home button override */
.stButton > button[data-testid="nav_home"] {{
    background-color: transparent !important;
    border: 1px solid {theme.BORDER_ALT} !important;
    color: {theme.TEXT_SECONDARY} !important;
    box-shadow: none !important;
    font-weight: 500 !important;
}}
.stButton > button[data-testid="nav_home"]:hover {{
    border-color: {theme.WINE_RED} !important;
    color: {theme.WINE_RED_LIGHT} !important;
    background-color: {theme.WINE_RED_MUTED} !important;
}}

/* ══════════════════════════════════════════════
   TEXT INPUTS
   ══════════════════════════════════════════════ */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {{
    background-color: {theme.BG_CARD} !important;
    border: 1px solid {theme.BORDER_ALT} !important;
    border-radius: {theme.RADIUS_MD} !important;
    color: {theme.TEXT_PRIMARY} !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: 14px !important;
    padding: 10px 14px !important;
    transition: border-color 0.18s ease, box-shadow 0.18s ease !important;
    caret-color: {theme.WINE_RED} !important;
}}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {{
    border-color: {theme.WINE_RED} !important;
    box-shadow: 0 0 0 2px rgba(139, 30, 45, 0.12) !important;
    outline: none !important;
}}

.stTextInput > div > div > input::placeholder,
.stNumberInput > div > div > input::placeholder {{
    color: {theme.TEXT_MUTED} !important;
}}

/* ══════════════════════════════════════════════
   LABELS
   ══════════════════════════════════════════════ */
.stTextInput > label,
.stNumberInput > label,
.stTextArea > label,
.stSelectbox > label,
.stMultiSelect > label,
.stSlider > label,
.stCheckbox > label span,
[data-testid="stWidgetLabel"] {{
    color: {theme.TEXT_SECONDARY} !important;
    font-size: {theme.FONT_SM} !important;
    font-weight: 500 !important;
    font-family: {theme.FONT_FAMILY} !important;
    letter-spacing: 0.1px !important;
}}

/* ══════════════════════════════════════════════
   SELECT BOX & MULTISELECT
   ══════════════════════════════════════════════ */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
    background-color: {theme.BG_CARD} !important;
    border: 1px solid {theme.BORDER_ALT} !important;
    border-radius: {theme.RADIUS_MD} !important;
    color: {theme.TEXT_PRIMARY} !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: 14px !important;
    transition: border-color 0.18s ease !important;
}}

.stSelectbox > div > div:focus-within {{
    border-color: {theme.WINE_RED} !important;
    box-shadow: 0 0 0 2px rgba(139, 30, 45, 0.12) !important;
}}

/* Dropdown menu */
[data-baseweb="popover"] ul {{
    background-color: {theme.BG_SECONDARY} !important;
    border: 1px solid {theme.BORDER_ALT} !important;
    border-radius: {theme.RADIUS_MD} !important;
}}

[data-baseweb="popover"] li:hover {{
    background-color: {theme.WINE_RED_MUTED} !important;
}}

/* Multi-select tags */
[data-baseweb="tag"] {{
    background-color: {theme.WINE_RED_MUTED} !important;
    border-color: {theme.WINE_RED_BORDER} !important;
    color: {theme.WINE_RED_LIGHT} !important;
    border-radius: {theme.RADIUS_FULL} !important;
    font-size: 12px !important;
}}

/* ══════════════════════════════════════════════
   NUMBER INPUT STEPPERS
   ══════════════════════════════════════════════ */
.stNumberInput > div > div > div > button {{
    background-color: {theme.BG_SECONDARY} !important;
    border: 1px solid {theme.BORDER} !important;
    border-radius: {theme.RADIUS_SM} !important;
    color: {theme.TEXT_SECONDARY} !important;
    min-height: unset !important;
    width: 28px !important;
    padding: 0 !important;
    box-shadow: none !important;
}}

.stNumberInput > div > div > div > button:hover {{
    background-color: {theme.WINE_RED} !important;
    color: white !important;
    border-color: {theme.WINE_RED} !important;
    transform: none !important;
}}

/* ══════════════════════════════════════════════
   SLIDERS
   ══════════════════════════════════════════════ */
[data-testid="stSlider"] [data-baseweb="slider"] > div {{
    background-color: {theme.BORDER_ALT} !important;
}}

[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {{
    background-color: {theme.WINE_RED} !important;
    border-color: {theme.WINE_RED} !important;
    box-shadow: 0 0 0 4px rgba(139, 30, 45, 0.15) !important;
}}

/* Filled portion */
[data-testid="stSlider"] [data-baseweb="slider"] > div > div:first-child {{
    background-color: {theme.WINE_RED} !important;
}}

/* ══════════════════════════════════════════════
   CHECKBOXES
   ══════════════════════════════════════════════ */
[data-testid="stCheckbox"] span[aria-checked="true"] {{
    background-color: {theme.WINE_RED} !important;
    border-color: {theme.WINE_RED} !important;
}}

[data-testid="stCheckbox"] span {{
    border-color: {theme.BORDER_ALT} !important;
    border-radius: 3px !important;
}}

/* ══════════════════════════════════════════════
   TABS
   ══════════════════════════════════════════════ */
[data-baseweb="tab-list"] {{
    background-color: transparent !important;
    border-bottom: 1px solid {theme.BORDER} !important;
    gap: 4px !important;
}}

[data-baseweb="tab"] {{
    background-color: transparent !important;
    color: {theme.TEXT_MUTED} !important;
    border-bottom: 2px solid transparent !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: {theme.FONT_SM} !important;
    font-weight: 500 !important;
    padding: 10px 20px !important;
    transition: color 0.18s !important;
    border-radius: 0 !important;
}}

[data-baseweb="tab"]:hover {{
    color: {theme.TEXT_SECONDARY} !important;
    background-color: transparent !important;
}}

[data-baseweb="tab"][aria-selected="true"] {{
    color: {theme.WINE_RED_LIGHT} !important;
    border-bottom: 2px solid {theme.WINE_RED} !important;
    background-color: transparent !important;
    font-weight: 600 !important;
}}

[data-baseweb="tab-panel"] {{
    background-color: transparent !important;
    padding: 20px 0 !important;
    color: {theme.TEXT_SECONDARY} !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: {theme.FONT_MD} !important;
    line-height: 1.75 !important;
}}

/* ══════════════════════════════════════════════
   ALERTS / STATUS MESSAGES
   ══════════════════════════════════════════════ */
[data-testid="stAlert"] [data-baseweb="notification"] {{
    border-radius: {theme.RADIUS_MD} !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-size: {theme.FONT_SM} !important;
}}

div[data-baseweb="notification"][kind="positive"],
.stSuccess > div {{
    background-color: {theme.SUCCESS_BG} !important;
    border: 1px solid {theme.SUCCESS} !important;
    border-radius: {theme.RADIUS_MD} !important;
    color: {theme.SUCCESS_TEXT} !important;
}}

div[data-baseweb="notification"][kind="negative"],
.stError > div {{
    background-color: {theme.ERROR_BG} !important;
    border: 1px solid {theme.ERROR} !important;
    border-radius: {theme.RADIUS_MD} !important;
    color: {theme.ERROR_TEXT} !important;
}}

div[data-baseweb="notification"][kind="warning"],
.stWarning > div {{
    background-color: {theme.WARNING_BG} !important;
    border: 1px solid {theme.WARNING} !important;
    border-radius: {theme.RADIUS_MD} !important;
    color: {theme.WARNING_TEXT} !important;
}}

/* ══════════════════════════════════════════════
   HEADINGS & BODY TEXT
   ══════════════════════════════════════════════ */
h1, h2, h3, h4, h5, h6 {{
    color: {theme.TEXT_PRIMARY} !important;
    font-family: {theme.FONT_FAMILY} !important;
    font-weight: 700 !important;
}}

p, li, span {{
    font-family: {theme.FONT_FAMILY} !important;
}}

/* Markdown rendered text */
.stMarkdown p {{
    color: {theme.TEXT_SECONDARY} !important;
    font-size: {theme.FONT_MD} !important;
    line-height: 1.7 !important;
}}

/* ══════════════════════════════════════════════
   IMAGES
   ══════════════════════════════════════════════ */
.stImage > img {{
    border-radius: {theme.RADIUS_LG} !important;
    border: 1px solid {theme.BORDER} !important;
}}

/* ══════════════════════════════════════════════
   DIVIDER
   ══════════════════════════════════════════════ */
hr {{
    border-color: {theme.BORDER} !important;
    opacity: 1 !important;
    margin: 24px 0 !important;
}}

/* ══════════════════════════════════════════════
   GLOBAL SCROLLBAR
   ══════════════════════════════════════════════ */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: {theme.BG_PRIMARY}; }}
::-webkit-scrollbar-thumb {{ background: {theme.BORDER_HOVER}; border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: {theme.WINE_RED}; }}

/* ══════════════════════════════════════════════
   HERO PAGE
   ══════════════════════════════════════════════ */
.hero-section {{
    text-align: center;
    padding: 64px 24px 48px;
}}

.hero-logo img {{
    width: 120px;
    height: 120px;
    object-fit: contain;
    border: none !important;
    border-radius: 0 !important;
    margin-bottom: 28px;
}}

.hero-tag {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: {theme.WINE_RED_MUTED};
    border: 1px solid {theme.WINE_RED_BORDER};
    color: {theme.WINE_RED_LIGHT};
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 6px 18px;
    border-radius: {theme.RADIUS_FULL};
    margin-bottom: 28px;
    font-family: {theme.FONT_FAMILY};
}}

.hero-title {{
    font-size: 52px;
    font-weight: 800;
    color: {theme.TEXT_PRIMARY};
    line-height: 1.12;
    margin-bottom: 14px;
    letter-spacing: -1.5px;
    font-family: {theme.FONT_FAMILY};
}}

.hero-title span {{ color: {theme.WINE_RED_LIGHT}; }}

.hero-subtitle {{
    font-size: 17px;
    color: {theme.TEXT_SECONDARY};
    margin-bottom: 10px;
    font-weight: 400;
    font-family: {theme.FONT_FAMILY};
    line-height: 1.6;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}}

.hero-tagline {{
    font-size: 11px;
    color: {theme.TEXT_MUTED};
    letter-spacing: 3px;
    margin-bottom: 36px;
    text-transform: uppercase;
    font-weight: 500;
    font-family: {theme.FONT_FAMILY};
}}

/* Stats row */
.stats-row {{
    display: flex;
    justify-content: center;
    gap: 56px;
    padding: 28px 0;
    border-top: 1px solid {theme.BORDER};
    border-bottom: 1px solid {theme.BORDER};
    margin: 36px 0;
}}

.stat-item {{ text-align: center; }}

.stat-number {{
    font-size: 30px;
    font-weight: 800;
    color: {theme.WINE_RED};
    line-height: 1;
    margin-bottom: 5px;
    font-family: {theme.FONT_FAMILY};
}}

.stat-label {{
    font-size: 11px;
    color: {theme.TEXT_MUTED};
    letter-spacing: 0.5px;
    font-family: {theme.FONT_FAMILY};
}}

/* Disease cards grid */
.disease-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
}}

@media (max-width: 768px) {{
    .disease-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}

.disease-card {{
    background: {theme.BG_CARD};
    border: 1px solid {theme.BORDER};
    border-radius: {theme.RADIUS_LG};
    padding: 20px 16px;
    text-align: center;
    transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
}}

.disease-card:hover {{
    border-color: {theme.WINE_RED};
    transform: translateY(-2px);
    box-shadow: {theme.SHADOW_MD};
}}

.disease-card-icon {{
    font-size: 28px;
    margin-bottom: 10px;
    display: block;
}}

.disease-card-name {{
    font-size: 13px;
    font-weight: 600;
    color: {theme.TEXT_PRIMARY};
    margin-bottom: 5px;
    font-family: {theme.FONT_FAMILY};
}}

.disease-card-desc {{
    font-size: 11px;
    color: {theme.TEXT_MUTED};
    line-height: 1.5;
    font-family: {theme.FONT_FAMILY};
}}

/* How it works */
.steps-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}}

@media (max-width: 900px) {{
    .steps-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}

.step-card {{
    background: {theme.BG_SECONDARY};
    border: 1px solid {theme.BORDER};
    border-radius: {theme.RADIUS_LG};
    padding: 22px 18px;
    text-align: center;
    position: relative;
    transition: border-color 0.2s;
}}

.step-card:hover {{ border-color: {theme.BORDER_HOVER}; }}

.step-number {{
    font-size: 10px;
    font-weight: 700;
    color: {theme.WINE_RED};
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 10px;
    font-family: {theme.FONT_FAMILY};
}}

.step-icon {{
    font-size: 26px;
    margin-bottom: 10px;
    display: block;
}}

.step-title {{
    font-size: 14px;
    font-weight: 600;
    color: {theme.TEXT_PRIMARY};
    margin-bottom: 5px;
    font-family: {theme.FONT_FAMILY};
}}

.step-desc {{
    font-size: 11px;
    color: {theme.TEXT_MUTED};
    line-height: 1.5;
    font-family: {theme.FONT_FAMILY};
}}

/* Section heading */
.section-heading {{
    text-align: center;
    margin-bottom: 32px;
    margin-top: 16px;
}}

.section-label {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: {theme.WINE_RED};
    margin-bottom: 8px;
    font-family: {theme.FONT_FAMILY};
}}

.section-title {{
    font-size: 26px;
    font-weight: 700;
    color: {theme.TEXT_PRIMARY};
    margin-bottom: 8px;
    line-height: 1.3;
    font-family: {theme.FONT_FAMILY};
    letter-spacing: -0.5px;
}}

.section-subtitle {{
    font-size: 14px;
    color: {theme.TEXT_MUTED};
    font-family: {theme.FONT_FAMILY};
    line-height: 1.5;
}}

/* Separator */
.separator {{
    height: 1px;
    background: linear-gradient(90deg, transparent, {theme.BORDER_ALT}, transparent);
    margin: 48px 0;
}}

/* Disclaimer */
.disclaimer-card {{
    background: {theme.BG_SECONDARY};
    border: 1px solid {theme.BORDER_ALT};
    border-left: 3px solid {theme.WINE_RED};
    border-radius: 0 {theme.RADIUS_MD} {theme.RADIUS_MD} 0;
    padding: 18px 22px;
}}

.disclaimer-title {{
    font-size: 11px;
    font-weight: 700;
    color: {theme.WINE_RED_LIGHT};
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-family: {theme.FONT_FAMILY};
}}

.disclaimer-text {{
    font-size: 13px;
    color: {theme.TEXT_MUTED};
    line-height: 1.75;
    font-family: {theme.FONT_FAMILY};
}}

/* ══════════════════════════════════════════════
   DISEASE PAGE COMPONENTS
   ══════════════════════════════════════════════ */
.page-header {{
    margin-bottom: 28px;
    padding-bottom: 18px;
    border-bottom: 1px solid {theme.BORDER};
}}

.page-header-tag {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: {theme.WINE_RED};
    margin-bottom: 8px;
    font-family: {theme.FONT_FAMILY};
}}

.page-header-title {{
    font-size: 26px;
    font-weight: 700;
    color: {theme.TEXT_PRIMARY};
    line-height: 1.2;
    margin-bottom: 7px;
    font-family: {theme.FONT_FAMILY};
    letter-spacing: -0.5px;
}}

.page-header-desc {{
    font-size: 13px;
    color: {theme.TEXT_MUTED};
    font-family: {theme.FONT_FAMILY};
    line-height: 1.6;
}}

/* Input section labels */
.input-section-title {{
    font-size: 10px;
    font-weight: 700;
    color: {theme.TEXT_MUTED};
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid {theme.BORDER};
    font-family: {theme.FONT_FAMILY};
}}

/* Result card */
.result-card {{
    background: {theme.BG_SECONDARY};
    border: 1px solid {theme.BORDER_ALT};
    border-radius: {theme.RADIUS_LG};
    padding: 32px 28px;
    margin-top: 24px;
    text-align: center;
}}

.result-card.risk {{
    border-color: rgba(139, 30, 45, 0.45);
    background: linear-gradient(135deg, {theme.BG_SECONDARY} 0%, {theme.ERROR_BG} 100%);
    box-shadow: 0 4px 20px rgba(139, 30, 45, 0.1);
}}

.result-card.safe {{
    border-color: rgba(45, 106, 79, 0.45);
    background: linear-gradient(135deg, {theme.BG_SECONDARY} 0%, {theme.SUCCESS_BG} 100%);
    box-shadow: 0 4px 20px rgba(45, 106, 79, 0.1);
}}

.result-label {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: {theme.TEXT_MUTED};
    margin-bottom: 14px;
    font-family: {theme.FONT_FAMILY};
}}

.result-icon {{
    font-size: 52px;
    margin-bottom: 16px;
    display: block;
    line-height: 1;
}}

.result-title {{
    font-size: 22px;
    font-weight: 700;
    color: {theme.TEXT_PRIMARY};
    margin-bottom: 8px;
    font-family: {theme.FONT_FAMILY};
    letter-spacing: -0.3px;
}}

.result-title.risk  {{ color: {theme.ERROR_TEXT}; }}
.result-title.safe  {{ color: {theme.SUCCESS_TEXT}; }}

.result-patient {{
    font-size: 14px;
    color: {theme.TEXT_SECONDARY};
    margin-bottom: 16px;
    font-family: {theme.FONT_FAMILY};
}}

.result-patient strong {{ color: {theme.TEXT_PRIMARY}; font-weight: 600; }}

.result-message {{
    font-size: 14px;
    color: {theme.TEXT_MUTED};
    line-height: 1.7;
    max-width: 520px;
    margin: 0 auto;
    font-family: {theme.FONT_FAMILY};
}}

.result-divider {{
    height: 1px;
    background: {theme.BORDER};
    margin: 18px auto;
    width: 60%;
}}

/* ══════════════════════════════════════════════
   WINE-RED LOADING ANIMATION
   ══════════════════════════════════════════════ */
.wine-loader {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 32px;
    gap: 14px;
}}

.wine-loader-text {{
    color: {theme.TEXT_MUTED};
    font-family: {theme.FONT_FAMILY};
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    animation: wl-pulse 1.6s ease-in-out infinite;
}}

.wine-loader-bar-bg {{
    width: 180px;
    height: 4px;
    background-color: {theme.BORDER_ALT};
    border-radius: 2px;
    overflow: hidden;
}}

.wine-loader-bar {{
    height: 100%;
    background: linear-gradient(90deg, 
        {theme.WINE_RED_DEEP}, 
        {theme.WINE_RED}, 
        {theme.WINE_RED_LIGHT}, 
        {theme.WINE_RED}, 
        {theme.WINE_RED_DEEP}
    );
    background-size: 300% 100%;
    border-radius: 2px;
    animation: wl-slide 1.6s ease-in-out infinite;
}}

@keyframes wl-slide {{
    0%   {{ background-position: 100% 0; }}
    100% {{ background-position: -100% 0; }}
}}

@keyframes wl-pulse {{
    0%, 100% {{ opacity: 0.4; }}
    50%       {{ opacity: 1; }}
}}
"""


def inject_css() -> None:
    """Inject the full design system CSS into the Streamlit app."""
    import streamlit as st
    css = get_global_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
