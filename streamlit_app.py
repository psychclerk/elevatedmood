import streamlit as st
import random

# -----------------------------------
# App Configuration
# -----------------------------------
st.set_page_config(
    page_title="Elevated Mood Case Simulator",
    layout="centered"
)

st.title("😄 Excessive Happiness / Elevated Mood – Case Simulator")
st.caption("Psychiatry presentation-based cases | MBBS / OSCE level")

# -----------------------------------
# Case Generator
# -----------------------------------
def generate_case():
    cases = [

        {
            "diagnosis": "Bipolar Disorder – Manic Episode",
            "age": 28,
            "sex": "Male",
            "presenting_complaint": "Excessive happiness and increased energy",
            "duration": "10 days",
            "associated": "Decreased sleep, pressured speech, grandiosity, spending sprees",
            "risk_factors": ["Past depressive episode"],
            "mse": (
                "Elated mood, increased psychomotor activity, pressured speech, "
                "flight of ideas, inflated self-esteem"
            ),
            "investigations": "Routine blood tests normal",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low (but high risk of impulsive harm)"
            },
            "explanation": (
                "Sustained elevated mood with increased energy, reduced need for sleep "
                "and marked functional impairment consistent with mania."
            ),
            "management": (
                "• Hospitalize if severe or risky behavior\n"
                "• Mood stabilizer (Lithium / Valproate)\n"
                "• Antipsychotic for acute control\n"
                "• Avoid antidepressants"
            )
        },

        {
            "diagnosis": "Bipolar Disorder – Hypomanic Episode",
            "age": 24,
            "sex": "Female",
            "presenting_complaint": "Feeling unusually happy and productive",
            "duration": "5 days",
            "associated": "Reduced sleep, talkativeness, increased goal-directed activity",
            "risk_factors": ["Family history of bipolar disorder"],
            "mse": (
                "Cheerful mood, increased speech, mildly distractible, no psychosis"
            ),
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": (
                "Hypomania is a milder form of mania without marked social or occupational impairment."
            ),
            "management": (
                "• Mood stabilizer if recurrent\n"
                "• Psychoeducation\n"
                "• Monitor for progression to mania"
            )
        },

        {
            "diagnosis": "Substance-Induced Mood Disorder (Stimulants)",
            "age": 31,
            "sex": "Male",
            "presenting_complaint": "Extreme happiness and confidence after drug use",
            "duration": "2 days",
            "associated": "Insomnia, agitation, palpitations",
            "risk_factors": ["Cocaine use"],
            "mse": (
                "Euphoric mood, restlessness, pressured speech"
            ),
            "investigations": "Urine toxicology positive for stimulants",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low–Moderate (impulsivity)"
            },
            "explanation": (
                "Mood elevation temporally related to substance use."
            ),
            "management": (
                "• Stop offending substance\n"
                "• Supportive care\n"
                "• Treat agitation if required"
            )
        },

        {
            "diagnosis": "Antidepressant-Induced Mania",
            "age": 35,
            "sex": "Female",
            "presenting_complaint": "Sudden excessive happiness after starting medication",
            "duration": "1 week",
            "associated": "Reduced sleep, increased confidence, overtalkative",
            "risk_factors": ["Recent SSRI initiation"],
            "mse": (
                "Elated mood, pressured speech, increased activity"
            ),
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Low"
            },
            "explanation": (
                "Antidepressants can precipitate mania in vulnerable individuals."
            ),
            "management": (
                "• Stop antidepressant\n"
                "• Start mood stabilizer\n"
                "• Re-evaluate diagnosis (bipolarity)"
            )
        },

        {
            "diagnosis": "Schizoaffective Disorder – Manic Type",
            "age": 29,
            "sex": "Male",
            "presenting_complaint": "Excessive happiness with unusual beliefs",
            "duration": "3 weeks",
            "associated": "Decreased sleep, grandiose delusions",
            "risk_factors": ["Past psychotic episodes"],
            "mse": (
                "Elated mood, grandiosity, delusional ideas"
            ),
            "investigations": "Normal",
            "suicide_risk": {
                "ideation": "Absent",
                "plan": "Absent",
                "risk_level": "Moderate (poor judgment)"
            },
            "explanation": (
                "Concurrent mood symptoms and psychotic features independent of mood episodes."
            ),
            "management": (
                "• Antipsychotic\n"
                "• Mood stabilizer\n"
                "• Long-term psychiatric follow-up"
            )
        }

    ]

    return random.choice(cases)

# -----------------------------------
# Session State Initialization
# -----------------------------------
if "case" not in st.session_state:
    st.session_state.case = generate_case()
    st.session_state.reveal = {
        "history": False,
        "mse": False,
        "investigations": False,
        "suicide": False,
        "explanation": False,
        "management": False
    }

case = st.session_state.case

# -----------------------------------
# UI Sections
# -----------------------------------

st.header("📜 History")
if st.button("Reveal History", key="btn_history"):
    st.session_state.reveal["history"] = True

if st.session_state.reveal["history"]:
    st.write(f"**Age / Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Presenting Complaint:** {case['presenting_complaint']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated Symptoms:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

st.header("🩺 Mental Status Examination")
if st.button("Reveal MSE", key="btn_mse"):
    st.session_state.reveal["mse"] = True
if st.session_state.reveal["mse"]:
    st.write(case["mse"])

st.header("🧪 Investigations")
if st.button("Reveal Investigations", key="btn_inv"):
    st.session_state.reveal["investigations"] = True
if st.session_state.reveal["investigations"]:
    st.write(case["investigations"])

st.header("⚠️ Risk Assessment")
if st.button("Assess Risk", key="btn_risk"):
    st.session_state.reveal["suicide"] = True
if st.session_state.reveal["suicide"]:
    sr = case["suicide_risk"]
    st.write(f"Ideation: {sr['ideation']}")
    st.write(f"Plan: {sr['plan']}")
    st.write(f"Overall Risk: {sr['risk_level']}")

st.header("🧠 Most Likely Diagnosis")
options = [
    "Bipolar Disorder – Manic Episode",
    "Bipolar Disorder – Hypomanic Episode",
    "Substance-Induced Mood Disorder (Stimulants)",
    "Antidepressant-Induced Mania",
    "Schizoaffective Disorder – Manic Type"
]
user_dx = st.selectbox("Select diagnosis", options)

if st.button("Submit Diagnosis", key="btn_dx"):
    if user_dx == case["diagnosis"]:
        st.success("✅ Correct diagnosis")
    else:
        st.error(f"❌ Correct answer: {case['diagnosis']}")

st.header("📖 Explanation")
if st.button("Reveal Explanation", key="btn_exp"):
    st.session_state.reveal["explanation"] = True
if st.session_state.reveal["explanation"]:
    st.info(case["explanation"])

st.header("💊 Management")
if st.button("Reveal Management", key="btn_mgmt"):
    st.session_state.reveal["management"] = True
if st.session_state.reveal["management"]:
    st.success(case["management"])

st.divider()
if st.button("🔄 New Case", key="btn_new"):
    st.session_state.clear()
    st.rerun()
