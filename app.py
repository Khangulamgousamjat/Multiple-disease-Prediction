"""
app.py — Multiple Disease Prediction Web Application
Streamlit entry-point.  ML prediction logic is unchanged.
UI is driven by the centralized ui/ module.
"""

# ── Standard library / third-party imports ────────────────────────────────────
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# ── Internal imports ──────────────────────────────────────────────────────────
from code.DiseaseModel import DiseaseModel
from code.helper import prepare_symptoms_array

# ── UI system ─────────────────────────────────────────────────────────────────
from ui.styles     import inject_css
from ui.components import render_hero, page_header, section_label, render_result
from ui.sidebar    import render_sidebar

# ══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION  (must be the very first Streamlit call)
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Multiple Disease Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject global CSS design system ──────────────────────────────────────────
inject_css()

# ══════════════════════════════════════════════════════════════════════════════
# LOAD ML MODELS  (unchanged)
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource(show_spinner=False)
def load_models():
    models = {}
    models["diabetes"]   = joblib.load("models/diabetes_model.sav")
    models["heart"]      = joblib.load("models/heart_disease_model.sav")
    models["parkinson"]  = joblib.load("models/parkinsons_model.sav")
    models["lung"]       = joblib.load("models/lung_cancer_model.sav")
    models["breast"]     = joblib.load("models/breast_cancer.sav")
    models["chronic"]    = joblib.load("models/chronic_model.sav")
    models["hepatitis"]  = joblib.load("models/hepititisc_model.sav")
    models["liver"]      = joblib.load("models/liver_model.sav")
    return models

models = load_models()

diabetes_model      = models["diabetes"]
heart_model         = models["heart"]
parkinson_model     = models["parkinson"]
lung_cancer_model   = models["lung"]
breast_cancer_model = models["breast"]
chronic_disease_model = models["chronic"]
hepatitis_model     = models["hepatitis"]
liver_model         = models["liver"]

# ── Load lung cancer dataset (unchanged) ─────────────────────────────────────
lung_cancer_data = pd.read_csv("data/lung_cancer.csv")
lung_cancer_data["GENDER"] = lung_cancer_data["GENDER"].map({"M": "Male", "F": "Female"})

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "hero"

# ══════════════════════════════════════════════════════════════════════════════
# HERO / LANDING PAGE
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "hero":
    # Fully hide sidebar on hero page
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    render_hero()
    st.stop()   # Do not render the rest of the script


# ══════════════════════════════════════════════════════════════════════════════
# APP MODE — sidebar is fully visible
# ══════════════════════════════════════════════════════════════════════════════

selected = render_sidebar()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GENERAL DISEASE PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Disease Prediction":
    page_header(
        title="General Disease Prediction",
        subtitle="Enter your symptoms and our XGBoost model will predict the most likely disease.",
        tag="Symptom-Based Prediction",
    )

    # Load XGBoost model
    disease_model = DiseaseModel()
    disease_model.load_xgboost("model/xgboost_model.json")

    section_label("Symptom Input")
    symptoms = st.multiselect("What are your symptoms?", options=disease_model.all_symptoms)
    X = prepare_symptoms_array(symptoms)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔍 Predict Disease", key="btn_general_predict"):
        if not symptoms:
            st.warning("Please select at least one symptom before predicting.")
        else:
            with st.spinner(""):
                prediction, prob = disease_model.predict(X)

            render_result(
                is_positive=True,
                disease_name=prediction,
                custom_message=(
                    f"The model predicts <strong>{prediction}</strong> with "
                    f"<strong>{prob*100:.1f}%</strong> confidence based on the symptoms provided. "
                    "Please consult a healthcare professional for a clinical diagnosis."
                ),
            )

            st.markdown("<br>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["📄 Description", "🛡️ Precautions"])
            with tab1:
                st.write(disease_model.describe_predicted_disease())
            with tab2:
                precautions = disease_model.predicted_disease_precautions()
                for i in range(4):
                    st.write(f"**{i+1}.** {precautions[i]}")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: DIABETES PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Diabetes Prediction":
    page_header(
        title="Diabetes Prediction",
        subtitle="Enter clinical measurements to assess diabetes risk using a trained ML classifier.",
        tag="Endocrine Health",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="diab_name")

    section_label("Clinical Measurements")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, key="diab_preg")
    with col2:
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0, key="diab_glu")
    with col3:
        BloodPressure = st.number_input("Blood Pressure (mmHg)", min_value=0.0, key="diab_bp")
    with col1:
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0.0, key="diab_skin")
    with col2:
        Insulin = st.number_input("Insulin Level (µU/mL)", min_value=0.0, key="diab_ins")
    with col3:
        BMI = st.number_input("BMI (kg/m²)", min_value=0.0, key="diab_bmi")
    with col1:
        DiabetesPedigreefunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.001, format="%.3f", key="diab_dpf")
    with col2:
        Age = st.number_input("Age (years)", min_value=0, key="diab_age")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔍 Predict Diabetes", key="btn_diab"):
        diabetes_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness,
              Insulin, BMI, DiabetesPedigreefunction, Age]]
        )
        is_positive = diabetes_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Diabetes", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: HEART DISEASE PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Heart disease Prediction":
    page_header(
        title="Heart Disease Prediction",
        subtitle="Provide cardiovascular measurements to assess heart disease risk.",
        tag="Cardiovascular Health",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="heart_name")

    section_label("Patient Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (years)", min_value=0, key="heart_age")
    with col2:
        sex = 0
        sex_val = st.selectbox("Sex", ["Male", "Female"], key="heart_sex")
        sex = 1 if sex_val == "Male" else 0
    with col3:
        cp = 0
        cp_options = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
        cp_val = st.selectbox("Chest Pain Type", cp_options, key="heart_cp")
        cp = cp_options.index(cp_val)

    section_label("Vital Signs & Tests")
    with col1:
        trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=0.0, key="heart_rbp")
    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0.0, key="heart_chol")
    with col3:
        restecg_options = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
        restecg_val = st.selectbox("Resting ECG Result", restecg_options, key="heart_ecg")
        restecg = restecg_options.index(restecg_val)

    with col1:
        thalach = st.number_input("Max Heart Rate Achieved (bpm)", min_value=0.0, key="heart_thal")
    with col2:
        oldpeak = st.number_input("ST Depression (Exercise vs Rest)", min_value=0.0, step=0.1, format="%.1f", key="heart_op")
    with col3:
        slope_options = ["Upsloping", "Flat", "Downsloping"]
        slope_val = st.selectbox("Peak Exercise ST Slope", slope_options, key="heart_slope")
        slope = slope_options.index(slope_val)

    section_label("Additional Findings")
    with col1:
        ca = st.number_input("Major Vessels Colored by Fluoroscopy (0–3)", min_value=0, max_value=3, key="heart_ca")
    with col2:
        thal_options = ["Normal", "Fixed Defect", "Reversible Defect"]
        thal_val = st.selectbox("Thalassemia", thal_options, key="heart_thal_sel")
        thal = thal_options.index(thal_val)
    with col3:
        exang_cb = st.checkbox("Exercise-Induced Angina", key="heart_exang")
        exang = 1 if exang_cb else 0
    with col1:
        fbs_cb = st.checkbox("Fasting Blood Sugar > 120 mg/dL", key="heart_fbs")
        fbs = 1 if fbs_cb else 0

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Heart Disease", key="btn_heart"):
        heart_prediction = heart_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg,
              thalach, exang, oldpeak, slope, ca, thal]]
        )
        is_positive = heart_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Heart Disease", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PARKINSON'S PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Parkison Prediction":
    page_header(
        title="Parkinson's Disease Prediction",
        subtitle="Enter voice biomarker measurements to screen for Parkinson's disease.",
        tag="Neurological Health",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="park_name")

    section_label("MDVP Voice Measurements")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP          = st.number_input("MDVP: Fo (Hz)",          step=0.001, format="%.3f", key="park_fo")
    with col2:
        MDVPFIZ       = st.number_input("MDVP: Fhi (Hz)",         step=0.001, format="%.3f", key="park_fhi")
    with col3:
        MDVPFLO       = st.number_input("MDVP: Flo (Hz)",         step=0.001, format="%.3f", key="park_flo")
    with col1:
        MDVPJITTER    = st.number_input("MDVP: Jitter (%)",       step=0.00001, format="%.5f", key="park_jit")
    with col2:
        MDVPJitterAbs = st.number_input("MDVP: Jitter (Abs)",     step=0.00001, format="%.5f", key="park_jitabs")
    with col3:
        MDVPRAP       = st.number_input("MDVP: RAP",              step=0.00001, format="%.5f", key="park_rap")
    with col2:
        MDVPPPQ       = st.number_input("MDVP: PPQ",              step=0.00001, format="%.5f", key="park_ppq")
    with col3:
        JitterDDP     = st.number_input("Jitter: DDP",            step=0.00001, format="%.5f", key="park_ddp")

    section_label("Shimmer Measurements")
    with col1:
        MDVPShimmer    = st.number_input("MDVP: Shimmer",         step=0.00001, format="%.5f", key="park_shim")
    with col2:
        MDVPShimmer_dB = st.number_input("MDVP: Shimmer (dB)",   step=0.001,   format="%.3f", key="park_shimdb")
    with col3:
        Shimmer_APQ3   = st.number_input("Shimmer: APQ3",         step=0.00001, format="%.5f", key="park_apq3")
    with col1:
        ShimmerAPQ5    = st.number_input("Shimmer: APQ5",         step=0.00001, format="%.5f", key="park_apq5")
    with col2:
        MDVP_APQ       = st.number_input("MDVP: APQ",             step=0.00001, format="%.5f", key="park_apq")
    with col3:
        ShimmerDDA     = st.number_input("Shimmer: DDA",          step=0.00001, format="%.5f", key="park_dda")

    section_label("Noise Ratios & Nonlinear Features")
    with col1:
        NHR     = st.number_input("NHR",     step=0.0001, format="%.4f", key="park_nhr")
    with col2:
        HNR     = st.number_input("HNR",     step=0.001,  format="%.3f", key="park_hnr")
    with col2:
        RPDE    = st.number_input("RPDE",    step=0.0001, format="%.4f", key="park_rpde")
    with col3:
        DFA     = st.number_input("DFA",     step=0.0001, format="%.4f", key="park_dfa")
    with col1:
        spread1 = st.number_input("spread1", step=0.0001, format="%.4f", key="park_sp1")
    with col1:
        spread2 = st.number_input("spread2", step=0.0001, format="%.4f", key="park_sp2")
    with col3:
        D2      = st.number_input("D2",      step=0.0001, format="%.4f", key="park_d2")
    with col1:
        PPE     = st.number_input("PPE",     step=0.0001, format="%.4f", key="park_ppe")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Parkinson's", key="btn_park"):
        parkinson_prediction = parkinson_model.predict(
            [[MDVP, MDVPFIZ, MDVPFLO, MDVPJITTER, MDVPJitterAbs, MDVPRAP,
              MDVPPPQ, JitterDDP, MDVPShimmer, MDVPShimmer_dB, Shimmer_APQ3,
              ShimmerAPQ5, MDVP_APQ, ShimmerDDA, NHR, HNR, RPDE, DFA,
              spread1, spread2, D2, PPE]]
        )
        is_positive = parkinson_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Parkinson's Disease", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: LUNG CANCER PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Lung Cancer Prediction":
    page_header(
        title="Lung Cancer Prediction",
        subtitle="Assess lung cancer risk based on lifestyle factors and reported symptoms.",
        tag="Oncology Screening",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="lung_name")

    section_label("Demographics")
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", lung_cancer_data["GENDER"].unique(), key="lung_gen")
    with col2:
        age = st.number_input("Age (years)", min_value=0, key="lung_age")

    section_label("Lifestyle & Symptom Factors")
    with col3:
        smoking              = st.selectbox("Smoking",              ["NO", "YES"], key="lung_smk")
    with col1:
        yellow_fingers       = st.selectbox("Yellow Fingers",       ["NO", "YES"], key="lung_yf")
    with col2:
        anxiety              = st.selectbox("Anxiety",              ["NO", "YES"], key="lung_anx")
    with col3:
        peer_pressure        = st.selectbox("Peer Pressure",        ["NO", "YES"], key="lung_pp")
    with col1:
        chronic_disease      = st.selectbox("Chronic Disease",      ["NO", "YES"], key="lung_cd")
    with col2:
        fatigue              = st.selectbox("Fatigue",              ["NO", "YES"], key="lung_fat")
    with col3:
        allergy              = st.selectbox("Allergy",              ["NO", "YES"], key="lung_all")
    with col1:
        wheezing             = st.selectbox("Wheezing",             ["NO", "YES"], key="lung_wh")
    with col2:
        alcohol_consuming    = st.selectbox("Alcohol Consuming",    ["NO", "YES"], key="lung_alc")
    with col3:
        coughing             = st.selectbox("Coughing",             ["NO", "YES"], key="lung_co")
    with col1:
        shortness_of_breath  = st.selectbox("Shortness of Breath",  ["NO", "YES"], key="lung_sob")
    with col2:
        swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["NO", "YES"], key="lung_sd")
    with col3:
        chest_pain           = st.selectbox("Chest Pain",           ["NO", "YES"], key="lung_cp")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Lung Cancer", key="btn_lung"):
        user_data = pd.DataFrame({
            "GENDER":             [gender],
            "AGE":                [age],
            "SMOKING":            [smoking],
            "YELLOW_FINGERS":     [yellow_fingers],
            "ANXIETY":            [anxiety],
            "PEER_PRESSURE":      [peer_pressure],
            "CHRONICDISEASE":     [chronic_disease],
            "FATIGUE":            [fatigue],
            "ALLERGY":            [allergy],
            "WHEEZING":           [wheezing],
            "ALCOHOLCONSUMING":   [alcohol_consuming],
            "COUGHING":           [coughing],
            "SHORTNESSOFBREATH":  [shortness_of_breath],
            "SWALLOWINGDIFFICULTY": [swallowing_difficulty],
            "CHESTPAIN":          [chest_pain],
        })
        user_data.replace({"NO": 1, "YES": 2}, inplace=True)
        user_data.columns = user_data.columns.str.strip()
        numeric_cols = ["AGE", "FATIGUE", "ALLERGY", "ALCOHOLCONSUMING",
                        "COUGHING", "SHORTNESSOFBREATH"]
        user_data[numeric_cols] = user_data[numeric_cols].apply(pd.to_numeric, errors="coerce")

        cancer_prediction = lung_cancer_model.predict(user_data)
        is_positive = cancer_prediction[0] == "YES"
        render_result(is_positive=is_positive, disease_name="Lung Cancer", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: LIVER DISEASE PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Liver prediction":
    page_header(
        title="Liver Disease Prediction",
        subtitle="Enter liver function test results to assess liver disease risk.",
        tag="Hepatology",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="liver_name")

    section_label("Patient Demographics")
    col1, col2, col3 = st.columns(3)
    with col1:
        sex_val = st.selectbox("Sex", ["Male", "Female"], key="liver_sex")
        Sex = 0 if sex_val == "Male" else 1
    with col2:
        age = st.number_input("Age (years)", min_value=0, key="liver_age")

    section_label("Liver Function Panel")
    with col3:
        Total_Bilirubin              = st.number_input("Total Bilirubin (mg/dL)",             min_value=0.0, step=0.1, key="liver_tb")
    with col1:
        Direct_Bilirubin             = st.number_input("Direct Bilirubin (mg/dL)",            min_value=0.0, step=0.1, key="liver_db")
    with col2:
        Alkaline_Phosphotase         = st.number_input("Alkaline Phosphotase (IU/L)",         min_value=0.0, key="liver_ap")
    with col3:
        Alamine_Aminotransferase     = st.number_input("Alamine Aminotransferase (IU/L)",     min_value=0.0, key="liver_alt")
    with col1:
        Aspartate_Aminotransferase   = st.number_input("Aspartate Aminotransferase (IU/L)",   min_value=0.0, key="liver_ast")
    with col2:
        Total_Protiens               = st.number_input("Total Proteins (g/dL)",               min_value=0.0, step=0.1, key="liver_tp")
    with col3:
        Albumin                      = st.number_input("Albumin (g/dL)",                      min_value=0.0, step=0.1, key="liver_alb")
    with col1:
        Albumin_and_Globulin_Ratio   = st.number_input("Albumin / Globulin Ratio",            min_value=0.0, step=0.01, key="liver_agr")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Liver Disease", key="btn_liver"):
        liver_prediction = liver_model.predict(
            [[Sex, age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
              Alamine_Aminotransferase, Aspartate_Aminotransferase,
              Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]]
        )
        is_positive = liver_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Liver Disease", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: HEPATITIS PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Hepatitis prediction":
    page_header(
        title="Hepatitis Prediction",
        subtitle="Enter hepatic biomarker values to predict hepatitis risk.",
        tag="Infectious Disease",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="hep_name")

    section_label("Demographics")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (years)", min_value=0, key="hep_age")
    with col2:
        sex_val = st.selectbox("Sex", ["Male", "Female"], key="hep_sex")
        sex = 1 if sex_val == "Male" else 2

    section_label("Blood Panel")
    with col3:
        total_bilirubin          = st.number_input("ALB (Albumin)", min_value=0.0, step=0.1, key="hep_alb")
    with col1:
        direct_bilirubin         = st.number_input("ALP (Alkaline Phosphatase)", min_value=0.0, key="hep_alp")
    with col2:
        alkaline_phosphatase     = st.number_input("ALT (Alanine Aminotransferase)", min_value=0.0, key="hep_alt")
    with col3:
        alamine_aminotransferase = st.number_input("AST (Aspartate Aminotransferase)", min_value=0.0, key="hep_ast")
    with col1:
        aspartate_aminotransferase = st.number_input("BIL (Bilirubin)", min_value=0.0, step=0.1, key="hep_bil")
    with col2:
        total_proteins           = st.number_input("CHE (Cholinesterase)", min_value=0.0, step=0.1, key="hep_che")
    with col3:
        albumin                  = st.number_input("CHOL (Cholesterol)", min_value=0.0, step=0.1, key="hep_chol")
    with col1:
        albumin_and_globulin_ratio = st.number_input("CREA (Creatinine)", min_value=0.0, step=0.1, key="hep_crea")
    with col2:
        your_ggt_value           = st.number_input("GGT (Gamma-Glutamyl Transferase)", min_value=0.0, key="hep_ggt")
    with col3:
        your_prot_value          = st.number_input("PROT (Total Protein)", min_value=0.0, step=0.1, key="hep_prot")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Hepatitis", key="btn_hep"):
        user_data = pd.DataFrame({
            "Age":  [age],
            "Sex":  [sex],
            "ALB":  [total_bilirubin],
            "ALP":  [direct_bilirubin],
            "ALT":  [alkaline_phosphatase],
            "AST":  [alamine_aminotransferase],
            "BIL":  [aspartate_aminotransferase],
            "CHE":  [total_proteins],
            "CHOL": [albumin],
            "CREA": [albumin_and_globulin_ratio],
            "GGT":  [your_ggt_value],
            "PROT": [your_prot_value],
        })
        hepatitis_prediction = hepatitis_model.predict(user_data)
        is_positive = hepatitis_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Hepatitis", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CHRONIC KIDNEY DISEASE PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Chronic Kidney prediction":
    page_header(
        title="Chronic Kidney Disease Prediction",
        subtitle="Analyze renal health markers to predict chronic kidney disease risk.",
        tag="Nephrology",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="ckd_name")

    section_label("Basic Renal Indicators")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Age (years)",            1, 100, 25,       key="ckd_age")
    with col2:
        bp  = st.slider("Blood Pressure (mmHg)", 50, 200, 120,     key="ckd_bp")
    with col3:
        sg  = st.slider("Specific Gravity",       1.0, 1.05, 1.02, step=0.001, key="ckd_sg")

    with col1:
        al  = st.slider("Albumin (0–5)",          0, 5, 0,          key="ckd_al")
    with col2:
        su  = st.slider("Sugar (0–5)",             0, 5, 0,          key="ckd_su")
    with col3:
        rbc_val = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"], key="ckd_rbc")
        rbc = 1 if rbc_val == "Normal" else 0

    section_label("Cell & Bacteria Indicators")
    with col1:
        pc_val = st.selectbox("Pus Cells",       ["Normal", "Abnormal"], key="ckd_pc")
        pc = 1 if pc_val == "Normal" else 0
    with col2:
        pcc_val = st.selectbox("Pus Cell Clumps", ["Present", "Not Present"], key="ckd_pcc")
        pcc = 1 if pcc_val == "Present" else 0
    with col3:
        ba_val = st.selectbox("Bacteria",         ["Present", "Not Present"], key="ckd_ba")
        ba = 1 if ba_val == "Present" else 0

    section_label("Blood Chemistry")
    with col1:
        bgr = st.slider("Blood Glucose Random (mg/dL)", 50, 200, 120, key="ckd_bgr")
    with col2:
        bu  = st.slider("Blood Urea (mg/dL)",           10, 200, 60,  key="ckd_bu")
    with col3:
        sc  = st.slider("Serum Creatinine (mg/dL)",      0,  10,  3,  key="ckd_sc")
    with col1:
        sod = st.slider("Sodium (mEq/L)",               100, 200, 140, key="ckd_sod")
    with col2:
        pot = st.slider("Potassium (mEq/L)",              2,   7,  4,  key="ckd_pot")
    with col3:
        hemo = st.slider("Hemoglobin (g/dL)",             3,  17, 12,  key="ckd_hemo")

    section_label("Blood Count")
    with col1:
        pcv = st.slider("Packed Cell Volume (%)",        20, 60, 40,      key="ckd_pcv")
    with col2:
        wc  = st.slider("White Blood Cells (cells/µL)",2000,20000,10000,  key="ckd_wc")
    with col3:
        rc  = st.slider("Red Blood Cells (million/µL)",  2,   8,  4,     key="ckd_rc")

    section_label("Medical History")
    with col1:
        htn_val   = st.selectbox("Hypertension",          ["Yes", "No"], key="ckd_htn")
        htn = 1 if htn_val == "Yes" else 0
    with col2:
        dm_val    = st.selectbox("Diabetes Mellitus",     ["Yes", "No"], key="ckd_dm")
        dm = 1 if dm_val == "Yes" else 0
    with col3:
        cad_val   = st.selectbox("Coronary Artery Disease", ["Yes", "No"], key="ckd_cad")
        cad = 1 if cad_val == "Yes" else 0
    with col1:
        appet_val = st.selectbox("Appetite",              ["Good", "Poor"], key="ckd_appet")
        appet = 1 if appet_val == "Good" else 0
    with col2:
        pe_val    = st.selectbox("Pedal Edema",           ["Yes", "No"], key="ckd_pe")
        pe = 1 if pe_val == "Yes" else 0
    with col3:
        ane_val   = st.selectbox("Anemia",                ["Yes", "No"], key="ckd_ane")
        ane = 1 if ane_val == "Yes" else 0

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Chronic Kidney Disease", key="btn_ckd"):
        user_input = pd.DataFrame({
            "age": [age], "bp": [bp], "sg": [sg], "al": [al], "su": [su],
            "rbc": [rbc], "pc": [pc], "pcc": [pcc], "ba": [ba],
            "bgr": [bgr], "bu": [bu], "sc": [sc], "sod": [sod], "pot": [pot],
            "hemo": [hemo], "pcv": [pcv], "wc": [wc], "rc": [rc],
            "htn": [htn], "dm": [dm], "cad": [cad], "appet": [appet],
            "pe": [pe], "ane": [ane],
        })
        kidney_prediction = chronic_disease_model.predict(user_input)
        is_positive = kidney_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Chronic Kidney Disease", patient_name=name)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: BREAST CANCER PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
if selected == "Breast Cancer Prediction":
    page_header(
        title="Breast Cancer Prediction",
        subtitle="Enter tumor cell nucleus measurements to predict breast cancer malignancy.",
        tag="Oncology Screening",
    )

    name = st.text_input("Patient Name", placeholder="Enter patient name…", key="bc_name")

    section_label("Mean Nucleus Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        radius_mean              = st.slider("Radius Mean",              6.0,   30.0,  15.0,        key="bc_rm")
        texture_mean             = st.slider("Texture Mean",             9.0,   40.0,  20.0,        key="bc_tm")
        perimeter_mean           = st.slider("Perimeter Mean",          43.0,  190.0,  90.0,        key="bc_pm")
    with col2:
        area_mean                = st.slider("Area Mean",              143.0, 2501.0, 750.0,        key="bc_am")
        smoothness_mean          = st.slider("Smoothness Mean",          0.05,   0.25,   0.10, step=0.001, key="bc_sm")
        compactness_mean         = st.slider("Compactness Mean",         0.02,   0.30,   0.15, step=0.001, key="bc_cm")
    with col3:
        concavity_mean           = st.slider("Concavity Mean",           0.0,    0.50,   0.20, step=0.001, key="bc_con")
        concave_points_mean      = st.slider("Concave Points Mean",      0.0,    0.20,   0.10, step=0.001, key="bc_cpm")
        symmetry_mean            = st.slider("Symmetry Mean",            0.1,    1.0,    0.50, step=0.01,  key="bc_sym")

    section_label("Mean Nucleus Features (cont.)")
    with col1:
        fractal_dimension_mean   = st.slider("Fractal Dimension Mean",   0.01,   0.10,   0.05, step=0.001, key="bc_fdm")

    section_label("Standard Error Features")
    with col2:
        radius_se                = st.slider("Radius SE",                0.1,    3.0,    1.0,  step=0.01,  key="bc_rse")
        texture_se               = st.slider("Texture SE",               0.2,    2.0,    1.0,  step=0.01,  key="bc_tse")
    with col3:
        perimeter_se             = st.slider("Perimeter SE",             1.0,   30.0,   10.0,  step=0.1,   key="bc_pse")
    with col1:
        area_se                  = st.slider("Area SE",                  6.0,  500.0,  150.0,  step=1.0,   key="bc_ase")
        smoothness_se            = st.slider("Smoothness SE",            0.001,  0.03,   0.01, step=0.0001,key="bc_sse")
    with col2:
        compactness_se           = st.slider("Compactness SE",           0.002,  0.20,   0.10, step=0.001, key="bc_cse")
        concavity_se             = st.slider("Concavity SE",             0.0,    0.05,   0.02, step=0.001, key="bc_conse")
    with col3:
        concave_points_se        = st.slider("Concave Points SE",        0.0,    0.03,   0.01, step=0.001, key="bc_cpse")
        symmetry_se              = st.slider("Symmetry SE",              0.1,    1.0,    0.50, step=0.01,  key="bc_symse")
    with col1:
        fractal_dimension_se     = st.slider("Fractal Dimension SE",     0.01,   0.10,   0.05, step=0.001, key="bc_fdse")

    section_label("Worst-Case Features")
    with col2:
        radius_worst             = st.slider("Radius Worst",             7.0,   40.0,   20.0,  step=0.1,   key="bc_rw")
        texture_worst            = st.slider("Texture Worst",           12.0,   50.0,   25.0,  step=0.1,   key="bc_tw")
        perimeter_worst          = st.slider("Perimeter Worst",         50.0,  250.0,  120.0,  step=1.0,   key="bc_pw")
    with col3:
        area_worst               = st.slider("Area Worst",             185.0, 4250.0, 1500.0,  step=10.0,  key="bc_aw")
        smoothness_worst         = st.slider("Smoothness Worst",         0.07,   0.30,   0.15, step=0.001, key="bc_sw")
        compactness_worst        = st.slider("Compactness Worst",        0.03,   0.60,   0.30, step=0.001, key="bc_cw")
    with col1:
        concavity_worst          = st.slider("Concavity Worst",          0.0,    0.80,   0.40, step=0.01,  key="bc_conw")
        concave_points_worst     = st.slider("Concave Points Worst",     0.0,    0.20,   0.10, step=0.001, key="bc_cpw")
        symmetry_worst           = st.slider("Symmetry Worst",           0.1,    1.0,    0.50, step=0.01,  key="bc_symw")
    with col2:
        fractal_dimension_worst  = st.slider("Fractal Dimension Worst",  0.01,   0.20,   0.10, step=0.001, key="bc_fdw")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Predict Breast Cancer", key="btn_bc"):
        user_input = pd.DataFrame({
            "radius_mean":              [radius_mean],
            "texture_mean":             [texture_mean],
            "perimeter_mean":           [perimeter_mean],
            "area_mean":                [area_mean],
            "smoothness_mean":          [smoothness_mean],
            "compactness_mean":         [compactness_mean],
            "concavity_mean":           [concavity_mean],
            "concave points_mean":      [concave_points_mean],
            "symmetry_mean":            [symmetry_mean],
            "fractal_dimension_mean":   [fractal_dimension_mean],
            "radius_se":                [radius_se],
            "texture_se":               [texture_se],
            "perimeter_se":             [perimeter_se],
            "area_se":                  [area_se],
            "smoothness_se":            [smoothness_se],
            "compactness_se":           [compactness_se],
            "concavity_se":             [concavity_se],
            "concave points_se":        [concave_points_se],
            "symmetry_se":              [symmetry_se],
            "fractal_dimension_se":     [fractal_dimension_se],
            "radius_worst":             [radius_worst],
            "texture_worst":            [texture_worst],
            "perimeter_worst":          [perimeter_worst],
            "area_worst":               [area_worst],
            "smoothness_worst":         [smoothness_worst],
            "compactness_worst":        [compactness_worst],
            "concavity_worst":          [concavity_worst],
            "concave points_worst":     [concave_points_worst],
            "symmetry_worst":           [symmetry_worst],
            "fractal_dimension_worst":  [fractal_dimension_worst],
        })
        breast_cancer_prediction = breast_cancer_model.predict(user_input)
        is_positive = breast_cancer_prediction[0] == 1
        render_result(is_positive=is_positive, disease_name="Breast Cancer", patient_name=name)
