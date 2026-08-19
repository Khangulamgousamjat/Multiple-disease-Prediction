"""
components.py — Reusable UI components for the Multiple Disease Prediction app.
All visual presentation lives here; ML logic stays in app.py.

KEY: All inner elements inside result-card use <span style="display:block">.
Streamlit's markdown parser escapes nested <div> and <hr> inside an outer <div>,
but passes inline <span> elements through safely — preventing raw HTML output.
"""

import base64
import os
import streamlit as st


# ─────────────────────────────────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────────────────────────────────

def _logo_b64() -> str:
    """Return base64 data-URI for the project logo.
    Prefers logo1.png (high-quality) then logo.png as fallback.
    """
    for path in ["logo1.png", "logo.png", "Frontend/logo1.png", "Frontend/logo.png"]:
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# Loading animation
# ─────────────────────────────────────────────────────────────────────────────

def render_loader(text: str = "Analyzing...") -> None:
    """Render the wine-red animated loading bar."""
    st.markdown(f"""
<div class="wine-loader">
<span style="display:block;" class="wine-loader-text">{text}</span>
<span style="display:block;" class="wine-loader-bar-bg"><span class="wine-loader-bar"></span></span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Hero / landing page
# ─────────────────────────────────────────────────────────────────────────────

def render_hero() -> None:
    """Render the full landing / hero page."""

    logo_src = _logo_b64()
    logo_html = (
        f'<img src="{logo_src}" alt="Logo" style="width:180px;height:180px;object-fit:contain;margin:0 auto 20px;display:block;" />'
        if logo_src else
        '<span style="font-size:72px;display:block;margin:0 auto 20px;">&#127973;</span>'
    )

    # ── Hero top section ─────────────────────────────────────────────────────
    st.markdown(f"""
<div class="hero-section" style="text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px 20px 24px;">
<div class="hero-logo" style="text-align:center;margin:0 auto 20px;display:flex;justify-content:center;">{logo_html}</div>
<span class="hero-tag" style="display:inline-flex;margin:0 auto 24px;text-align:center;align-items:center;justify-content:center;">&#129516; AI-Powered Medical Intelligence</span>
<h1 class="hero-title" style="text-align:center;margin:0 auto 16px;">Multiple Disease<br><span>Prediction</span></h1>
<p class="hero-subtitle" style="text-align:center;margin:0 auto 14px;max-width:650px;display:block;">
    Instant, ML-powered health risk screening across all diseases.<br>
    Enter your clinical data &#8212; get a prediction in seconds.
</p>
<p class="hero-tagline" style="text-align:center;margin:0 auto 32px;display:block;">Predict &nbsp;&middot;&nbsp; Prevent &nbsp;&middot;&nbsp; Live Healthier</p>
</div>
""", unsafe_allow_html=True)

    # ── CTA button ────────────────────────────────────────────────────────────
    _, col_btn, _ = st.columns([2.5, 1, 2.5])
    with col_btn:
        if st.button("Get Started", key="hero_cta", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()

    # ── Stats row ─────────────────────────────────────────────────────────────
    st.markdown("""
<div class="stats-row">
<span style="display:inline-block;text-align:center;min-width:100px;">
    <span style="display:block;font-size:30px;font-weight:800;color:#8B1E2D;line-height:1;margin-bottom:5px;">ML</span>
    <span style="display:block;font-size:11px;color:#5A5A5A;letter-spacing:0.5px;">Powered</span>
</span>
<span style="display:inline-block;text-align:center;min-width:100px;">
    <span style="display:block;font-size:30px;font-weight:800;color:#8B1E2D;line-height:1;margin-bottom:5px;">&#9889;</span>
    <span style="display:block;font-size:11px;color:#5A5A5A;letter-spacing:0.5px;">Instant Results</span>
</span>
<span style="display:inline-block;text-align:center;min-width:100px;">
    <span style="display:block;font-size:30px;font-weight:800;color:#8B1E2D;line-height:1;margin-bottom:5px;">Free</span>
    <span style="display:block;font-size:11px;color:#5A5A5A;letter-spacing:0.5px;">Always Free</span>
</span>
</div>
""", unsafe_allow_html=True)

    # ── Supported diseases ────────────────────────────────────────────────────
    st.markdown("""
<div class="section-heading">
<span style="display:block;" class="section-label">Capabilities</span>
<span style="display:block;" class="section-title">What We Predict</span>
<span style="display:block;" class="section-subtitle">Accurate ML-powered screening across multiple conditions</span>
</div>
""", unsafe_allow_html=True)

    DISEASES = [
        ("&#128302;", "General Disease",   "Multi-symptom XGBoost classification"),
        ("&#129656;", "Diabetes",          "Blood glucose &amp; clinical indicators"),
        ("&#10084;&#65039;",  "Heart Disease",  "Cardiovascular risk assessment"),
        ("&#129504;", "Parkinson's",       "Voice biomarker analysis"),
        ("&#129920;", "Liver Disease",     "Liver function panel screening"),
        ("&#129408;", "Hepatitis",         "Hepatic biomarker prediction"),
        ("&#129785;", "Lung Cancer",       "Symptom &amp; lifestyle risk factors"),
        ("&#129656;", "Chronic Kidney",    "Renal health risk screening"),
        ("&#127895;&#65039;", "Breast Cancer", "Tumor feature classification"),
    ]

    cards_html = '<div class="disease-grid">'
    for icon, name, desc in DISEASES:
        cards_html += f"""<div class="disease-card">
<span style="display:block;font-size:28px;margin-bottom:10px;">{icon}</span>
<span style="display:block;font-size:13px;font-weight:600;color:#F2F2F2;margin-bottom:5px;">{name}</span>
<span style="display:block;font-size:11px;color:#5A5A5A;line-height:1.5;">{desc}</span>
</div>"""
    cards_html += "</div>"
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # ── How it works ──────────────────────────────────────────────────────────
    st.markdown("""
<div class="section-heading">
<span style="display:block;" class="section-label">Process</span>
<span style="display:block;" class="section-title">How It Works</span>
<span style="display:block;" class="section-subtitle">Four simple steps to your health insight</span>
</div>
""", unsafe_allow_html=True)

    STEPS = [
        ("01", "&#127973;", "Select a Module",     "Pick from 9 disease-prediction modules in the sidebar"),
        ("02", "&#128203;", "Enter Health Data",   "Fill in your clinical measurements or symptom history"),
        ("03", "&#129302;", "Run the Model",       "Our trained ML model analyzes your data instantly"),
        ("04", "&#128202;", "Review Your Result",  "Receive a clear, structured prediction with guidance"),
    ]

    steps_html = '<div class="steps-grid">'
    for num, icon, title, desc in STEPS:
        steps_html += f"""<div class="step-card">
<span style="display:block;font-size:10px;font-weight:700;color:#8B1E2D;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;">Step {num}</span>
<span style="display:block;font-size:26px;margin-bottom:10px;">{icon}</span>
<span style="display:block;font-size:14px;font-weight:600;color:#F2F2F2;margin-bottom:5px;">{title}</span>
<span style="display:block;font-size:11px;color:#5A5A5A;line-height:1.5;">{desc}</span>
</div>"""
    steps_html += "</div>"
    st.markdown(steps_html, unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # ── Disclaimer ────────────────────────────────────────────────────────────
    st.markdown("""
<div class="section-heading">
<span style="display:block;" class="section-label">Important Notice</span>
<span style="display:block;" class="section-title">Medical Disclaimer</span>
</div>
<div class="disclaimer-card">
<span style="display:block;" class="disclaimer-title">&#9877; For Informational Purposes Only</span>
<span style="display:block;" class="disclaimer-text">
This application uses machine-learning models trained on publicly available medical datasets.
The predictions generated are for educational and informational purposes only
and do not constitute a medical diagnosis or professional medical advice.<br><br>
Always consult a qualified and licensed healthcare professional for any health concerns,
medical decisions, or before changing any treatment or medication.
</span>
</div>
<br><br>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Disease page header
# ─────────────────────────────────────────────────────────────────────────────

def page_header(
    title: str,
    subtitle: str = "",
    tag: str = "Disease Prediction"
) -> None:
    """Consistent page header for every disease section."""
    sub_html = f'<span style="display:block;" class="page-header-desc">{subtitle}</span>' if subtitle else ""
    st.markdown(f"""
<div class="page-header">
<span style="display:block;" class="page-header-tag">&#128300; {tag}</span>
<span style="display:block;" class="page-header-title">{title}</span>
{sub_html}
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Section card label
# ─────────────────────────────────────────────────────────────────────────────

def section_label(text: str) -> None:
    """Render a small uppercase label above a group of inputs."""
    st.markdown(
        f'<div class="input-section-title">{text}</div>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Prediction result card
# ─────────────────────────────────────────────────────────────────────────────

def render_result(
    is_positive: bool,
    disease_name: str,
    patient_name: str = "",
    custom_message: str = "",
) -> None:
    """
    Render a professional prediction result card.

    IMPORTANT — uses only <span style="display:block"> for inner elements.
    Streamlit's markdown parser escapes nested <div> and <hr> when they appear
    inside an outer block-level <div>.  Inline <span> elements pass through
    the parser safely, so this avoids the raw-HTML-in-card bug.
    """
    if is_positive:
        card_class  = "risk"
        icon        = "&#9888;&#65039;"   # ⚠️
        title       = f"{disease_name} Risk Detected"
        title_color = "#E57373"
        default_msg = (
            f"Our model has identified potential risk indicators for {disease_name}. "
            "This does not confirm a diagnosis. Please consult a healthcare professional "
            "promptly for proper clinical evaluation and testing."
        )
    else:
        card_class  = "safe"
        icon        = "&#9989;"           # ✅
        title       = f"No {disease_name} Detected"
        title_color = "#6FCF97"
        default_msg = (
            f"Our model indicates lower risk indicators for {disease_name}. "
            "Continue maintaining a healthy lifestyle, stay hydrated, eat balanced meals, "
            "exercise regularly, and schedule routine medical check-ups."
        )

    message = custom_message if custom_message else default_msg

    name_span = (
        f'<span style="display:block;font-size:14px;color:#9A9A9A;margin-bottom:10px;">'
        f'Patient: <b style="color:#F2F2F2;font-weight:600;">{patient_name}</b></span>'
        if patient_name else ""
    )

    # ── Result card ──────────────────────────────────────────────────────────
    # All inner elements are <span style="display:block"> — NOT <div> or <hr>
    st.markdown(f"""
<div class="result-card {card_class}">
<span style="display:block;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5A5A5A;margin-bottom:14px;">PREDICTION RESULT</span>
<span style="display:block;font-size:52px;line-height:1.2;margin-bottom:12px;">{icon}</span>
<span style="display:block;font-size:22px;font-weight:700;color:{title_color};margin-bottom:10px;">{title}</span>
{name_span}
<span style="display:block;width:50%;height:1px;background:rgba(255,255,255,0.08);margin:12px auto 14px;"></span>
<span style="display:block;font-size:14px;color:#5A5A5A;line-height:1.75;max-width:520px;margin:0 auto;">{message}</span>
</div>
""", unsafe_allow_html=True)

    # ── Disclaimer ───────────────────────────────────────────────────────────
    st.markdown("""
<div class="disclaimer-card" style="margin-top:10px;">
<span style="display:block;font-size:13px;color:#5A5A5A;line-height:1.75;">&#9877; This prediction is for informational purposes only. Consult a qualified healthcare professional for medical advice, diagnosis, or treatment.</span>
</div>
""", unsafe_allow_html=True)
