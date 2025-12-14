import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import random

st.set_page_config(
    page_title="Fresh Grocery Shopping",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .product-card {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: white;
    }
    .quality-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 5px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .quality-high {
        background-color: #C8E6C9;
        color: #1B5E20;
    }
    .quality-medium {
        background-color: #FFF9C4;
        color: #F57F17;
    }
    .price-tag {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2E7D32;
    }
    .trace-path {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    .ai-response {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2E7D32;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_type' not in st.session_state:
    st.session_state.user_type = 'Quality Priority'
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Header
st.title("Fresh Grocery Shopping Platform")

if st.sidebar.button("Return to Home"):
    st.switch_page("Home.py")

# User Preference Detection
st.sidebar.markdown("### Your Shopping Profile")
user_type = st.sidebar.radio(
    "Shopping Preference",
    ["Auto-detect", "Quality Priority", "Value Priority"],
    index=0 if st.session_state.user_type == 'Auto-detect' else 
          (1 if st.session_state.user_type == 'Quality Priority' else 2)
)
st.session_state.user_type = user_type

if user_type == "Quality Priority":
    st.sidebar.info("Focus: Food safety, quality stability, traceability")
elif user_type == "Value Priority":
    st.sidebar.info("Focus: Price stability, value for money, budget control")
else:
    st.sidebar.info("We'll recommend based on your browsing behavior")

# Initialize behavior tracking session state
if 'behavior_data' not in st.session_state:
    st.session_state.behavior_data = {
        'quality_clicks': 0,
        'price_clicks': 0,
        'trace_views': 0,
        'discount_views': 0,
        'organic_views': 0,
        'detected_type': None,
        'confidence': 0
    }

# Sample product data
products = [
    {
        'name': 'Organic Baby Spinach',
        'price': 18.9,
        'original_price': 22.9,
        'quality_score': 0.95,
        'stability_score': 0.92,
        'origin': 'Shandong Province, China',
        'certification': 'Organic Certification',
        'trace_completeness': 0.95,
        'category': 'Vegetables',
        'low_pesticide': True
    },
    {
        'name': 'Grass-Fed Australian Beef',
        'price': 89.9,
        'original_price': 98.0,
        'quality_score': 0.93,
        'stability_score': 0.90,
        'origin': 'Victoria, Australia',
        'certification': 'Antibiotic-Free, Quality Certified',
        'trace_completeness': 0.88,
        'category': 'Meat',
        'low_pesticide': False
    },
    {
        'name': 'Fresh Norwegian Salmon',
        'price': 68.0,
        'original_price': 68.0,
        'quality_score': 0.91,
        'stability_score': 0.88,
        'origin': 'Norway',
        'certification': 'MSC Certified',
        'trace_completeness': 0.90,
        'category': 'Seafood',
        'low_pesticide': False
    },
    {
        'name': 'Low-Pesticide Cherry Tomatoes',
        'price': 15.8,
        'original_price': 19.8,
        'quality_score': 0.89,
        'stability_score': 0.87,
        'origin': 'Shouguang, Shandong',
        'certification': 'Low-Pesticide Certified',
        'trace_completeness': 0.85,
        'category': 'Vegetables',
        'low_pesticide': True
    },
    {
        'name': 'Free-Range Eggs (10pcs)',
        'price': 25.9,
        'original_price': 28.9,
        'quality_score': 0.92,
        'stability_score': 0.93,
        'origin': 'Jiangsu Province',
        'certification': 'Free-Range Certified',
        'trace_completeness': 0.92,
        'category': 'Eggs & Dairy',
        'low_pesticide': False
    },
    {
        'name': 'Organic Brown Rice (2kg)',
        'price': 35.0,
        'original_price': 42.0,
        'quality_score': 0.90,
        'stability_score': 0.95,
        'origin': 'Heilongjiang',
        'certification': 'Organic Certification',
        'trace_completeness': 0.87,
        'category': 'Grains',
        'low_pesticide': True
    }
]

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Personalized Recommendations",
    "Traceability System",
    "Price-Quality Balance Tool",
    "AI Shopping Assistant",
    "🧪 Auto-Detect Demo"
])

# TAB 1: Personalized Recommendations
with tab1:
    st.markdown("### Recommended for You")
    
    # Filter based on user type
    if user_type == "Quality Priority":
        recommended = sorted(products, key=lambda x: x['quality_score'], reverse=True)[:4]
    elif user_type == "Value Priority":
        recommended = sorted(products, key=lambda x: (x['original_price'] - x['price'])/x['original_price'], reverse=True)[:4]
    else:
        recommended = products[:4]
    
    # Display products
    for product in recommended:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class='product-card'>
            <h4>{product['name']}</h4>
            <p>Origin: {product['origin']}</p>
            <p><span class='quality-badge quality-high'>Quality: {product['quality_score']*100:.0f}%</span>
               <span class='quality-badge quality-high'>Stability: {product['stability_score']*100:.0f}%</span></p>
            <p>{product['certification']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if product['original_price'] > product['price']:
                st.markdown(f"<p style='text-decoration: line-through; color: #999;'>¥{product['original_price']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='price-tag'>¥{product['price']}</p>", unsafe_allow_html=True)
            
            if st.button(f"Add to Cart", key=f"cart_{product['name']}"):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")
    
    # Quick Replenishment
    st.markdown("---")
    st.markdown("### Quick Replenishment")
    st.caption("Based on your purchase history")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='product-card'>
        <h5>Organic Milk (1L)</h5>
        <p class='price-tag'>¥16.8</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Reorder", key="reorder1")
    
    with col2:
        st.markdown("""
        <div class='product-card'>
        <h5>Lettuce (1pc)</h5>
        <p class='price-tag'>¥8.9</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Reorder", key="reorder2")
    
    with col3:
        st.markdown("""
        <div class='product-card'>
        <h5>Fresh Tofu</h5>
        <p class='price-tag'>¥5.8</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Reorder", key="reorder3")

# TAB 2: Traceability System
with tab2:
    st.markdown("### Product Traceability System")
    
    selected_product = st.selectbox(
        "Select a product to view full traceability",
        [p['name'] for p in products]
    )
    
    product = next(p for p in products if p['name'] == selected_product)
    
    # Traceability Completeness Score
    st.markdown(f"""
    <div style='text-align: center; padding: 2rem; background-color: #E8F5E9; border-radius: 10px;'>
    <h2>Traceability Completeness</h2>
    <h1 style='color: #2E7D32; font-size: 4rem;'>{product['trace_completeness']*100:.0f}%</h1>
    <p>All supply chain stages documented and verified</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Supply Chain Visualization
    st.markdown("### Supply Chain Journey")
    
    stages = [
        {
            'stage': 'Origin',
            'location': product['origin'],
            'date': '2024-12-01',
            'status': 'Verified',
            'details': 'Farm/Producer certified and inspected'
        },
        {
            'stage': 'Processing',
            'location': 'Central Processing Facility',
            'date': '2024-12-02',
            'status': 'Verified',
            'details': 'Quality control and packaging completed'
        },
        {
            'stage': 'Cold Chain Transport',
            'location': 'Regional Distribution Center',
            'date': '2024-12-03',
            'status': 'Verified',
            'details': 'Temperature maintained at 2-4°C'
        },
        {
            'stage': 'Final Mile',
            'Responsibility': 'Includes photos taken before and after delivery',
            'location': 'Local Warehouse',
            'date': '2024-12-05',
            'status': 'Ready for Delivery',
            'details': 'Available for immediate delivery'
        }
    ]
    
    for i, stage in enumerate(stages):
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"**Step {i+1}**")
            st.markdown(f"<span class='quality-badge quality-high'>{stage['status']}</span>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='trace-path'>
            <h4>{stage['stage']}</h4>
            <p><strong>Location:</strong> {stage['location']}</p>
            <p><strong>Date:</strong> {stage['date']}</p>
            <p>{stage['details']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Certificates
    st.markdown("---")
    st.markdown("### Certifications & Test Reports")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #F5F5F5; padding: 1rem; border-radius: 5px; text-align: center;'>
        <h4>Origin Certificate</h4>
        <p>Verified</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #F5F5F5; padding: 1rem; border-radius: 5px; text-align: center;'>
        <h4>Quality Test Report</h4>
        <p>Passed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background-color: #F5F5F5; padding: 1rem; border-radius: 5px; text-align: center;'>
        <h4>{product['certification']}</h4>
        <p>Valid</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk Assessment
    if product['category'] in ['Meat', 'Seafood']:
        st.markdown("---")
        st.warning("""
        **Risk Category Alert:** This product category requires extra attention to cold chain management.
        Our system monitors temperature throughout the supply chain to ensure safety.
        """)

# TAB 3: Price-Quality Balance Tool
with tab3:
    st.markdown("### Price-Quality Balance Analysis")
    
    st.info("""
    This tool helps you make informed decisions by showing the relationship between price and quality.
    Find products that offer the best value for your priorities.
    """)
    
    # Interactive filter
    col1, col2 = st.columns(2)
    
    with col1:
        max_price = st.slider("Maximum Price (CNY)", 0, 100, 50)
    
    with col2:
        min_quality = st.slider("Minimum Quality Score", 0, 100, 80)
    
    # Filter products
    filtered = [p for p in products if p['price'] <= max_price and p['quality_score']*100 >= min_quality]
    
    if filtered:
        # Price-Quality Scatter Plot
        fig = go.Figure()
        
        for product in filtered:
            fig.add_trace(go.Scatter(
                x=[product['price']],
                y=[product['quality_score']*100],
                mode='markers+text',
                name=product['name'],
                text=[product['name']],
                textposition='top center',
                marker=dict(
                    size=15,
                    color='#2E7D32' if product['low_pesticide'] else '#1565C0',
                    line=dict(width=2, color='white')
                ),
                hovertemplate=f"<b>{product['name']}</b><br>" +
                             f"Price: ¥{product['price']}<br>" +
                             f"Quality: {product['quality_score']*100:.0f}%<br>" +
                             f"Value Score: {(product['quality_score']*100/product['price']):.1f}<extra></extra>"
            ))
        
        fig.update_layout(
            title="Price vs Quality Balance",
            xaxis_title="Price (CNY)",
            yaxis_title="Quality Score (%)",
            height=500,
            showlegend=False,
            yaxis=dict(range=[min_quality-5, 100])
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Value Rankings
        st.markdown("---")
        st.markdown("### Best Value Products")
        
        filtered_sorted = sorted(filtered, key=lambda x: x['quality_score']/x['price'], reverse=True)
        
        for i, product in enumerate(filtered_sorted[:3]):
            value_score = (product['quality_score']*100 / product['price']) * 10
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"**#{i+1} {product['name']}**")
                st.caption(f"{product['origin']}")
            
            with col2:
                st.metric("Price", f"¥{product['price']}")
            
            with col3:
                st.metric("Value Score", f"{value_score:.1f}/10")
    
    else:
        st.warning("No products match your criteria. Try adjusting the filters.")
    
    # Price Stability Promise
    st.markdown("---")
    st.markdown("""
    <div class='insight-box'>
    <h4>Price Stability Guarantee</h4>
    <p>We monitor market prices and commit to:</p>
    <ul>
    <li>No sudden price increases without 48-hour notice</li>
    <li>Price matching for equivalent quality products</li>
    <li>Transparent pricing with breakdown available</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# TAB 4: AI Shopping Assistant
with tab4:
    st.markdown("### AI Shopping Assistant")
    
    st.markdown("""
    Ask me anything about:
    - Product recommendations
    - Nutrition advice
    - Recipe suggestions
    - Food safety questions
    - Seasonal produce
    """)
    
    # Chat interface
    user_input = st.text_input("Your question:", placeholder="e.g., What vegetables are good for winter?")
    
    if st.button("Ask", type="primary"):
        if user_input:
            # Add to chat history
            st.session_state.chat_history.append({
                'user': user_input,
                'timestamp': datetime.now().strftime("%H:%M")
            })
            
            # Generate response based on input
            response = ""
            
            if "recommend" in user_input.lower() or "suggest" in user_input.lower():
                response = f"""Based on your preferences for {st.session_state.user_type.lower()}, I recommend:

1. **Organic Baby Spinach** - High in iron and vitamins, perfect for winter nutrition
2. **Fresh Norwegian Salmon** - Rich in Omega-3, supports immune system
3. **Free-Range Eggs** - Complete protein source with excellent quality stability

All products have full traceability and meet our quality standards."""
            
            elif "winter" in user_input.lower() or "seasonal" in user_input.lower():
                response = """Great question! Winter vegetables that are currently in season include:

- **Root Vegetables**: Carrots, turnips, and radishes (high vitamin content)
- **Leafy Greens**: Spinach, bok choy, and kale (cold-weather resilient)
- **Squash Family**: Pumpkin and butternut squash (stored well)

These are at their peak freshness and nutritional value. Would you like recipe suggestions?"""
            
            elif "safe" in user_input.lower() or "safety" in user_input.lower():
                response = """Food safety is our top priority! Here's what we do:

1. **Traceability**: 85-95% supply chain visibility
2. **Testing**: Regular pesticide and quality testing
3. **Cold Chain**: Temperature monitored throughout
4. **Certification**: All products have origin certificates

You can view detailed traceability for any product in the Traceability System tab."""
            
            elif "organic" in user_input.lower():
                response = """We have a dedicated organic product line:

- All organic products certified by national standards
- Lower pesticide residues (tested and verified)
- Sustainable farming practices
- Premium but fair pricing

Currently 60% of our customers choose organic options for their families."""
            
            else:
                response = f"""I'd be happy to help with that! Here are some insights:

Based on your question about "{user_input}", I recommend checking our product catalog. 
We have {len(products)} fresh products available today, all with quality scores above 85%.

Would you like specific recommendations based on:
- Nutritional needs
- Budget constraints
- Dietary restrictions
- Cooking preferences"""
            
            st.session_state.chat_history[-1]['assistant'] = response
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### Conversation History")
        
        for i, chat in enumerate(reversed(st.session_state.chat_history[-5:])):
            st.markdown(f"**You ({chat['timestamp']}):** {chat['user']}")
            if 'assistant' in chat:
                st.markdown(f"""
                <div class='ai-response'>
                <strong>AI Assistant:</strong><br>
                {chat['assistant']}
                </div>
                """, unsafe_allow_html=True)
            st.markdown("---")
    
    # Daily Knowledge Tip
    st.markdown("### Daily Nutrition Tip")
    
    tips = [
        "Did you know? Organic spinach has 30% more iron than conventional spinach.",
        "Winter tip: Root vegetables like carrots become sweeter after the first frost.",
        "Food safety: Always store raw meat on the bottom shelf to prevent cross-contamination.",
        "Nutrition fact: Wild-caught salmon has more Omega-3 than farm-raised.",
        "Storage tip: Keep tomatoes at room temperature for better flavor and texture."
    ]
    
    today_tip = tips[datetime.now().day % len(tips)]
    
    st.info(today_tip)

# TAB 5: Auto-Detect Demo
with tab5:
    st.markdown("### 🧪 Auto-Detect User Preference Demo")
    
    st.markdown("""
    <div style='background-color: #E3F2FD; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
    <h4>🎯 How Auto-Detection Works</h4>
    <p>Our AI system analyzes your browsing behavior in real-time to understand your shopping priorities.
    Try the interactive simulation below to see how we detect whether you're a <b>Quality Priority</b> or <b>Value Priority</b> shopper!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Reset behavior button
    if st.button("🔄 Reset Behavior Data", key="reset_behavior"):
        st.session_state.behavior_data = {
            'quality_clicks': 0,
            'price_clicks': 0,
            'trace_views': 0,
            'discount_views': 0,
            'organic_views': 0,
            'detected_type': None,
            'confidence': 0
        }
        st.rerun()
    
    st.markdown("---")
    
    # Interactive Behavior Simulation
    st.markdown("### 📊 Simulate Your Browsing Behavior")
    st.markdown("Click the buttons below to simulate different browsing behaviors:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: #E8F5E9; padding: 1rem; border-radius: 10px;'>
        <h4 style='color: #1B5E20;'>🌿 Quality-Related Actions</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("👆 Click on Quality Score", key="demo_quality_click"):
            st.session_state.behavior_data['quality_clicks'] += 1
            st.toast("Recorded: Quality score click")
        
        if st.button("🔍 View Traceability Info", key="demo_trace_view"):
            st.session_state.behavior_data['trace_views'] += 1
            st.toast("Recorded: Traceability view")
        
        if st.button("🥬 Browse Organic Products", key="demo_organic_view"):
            st.session_state.behavior_data['organic_views'] += 1
            st.toast("Recorded: Organic product view")
        
        if st.button("📋 Check Certifications", key="demo_cert_click"):
            st.session_state.behavior_data['quality_clicks'] += 1
            st.session_state.behavior_data['trace_views'] += 1
            st.toast("Recorded: Certification check")
    
    with col2:
        st.markdown("""
        <div style='background-color: #FFF3E0; padding: 1rem; border-radius: 10px;'>
        <h4 style='color: #E65100;'>💰 Value-Related Actions</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("👆 Click on Price Tag", key="demo_price_click"):
            st.session_state.behavior_data['price_clicks'] += 1
            st.toast("Recorded: Price click")
        
        if st.button("🏷️ View Discount Offers", key="demo_discount_view"):
            st.session_state.behavior_data['discount_views'] += 1
            st.toast("Recorded: Discount view")
        
        if st.button("📉 Sort by Price (Low to High)", key="demo_sort_price"):
            st.session_state.behavior_data['price_clicks'] += 2
            st.toast("Recorded: Price sorting")
        
        if st.button("🛒 Add Sale Item to Cart", key="demo_sale_add"):
            st.session_state.behavior_data['price_clicks'] += 1
            st.session_state.behavior_data['discount_views'] += 1
            st.toast("Recorded: Sale item added")
    
    st.markdown("---")
    
    # Detection Algorithm Visualization
    st.markdown("### 🤖 Detection Algorithm (Real-time)")
    
    # Calculate scores
    quality_score = (
        st.session_state.behavior_data['quality_clicks'] * 2 +
        st.session_state.behavior_data['trace_views'] * 3 +
        st.session_state.behavior_data['organic_views'] * 2.5
    )
    
    value_score = (
        st.session_state.behavior_data['price_clicks'] * 2 +
        st.session_state.behavior_data['discount_views'] * 3
    )
    
    total_score = quality_score + value_score
    
    # Show algorithm code
    with st.expander("📝 View Detection Algorithm Code", expanded=True):
        st.code('''
def detect_user_preference(behavior_data):
    """
    Auto-detect user preference based on browsing behavior.
    
    Weights:
    - Quality indicators: quality_clicks(2x), trace_views(3x), organic_views(2.5x)
    - Value indicators: price_clicks(2x), discount_views(3x)
    """
    
    # Calculate weighted scores
    quality_score = (
        behavior_data['quality_clicks'] * 2.0 +
        behavior_data['trace_views'] * 3.0 +
        behavior_data['organic_views'] * 2.5
    )
    
    value_score = (
        behavior_data['price_clicks'] * 2.0 +
        behavior_data['discount_views'] * 3.0
    )
    
    total_score = quality_score + value_score
    
    # Determine preference type
    if total_score == 0:
        return {
            'type': 'Undetermined',
            'confidence': 0,
            'message': 'Not enough data. Keep browsing!'
        }
    
    # Calculate confidence (difference between scores / total)
    confidence = abs(quality_score - value_score) / total_score * 100
    
    if quality_score > value_score:
        preference_type = 'Quality Priority'
        primary_score = quality_score
    else:
        preference_type = 'Value Priority'
        primary_score = value_score
    
    # Minimum threshold for confident detection
    min_actions = 3
    total_actions = sum(behavior_data.values())
    
    if total_actions < min_actions:
        confidence = confidence * (total_actions / min_actions)
    
    return {
        'type': preference_type,
        'confidence': min(confidence, 95),  # Cap at 95%
        'quality_score': quality_score,
        'value_score': value_score,
        'recommendation': get_personalized_recommendation(preference_type)
    }

def get_personalized_recommendation(preference_type):
    """Generate personalized product recommendations"""
    if preference_type == 'Quality Priority':
        return {
            'sort_by': 'quality_score',
            'highlight': ['certification', 'traceability', 'organic'],
            'filters': {'min_quality': 0.9}
        }
    else:
        return {
            'sort_by': 'discount_percent',
            'highlight': ['price', 'savings', 'value_score'],
            'filters': {'max_price': 50}
        }
''', language='python')
    
    st.markdown("---")
    
    # Real-time Detection Results
    st.markdown("### 📈 Detection Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Quality Score", 
            f"{quality_score:.1f}",
            delta=f"+{st.session_state.behavior_data['quality_clicks'] + st.session_state.behavior_data['trace_views'] + st.session_state.behavior_data['organic_views']} actions"
        )
    
    with col2:
        st.metric(
            "Value Score", 
            f"{value_score:.1f}",
            delta=f"+{st.session_state.behavior_data['price_clicks'] + st.session_state.behavior_data['discount_views']} actions"
        )
    
    with col3:
        if total_score > 0:
            confidence = abs(quality_score - value_score) / total_score * 100
            confidence = min(confidence, 95)
        else:
            confidence = 0
        st.metric("Confidence", f"{confidence:.0f}%")
    
    # Visualization - Score Comparison Bar
    if total_score > 0:
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=['Quality Priority', 'Value Priority'],
            y=[quality_score, value_score],
            marker_color=['#2E7D32', '#E65100'],
            text=[f'{quality_score:.1f}', f'{value_score:.1f}'],
            textposition='outside'
        ))
        
        fig.update_layout(
            title="Behavior Score Comparison",
            yaxis_title="Weighted Score",
            height=300,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Detection Result Display
    st.markdown("### 🎯 Detected User Type")
    
    if total_score == 0:
        st.warning("""
        **Status: Collecting Data...**
        
        We haven't detected enough browsing behavior yet. Try clicking on some of the action buttons above to simulate your shopping behavior!
        """)
    elif total_score > 0 and confidence < 30:
        st.info(f"""
        **Status: Still Learning...**
        
        Current tendency: {"Quality Priority" if quality_score > value_score else "Value Priority"}
        
        Confidence is still low ({confidence:.0f}%). We need more browsing data to make a confident prediction.
        Keep interacting with the simulation!
        """)
    else:
        detected_type = "Quality Priority" if quality_score > value_score else "Value Priority"
        
        if detected_type == "Quality Priority":
            st.success(f"""
            **🌿 Detected: Quality Priority Shopper**
            
            Confidence: {confidence:.0f}%
            
            **Based on your behavior, we've identified that you prioritize:**
            - Food safety and quality assurance
            - Full supply chain traceability
            - Organic and certified products
            - Quality stability over price fluctuations
            
            **Personalized Experience Activated:**
            - Products sorted by quality score
            - Quality badges and certifications highlighted
            - Traceability information prominently displayed
            - Organic products recommended first
            """)
        else:
            st.success(f"""
            **💰 Detected: Value Priority Shopper**
            
            Confidence: {confidence:.0f}%
            
            **Based on your behavior, we've identified that you prioritize:**
            - Competitive pricing and good deals
            - Discount offers and promotions
            - Value for money ratio
            - Budget-conscious shopping
            
            **Personalized Experience Activated:**
            - Products sorted by discount percentage
            - Price tags and savings highlighted
            - Best value recommendations shown first
            - Price alerts for favorite products
            """)
    
    # Behavior Data Summary
    st.markdown("---")
    st.markdown("### 📋 Behavior Data Log")
    
    behavior_df_data = {
        'Behavior Type': [
            'Quality Score Clicks',
            'Traceability Views', 
            'Organic Product Views',
            'Price Clicks',
            'Discount Views'
        ],
        'Count': [
            int(st.session_state.behavior_data['quality_clicks']),
            int(st.session_state.behavior_data['trace_views']),
            int(st.session_state.behavior_data['organic_views']),
            int(st.session_state.behavior_data['price_clicks']),
            int(st.session_state.behavior_data['discount_views'])
        ],
        'Weight': ['2.0', '3.0', '2.5', '2.0', '3.0'],
        'Category': ['Quality', 'Quality', 'Quality', 'Value', 'Value']
    }
    
    behavior_df = pd.DataFrame(behavior_df_data)
    # Calculate weighted score as string to avoid type issues
    weighted_scores = [
        float(behavior_df_data['Count'][i]) * float(behavior_df_data['Weight'][i]) 
        for i in range(5)
    ]
    behavior_df['Weighted Score'] = [f"{s:.1f}" for s in weighted_scores]
    
    st.dataframe(behavior_df, use_container_width=True, hide_index=True)
    
    # Technical Implementation Note
    st.markdown("---")
    with st.expander("🔧 Technical Implementation Details"):
        st.markdown("""
        ### How This Would Work in Production
        
        **1. Data Collection Points:**
        - Click events on product cards (quality badges, price tags, etc.)
        - Time spent viewing traceability information
        - Filter and sort preferences
        - Cart additions and purchase history
        - Search queries analysis
        
        **2. Machine Learning Model:**
        ```python
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import StandardScaler
        
        class UserPreferenceDetector:
            def __init__(self):
                self.model = RandomForestClassifier(n_estimators=100)
                self.scaler = StandardScaler()
            
            def extract_features(self, user_session):
                return {
                    'quality_click_ratio': user_session.quality_clicks / max(user_session.total_clicks, 1),
                    'trace_view_time_pct': user_session.trace_view_time / max(user_session.total_time, 1),
                    'organic_browse_ratio': user_session.organic_views / max(user_session.total_views, 1),
                    'price_sort_count': user_session.price_sort_events,
                    'discount_click_ratio': user_session.discount_clicks / max(user_session.total_clicks, 1),
                    'avg_cart_item_price': user_session.avg_cart_price,
                    'cart_discount_items_pct': user_session.discount_items / max(user_session.cart_size, 1)
                }
            
            def predict(self, features):
                scaled_features = self.scaler.transform([features])
                prediction = self.model.predict(scaled_features)
                confidence = max(self.model.predict_proba(scaled_features)[0])
                return prediction[0], confidence
        ```
        
        **3. Real-time Updates:**
        - Behavior tracked via event stream (Kafka/Redis)
        - Model inference at edge for low latency
        - A/B testing for recommendation strategies
        - Continuous model retraining with new data
        
        **4. Privacy Considerations:**
        - All behavior data anonymized
        - User consent for personalization
        - Option to reset preferences
        - Transparent algorithm explanation
        """)

# Shopping Cart in Sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### Shopping Cart")
    
    if st.session_state.cart:
        total = sum(item['price'] for item in st.session_state.cart)
        
        for item in st.session_state.cart:
            st.markdown(f"- {item['name']}: ¥{item['price']}")
        
        st.markdown(f"**Total: ¥{total:.2f}**")
        
        if st.button("Proceed to Checkout", type="primary"):
            st.success("Order placed successfully!")
            st.session_state.cart = []
    else:
        st.caption("Your cart is empty")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem 0;'>
<p>Fresh Grocery Shopping Platform | Safe, Transparent, Quality Assured</p>
<p>Delivery within 30 minutes | 100% Traceability | Quality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
