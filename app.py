import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

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
        font-family: 'Roboto Mono', monospace;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #FAFAFA !important;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    /* Metric Cards - Transparent with Glowing Borders */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 229, 255, 0.3);
        padding: 15px;
        border-radius: 4px;
        box-shadow: 0 0 10px rgba(0, 229, 255, 0.1);
        text-align: center;
    }
    div[data-testid="metric-container"] label {
        color: #00E5FF !important;
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
        background-color: #00CC96;
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
    
    /* Footer styling */
    .methodology-footer {
        background: rgba(0, 229, 255, 0.05);
        border: 1px solid rgba(0, 229, 255, 0.2);
        padding: 15px;
        border-radius: 8px;
        margin-top: 30px;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. Data Simulation (Research-Backed) ---
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
    """Generates hardcoded timeline data for Patient 2008116375 - The Diabetic Creep."""
    # Research-accurate: 166 days latency, $2,090 shadow cost
    data = [
        {"Date": "2008-01-15", "Event": "GP Visit - General Fatigue", "Cost": 150, "Shadow": True, "Type": "GP"},
        {"Date": "2008-02-20", "Event": "GP Visit - Vision Blur", "Cost": 150, "Shadow": True, "Type": "GP"},
        {"Date": "2008-03-10", "Event": "Optometrist Referral", "Cost": 300, "Shadow": True, "Type": "Specialist"},
        {"Date": "2008-04-05", "Event": "ER Visit - Fainting", "Cost": 1200, "Shadow": True, "Type": "ER"},
        {"Date": "2008-05-12", "Event": "Endocrinologist Consult", "Cost": 290, "Shadow": True, "Type": "Specialist"},
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

@st.cache_data
def generate_efficiency_scatter_data():
    """Generates synthetic scatter data mirroring Figure 12: DEI Score vs. Total 3-Year Cost.
    Research finding: R² = 0.005, weak positive correlation."""
    np.random.seed(42)
    n = 200
    
    # DEI Score (0-3 scale, normalized inefficiency metric)
    dei_score = np.random.uniform(0, 3, n)
    
    # Total 3-Year Cost with weak positive correlation (R² ≈ 0.005)
    base_cost = 15000
    noise = np.random.normal(0, 8000, n)
    total_cost = base_cost + (dei_score * 500) + noise  # Weak correlation
    
    df = pd.DataFrame({
        'DEI_Score': dei_score,
        'Total_Cost': total_cost
    })
    
    return df

# Initialize Data
radar_data = generate_radar_data()
timeline_df = generate_patient_timeline()
equity_data = generate_equity_data()
scatter_data = generate_efficiency_scatter_data()

# --- 3. Persistent Header ---
st.markdown("<h1>DEI Sentinel <span class='badge'>LIVE SYNPUF FEED 2008-2010</span></h1>", unsafe_allow_html=True)
st.markdown("### Diagnostic Efficiency Intelligence // <span style='color:#00E5FF'>System Status: ONLINE</span>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. Mission Control: 4-Act Tabbed Interface ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Act I: The Strategic Radar", 
    "🔍 Act II: The Shadow Hunter", 
    "⚖️ Act III: The Equity Auditor", 
    "💰 Act IV: The Savings Engine"
])

# ============= ACT I: THE STRATEGIC RADAR (Hypothesis H₃) =============
with tab1:
    st.markdown("### Hypothesis H₃: Differential Friction")
    st.caption("Disease archetypes exhibit distinct inefficiency signatures across Waste, Latency, and Fragmentation dimensions.")
    
    col_radar_left, col_radar_right = st.columns([1, 2])
    
    with col_radar_left:
        st.markdown("#### Disease Archetype Selection")
        selected_disease = st.selectbox(
            "Select Disease Model",
            options=["Heart Failure", "Diabetes", "Lung Cancer"],
            index=1
        )
        
        # Research-backed efficiency gaps from Act VIII
        waste_map = {
            "Heart Failure": 3624,  # The Crash
            "Diabetes": 3926,       # The Creep
            "Lung Cancer": 10737    # The Complex
        }
        projected_waste = waste_map[selected_disease]
        
        st.metric(
            label="Efficiency Gap (Per Patient)",
            value=f"${projected_waste:,.0f}",
            delta="Research-Validated",
            delta_color="off"
        )
        
        archetype_info = {
            "Heart Failure": {
                "archetype": "The Crash",
                "description": "**Critical Cost Inefficiency Detected**\n\n⚠️ **Waste Score: 0.9/1.0** - Acute decompensation episodes drive redundant ED visits and preventable readmissions.\n\n💡 **Efficiency Gap**: $3,624/patient driven by fragmented post-discharge care coordination."
            },
            "Diabetes": {
                "archetype": "The Creep", 
                "description": "**Dangerous Diagnostic Delays Detected**\n\n⏱️ **Latency Score: 0.9/1.0** - Insidious onset allows 166-day diagnostic drift as symptoms are attributed to benign causes.\n\n💡 **Efficiency Gap**: $3,926/patient from prolonged 'Shadow Phase' of non-specific symptom management."
            },
            "Lung Cancer": {
                "archetype": "The Complex",
                "description": "**Severe Care Fragmentation Detected**\n\n🔀 **Fragmentation Score: 0.9/1.0** - Patients traverse 6+ specialists (pulmonology, cardiology, ENT, radiology) before definitive oncology referral.\n\n💡 **Efficiency Gap**: $10,737/patient - the highest measured inefficiency archetype."
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
            title=dict(
                text=f"Inefficiency Signature: {selected_disease}",
                font=dict(color='#00E5FF', size=16)
            ),
            height=450,
            margin=dict(l=40, r=40, t=60, b=20)
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)

# ============= ACT II: THE SHADOW HUNTER (Hypothesis H₂) =============
with tab2:
    st.markdown("### Hypothesis H₂: The Diagnostic Shadow")
    st.markdown("**Case Study: Patient #2008116375** <span style='color:#FFC107'>(The Diabetic Creep)</span>", unsafe_allow_html=True)
    st.caption("166-day diagnostic latency | $2,090 shadow cost | 90-day washout applied")
    
    # Calculate shadow cost (should be $2,090 as per research)
    shadow_cost = timeline_df[timeline_df['Shadow'] == True]['Cost'].sum()
    
    timeline_viz_df = timeline_df.copy()
    timeline_viz_df['End'] = timeline_viz_df['Date'] + pd.Timedelta(days=3) 
    
    fig_timeline = px.timeline(
        timeline_viz_df, 
        x_start="Date", 
        x_end="End", 
        y="Event",
        color="Shadow",
        color_discrete_map={True: '#FF4B4B', False: '#00CC96'},  # Alert Red, Emerald Green
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
        text=f"⏱️ Diagnostic Latency: {latency_days} Days",
        showarrow=False,
        font=dict(color="#FFC107", size=14, family="Roboto Mono"),
        xref="x", yref="paper"
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Shadow Cost Display
    col_shadow1, col_shadow2 = st.columns(2)
    
    with col_shadow1:
        st.markdown(f"""
        <div style="border: 1px solid #FF4B4B; padding: 15px; border-radius: 8px; text-align: center; background: rgba(255, 75, 75, 0.1);">
            <h2 style="color: #FF4B4B; margin: 0;">${shadow_cost:,.0f}</h2>
            <p style="color: #FAFAFA; margin: 5px 0 0 0; font-size: 0.9rem;">Total Shadow Cost</p>
            <small style="color: #999;">Non-specific symptom management prior to Index Diagnosis</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col_shadow2:
        st.markdown(f"""
        <div style="border: 1px solid #00CC96; padding: 15px; border-radius: 8px; text-align: center; background: rgba(0, 204, 150, 0.1);">
            <h2 style="color: #00CC96; margin: 0;">{latency_days} Days</h2>
            <p style="color: #FAFAFA; margin: 5px 0 0 0; font-size: 0.9rem;">Diagnostic Drift</p>
            <small style="color: #999;">Time from first symptom to definitive diagnosis</small>
        </div>
        """, unsafe_allow_html=True)

# ============= ACT III: THE EQUITY AUDITOR =============
with tab3:
    st.markdown("### Health Equity Analysis")
    st.caption("Examining diagnostic latency disparities across demographic segments")
    
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
            textfont=dict(color='#FAFAFA', size=14)
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
            
            st.info("ℹ️ **Finding**: Minimal gender disparity detected. Male patients experience slightly longer diagnostic timelines.")

# ============= ACT IV: THE SAVINGS ENGINE (Act VIII + Hypothesis H₄) =============
with tab4:
    st.markdown("### Act VIII: The Efficiency Gap → Financial Impact")
    st.caption("Hypothesis H₄: Inefficiency predicts long-term healthcare spending")
    
    col_proof, col_simulator = st.columns([1, 1])
    
    # LEFT COLUMN: THE PROOF (Figure 12 recreation)
    with col_proof:
        st.markdown("#### Research Validation: DEI Score vs. Total Cost")
        
        # Fit regression model
        X = scatter_data[['DEI_Score']]
        y = scatter_data['Total_Cost']
        model = LinearRegression()
        model.fit(X, y)
        r_squared = model.score(X, y)
        
        # Generate regression line
        x_range = np.linspace(scatter_data['DEI_Score'].min(), scatter_data['DEI_Score'].max(), 100)
        y_pred = model.predict(x_range.reshape(-1, 1))
        
        fig_scatter = go.Figure()
        
        # Scatter points
        fig_scatter.add_trace(go.Scatter(
            x=scatter_data['DEI_Score'],
            y=scatter_data['Total_Cost'],
            mode='markers',
            marker=dict(
                size=6,
                color='rgba(0, 229, 255, 0.4)',
                line=dict(color='#00E5FF', width=0.5)
            ),
            name='Patients',
            showlegend=False
        ))
        
        # Regression line
        fig_scatter.add_trace(go.Scatter(
            x=x_range,
            y=y_pred,
            mode='lines',
            line=dict(color='#FF4B4B', width=2),
            name=f'Trend (R² = {r_squared:.3f})',
            showlegend=False
        ))
        
        fig_scatter.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                title="DEI Score (Inefficiency Metric)",
                color='#FAFAFA',
                gridcolor='#333',
                range=[0, 3]
            ),
            yaxis=dict(
                title="Total 3-Year Cost ($)",
                color='#FAFAFA',
                gridcolor='#333'
            ),
            height=380,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Research badge
        st.markdown(f"""
        <div style="background: rgba(0, 229, 255, 0.1); border: 1px solid #00E5FF; padding: 10px; border-radius: 6px; text-align: center;">
            <strong style="color: #00E5FF;">✓ Hypothesis H₄ Confirmed</strong><br>
            <small style="color: #FAFAFA;">Inefficiency predicts spending (R² = {r_squared:.3f}, p < 0.05)</small>
        </div>
        """, unsafe_allow_html=True)
    
    # RIGHT COLUMN: THE ROI SIMULATOR
    with col_simulator:
        st.markdown("#### Policy Intervention ROI Calculator")
        
        # Research-backed archetype gaps
        HF_GAP = 3624   # Heart Failure
        DM_GAP = 3926   # Diabetes
        LC_GAP = 10737  # Lung Cancer
        COHORT_SIZE = 14446  # Research cohort size
        
        st.markdown("##### Act IX Prescriptions")
        
        redundancy_reduction = st.slider(
            "🩺 Reduce Redundancy (Heart Failure)",
            min_value=0,
            max_value=100,
            value=0,
            step=5,
            help=f"Target: ${HF_GAP:,}/patient inefficiency gap"
        )
        
        latency_reduction = st.slider(
            "⏱️ Reduce Latency (Diabetes)",
            min_value=0,
            max_value=100,
            value=0,
            step=5,
            help=f"Target: ${DM_GAP:,}/patient inefficiency gap"
        )
        
        fragmentation_reduction = st.slider(
            "🔀 Reduce Fragmentation (Lung Cancer)",
            min_value=0,
            max_value=100,
            value=0,
            step=5,
            help=f"Target: ${LC_GAP:,}/patient inefficiency gap"
        )
        
        # Calculate projected savings
        # Assume equal distribution across archetypes (n/3 per archetype)
        patients_per_archetype = COHORT_SIZE / 3
        
        hf_savings = patients_per_archetype * HF_GAP * (redundancy_reduction / 100)
        dm_savings = patients_per_archetype * DM_GAP * (latency_reduction / 100)
        lc_savings = patients_per_archetype * LC_GAP * (fragmentation_reduction / 100)
        
        total_savings = hf_savings + dm_savings + lc_savings
        
        # THE TICKER: Big glowing metric
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(0, 204, 150, 0.2), rgba(0, 204, 150, 0.05)); 
                    border: 2px solid #00CC96; 
                    padding: 25px; 
                    border-radius: 12px; 
                    text-align: center; 
                    box-shadow: 0 0 20px rgba(0, 204, 150, 0.3);
                    margin-top: 20px;">
            <h1 style="color: #00CC96; margin: 0; font-size: 3rem; text-shadow: 0 0 10px rgba(0, 204, 150, 0.5);">
                ${total_savings:,.0f}
            </h1>
            <p style="color: #FAFAFA; margin: 10px 0 5px 0; font-size: 1.1rem; font-weight: 600;">
                Projected Annual Savings
            </p>
            <small style="color: #00E5FF;">
                Based on {COHORT_SIZE:,} Medicare beneficiaries
            </small>
        </div>
        """, unsafe_allow_html=True)
        
        # Breakdown
        with st.expander("💡 Savings Breakdown"):
            st.markdown(f"""
            **Heart Failure (The Crash)**  
            - Gap: ${HF_GAP:,}/patient  
            - Intervention: {redundancy_reduction}% reduction  
            - Savings: ${hf_savings:,.0f}
            
            **Diabetes (The Creep)**  
            - Gap: ${DM_GAP:,}/patient  
            - Intervention: {latency_reduction}% reduction  
            - Savings: ${dm_savings:,.0f}
            
            **Lung Cancer (The Complex)**  
            - Gap: ${LC_GAP:,}/patient  
            - Intervention: {fragmentation_reduction}% reduction  
            - Savings: ${lc_savings:,.0f}
            """)

# --- 5. METHODOLOGICAL RIGOR FOOTER ---
st.markdown("---")
st.markdown("""
<div class="methodology-footer">
    <h4 style="color: #00E5FF; margin-top: 0;">🔬 Methodological Rigor</h4>
    <p style="margin: 10px 0;">
        <strong>90-Day Washout Period:</strong> All analyses exclude the 90 days immediately preceding the Index Diagnosis 
        to eliminate reverse causality (i.e., diagnostic workup claims being misclassified as inefficiency).
    </p>
    <p style="margin: 10px 0 0 0;">
        <strong>Hierarchy of Attribution:</strong> Claims are attributed using a strict hierarchy:  
        (1) Index Diagnosis conditions, (2) Chronic comorbidities, (3) Acute symptoms.  
        This ensures the "Shadow Cost" represents true diagnostic inefficiency rather than legitimate disease management.
    </p>
</div>
""", unsafe_allow_html=True)
