import streamlit as st

st.set_page_config(
    page_title="CP Group - Grocery Platform Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        color: #2E7D32;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .project-info {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
    .stButton > button {
        height: 80px;
        font-size: 18px;
        font-weight: 600;
    }
    .feature-list {
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>AI-DRIVEN MARKET OPPORTUNITY ANALYSIS</h1>", unsafe_allow_html=True)
# st.markdown("<h3 class='sub-header'>Freshippo, Dingdong, Metro, and Aldi Analysis</h3>", unsafe_allow_html=True)

st.markdown("---")

# Project Overview
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("""
    <div class='project-info'>
    <h3 style='text-align: center; margin-bottom: 1rem;'>Project Overview</h3>
    <p style='font-size: 16px; line-height: 1.6;'>
    To identify and compare market opportunities for leading online and offline grocery platforms using AI tools.
    </p>
    <p style='font-size: 16px; line-height: 1.6;'>
    <strong>CP Group (Charoen Pokphand Group)</strong> - One of the world's largest conglomerates, 
    operating over 200 subsidiaries across animal feed, livestock, agriculture, supermarkets, and e-commerce in China. 
    With strong local partnerships and integrated supply chains, CP Group plays a key role in China's food security 
    and agribusiness innovation.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Entry Points
st.markdown("<h2 style='text-align: center; margin: 2rem 0;'>Select Your Entry Point</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='text-align: center; margin-bottom: 1rem;'>
    <h3>CP Dashboard</h3>
    <p>Strategic insights and competitor intelligence for decision makers</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-list'>
    <ul>
    <li>Interactive Competitor Intelligence</li>
    <li>Market Analysis & Trends</li>
    <li>Customer Insights</li>
    <li>Opportunity Engine</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Enter CP Dashboard", use_container_width=True, type="primary", key="cp"):
        st.switch_page("pages/1_CP_Dashboard.py")

with col2:
    st.markdown("""
    <div style='text-align: center; margin-bottom: 1rem;'>
    <h3>Consumer Application</h3>
    <p>User-centered shopping experience with AI-powered features</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-list'>
    <ul>
    <li>Personalized Recommendations</li>
    <li>Product Traceability System</li>
    <li>Price-Quality Balance Tool</li>
    <li>AI Shopping Assistant</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Enter Consumer App", use_container_width=True, type="primary", key="consumer"):
        st.switch_page("pages/2_Consumer_App.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
<p>ENT302TC - Cutting-edge Practice in Innovation and Entrepreneurship</p>
<p>XJTLU Entrepreneur College (Taicang)</p>
</div>
""", unsafe_allow_html=True)
