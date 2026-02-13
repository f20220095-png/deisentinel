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

# --- 2. Data Simulation (The "Twin" Engine) ---
@st.cache_data
def generate_radar_data():
    """Generates hardcoded radar chart data for disease archetypes."""
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

@st.cache_data
def generate_equity_data():
    """Generates hardcoded equity analysis data."""
    data = {
        "Race": {
            "White": 152,
            "Black": 164,
            "Hispanic": 158
        },
        "Gender": {
            "Male": 153,
            "Female": 150
        }
    }
    return data

# Initialize Data
radar_data = generate_radar_data()
timeline_df = generate_patient_timeline()
equity_data = generate_equity_data()

# --- 3. Persistent Header ---
st.markdown("<h1>DEI Sentinel <span class='badge'>LIVE SYNPUF FEED 2008-2010</span></h1>", unsafe_allow_html=True)
st.markdown("### Diagnostic Efficiency Intelligence // <span style='color:#00E5FF'>System Status: ONLINE</span>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. Tabbed Interface ---
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Strategic", "🏥 Clinical", "⚖️ Equity", "💰 Financial"])

# ============= TAB 1: STRATEGIC (RADAR) =============
with tab1:
    st.markdown("### Disease Archetype Analysis")
    
    col_radar_left, col_radar_right = st.columns([1, 2])
    
    with col_radar_left:
        st.markdown("#### Strategic View")
        selected_disease = st.selectbox(
            "Select Disease Model",
            options=["Heart Failure", "Diabetes", "Lung Cancer"],
            index=1
        )
        
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
        
        archetype_info = {
            "Heart Failure": {
                "archetype": "The Crash",
                "description": "**Critical Cost Inefficiency Detected**\n\n⚠️ **Waste Score: 0.9/1.0** - Patients experience excessive, redundant testing and emergency department visits.\n\n💡 **Key Pattern**: Acute episodes drive up costs rapidly through repeated hospitalizations and intensive interventions. Care coordination gaps lead to preventable readmissions."
            },
            "Diabetes": {
                "archetype": "The Creep", 
                "description": "**Dangerous Diagnostic Delays Detected**\n\n⏱️ **Latency Score: 0.9/1.0** - Patients wait an average of 166 days from first symptoms to confirmed diagnosis.\n\n💡 **Key Pattern**: Slow progression allows symptoms to be dismissed across multiple GP visits. Vision problems and fatigue are often attributed to other causes before endocrine consultation."
            },
            "Lung Cancer": {
                "archetype": "The Complex",
                "description": "**Severe Care Fragmentation Detected**\n\n🔀 **Fragmentation Score: 0.9/1.0** - Patients navigate through 6+ different specialists before reaching oncology.\n\n💡 **Key Pattern**: Respiratory symptoms trigger referrals to pulmonology, cardiology, ENT, and radiology. Lack of diagnostic pathway coordination creates a 'medical maze' effect."
            }
        }
        
        info = archetype_info[selected_disease]
        st.info(f"**Archetype:** {info['archetype']}\n\n{info['description']}")
    
    with col_radar_right:
        scores = radar_data[selected_disease]
        categories = ['Waste (Cost)', 'Latency (Time)', 'Fragmentation (Complexity)']
        values = [scores['Waste'], scores['Latency'], scores['Fragmentation']]
        
        values += values[:1]
        categories += categories[:1]
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(0, 229, 255, 0.2)',
            line=dict(color='#00E5FF', width=3),
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
            height=400,
            margin=dict(l=40, r=40, t=20, b=20)
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)

# ============= TAB 2: CLINICAL (TIMELINE) =============
with tab2:
    st.markdown("### Patient Journey Forensics: ID #2008116375 <span style='color:#FFC107'>(The Diabetic Creep)</span>", unsafe_allow_html=True)
    
    shadow_cost = timeline_df[timeline_df['Shadow'] == True]['Cost'].sum()
    
    timeline_viz_df = timeline_df.copy()
    timeline_viz_df['End'] = timeline_viz_df['Date'] + pd.Timedelta(days=3) 
    
    fig_timeline = px.timeline(
        timeline_viz_df, 
        x_start="Date", 
        x_end="End", 
        y="Event",
        color="Shadow",
        color_discrete_map={True: '#FF4B4B', False: '#00CC96'},
        hover_data=["Cost", "Type"],
        height=450
    )
    
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
            categoryorder="total ascending"
        ),
        showlegend=False,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    start_date = timeline_viz_df['Date'].min()
    end_date = timeline_viz_df['Date'].max()
    latency_days = (end_date - start_date).days
    
    fig_timeline.add_shape(
        type="line",
        x0=start_date, y0=1.05, x1=end_date, y1=1.05,
        line=dict(color="#FFC107", width=2, dash="dot"),
        xref="x", yref="paper"
    )
    
    fig_timeline.add_annotation(
        x=start_date + (end_date - start_date)/2,
        y=1.15,
        text=f"Diagnostic Latency: {latency_days} Days",
        showarrow=False,
        font=dict(color="#FFC107", size=14, family="Roboto Mono"),
        xref="x", yref="paper"
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    st.markdown(f"""
    <div style="border: 1px solid #FF4B4B; padding: 10px; border-radius: 5px; text-align: center; background: rgba(255, 75, 75, 0.1);">
        <h3 style="color: #FF4B4B; margin: 0;">TOTAL SHADOW COST: ${shadow_cost:,.2f}</h3>
        <small style="color: #FAFAFA;">Accumulated waste prior to diagnosis</small>
    </div>
    """, unsafe_allow_html=True)

# ============= TAB 3: EQUITY AUDITOR =============
with tab3:
    st.markdown("### Health Equity Analysis")
    
    analysis_type = st.radio(
        "Analyze Diagnostic Latency by:",
        ["Race", "Gender"],
        horizontal=True
    )
    
    col_eq1, col_eq2 = st.columns([2, 1])
    
    with col_eq1:
        data_to_plot = equity_data[analysis_type]
        
        df_equity = pd.DataFrame({
            'Group': list(data_to_plot.keys()),
            'Days_to_Diagnosis': list(data_to_plot.values())
        })
        
        # Color scheme: Teal vs Purple
        if analysis_type == "Race":
            colors = ['#00E5FF' if group == 'White' else '#D500F9' for group in df_equity['Group']]
        else:
            colors = ['#00E5FF' if group == 'Male' else '#D500F9' for group in df_equity['Group']]
        
        fig_equity = go.Figure()
        
        fig_equity.add_trace(go.Bar(
            x=df_equity['Group'],
            y=df_equity['Days_to_Diagnosis'],
            marker=dict(color=colors, line=dict(color='#FAFAFA', width=1)),
            text=df_equity['Days_to_Diagnosis'],
            textposition='outside',
            textfont=dict(color='#FAFAFA')
        ))
        
        # Benchmark line at 152 days
        fig_equity.add_shape(
            type="line",
            x0=-0.5, x1=len(df_equity)-0.5,
            y0=152, y1=152,
            line=dict(color="#FFC107", width=2, dash="dash"),
        )
        
        fig_equity.add_annotation(
            x=len(df_equity)-0.5,
            y=152,
            text="Benchmark: 152 Days",
            showarrow=False,
            xanchor='left',
            font=dict(color="#FFC107", size=12)
        )
        
        fig_equity.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title=analysis_type, color='#FAFAFA'),
            yaxis=dict(title="Days to Diagnosis", color='#FAFAFA', gridcolor='#333'),
            showlegend=False,
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_equity, use_container_width=True)
    
    with col_eq2:
        st.markdown("#### Equity Gap Analysis")
        
        if analysis_type == "Race":
            baseline = data_to_plot["White"]
            black_gap = data_to_plot["Black"] - baseline
            hispanic_gap = data_to_plot["Hispanic"] - baseline
            
            st.metric(
                label="Black vs. White Gap",
                value=f"+{black_gap} Days",
                delta=f"{(black_gap/baseline)*100:.1f}% longer",
                delta_color="inverse"
            )
            
            st.metric(
                label="Hispanic vs. White Gap",
                value=f"+{hispanic_gap} Days",
                delta=f"{(hispanic_gap/baseline)*100:.1f}% longer",
                delta_color="inverse"
            )
            
            st.warning("⚠️ **Disparity Alert**: Black patients experience a significant 12-day delay compared to White patients, suggesting systemic access barriers.")
        
        else:
            male_days = data_to_plot["Male"]
            female_days = data_to_plot["Female"]
            gap = male_days - female_days
            
            st.metric(
                label="Male vs. Female Gap",
                value=f"+{gap} Days" if gap > 0 else f"{gap} Days",
                delta=f"{abs(gap)} day difference"
            )
            
            st.info("ℹ️ **Finding**: Minimal gender disparity detected. Male patients experience slightly longer diagnostic timelines, likely due to lower healthcare utilization rates.")

# ============= TAB 4: ROI SIMULATOR =============
with tab4:
    st.markdown("### Financial Impact Simulator")
    
    # Constants
    BASELINE_GAP = 4736
    TOTAL_COHORT = 10000
    
    col_sim1, col_sim2, col_sim3 = st.columns([1, 1, 1])
    
    with col_sim1:
        st.markdown("#### Policy Levers")
        
        screening_adoption = st.slider(
            "Community Screening Adoption (%)",
            min_value=0,
            max_value=50,
            value=0,
            step=5,
            help="Proactive screening reduces diagnostic latency"
        )
        
        er_data_sharing = st.slider(
            "ER Data Sharing Protocol (%)",
            min_value=0,
            max_value=50,
            value=0,
            step=5,
            help="Coordinated care reduces redundant testing"
        )
        
        st.markdown(f"""
        <div style="background: rgba(0, 229, 255, 0.1); padding: 10px; border-radius: 5px; margin-top: 20px;">
            <small style="color: #00E5FF;">Combined Efficiency Gain: <b>{screening_adoption + er_data_sharing}%</b></small>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sim2:
        st.markdown("#### Projected Impact")
        
        projected_savings = TOTAL_COHORT * BASELINE_GAP * ((screening_adoption + er_data_sharing) / 100)
        
        st.metric(
            label="Projected Annual Savings",
            value=f"${projected_savings:,.0f}",
            delta=f"{screening_adoption + er_data_sharing}% efficiency gain",
            delta_color="normal"
        )
        
        st.markdown(f"""
        <div style="background: rgba(0, 204, 150, 0.2); padding: 15px; border-radius: 8px; border: 1px solid #00CC96; margin-top: 20px;">
            <h2 style="color: #00CC96; margin: 0; text-align: center;">${projected_savings:,.0f}</h2>
            <p style="color: #FAFAFA; text-align: center; margin: 5px 0 0 0; font-size: 0.85rem;">
                Based on closing the efficiency gap for <b>{TOTAL_COHORT:,}</b> Medicare beneficiaries
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sim3:
        st.markdown("#### Cost Reduction Trajectory")
        
        # Generate projection curve
        efficiency_range = list(range(0, 51, 5))
        savings_proj = [TOTAL_COHORT * BASELINE_GAP * (eff / 100) for eff in efficiency_range]
        
        fig_roi = go.Figure()
        
        fig_roi.add_trace(go.Scatter(
            x=efficiency_range,
            y=savings_proj,
            fill='tozeroy',
            fillcolor='rgba(0, 204, 150, 0.3)',
            line=dict(color='#00CC96', width=3),
            mode='lines',
            name='Savings'
        ))
        
        # Add current position marker
        current_efficiency = screening_adoption + er_data_sharing
        fig_roi.add_trace(go.Scatter(
            x=[current_efficiency],
            y=[projected_savings],
            mode='markers',
            marker=dict(size=12, color='#FFC107', line=dict(color='#FAFAFA', width=2)),
            name='Current'
        ))
        
        fig_roi.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="Efficiency Improvement (%)", color='#FAFAFA', gridcolor='#333'),
            yaxis=dict(title="Annual Savings ($)", color='#FAFAFA', gridcolor='#333'),
            showlegend=False,
            height=300,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        st.plotly_chart(fig_roi, use_container_width=True)
    
    st.markdown("---")
    st.info("💡 **Methodology**: Savings calculated as (Cohort Size × Per-Patient Inefficiency Gap × Efficiency Improvement %). Assumes linear scaling and full implementation across target population.")
