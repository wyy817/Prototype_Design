import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils.data_loader import load_all_data

st.set_page_config(
    page_title="CP Dashboard - Strategic Intelligence",
    page_icon="📊",
    layout="wide"
)

# Load all data
competitors, market, segments, financials = load_all_data()

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E7D32;
    }
    .insight-box {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .competitor-card {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        background-color: white;
    }
    .swot-positive {
        color: #2E7D32;
        font-weight: 500;
    }
    .swot-negative {
        color: #C62828;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("CP Dashboard Navigation")
page = st.sidebar.radio(
    "Select Module",
    ["Overview", "Competitor Intelligence", "Market Analysis", "Customer Insights", "Opportunity Engine"]
)

if st.sidebar.button("Return to Home"):
    st.switch_page("Home.py")

# ============ OVERVIEW PAGE ============
if page == "Overview":
    st.title("CP Group - Strategic Market Analysis Dashboard")
    st.markdown("### Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Market Size (2024)",
            f"¥{market['market_size_2024']/1e9:.1f}B",
            f"+{market['growth_rate_cagr']*100:.0f}% CAGR"
        )
    
    with col2:
        st.metric(
            "Target Segment",
            "45%",
            "Pragmatic Middle-Class"
        )
    
    with col3:
        st.metric(
            "Tier 1 Penetration",
            f"{market['instant_retail_penetration']['tier1']*100:.0f}%",
            "Instant Retail"
        )
    
    with col4:
        st.metric(
            "Key Competitors",
            "2",
            "Dingdong & Freshippo"
        )
    
    st.markdown("---")
    
    # Key Insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='insight-box'>
        <h4>Market Opportunity</h4>
        <ul>
        <li>¥580B market growing at 22% CAGR</li>
        <li>45% pragmatic middle-class segment underserved</li>
        <li>Consumer shift from bulk to frequent small purchases</li>
        <li>Strong demand for quality-price balance</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='insight-box'>
        <h4>Competitive Gaps</h4>
        <ul>
        <li>Partial traceability (25-30% coverage)</li>
        <li>High fulfillment costs (¥80-87M)</li>
        <li>Limited organic product offerings</li>
        <li>Weak price-quality optimization</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Competitor Comparison
    st.markdown("### Quick Competitor Comparison")
    
    comp_data = {
        "": ["Business Model", "Cities", "SKU Count", "Traceability", "Fulfillment Cost"],
        "Dingdong": [
            competitors['dingdong']['model'],
            f"{len(competitors['dingdong']['cities'])} (YRD focus)",
            competitors['dingdong']['sku_count'],
            "Partial (25%)",
            "¥87.2M"
        ],
        "Freshippo": [
            competitors['freshippo']['model'],
            "10+ (Tier 1+2)",
            competitors['freshippo']['sku_count'],
            "Partial (30%)",
            "¥82M"
        ]
    }
    
    st.table(pd.DataFrame(comp_data))

# ============ COMPETITOR INTELLIGENCE PAGE ============
elif page == "Competitor Intelligence":
    st.title("Interactive Competitor Intelligence Dashboard")
    
    # Competitor Selection
    competitor = st.selectbox(
        "Select Competitor for Detailed Analysis",
        ["Dingdong Maicai", "Freshippo (Hema Fresh)", "Side-by-Side Comparison"]
    )
    
    if competitor == "Side-by-Side Comparison":
        st.markdown("### Comprehensive Competitor Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='competitor-card'>
            <h3>Dingdong Maicai</h3>
            <p><strong>Model:</strong> Front Warehouse (Pure Online)</p>
            <p><strong>Geographic Focus:</strong> Yangtze River Delta</p>
            <p><strong>Strategy:</strong> Quality over expansion</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Strengths")
            for s in competitors['dingdong']['strengths']:
                st.markdown(f"<span class='swot-positive'>✓ {s}</span>", unsafe_allow_html=True)
            
            st.markdown("#### Weaknesses")
            for w in competitors['dingdong']['weaknesses']:
                st.markdown(f"<span class='swot-negative'>✗ {w}</span>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='competitor-card'>
            <h3>Freshippo (Hema Fresh)</h3>
            <p><strong>Model:</strong> Store-Warehouse Integration</p>
            <p><strong>Geographic Focus:</strong> National (Tier 1+2)</p>
            <p><strong>Strategy:</strong> Omnichannel premium</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Strengths")
            for s in competitors['freshippo']['strengths']:
                st.markdown(f"<span class='swot-positive'>✓ {s}</span>", unsafe_allow_html=True)
            
            st.markdown("#### Weaknesses")
            for w in competitors['freshippo']['weaknesses']:
                st.markdown(f"<span class='swot-negative'>✗ {w}</span>", unsafe_allow_html=True)
        
        # Financial Performance - Dingdong
        st.markdown("---")
        st.markdown("### Dingdong Maicai Financial Performance (2021-2024)")
        
        df_fin = pd.DataFrame(financials['annual_data'])
        df_fin['period'] = df_fin['year'].astype(str) + ' ' + df_fin['quarter']
        df_fin['net_loss_m'] = df_fin['net_loss'] / 1e6
        
        fig = go.Figure()
        
        colors = ['red' if x < 0 else 'green' for x in df_fin['net_loss_m']]
        
        fig.add_trace(go.Scatter(
            x=df_fin['period'],
            y=df_fin['net_loss_m'],
            mode='lines+markers',
            name='Net Profit/Loss',
            line=dict(color='#2E7D32', width=3),
            marker=dict(size=8, color=colors)
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Break-even")
        
        fig.update_layout(
            title="Dingdong Maicai Profit/Loss Trend (Million CNY)",
            xaxis_title="Quarter",
            yaxis_title="Net Profit/Loss (Million CNY)",
            height=500,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='insight-box'>
        <strong>Key Insight:</strong> Dingdong achieved profitability in Q1 2024 after strategic 
        withdrawal from unprofitable tier 3/4 cities and focus on the Yangtze River Delta region. 
        This demonstrates the viability of the front warehouse model when properly executed in 
        high-density urban markets.
        </div>
        """, unsafe_allow_html=True)
        
        # SKU Comparison
        st.markdown("---")
        st.markdown("### Product Portfolio Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = go.Figure(data=[go.Pie(
                labels=list(competitors['dingdong']['product_categories'].keys()),
                values=list(competitors['dingdong']['product_categories'].values()),
                hole=0.3,
                marker_colors=['#2E7D32', '#66BB6A', '#A5D6A7', '#C8E6C9', '#E8F5E9']
            )])
            fig1.update_layout(title="Dingdong Product Mix", height=400)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = go.Figure(data=[go.Pie(
                labels=list(competitors['freshippo']['product_categories'].keys()),
                values=list(competitors['freshippo']['product_categories'].values()),
                hole=0.3,
                marker_colors=['#1565C0', '#42A5F5', '#90CAF9', '#BBDEFB', '#E3F2FD']
            )])
            fig2.update_layout(title="Freshippo Product Mix", height=400)
            st.plotly_chart(fig2, use_container_width=True)
        
        # Technology Capabilities
        st.markdown("---")
        st.markdown("### Technology & Innovation Capabilities")
        
        tech_comparison = {
            "Capability": ["AI Integration", "Traceability", "Membership System", "Omnichannel", "Supply Chain Digitization"],
            "Dingdong": [0.75, 0.25, 0.85, 0.00, 0.70],
            "Freshippo": [0.60, 0.30, 0.75, 0.95, 0.65]
        }
        
        df_tech = pd.DataFrame(tech_comparison)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Dingdong',
            x=df_tech['Capability'],
            y=df_tech['Dingdong'],
            marker_color='#2E7D32'
        ))
        
        fig.add_trace(go.Bar(
            name='Freshippo',
            x=df_tech['Capability'],
            y=df_tech['Freshippo'],
            marker_color='#1565C0'
        ))
        
        fig.update_layout(
            title="Technology Capability Comparison (0-1 scale)",
            barmode='group',
            height=400,
            yaxis=dict(range=[0, 1])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    elif competitor == "Dingdong Maicai":
        comp_data = competitors['dingdong']
        st.markdown(f"### {comp_data['name']} - Detailed Analysis")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Business Model", comp_data['model'])
        with col2:
            st.metric("SKU Count", f"{comp_data['sku_count']:,}")
        with col3:
            st.metric("City Coverage", len(comp_data['cities']))
        
        st.markdown("#### City Strategy")
        st.info(comp_data['city_strategy'])
        
        st.markdown("#### Covered Cities")
        st.write(", ".join(comp_data['cities']))
        
        # SWOT Analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Strengths")
            for s in comp_data['strengths']:
                st.success(s)
            
            st.markdown("#### Opportunities")
            for o in comp_data['opportunities']:
                st.info(o)
        
        with col2:
            st.markdown("#### Weaknesses")
            for w in comp_data['weaknesses']:
                st.warning(w)
            
            st.markdown("#### Threats")
            for t in comp_data['threats']:
                st.error(t)
        
        # AI Features
        st.markdown("#### AI Features")
        for feature in comp_data['ai_features']:
            st.markdown(f"- {feature}")
        
        # Membership Benefits
        st.markdown("#### Membership Benefits")
        for benefit in comp_data['membership_benefits']:
            st.markdown(f"- {benefit}")
    
    else:  # Freshippo
        comp_data = competitors['freshippo']
        st.markdown(f"### {comp_data['name']} - Detailed Analysis")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Business Model", comp_data['model'])
        with col2:
            st.metric("SKU Count", f"{comp_data['sku_count']:,}")
        with col3:
            st.metric("Formats", "2 (Fresh + NB)")
        
        st.markdown("#### Business Formats")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Hema Fresh**")
            st.write(f"- Target: {comp_data['formats']['hema_fresh']['target']}")
            st.write(f"- Positioning: {comp_data['formats']['hema_fresh']['positioning']}")
            st.write(f"- Format: {comp_data['formats']['hema_fresh']['store_size']}")
        
        with col2:
            st.markdown("**Hema NB (Neighborhood)**")
            st.write(f"- Target: {comp_data['formats']['hema_nb']['target']}")
            st.write(f"- Positioning: {comp_data['formats']['hema_nb']['positioning']}")
            st.write(f"- Format: {comp_data['formats']['hema_nb']['store_size']}")
        
        # SWOT Analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Strengths")
            for s in comp_data['strengths']:
                st.success(s)
            
            st.markdown("#### Opportunities")
            for o in comp_data['opportunities']:
                st.info(o)
        
        with col2:
            st.markdown("#### Weaknesses")
            for w in comp_data['weaknesses']:
                st.warning(w)
            
            st.markdown("#### Threats")
            for t in comp_data['threats']:
                st.error(t)

# ============ MARKET ANALYSIS PAGE ============
elif page == "Market Analysis":
    st.title("Market Analysis & Industry Trends")
    
    # Market Size Growth
    st.markdown("### Market Size & Growth Trajectory")
    
    years = [2023, 2024, 2025]
    sizes = [
        market['market_size_2023']/1e9,
        market['market_size_2024']/1e9,
        market['market_size_2025_projected']/1e9
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=years,
        y=sizes,
        text=[f'¥{s:.1f}B' for s in sizes],
        textposition='outside',
        marker_color='#2E7D32'
    ))
    
    fig.update_layout(
        title=f"Chinese Fresh E-commerce Market Size (CAGR: {market['growth_rate_cagr']*100:.0f}%)",
        xaxis_title="Year",
        yaxis_title="Market Size (Billion CNY)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # City Tier Penetration
    st.markdown("### Instant Retail Penetration by City Tier")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        penetration_data = market['instant_retail_penetration']
        
        fig = go.Figure(go.Bar(
            x=list(penetration_data.keys()),
            y=[v*100 for v in penetration_data.values()],
            text=[f'{v*100:.0f}%' for v in penetration_data.values()],
            textposition='outside',
            marker_color=['#1B5E20', '#2E7D32', '#66BB6A', '#A5D6A7']
        ))
        
        fig.update_layout(
            title="Instant Retail Market Penetration",
            xaxis_title="City Tier",
            yaxis_title="Penetration Rate (%)",
            height=400,
            yaxis=dict(range=[0, 50])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
        <h4>Key Insights</h4>
        <ul>
        <li>Tier 1 cities: 45% penetration</li>
        <li>Strong growth in New Tier 1</li>
        <li>Tier 2/3 remain underpenetrated</li>
        <li>Opportunity in lower tiers</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Consumer Segments
    st.markdown("---")
    st.markdown("### Consumer Segmentation")
    
    segment_data = market['consumer_segments']
    
    fig = go.Figure(data=[go.Pie(
        labels=list(segment_data.keys()),
        values=list(segment_data.values()),
        hole=0.4,
        marker_colors=['#2E7D32', '#FFA726', '#42A5F5'],
        textinfo='label+percent'
    )])
    
    fig.update_layout(
        title="Consumer Segment Distribution",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Pain Points Analysis
    st.markdown("---")
    st.markdown("### Industry Pain Points (Severity Analysis)")
    
    pain_points = market['key_pain_points']
    
    pain_df = pd.DataFrame([
        {
            'Pain Point': k.replace('_', ' ').title(),
            'Severity': v['severity'],
            'Description': v['description']
        }
        for k, v in pain_points.items()
    ]).sort_values('Severity', ascending=True)
    
    fig = go.Figure(go.Bar(
        x=pain_df['Severity'],
        y=pain_df['Pain Point'],
        orientation='h',
        text=[f'{s*100:.0f}%' for s in pain_df['Severity']],
        textposition='outside',
        marker_color=['#C62828' if s > 0.8 else '#F57C00' if s > 0.7 else '#FFA726' 
                      for s in pain_df['Severity']]
    ))
    
    fig.update_layout(
        title="Industry Pain Points by Severity",
        xaxis_title="Severity Score",
        yaxis_title="",
        height=500,
        xaxis=dict(range=[0, 1])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display descriptions
    with st.expander("View Pain Point Descriptions"):
        for _, row in pain_df.iterrows():
            st.markdown(f"**{row['Pain Point']}**: {row['Description']}")
    
    # AI & Technology Trends
    st.markdown("---")
    st.markdown("### Technology Adoption Trends")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
        <h4>AI Adoption</h4>
        <p><strong>Current:</strong> 35%</p>
        <p><strong>2026 Projection:</strong> 62%</p>
        <p style='color: #2E7D32; font-weight: bold;'>+77% Growth</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
        <h4>Supply Chain Digitization</h4>
        <p><strong>Current:</strong> 48%</p>
        <p><strong>2026 Projection:</strong> 75%</p>
        <p style='color: #2E7D32; font-weight: bold;'>+56% Growth</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
        <h4>Sustainability Focus</h4>
        <p><strong>Importance:</strong> 68%</p>
        <p><strong>Premium Willingness:</strong> 23%</p>
        <p style='color: #F57C00;'>Growing concern</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Industry Health Index
    st.markdown("---")
    st.markdown("### Industry Health Index")
    
    health_metrics = {
        'Market Growth': 0.85,
        'Profitability': 0.45,
        'Technology Adoption': 0.65,
        'Supply Chain Maturity': 0.58,
        'Customer Satisfaction': 0.62,
        'Competitive Intensity': 0.75
    }
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(health_metrics.values()),
        theta=list(health_metrics.keys()),
        fill='toself',
        fillcolor='rgba(46, 125, 50, 0.3)',
        line=dict(color='#2E7D32', width=2)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        title="Industry Health Assessment (0-1 scale)",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============ CUSTOMER INSIGHTS PAGE ============
elif page == "Customer Insights":
    st.title("Customer Insights & Segmentation Analysis")
    
    segment_key = st.selectbox(
        "Select Customer Segment",
        list(segments.keys()),
        format_func=lambda x: segments[x]['segment_name']
    )
    
    segment = segments[segment_key]
    
    # Segment Overview
    st.markdown(f"### {segment['segment_name']}")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Market Share", f"{segment['percentage']*100:.0f}%")
    with col2:
        st.metric("Income Range", f"¥{segment['income_range_cny']}")
    with col3:
        if 'age_range' in segment:
            st.metric("Age Range", segment['age_range'])
    with col4:
        if 'household_size' in segment:
            st.metric("Household", segment['household_size'])
    
    # Jobs to Be Done
    st.markdown("---")
    st.markdown("### Jobs to Be Done (JTBD)")
    st.info(segment['jobs_to_be_done'])
    
    if segment_key == 'pragmatic_middle_class':
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Functional Jobs")
            for job in segment['functional_jobs']:
                st.markdown(f"- {job}")
        
        with col2:
            st.markdown("#### Emotional Jobs")
            for job in segment['emotional_jobs']:
                st.markdown(f"- {job}")
        
        with col3:
            st.markdown("#### Social Jobs")
            for job in segment['social_jobs']:
                st.markdown(f"- {job}")
    
    # Priorities
    st.markdown("---")
    st.markdown("### Customer Priorities")
    
    priorities = segment['priorities']
    
    fig = go.Figure(go.Bar(
        x=list(priorities.values()),
        y=list(priorities.keys()),
        orientation='h',
        text=[f'{v*100:.0f}%' for v in priorities.values()],
        textposition='outside',
        marker_color='#2E7D32'
    ))
    
    fig.update_layout(
        title="Priority Rankings",
        xaxis_title="Importance Score",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 1])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    if segment_key == 'pragmatic_middle_class':
        # Pain Points
        st.markdown("---")
        st.markdown("### Pain Points Analysis")
        
        tab1, tab2, tab3 = st.tabs(["Functional Pains", "Emotional Pains", "Social Pains"])
        
        with tab1:
            for pain in segment['pain_points']['functional']:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{pain['pain']}**")
                with col2:
                    severity_color = '#C62828' if pain['severity'] > 0.8 else '#F57C00'
                    st.markdown(f"<span style='color: {severity_color}; font-weight: bold;'>{pain['severity']*100:.0f}% severity</span>", unsafe_allow_html=True)
                st.caption(f"Frequency: {pain['frequency']}")
                st.markdown("---")
        
        with tab2:
            for pain in segment['pain_points']['emotional']:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{pain['pain']}**")
                with col2:
                    severity_color = '#C62828' if pain['severity'] > 0.8 else '#F57C00'
                    st.markdown(f"<span style='color: {severity_color}; font-weight: bold;'>{pain['severity']*100:.0f}% severity</span>", unsafe_allow_html=True)
                st.caption(f"Frequency: {pain['frequency']}")
                st.markdown("---")
        
        with tab3:
            for pain in segment['pain_points']['social']:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{pain['pain']}**")
                with col2:
                    severity_color = '#C62828' if pain['severity'] > 0.8 else '#F57C00'
                    st.markdown(f"<span style='color: {severity_color}; font-weight: bold;'>{pain['severity']*100:.0f}% severity</span>", unsafe_allow_html=True)
                st.caption(f"Frequency: {pain['frequency']}")
                st.markdown("---")
        
        # Gains
        st.markdown("---")
        st.markdown("### Expected Gains")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Functional Gains")
            for gain in segment['gains']['functional']:
                st.success(gain)
        
        with col2:
            st.markdown("#### Emotional Gains")
            for gain in segment['gains']['emotional']:
                st.success(gain)
        
        with col3:
            st.markdown("#### Social Gains")
            for gain in segment['gains']['social']:
                st.success(gain)
        
        # Shopping Behavior
        st.markdown("---")
        st.markdown("### Shopping Behavior Profile")
        
        behavior = segment['shopping_behavior']
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Purchase Frequency", behavior['frequency'])
            st.metric("Avg Basket Size", behavior['avg_basket_size_cny'])
        
        with col2:
            st.metric("Preferred Time", behavior['preferred_time'])
            st.metric("Decision Time", behavior['decision_time'])
        
        with col3:
            st.metric("Device", behavior['device_preference'])
        
        # Product Preferences
        st.markdown("---")
        st.markdown("### Product Preferences")
        
        prefs = segment['product_preferences']
        
        fig = go.Figure(data=[go.Pie(
            labels=list(prefs.keys()),
            values=list(prefs.values()),
            hole=0.3,
            textinfo='label+percent'
        )])
        
        fig.update_layout(
            title="Product Category Preferences",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ============ OPPORTUNITY ENGINE PAGE ============
elif page == "Opportunity Engine":
    st.title("Opportunity Engine - Market Entry Strategy")
    
    st.markdown("""
    This module identifies market gaps and calculates opportunity scores based on:
    - Unmet customer needs
    - Competitor weaknesses
    - Market trends
    - CP Group capabilities
    """)
    
    st.markdown("---")
    
    # Opportunity Scoring
    st.markdown("### Market Opportunity Scoring")
    
    opportunities = [
        {
            'Opportunity': 'Full Supply Chain Traceability',
            'Market Need': 0.95,
            'Competitor Gap': 0.75,
            'CP Capability': 0.85,
            'Market Size': 0.80,
            'Score': 0
        },
        {
            'Opportunity': 'Organic & Low-Pesticide Products',
            'Market Need': 0.85,
            'Competitor Gap': 0.90,
            'CP Capability': 0.80,
            'Market Size': 0.65,
            'Score': 0
        },
        {
            'Opportunity': 'Price-Quality Optimization Platform',
            'Market Need': 0.90,
            'Competitor Gap': 0.85,
            'CP Capability': 0.75,
            'Market Size': 0.90,
            'Score': 0
        },
        {
            'Opportunity': 'AI-Powered Personalization',
            'Market Need': 0.75,
            'Competitor Gap': 0.60,
            'CP Capability': 0.70,
            'Market Size': 0.85,
            'Score': 0
        },
        {
            'Opportunity': 'Community-Based Distribution',
            'Market Need': 0.70,
            'Competitor Gap': 0.50,
            'CP Capability': 0.90,
            'Market Size': 0.70,
            'Score': 0
        }
    ]
    
    # Calculate scores
    for opp in opportunities:
        opp['Score'] = (
            opp['Market Need'] * 0.3 +
            opp['Competitor Gap'] * 0.25 +
            opp['CP Capability'] * 0.25 +
            opp['Market Size'] * 0.2
        )
    
    opportunities.sort(key=lambda x: x['Score'], reverse=True)
    
    # Display opportunity cards
    for i, opp in enumerate(opportunities):
        with st.expander(f"#{i+1} {opp['Opportunity']} - Score: {opp['Score']*100:.1f}/100"):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Market Need", f"{opp['Market Need']*100:.0f}%")
            with col2:
                st.metric("Competitor Gap", f"{opp['Competitor Gap']*100:.0f}%")
            with col3:
                st.metric("CP Capability", f"{opp['CP Capability']*100:.0f}%")
            with col4:
                st.metric("Market Size", f"{opp['Market Size']*100:.0f}%")
            
            # Radar chart for this opportunity
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=[opp['Market Need'], opp['Competitor Gap'], opp['CP Capability'], opp['Market Size']],
                theta=['Market Need', 'Competitor Gap', 'CP Capability', 'Market Size'],
                fill='toself',
                fillcolor='rgba(46, 125, 50, 0.3)',
                line=dict(color='#2E7D32', width=2)
            ))
            
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                height=300,
                margin=dict(l=80, r=80, t=20, b=20)
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # Strategic Recommendations
    st.markdown("---")
    st.markdown("### Strategic Recommendations for CP Group")
    
    st.markdown("""
    <div class='insight-box'>
    <h4>Top 3 Entry Strategies</h4>
    
    <h5>1. Full Supply Chain Traceability (Score: 84/100)</h5>
    <ul>
    <li><strong>Why:</strong> Highest customer need (95%) and significant competitor gap (75%)</li>
    <li><strong>How:</strong> Leverage CP Group's integrated supply chain across 200+ subsidiaries</li>
    <li><strong>Advantage:</strong> From farm to table visibility - unique differentiator</li>
    <li><strong>Target:</strong> Pragmatic middle-class (45% of market)</li>
    </ul>
    
    <h5>2. Price-Quality Optimization Platform (Score: 83/100)</h5>
    <ul>
    <li><strong>Why:</strong> Addresses core pain point of balancing price and quality (90% need)</li>
    <li><strong>How:</strong> AI-powered recommendations showing quality-price balance scores</li>
    <li><strong>Advantage:</strong> Serves both quality-sensitive and price-sensitive segments</li>
    <li><strong>Market:</strong> 580B market with 22% CAGR</li>
    </ul>
    
    <h5>3. Organic & Low-Pesticide Product Line (Score: 80/100)</h5>
    <ul>
    <li><strong>Why:</strong> Massive competitor gap (90%) - neither Dingdong nor Freshippo have dedicated organic sections</li>
    <li><strong>How:</strong> Develop dedicated organic supply chain leveraging CP's agriculture network</li>
    <li><strong>Advantage:</strong> First-mover in dedicated organic grocery e-commerce</li>
    <li><strong>Premium:</strong> 23% of consumers willing to pay premium for sustainable products</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # City Entry Priority
    st.markdown("---")
    st.markdown("### City Entry Priority Ranking")
    
    city_data = {
        'City': ['Shanghai', 'Beijing', 'Hangzhou', 'Guangzhou', 'Shenzhen', 'Suzhou', 'Nanjing', 'Chengdu'],
        'Market Size': [0.95, 0.90, 0.75, 0.85, 0.80, 0.65, 0.70, 0.75],
        'Competition': [0.90, 0.85, 0.70, 0.80, 0.80, 0.60, 0.65, 0.70],
        'Infrastructure': [0.95, 0.90, 0.85, 0.85, 0.85, 0.80, 0.75, 0.70],
        'Target Segment': [0.90, 0.85, 0.80, 0.75, 0.75, 0.85, 0.80, 0.65]
    }
    
    df_cities = pd.DataFrame(city_data)
    df_cities['Priority Score'] = (
        df_cities['Market Size'] * 0.3 +
        (1 - df_cities['Competition']) * 0.2 +
        df_cities['Infrastructure'] * 0.25 +
        df_cities['Target Segment'] * 0.25
    )
    
    df_cities = df_cities.sort_values('Priority Score', ascending=False)
    
    fig = go.Figure(go.Bar(
        x=df_cities['Priority Score'],
        y=df_cities['City'],
        orientation='h',
        text=[f'{s*100:.1f}' for s in df_cities['Priority Score']],
        textposition='outside',
        marker_color='#2E7D32'
    ))
    
    fig.update_layout(
        title="City Entry Priority Scores",
        xaxis_title="Priority Score",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 1])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ROI Simulation
    st.markdown("---")
    st.markdown("### Market Entry Strategy Simulator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        entry_model = st.selectbox(
            "Business Model",
            ["Front Warehouse", "Store-Warehouse Integration", "Hybrid Model"]
        )
        
        initial_cities = st.slider("Initial City Coverage", 1, 5, 3)
        
        traceability_level = st.slider("Traceability Coverage", 0, 100, 80)
    
    with col2:
        organic_focus = st.slider("Organic Product Focus", 0, 100, 60)
        
        tech_investment = st.slider("AI/Tech Investment Level", 0, 100, 70)
        
        price_positioning = st.selectbox(
            "Price Positioning",
            ["Premium", "Mid-range", "Value"]
        )
    
    if st.button("Calculate Entry Strategy ROI", type="primary"):
        # Simple simulation
        base_score = 50
        
        if entry_model == "Hybrid Model":
            base_score += 15
        elif entry_model == "Store-Warehouse Integration":
            base_score += 10
        else:
            base_score += 5
        
        base_score += initial_cities * 3
        base_score += traceability_level * 0.2
        base_score += organic_focus * 0.15
        base_score += tech_investment * 0.1
        
        if price_positioning == "Mid-range":
            base_score += 10
        
        success_probability = min(base_score, 95)
        
        st.markdown("---")
        st.markdown("### Simulation Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Success Probability", f"{success_probability:.1f}%")
        with col2:
            est_market_share = success_probability * 0.08
            st.metric("Est. Market Share (Y3)", f"{est_market_share:.1f}%")
        with col3:
            est_revenue = est_market_share * market['market_size_2025_projected'] / 100
            st.metric("Est. Revenue (Y3)", f"¥{est_revenue/1e9:.2f}B")
        
        st.success(f"""
        **Recommendation:** This configuration shows {success_probability:.1f}% success probability.
        
        Key factors:
        - {entry_model} model provides operational flexibility
        - {traceability_level}% traceability coverage addresses major pain point
        - {organic_focus}% organic focus taps into underserved market
        - {initial_cities} cities allows manageable scaling
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem 0;'>
<p>CP Group Strategic Intelligence Dashboard | Data Updated: December 2024</p>
</div>
""", unsafe_allow_html=True)
