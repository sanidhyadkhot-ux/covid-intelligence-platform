import streamlit as st
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
latest = pd.read_csv(ROOT / "data" / "cleaned" / "country_intelligence_summary.csv")
trend = pd.read_csv(ROOT / "data" / "cleaned" / "global_trend.csv")
st.title("Executive Command Center")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Countries", latest["location"].nunique())
c2.metric("Total Cases", f"{latest['total_cases'].sum()/1_000_000:.1f}M")
c3.metric("Total Deaths", f"{latest['total_deaths'].sum()/1000:.0f}K")
c4.metric("Avg Vaccination", f"{latest['vaccination_coverage_pct'].mean():.1f}%")
st.line_chart(trend.set_index("date")["new_cases"])
st.bar_chart(latest.sort_values("infection_rate_pct", ascending=False).set_index("location")["infection_rate_pct"].head(10))
