"""
components.py — Reusable UI components for the Multiple Disease Prediction app.
All visual presentation lives here; ML logic stays in app.py.
"""

import base64
import os
import streamlit as st


# ─────────────────────────────────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────────────────────────────────

def _logo_b64() -> str:
    """Return base64 data-URI for the project logo, or empty string.
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
        <div class="wine-loader-text">{text}</div>
        <div class="wine-loader-bar-bg">
            <div class="wine-loader-bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Hero / landing page
# ─────────────────────────────────────────────────────────────────────────────

def render_hero() -> None:
    """Render the full landing / hero page."""

    logo_src = _logo_b64()
    logo_html = (
        f'<img src="{logo_src}" alt="Logo" />'
        if logo_src else
        '<span style="font-size:64px;">🏥</span>'
    )

    # ── Hero top section ─────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-logo">{logo_html}</div>
        <div class="hero-tag">🧬 AI-Powered Medical Intelligence</div>
        <h1 class="hero-title">Multiple Disease<br><span>Prediction</span></h1>
        <p class="hero-subtitle">
            Instant, ML-powered health risk screening across 9 diseases.<br>
            Enter your clinical data — get a prediction in seconds.
        </p>
        <p class="hero-tagline">Predict &nbsp;·&nbsp; Prevent &nbsp;·&nbsp; Live Healthier</p>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA button — no rocket emoji ─────────────────────────────────────────
    _, col_btn, _ = st.columns([2.5, 1, 2.5])
    with col_btn:
        if st.button("Get Started", key="hero_cta", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()

    # ── Stats row — actual disease names instead of "9+" ─────────────────────
    st.markdown("""
    <div class="stats-row">
        <div class="stat-item">
            <div class="stat-number">ML</div>
            <div class="stat-label">Powered</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">⚡</div>
            <div class="stat-label">Instant Results</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">Free</div>
            <div class="stat-label">Always Free</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Supported diseases ────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-heading">
        <div class="section-label">Capabilities</div>
        <div class="section-title">What We Predict</div>
        <div class="section-subtitle">Accurate ML-powered screening across multiple conditions</div>
    </div>
    """, unsafe_allow_html=True)

    DISEASES = [
        ("🔬", "General Disease",   "Multi-symptom XGBoost classification"),
        ("🩸", "Diabetes",          "Blood glucose & clinical indicators"),
        ("❤️",  "Heart Disease",     "Cardiovascular risk assessment"),
        ("🧠", "Parkinson's",       "Voice biomarker analysis"),
        ("🫀", "Liver Disease",     "Liver function panel screening"),
        ("🦠", "Hepatitis",         "Hepatic biomarker prediction"),
        ("🫁", "Lung Cancer",       "Symptom & lifestyle risk factors"),
        ("🫘", "Chronic Kidney",    "Renal health risk screening"),
        ("🎗️", "Breast Cancer",     "Tumor feature classification"),
    ]

    cards_html = '<div class="disease-grid">'
    for icon, name, desc in DISEASES:
        cards_html += f"""
        <div class="disease-card">
            <span class="disease-card-icon">{icon}</span>
            <div class="disease-card-name">{name}</div>
            <div class="disease-card-desc">{desc}</div>
        </div>"""
    cards_html += "</div>"
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # ── How it works ──────────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-heading">
        <div class="section-label">Process</div>
        <div class="section-title">How It Works</div>
        <div class="section-subtitle">Four simple steps to your health insight</div>
    </div>
    """, unsafe_allow_html=True)

    STEPS = [
        ("01", "🏥", "Select a Module",     "Pick from 9 disease-prediction modules in the sidebar"),
        ("02", "📋", "Enter Health Data",   "Fill in your clinical measurements or symptom history"),
        ("03", "🤖", "Run the Model",       "Our trained ML model analyzes your data instantly"),
        ("04", "📊", "Review Your Result",  "Receive a clear, structured prediction with guidance"),
    ]

    steps_html = '<div class="steps-grid">'
    for num, icon, title, desc in STEPS:
        steps_html += f"""
        <div class="step-card">
            <div class="step-number">Step {num}</div>
            <span class="step-icon">{icon}</span>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
        </div>"""
    steps_html += "</div>"
    st.markdown(steps_html, unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # ── Disclaimer ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-heading">
        <div class="section-label">Important Notice</div>
        <div class="section-title">Medical Disclaimer</div>
    </div>
    <div class="disclaimer-card">
        <div class="disclaimer-title">&#9877; For Informational Purposes Only</div>
        <div class="disclaimer-text">
            This application uses machine-learning models trained on publicly available medical datasets.
            The predictions generated are for educational and informational purposes only
            and do not constitute a medical diagnosis or professional medical advice.<br><br>
            Always consult a qualified and licensed healthcare professional for any health concerns,
            medical decisions, or before changing any treatment or medication.
            Do not disregard professional advice because of something you read here.
        </div>
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
    sub_html = f'<div class="page-header-desc">{subtitle}</div>' if subtitle else ""
    st.markdown(f"""
    <div class="page-header">
        <div class="page-header-tag">&#128300; {tag}</div>
        <div class="page-header-title">{title}</div>
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
    Splits into multiple st.markdown() calls to avoid Streamlit HTML nesting issues.

    Args:
        is_positive   : True if the model predicted the disease is present.
        disease_name  : Human-readable disease name (e.g. 'Diabetes').
        patient_name  : Optional patient name to display.
        custom_message: Plain-text override for the result message.
    """
    if is_positive:
        card_class  = "risk"
        title_class = "risk"
        icon        = "⚠️"
        title       = f"{disease_name} Risk Detected"
        default_msg = (
            f"Our model has identified potential risk indicators for {disease_name}. "
            "This does not confirm a diagnosis. Please consult a healthcare professional "
            "promptly for proper clinical evaluation and testing."
        )
    else:
        card_class  = "safe"
        title_class = "safe"
        icon        = "✅"
        title       = f"No {disease_name} Detected"
        default_msg = (
            f"Our model indicates lower risk indicators for {disease_name}. "
            "Continue maintaining a healthy lifestyle, stay hydrated, eat balanced meals, "
            "exercise regularly, and schedule routine medical check-ups."
        )

    # Use plain text only — avoid passing raw HTML in message to prevent rendering issues
    message = custom_message if custom_message else default_msg

    name_row = ""
    if patient_name:
        name_row = f"""
        <tr>
            <td style="padding:4px 0;color:#9A9A9A;font-size:14px;text-align:center;">
                Patient: <span style="color:#F2F2F2;font-weight:600;">{patient_name}</span>
            </td>
        </tr>"""

    # ── Card header (icon, title, patient) ────────────────────────────────────
    st.markdown(f"""
    <div class="result-card {card_class}">
        <div class="result-label">Prediction Result</div>
        <div style="font-size:52px;line-height:1;margin-bottom:14px;">{icon}</div>
        <div class="result-title {title_class}">{title}</div>
        {"" if not patient_name else f'<div class="result-patient">Patient: <span style="color:#F2F2F2;font-weight:600;">{patient_name}</span></div>'}
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.08);margin:16px auto;width:50%;">
        <div style="font-size:14px;color:#5A5A5A;line-height:1.75;max-width:520px;margin:0 auto;">
            {message}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Disclaimer below card ─────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-top:10px;" class="disclaimer-card">
        <div class="disclaimer-text">
            &#9877; This prediction is for informational purposes only.
            Consult a qualified healthcare professional for medical advice,
            diagnosis, or treatment.
        </div>
    </div>
    """, unsafe_allow_html=True)
