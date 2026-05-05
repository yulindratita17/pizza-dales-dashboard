import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("pizza_sales_done.csv")

st.title("🍕 Pizza Sales Dashboard")

# =========================
# 📊 KPI Section
# =========================
total_revenue = df['total_price'].sum()
total_orders = df['order_id'].nunique()
total_quantity = df['quantity'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Quantity Sold", total_quantity)

# =========================
# 📅 Sales by Month
# =========================
st.subheader("📅 Sales by Month")

monthly_sales = df.groupby('month_name')['total_price'].sum()

st.bar_chart(monthly_sales)

# =========================
# 🍕 Top 10 Pizza
# =========================
st.subheader("🍕 Top 10 Best Selling Pizza")

top_pizza = df.groupby('pizza_name')['quantity'].sum().sort_values(ascending=False).head(10)

st.bar_chart(top_pizza)

# =========================
# 📦 Category Analysis
# =========================
st.subheader("📦 Sales by Category")

category_sales = df.groupby('pizza_category')['total_price'].sum()

st.bar_chart(category_sales)

# =========================
# 📏 Size Analysis
# =========================
st.subheader("📏 Sales by Size")

size_sales = df.groupby('pizza_size')['total_price'].sum()

st.bar_chart(size_sales)

# =========================
# 📅 Day Analysis
# =========================
st.subheader("📅 Orders by Day")

day_orders = df['day_name'].value_counts()

st.bar_chart(day_orders)

# =============================================

category = st.selectbox("Select Category", df['pizza_category'].unique())
filtered_df = df[df['pizza_category'] == category]

st.write(filtered_df.head())

# =============================================

df['new_order_date'] = pd.to_datetime(df['new_order_date'])