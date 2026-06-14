import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="COVID Intelligence Platform 2026", page_icon="⚕️", layout="wide")

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "cleaned" / "covid_intelligence_tableau_ready.csv")
latest = pd.read_csv(ROOT / "data" / "cleaned" / "country_intelligence_summary.csv")
trend = pd.read_csv(ROOT / "data" / "cleaned" / "global_trend.csv")

st.markdown("""
<style>
.stApp { background-color: #0B1020; color: white; }
[data-testid="stMetricValue"] { color: #38BDF8; }
</style>
""", unsafe_allow_html=True)

st.title("⚕️ COVID Intelligence Platform 2026")
st.caption("Modern SQL + Tableau style portfolio app with executive dashboards, vaccination intelligence and AI-style insights.")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Countries", latest["location"].nunique())
c2.metric("Total Cases", f"{latest['total_cases'].sum()/1_000_000:.1f}M")
c3.metric("Total Deaths", f"{latest['total_deaths'].sum()/1000:.0f}K")
c4.metric("Avg Vaccination", f"{latest['vaccination_coverage_pct'].mean():.1f}%")

tab1, tab2, tab3, tab4 = st.tabs(["Executive", "Global Monitoring", "Vaccination Intelligence", "AI Insights"])

with tab1:
    st.subheader("Executive Command Center")
    a,b = st.columns([1.2,1])
    with a:
        st.line_chart(trend.set_index("date")["new_cases"])
    with b:
        st.bar_chart(latest.sort_values("infection_rate_pct", ascending=False).set_index("location")["infection_rate_pct"].head(10))
    st.dataframe(latest.sort_values("risk_score", ascending=False), use_container_width=True)

with tab2:
    st.subheader("Global Monitoring")
    countries = st.multiselect("Select countries", sorted(df["location"].unique()), default=["Australia","United States","India","Brazil"])
    filtered = df[df["location"].isin(countries)]
    st.line_chart(filtered.pivot(index="date", columns="location", values="infection_rate_pct"))
    st.bar_chart(latest.groupby("continent")["case_fatality_rate_pct"].mean())

with tab3:
    st.subheader("Vaccination Intelligence")
    countries = st.multiselect("Vaccination countries", sorted(df["location"].unique()), default=["Australia","United States","India","United Kingdom"])
    filtered = df[df["location"].isin(countries)]
    st.line_chart(filtered.pivot(index="date", columns="location", values="vaccination_coverage_pct"))
    st.bar_chart(latest.sort_values("vaccination_coverage_pct", ascending=False).set_index("location")["vaccination_coverage_pct"].head(10))

with tab4:
    st.subheader("AI-Style Insight Center")
    q = st.text_input("Ask a question, e.g. Which country has the highest infection rate?")
    if q:
        ql = q.lower()
        if "infection" in ql:
            top = latest.sort_values("infection_rate_pct", ascending=False).iloc[0]
            st.success(f"{top['location']} has the highest infection rate at {top['infection_rate_pct']:.2f}% of population. This is a better comparison than raw total cases.")
        elif "death" in ql or "fatality" in ql:
            top = latest.sort_values("case_fatality_rate_pct", ascending=False).iloc[0]
            st.warning(f"{top['location']} has the highest case fatality rate at {top['case_fatality_rate_pct']:.2f}%. Consider healthcare capacity and reporting context.")
        elif "vaccination" in ql:
            top = latest.sort_values("vaccination_coverage_pct", ascending=False).iloc[0]
            st.success(f"{top['location']} has the highest vaccination coverage at {top['vaccination_coverage_pct']:.1f}%.")
        else:
            st.info("This demo can answer questions about infection rate, death rate and vaccination coverage.")
