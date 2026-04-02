import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Smart Flight Intelligence", layout="wide")

# =========================
# CUSTOM UI (🔥 MODERN LOOK)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #020617;
}

.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 15px;
}

h1, h2, h3, h4 {
    color: #f8fafc;
}

.stButton>button {
    background: linear-gradient(90deg, #22c55e, #4ade80);
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("./data/flights_cleaned_m1.csv")

df = load_data()

# =========================
# TRAIN MODEL
# =========================
@st.cache_data
def train_model(df):
    model_df = df[['hour', 'distance', 'arr_delay']].dropna()
    X = model_df[['hour', 'distance']]
    y = model_df['arr_delay']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

model = train_model(df)

# =========================
# TITLE
# =========================
st.markdown("""
<h1>✈️ Smart Flight Intelligence</h1>
<p style='color:gray;'>Plan smarter travel with AI-powered insights</p>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.header("🔍 Filters")

selected_airline = st.sidebar.selectbox(
    "Airline", ["All"] + sorted(df['name'].dropna().unique())
)

selected_month = st.sidebar.selectbox(
    "Month", ["All"] + sorted(df['month_name'].dropna().unique())
)

st.sidebar.header("🎯 Preference")

priority = st.sidebar.selectbox(
    "Goal",
    ["Minimum Delay", "Low Cancellation Risk", "Balanced"]
)

filtered_df = df.copy()

if selected_airline != "All":
    filtered_df = filtered_df[filtered_df['name'] == selected_airline]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df['month_name'] == selected_month]

# =========================
# KPI CARDS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<div class='card'><h4>Total Flights</h4><h2>{len(filtered_df)}</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='card'><h4>Avg Delay</h4><h2>{round(filtered_df['arr_delay'].mean(),2)}</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='card'><h4>Cancelled</h4><h2>{int(filtered_df['is_cancelled'].sum())}</h2></div>", unsafe_allow_html=True)
col4.markdown(f"<div class='card'><h4>Delayed</h4><h2>{int(filtered_df['is_delayed'].sum())}</h2></div>", unsafe_allow_html=True)

# =========================
# ROUTE FINDER
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧭 Best Route Finder")

col1, col2 = st.columns(2)
origins = sorted(df['origin'].dropna().unique())
destinations = sorted(df['dest'].dropna().unique())

with col1:
    selected_origin = st.selectbox("Origin", origins)

with col2:
    selected_dest = st.selectbox("Destination", destinations)

route_df = df[(df['origin'] == selected_origin) & (df['dest'] == selected_dest)]

if not route_df.empty:
    airline_delay = route_df.groupby('name')['arr_delay'].mean()
    best_airline = airline_delay.idxmin()
    avg_delay = airline_delay.min()

    st.success(f"✈️ {best_airline} | ⏱️ {round(avg_delay,2)} min delay")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# BEST DAY
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📅 Best Day to Travel")

day_delay = filtered_df.groupby('day_of_week')['arr_delay'].mean().sort_values()
best_day = day_delay.idxmin()

fig = px.bar(x=day_delay.values, y=day_delay.index, orientation='h')
st.plotly_chart(fig, use_container_width=True)

st.success(f"Best Day: {best_day}")
st.markdown("</div>", unsafe_allow_html=True)



# =========================
# ML PREDICTION
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🤖 Delay Prediction")

h = st.slider("Hour", 0, 23, 10)
d = st.slider("Distance", 100, 3000, 500)

if st.button("Predict"):
    pred = model.predict([[h, d]])[0]
    st.success(f"Predicted Delay: {round(pred,2)} min")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SMART ASSISTANT
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧠 Smart Travel Assistant")

analysis_df = route_df if not route_df.empty else filtered_df

delay_by_airline = analysis_df.groupby('name')['arr_delay'].mean()
cancel_rate = analysis_df.groupby('name')['is_cancelled'].mean()

best_airline = delay_by_airline.idxmin()
best_hour = analysis_df.groupby('hour')['arr_delay'].mean().idxmin()

st.success(f"""
🚀 Airline: {best_airline}  
🕒 Time: {best_hour}:00 hrs  
""")

st.markdown("</div>", unsafe_allow_html=True)