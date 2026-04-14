import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Logistics Dashboard", layout="wide")
st.title("🚚 Logistics Efficiency Dashboard")

# Load Excel file
try:
    df = pd.read_csv("C:\\Users\\sippy\\OneDrive\\Desktop\\Project 1\\Nassau Candy Distributor.csv")
    st.success("✅ Data Loaded Successfully")
except Exception as e:
    st.error(f"❌ Error loading file: {e}")
    st.stop()

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y', errors='coerce')

# Feature Engineering
df['Delivery Time'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Delay Status'] = df['Delivery Time'].apply(lambda x: 'Delayed' if x > 5 else 'On-Time')

# Create Route (State → Region)
df['Route'] = df['State/Province'] + " → " + df['Region']

# Sidebar Filters
st.sidebar.header("🔎 Filters")

region = st.sidebar.multiselect("Region", df['Region'].unique())
state = st.sidebar.multiselect("State", df['State/Province'].unique())
ship_mode = st.sidebar.multiselect("Ship Mode", df['Ship Mode'].unique())

# Apply Filters
filtered_df = df.copy()

if region:
    filtered_df = filtered_df[filtered_df['Region'].isin(region)]

if state:
    filtered_df = filtered_df[filtered_df['State/Province'].isin(state)]

if ship_mode:
    filtered_df = filtered_df[filtered_df['Ship Mode'].isin(ship_mode)]

# KPIs
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", len(filtered_df))
col2.metric("Avg Delivery Time", round(filtered_df['Delivery Time'].mean(), 2))
col3.metric("Delayed Orders", (filtered_df['Delay Status'] == 'Delayed').sum())

# Route Efficiency
st.subheader("📍 Route Efficiency")

route_perf = filtered_df.groupby('Route')['Delivery Time'].mean().sort_values()

st.write("✅ Fastest Routes")
st.bar_chart(route_perf.head(5))

st.write("❌ Slowest Routes")
st.bar_chart(route_perf.tail(5))

# Shipping Mode Performance
st.subheader("🚚 Shipping Mode Performance")

ship_perf = filtered_df.groupby('Ship Mode')['Delivery Time'].mean()
st.bar_chart(ship_perf)

# Delay Analysis
st.subheader("⏱️ Delay Analysis")

delay_counts = filtered_df['Delay Status'].value_counts()
st.bar_chart(delay_counts)

# Trend Over Time
st.subheader("📅 Delivery Trend")

filtered_df['Month'] = filtered_df['Order Date'].dt.to_period('M').astype(str)
trend = filtered_df.groupby('Month')['Delivery Time'].mean()

st.line_chart(trend)

# Data View
st.subheader("📂 Data Preview")

if st.checkbox("Show Data"):
    st.dataframe(filtered_df)