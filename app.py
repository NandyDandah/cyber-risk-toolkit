import streamlit as st
import pandas as pd
from risk_engine import assess_risk


def convert_rating(value):
    rating_map = {
        "very low": 1,
        "low": 2,
        "medium": 3,
        "high": 4,
        "very high": 5,
        "critical": 5
    }

    value = str(value).strip().lower()
    value = value.replace("|", "")
    value = value.replace("'", "")
    value = value.replace('"', "")
    value = value.strip()

    if value in rating_map:
        return rating_map[value]

    try:
        return int(float(value))
    except ValueError:
        raise ValueError(f"Invalid rating value found: {value}")


def assess_all_risks(dataframe):
    assessed_risks = []

    for _, row in dataframe.iterrows():
        result = assess_risk(
            asset=row["asset"],
            threat=row["threat"],
            vulnerability=row["vulnerability"],
            likelihood=convert_rating(row["likelihood"]),
            impact=convert_rating(row["impact"])
        )

        assessed_risks.append(result)

    return pd.DataFrame(assessed_risks)


st.set_page_config(
    page_title="Cybersecurity Risk Assessment Toolkit",
    layout="wide"
)

st.title("🔐 Cybersecurity Risk Assessment Toolkit")
st.write("Upload or load cybersecurity risks and assess their risk level automatically.")

uploaded_file = st.file_uploader("Upload your risk data CSV", type=["csv"])

if uploaded_file is not None:
    risk_data = pd.read_csv(uploaded_file)
else:
    risk_data = pd.read_csv("data/risk_data.csv")

st.subheader("Original Risk Data")
st.dataframe(risk_data)

assessed_risks = assess_all_risks(risk_data)

st.subheader("Assessed Risk Report")
st.dataframe(assessed_risks)

st.subheader("Risk Summary")

total_risks = len(assessed_risks)
critical_risks = len(assessed_risks[assessed_risks["risk_level"] == "Critical"])
high_risks = len(assessed_risks[assessed_risks["risk_level"] == "High"])
medium_risks = len(assessed_risks[assessed_risks["risk_level"] == "Medium"])
low_risks = len(assessed_risks[assessed_risks["risk_level"] == "Low"])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Risks", total_risks)
col2.metric("Critical", critical_risks)
col3.metric("High", high_risks)
col4.metric("Medium", medium_risks)
col5.metric("Low", low_risks)

st.subheader("Risk Level Chart")
risk_counts = assessed_risks["risk_level"].value_counts()
st.bar_chart(risk_counts)

st.subheader("Top 5 Risks")
top_risks = assessed_risks.sort_values(by="risk_score", ascending=False).head(5)
st.dataframe(top_risks)

csv = assessed_risks.to_csv(index=False)

st.download_button(
    label="Download Risk Assessment Report",
    data=csv,
    file_name="risk_assessment_report.csv",
    mime="text/csv"
)