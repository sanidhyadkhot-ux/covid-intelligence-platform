import streamlit as st
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data" / "cleaned" / "covid_intelligence_tableau_ready.csv")
latest = pd.read_csv(ROOT / "data" / "cleaned" / "country_intelligence_summary.csv")
st.title("Vaccination Intelligence")
countries = st.multiselect("Select countries", sorted(df["location"].unique()), default=["Australia","United States","India","United Kingdom"])
filtered = df[df["location"].isin(countries)]
st.line_chart(filtered.pivot(index="date", columns="location", values="vaccination_coverage_pct"))
st.bar_chart(latest.sort_values("vaccination_coverage_pct", ascending=False).set_index("location")["vaccination_coverage_pct"].head(10))
