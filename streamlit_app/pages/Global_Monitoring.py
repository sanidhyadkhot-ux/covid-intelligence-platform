import streamlit as st
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data" / "cleaned" / "covid_intelligence_tableau_ready.csv")
st.title("Global Monitoring")
countries = st.multiselect("Select countries", sorted(df["location"].unique()), default=["Australia","United States","India","Brazil"])
filtered = df[df["location"].isin(countries)]
st.line_chart(filtered.pivot(index="date", columns="location", values="infection_rate_pct"))
