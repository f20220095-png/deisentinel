import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# --- 1. Page Configuration & Cyber-Clinical Theme ---
st.set_page_config(
    page_title="DEI Sentinel",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for "Cyber-Clinical Dark Mode"
st.markdown("""
<style>
    /* Main Background & Font */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
        font-family: 'Roboto Mono', monospace; /* Tech feel */
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #FAFAFA !important;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    /* Metric Cards - Transparent with Glowing Borders */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05); /* Transparent */
        border: 1px solid rgba(0, 229, 255, 0.3); /* Cyber Cyan Glow */
        padding: 15px;
        border-radius: 4px;
        box-shadow: 0 0 10px rgba(0, 229, 255, 0.1);
        text-align: center;
    }
    div[data-testid="metric-container"] label {
        color: #00E5FF !important; /* Cyber Cyan Label */
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #FAFAFA !important;
        font-size: 1.8rem;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    
    /* Custom Badge */
    .badge {
        background-color: #00CC96; /* Emerald Green */
        color: #0E1117;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: bold;
        vertical-align: middle;
        margin-left: 10px;
    }

    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. Data Simulation ( The "Twin" Engine ) ---
@st.cache_data
def generate_radar_data():
    """Generates hardcoded radar chart data for disease archetypes."""
    # Normalized scores (0.0 to 1.0)
    data = {
        "Heart Failure": {"Waste": 0.9, "Latency": 0.4, "Fragmentation": 0.5},
        "Diabetes":      {"Waste": 0.3, "Latency": 0.9, "Fragmentation": 0.3},
        "Lung Cancer":   {"Waste": 0.6, "Latency": 0.5, "Fragmentation": 0.9}
    }
    return data

@st.cache_data
def generate_patient_timeline():
    """Generates hardcoded timeline data for Patient 2008116375."""
    data = [
        {"Date": "2008-01-15", "Event": "GP Visit - General Fatigue", "Cost": 120, "Shadow": True, "Type": "GP"},
        {"Date": "2008-02-20", "Event": "GP Visit - Vision Blur", "Cost": 120, "Shadow": True, "Type": "GP"},
        {"Date": "2008-03-10", "Event": "Optometrist Referral", "Cost": 250, "Shadow": True, "Type": "Specialist"},
        {"Date": "2008-04-05", "Event": "ER Visit - Fainting", "Cost": 1200, "Shadow": True, "Type": "ER"},
        {"Date": "2008-05-12", "Event": "Endocrinologist Consult", "Cost": 400, "Shadow": True, "Type": "Specialist"},
        {"Date": "2008-06-30", "Event": "Inpatient Admission - DIABETES DIAGNOSIS", "Cost": 15000, "Shadow": False, "Type": "Inpatient"}
    ]
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Initialize Data
radar_data = generate_radar_data()
timeline_df = generate_patient_timeline()

# --- 3. Layout Structure ---

# Header Section
st.markdown("<h1>DEI Sentinel <span class='badge'>LIVE SYNPUF FEED 2008-2010</span></h1>", unsafe_allow_html=True)
st.markdown("### Diagnostic Efficiency Intelligence // <span style='color:#00E5FF'>System Status: ONLINE</span>", unsafe_allow_html=True)
st.markdown("---")

# Part 2: Top Row (The Radar)
col_radar_left, col_radar_right = st.columns([1, 2])

with col_radar_left:
    st.markdown("#### Strategic View")
    selected_disease = st.selectbox(
        "Select Disease Model",
        options=["Heart Failure", "Diabetes", "Lung Cancer"],
        index=1 # Default to Diabetes (The "Creep")
    )
    
    # Calculate projected waste based on selection (Mock logic)
    waste_map = {
        "Heart Failure": 8450,
        "Diabetes": 4736,
        "Lung Cancer": 12300 
    }
    projected_waste = waste_map[selected_disease]
    
    st.metric(
        label="Projected Waste / Patient",
        value=f"${projected_waste:,.0f}",
        delta="Detected Pattern",
        delta_color="off"
    )
    
    st.info(f"**Archetype Detected:** {selected_disease}\n\nHigh latency observed in initial diagnostic phase.")

with col_radar_right:
    # Radar Chart
    scores = radar_data[selected_disease]
    categories = ['Waste (Cost)', 'Latency (Time)', 'Fragmentation (Complexity)']
    values = [scores['Waste'], scores['Latency'], scores['Fragmentation']]
    
    # Close the loop
    values += values[:1]
    categories += categories[:1]
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(0, 229, 255, 0.2)', # Cyan fill
        line=dict(color='#00E5FF', width=3), # Neon Cyan Line
        name=selected_disease
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                color='#FAFAFA',
                gridcolor='#333'
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font=dict(color='#FAFAFA'),
        height=350,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("---")

# Part 3: Bottom Row (The Shadow Hunter)
st.markdown("#### Patient Journey Forensics: ID #2008116375 <span style='color:#FFC107'>(The Diabetic Creep)</span>", unsafe_allow_html=True)

# Calculate total shadow cost
shadow_cost = timeline_df[timeline_df['Shadow'] == True]['Cost'].sum()

# Gantt Chart (Timeline) logic
# We use a timeline but trick it to show single points or short durations. 
# Better: Scatter plot on a timeline axis or a Gantt where end = start + small delta.
# Let's use Gantt (timeline) and set end date = start date + 2 days for visibility.
timeline_viz_df = timeline_df.copy()
timeline_viz_df['End'] = timeline_viz_df['Date'] + pd.Timedelta(days=3) 

# Color mapping logic
color_map = {True: '#FF4B4B', False: '#00CC96'} # Red for Shadow, Green for Diagnosis
timeline_viz_df['Color'] = timeline_viz_df['Shadow'].map(color_map)

fig_timeline = px.timeline(
    timeline_viz_df, 
    x_start="Date", 
    x_end="End", 
    y="Event",
    color="Shadow",
    color_discrete_map={True: '#FF4B4B', False: '#00CC96'},
    hover_data=["Cost", "Type"],
    height=400
)

# Customizing the Timeline
fig_timeline.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title="Timeline (2008)",
        showgrid=True,
        gridcolor='#333',
        color='#FAFAFA'
    ),
    yaxis=dict(
        title="",
        color='#FAFAFA',
        categoryorder="total ascending" # Keeps order somewhat logical
    ),
    showlegend=False, # We use the color contextually
    margin=dict(l=20, r=20, t=30, b=20)
)

# Add Annotation for Latency
start_date = timeline_viz_df['Date'].min()
end_date = timeline_viz_df['Date'].max()
latency_days = (end_date - start_date).days

fig_timeline.add_shape(
    type="line",
    x0=start_date, y0=-0.5, x1=end_date, y1=-0.5,
    line=dict(color="#FFC107", width=2, dash="dot"),
    xref="x", yref="paper" # Position at bottom
)

fig_timeline.add_annotation(
    x=start_date + (end_date - start_date)/2,
    y=-0.1,
    text=f"Diagnostic Latency: {latency_days} Days",
    showarrow=False,
    font=dict(color="#FFC107", size=14, family="Roboto Mono"),
    xref="x", yref="paper"
)

st.plotly_chart(fig_timeline, use_container_width=True)

# Footer Metric
st.markdown(f"""
<div style="border: 1px solid #FF4B4B; padding: 10px; border-radius: 5px; text-align: center; background: rgba(255, 75, 75, 0.1);">
    <h3 style="color: #FF4B4B; margin: 0;">TOTAL SHADOW COST: ${shadow_cost:,.2f}</h3>
    <small style="color: #FAFAFA;">Accumulated waste prior to diagnosis</small>
</div>
""", unsafe_allow_html=True)
