import streamlit as st
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
latest = pd.read_csv(ROOT / "data" / "cleaned" / "country_intelligence_summary.csv")
st.title("AI-Style Insights")
q = st.text_input("Ask a question about infection, death rate or vaccination")
if q:
    ql = q.lower()
    if "infection" in ql:
        top = latest.sort_values("infection_rate_pct", ascending=False).iloc[0]
        st.success(f"{top['location']} has the highest infection rate at {top['infection_rate_pct']:.2f}%.")
    elif "death" in ql or "fatality" in ql:
        top = latest.sort_values("case_fatality_rate_pct", ascending=False).iloc[0]
        st.warning(f"{top['location']} has the highest case fatality rate at {top['case_fatality_rate_pct']:.2f}%.")
    elif "vaccination" in ql:
        top = latest.sort_values("vaccination_coverage_pct", ascending=False).iloc[0]
        st.success(f"{top['location']} has the highest vaccination coverage at {top['vaccination_coverage_pct']:.1f}%.")
    else:
        st.info("Try asking about infection rate, death rate or vaccination coverage.")
