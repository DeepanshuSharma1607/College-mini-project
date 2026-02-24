import streamlit as st
import requests

st.set_page_config(page_title="CGPA Predictor", layout="centered")

st.title("🎓 CGPA Predictor")

# Year selection
year = st.selectbox("Select your year", ["2nd Year","3rd Year","4th Year"])

# Inputs
gender = st.selectbox("Gender",["Male","Female","Other"])
attendance = st.number_input("Attendance %",0,100,80)
study_hours = st.number_input("Study Hours",0,24,5)

st.subheader("CGPA Inputs")

cgpa1 = st.number_input("1st Year CGPA",0.0,5.0,3.2,step=0.01)

cgpa2 = None
cgpa3 = None

if year in ["3rd Year","4th Year"]:
    cgpa2 = st.number_input("2nd Year CGPA",0.0,5.0,step=0.01)

if year=="4th Year":
    cgpa3 = st.number_input("3rd Year CGPA",0.0,5.0,step=0.01)

# Predict
if st.button("Predict"):

    year_num = {"2nd Year":2,"3rd Year":3,"4th Year":4}[year]

    body = {
        "Gender": gender,
        "attendance": float(attendance),
        "study_hours": float(study_hours),
        "CGPA100": float(cgpa1),
    }

    if cgpa2 is not None:
        body["CGPA200"] = float(cgpa2)

    if cgpa3 is not None:
        body["CGPA300"] = float(cgpa3)

    try:
        res = requests.post(
            "http://13.60.80.101/predict",
            params={"year": year_num},
            json=body
        )

        # Show backend error
        if res.status_code != 200:
            st.error(res.text)
            st.stop()

        out = res.json()

        st.success("Prediction Done ✅")

        st.metric("Average SGPA", out["current_avg_cgpa"])
        st.metric("Predicted CGPA", out["predicted_cgpa"])
        st.info(out["status"])

    except Exception as e:
        st.error(f"Connection error: {e}")