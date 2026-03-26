import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Cash Collection Dashboard", layout="wide")

st.title("Billing & Cash Collection Dashboard")
st.markdown("**MTD & YTD Analys**（Mar 2026）Currency: USD")

# ====================== KPI 卡片 ======================
st.subheader("📊 KPI")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="MTD Billing",
        value="0.00",
        delta=" vs Target"
    )

with col2:
    st.metric(
        label="MTD Collection",
        value="57,923.50",
        delta=""
    )

with col3:
    st.metric(
        label="YTD Billing",
        value="121,789.21",
        delta=" vs Target"
    )

with col4:
    st.metric(
        label="YTD Collection",
        value="57,923.50",
        delta=""
    )

# ====================== MTD & YTD 表格 ======================
st.subheader("📅 MTD & YTD Breakdown")

c1, c2 = st.columns(2)

# MTD 周表
with c1:
    st.markdown("**📅 Month-to-Date (MTD)** <span style='background:#667eea;color:white;padding:2px 10px;border-radius:20px;font-size:0.85em;'>March 2026</span>", unsafe_allow_html=True)
    
    mtd_data = {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "MTD Total"],
        "Target": ["106,250.00","106,250.00", "106,250.00", "106,250.00",  "425,000.00"],
        "Actual": ["0.00", "0.00", "0.00", "0.00","0.00",],
        "Achievement": ["0.0%", "0.0%", "0.0%", "0.0%", "0.0%"],
        "Trend": [" ", " ", " ", " ", " "]
    }
    mtd_df = pd.DataFrame(mtd_data)
    st.dataframe(mtd_df, use_container_width=True, hide_index=True)

# YTD 月表
with c2:
    st.markdown("**📊 Year-to-Date (YTD)** <span style='background:#667eea;color:white;padding:2px 10px;border-radius:20px;font-size:0.85em;'>Jan - Mar 2026</span>", unsafe_allow_html=True)
    
    ytd_data = {
        "Month": ["January", "February", "March (MTD)", "YTD Total"],
        "Target": ["425,000.00", "425,000.00", "425,000.00", "1,275,000.00"],
        "Actual": ["38,111.52", "83,677.67", "0.00", "121,789.21"],
        "Achievement": ["8.97%", "19.67%", "0.0%", "9.55%"],
        "Trend": [" ", " ", " ", " "]
    }
    ytd_df = pd.DataFrame(ytd_data)
    st.dataframe(ytd_df, use_container_width=True, hide_index=True)

# ====================== Performance Summary ======================
st.subheader("📈 Performance Summary")
st.markdown("Comprehensive analysis based on current MTD and YTD data")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric("Best Performing Month", "February", "  Achievement")
with s2:
    st.metric("Average Monthly Collection", " ", "YTD Average")
with s3:
    st.metric("Remaining Q1 Target", " ", "To reach Q1 Goal")
with s4:
    st.metric("Projected YTD", " ", "Based on current trend")

# ====================== 模拟实时更新按钮 ======================
st.markdown("---")
if st.button(" ", type="primary", use_container_width=True):
    st.success(" ")
    st.rerun()

st.caption(" ")
