import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

st.set_page_config(page_title="Cash Collection 仪表板", layout="wide")
st.title("💰 Cash Collection 现金回收追踪仪表板")
st.markdown("**实时更新 · MTD · YTD**（2026 年 3 月示例）")

# ==================== 初始化数据（可后期换成真实数据） ====================
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame({
        "date": ["2026-03-01","2026-03-03","2026-03-05","2026-03-08","2026-03-10",
                 "2026-03-12","2026-03-15","2026-03-18","2026-03-20","2026-03-21",
                 "2025-12-15"],
        "amount": [8500,6200,4500,12000,3300,7800,9500,4100,6700,11200,5000],
        "category": ["客户A","客户B","客户C","客户A","客户D","客户B","客户E","客户A","客户C","客户B","客户F"]
    })

df = st.session_state.df.copy()
df["date"] = pd.to_datetime(df["date"])

# ==================== 计算 KPI ====================
now = datetime.now()
this_year = now.year
this_month = now.month

total = int(df["amount"].sum())
mtd = int(df[(df["date"].dt.year == this_year) & (df["date"].dt.month == this_month)]["amount"].sum())
ytd = int(df[df["date"].dt.year == this_year]["amount"].sum())
rate = round((total / (total * 1.1)) * 100) if total > 0 else 0

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("总回收金额", f"¥{total:,}")
with col2: st.metric("MTD（本月至今）", f"¥{mtd:,}")
with col3: st.metric("YTD（今年至今）", f"¥{ytd:,}")
with col4: st.metric("回收率", f"{rate}%")

# ==================== 图表 ====================
st.subheader("📈 每日回收趋势")
daily = df.groupby(df["date"].dt.date)["amount"].sum().reset_index()
daily.columns = ["date", "amount"]
fig_line = px.line(daily, x="date", y="amount", markers=True, title="每日回收趋势")
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("🥧 回收分类分布")
cat = df.groupby("category")["amount"].sum().reset_index()
fig_pie = px.pie(cat, names="category", values="amount")
st.plotly_chart(fig_pie, use_container_width=True)

# ==================== 表格 ====================
st.subheader("最近 10 笔记录")
st.dataframe(df.sort_values("date", ascending=False).head(10), use_container_width=True)

# ==================== 模拟实时更新 ====================
st.subheader("🔄 模拟实时更新（点击按钮新增记录）")
if st.button("➕ 新增一笔回收记录（演示实时）", type="primary"):
    today = datetime.now().strftime("%Y-%m-%d")
    new_amount = random.randint(3000, 12000)
    new_cat = random.choice(["客户A","客户B","客户C","客户D","新客户"])
    new_row = pd.DataFrame({"date": [today], "amount": [new_amount], "category": [new_cat]})
    new_row["date"] = pd.to_datetime(new_row["date"])
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    st.success(f"✅ 新增成功！ ¥{new_amount}（{new_cat}）")
    st.rerun()
