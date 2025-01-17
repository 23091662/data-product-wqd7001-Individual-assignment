# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Poverty Risk Monitoring Dashboard", layout="wide")

# Sample data
risk_trend_data = pd.DataFrame([
    {"month": "Jan", "highRisk": 120, "mediumRisk": 250, "lowRisk": 430},
    {"month": "Feb", "highRisk": 150, "mediumRisk": 230, "lowRisk": 420},
    {"month": "Mar", "highRisk": 140, "mediumRisk": 240, "lowRisk": 440},
    {"month": "Apr", "highRisk": 160, "mediumRisk": 220, "lowRisk": 410}
])

# Title
st.title("Poverty Risk Monitoring Dashboard")

# Alert section
st.error("🚨 High Risk Alert: 160 households require immediate intervention")

# Main stats in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Monitored",
        value="1,250",
        delta="Households",
        delta_color="off"
    )

with col2:
    st.metric(
        label="High Risk Cases",
        value="160",
        delta="Requiring Action",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Monthly Change",
        value="+12.8%",
        delta="In High Risk Cases",
        delta_color="inverse"
    )

# Risk Trend Chart
st.subheader("Risk Level Trends")

# Create line chart using plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=risk_trend_data["month"],
    y=risk_trend_data["highRisk"],
    name="High Risk",
    line=dict(color="#ef4444")
))

fig.add_trace(go.Scatter(
    x=risk_trend_data["month"],
    y=risk_trend_data["mediumRisk"],
    name="Medium Risk",
    line=dict(color="#f97316")
))

fig.add_trace(go.Scatter(
    x=risk_trend_data["month"],
    y=risk_trend_data["lowRisk"],
    name="Low Risk",
    line=dict(color="#22c55e")
))

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Number of Households",
    plot_bgcolor="white",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# Additional Analysis Section
st.subheader("Detailed Analysis")
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Average High Risk Cases",
        value="142.5",
        delta="13.3%",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Risk Trend",
        value="Increasing",
        delta="Alert Status",
        delta_color="inverse"
    )

# Add filters in sidebar
st.sidebar.title("Filters")
selected_months = st.sidebar.multiselect(
    "Select Months",
    options=risk_trend_data["month"].unique(),
    default=risk_trend_data["month"].unique()
)

risk_level = st.sidebar.selectbox(
    "Risk Level",
    ["All", "High Risk", "Medium Risk", "Low Risk"]
)
