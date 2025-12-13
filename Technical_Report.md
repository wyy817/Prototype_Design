# Technical Report: AI-Driven Grocery Platform Prototype

## CP Group Market Opportunity Analysis System

**Course:** ENT302TC - Cutting-edge Practice in Innovation and Entrepreneurship  
**Institution:** XJTLU Entrepreneur College (Taicang)  
**Report Date:** December 2024

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Overview](#2-project-overview)
3. [System Architecture](#3-system-architecture)
4. [Technology Stack](#4-technology-stack)
5. [Part A: CP Dashboard (B2B)](#5-part-a-cp-dashboard-b2b)
6. [Part B: Consumer Application (B2C)](#6-part-b-consumer-application-b2c)
7. [Data Architecture](#7-data-architecture)
8. [User Interface Design](#8-user-interface-design)
9. [Key Features Implementation](#9-key-features-implementation)
10. [Future Development Recommendations](#10-future-development-recommendations)
11. [Conclusion](#11-conclusion)

---

## 1. Executive Summary

This technical report documents the design and implementation of an AI-driven market opportunity analysis prototype for CP Group (Charoen Pokphand Group). The system consists of two main components:

1. **CP Dashboard (B2B)**: A strategic intelligence platform providing competitor analysis, market insights, customer segmentation, and opportunity scoring for business decision-makers.

2. **Consumer Application (B2C)**: A user-centered shopping platform featuring personalized recommendations, full supply chain traceability, price-quality balance tools, and an AI shopping assistant.

The prototype addresses a ¥580 billion Chinese fresh e-commerce market growing at 22% CAGR, targeting the pragmatic middle-class segment (45% of the market) who seek quality-assured, traceable, and reasonably-priced fresh food products.

---

## 2. Project Overview

### 2.1 Background

CP Group (Charoen Pokphand Group) is one of the world's largest conglomerates, operating over 200 subsidiaries across animal feed, livestock, agriculture, supermarkets, and e-commerce in China. The company seeks to identify and compare market opportunities for leading online and offline grocery platforms using AI-driven analysis tools.

### 2.2 Objectives

- Identify market gaps and opportunities in China's fresh e-commerce sector
- Analyze key competitors (Dingdong Maicai and Freshippo)
- Understand customer segments and their pain points
- Develop a prototype demonstrating potential market entry strategies
- Create a consumer-facing application showcasing differentiated features

### 2.3 Scope

The prototype focuses on:
- **Competitors Analyzed**: Dingdong Maicai, Freshippo (Hema Fresh)
- **Market Coverage**: Tier 1 and New Tier 1 cities in China
- **Primary Target Segment**: Pragmatic Middle-Class Families (28-45 years, ¥150,000-300,000 income)

---

## 3. System Architecture

### 3.1 Overall Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface Layer                      │
├─────────────────────────────────┬───────────────────────────────┤
│        Home.py (Landing Page)   │                               │
├─────────────────────────────────┼───────────────────────────────┤
│    CP Dashboard (B2B)           │    Consumer App (B2C)         │
│    - Overview                   │    - Personalized Recs        │
│    - Competitor Intelligence    │    - Traceability System      │
│    - Market Analysis            │    - Price-Quality Tool       │
│    - Customer Insights          │    - AI Shopping Assistant    │
│    - Opportunity Engine         │    - Auto-Detect Demo         │
├─────────────────────────────────┴───────────────────────────────┤
│                      Data Loading Layer                          │
│                      (utils/data_loader.py)                      │
├─────────────────────────────────────────────────────────────────┤
│                        Data Storage Layer                        │
│  ┌─────────────┬─────────────┬─────────────┬─────────────────┐  │
│  │competitors  │ market_data │ customer    │ dingdong        │  │
│  │  .json      │   .json     │ segments    │ financials      │  │
│  │             │             │   .json     │   .json         │  │
│  └─────────────┴─────────────┴─────────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 File Structure

```
Prototype_Design-main/
├── Home.py                       # Landing page & navigation
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version specification
├── data/
│   ├── competitors.json          # Competitor analysis data
│   ├── market_data.json          # Market research data
│   ├── customer_segments.json    # Customer segmentation data
│   └── dingdong_financials.json  # Financial performance data
├── pages/
│   ├── 1_CP_Dashboard.py         # B2B strategic dashboard
│   └── 2_Consumer_App.py         # B2C consumer application
└── utils/
    ├── __init__.py               # Package initializer
    └── data_loader.py            # Data loading utilities
```

### 3.3 Navigation Flow

```
                     ┌──────────────┐
                     │   Home.py    │
                     │ (Landing)    │
                     └──────┬───────┘
                            │
           ┌────────────────┴────────────────┐
           │                                 │
           ▼                                 ▼
┌─────────────────────┐         ┌─────────────────────┐
│   CP Dashboard      │         │   Consumer App      │
│   (B2B Entry)       │         │   (B2C Entry)       │
├─────────────────────┤         ├─────────────────────┤
│ • Overview          │         │ • Personalized Recs │
│ • Competitor Intel  │         │ • Traceability      │
│ • Market Analysis   │         │ • Price-Quality     │
│ • Customer Insights │         │ • AI Assistant      │
│ • Opportunity Engine│         │ • Auto-Detect Demo  │
└─────────────────────┘         └─────────────────────┘
```

---

## 4. Technology Stack

### 4.1 Core Technologies

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| Frontend Framework | Streamlit | 1.52.1 | Web application framework |
| Data Visualization | Plotly | 5.18.0 | Interactive charts and graphs |
| Data Processing | Pandas | 2.1.4 | Data manipulation and analysis |
| Numerical Computing | NumPy | 1.26.2 | Numerical operations |
| Runtime | Python | 3.10 | Programming language |

### 4.2 Key Library Features Used

**Streamlit Features:**
- Multi-page application support (`st.switch_page()`)
- Session state management for cart and user preferences
- Custom CSS styling with `st.markdown(unsafe_allow_html=True)`
- Interactive widgets (sliders, selectboxes, buttons, tabs)
- Layout components (columns, expanders, containers)

**Plotly Features:**
- Pie charts for product and segment distribution
- Bar charts for comparisons and rankings
- Line charts for financial trend analysis
- Scatter plots for price-quality visualization
- Radar/Spider charts for multi-dimensional analysis
- Interactive hover effects and annotations

### 4.3 Data Format

All data is stored in JSON format, allowing:
- Easy modification without code changes
- Clear separation of concerns
- Simple integration with external data sources
- Human-readable data storage

---

## 5. Part A: CP Dashboard (B2B)

### 5.1 Module Overview

The CP Dashboard is designed for business decision-makers and strategic planners. It provides five main modules accessible via sidebar navigation.

### 5.2 Module 1: Overview

**Purpose:** Executive summary providing key metrics at a glance.

**Key Metrics Displayed:**
| Metric | Value | Description |
|--------|-------|-------------|
| Market Size (2024) | ¥580B | Total Chinese fresh e-commerce market |
| Target Segment | 45% | Pragmatic middle-class market share |
| Tier 1 Penetration | 45% | Instant retail penetration rate |
| Key Competitors | 2 | Dingdong & Freshippo |

**Implementation Details:**
```python
# Key metrics display using Streamlit columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        "Market Size (2024)",
        f"¥{market['market_size_2024']/1e9:.1f}B",
        f"+{market['growth_rate_cagr']*100:.0f}% CAGR"
    )
```

**Features:**
- Quick competitor comparison table
- Market opportunity highlights
- Competitive gaps identification
- Visual insight boxes for key findings

### 5.3 Module 2: Competitor Intelligence

**Purpose:** In-depth analysis of key competitors with SWOT analysis and financial performance tracking.

**Competitors Analyzed:**

| Feature | Dingdong Maicai | Freshippo (Hema Fresh) |
|---------|-----------------|------------------------|
| Model | Front Warehouse | Store-Warehouse Integration |
| SKU Count | 2,800 | 3,500 |
| Cities | 6 (YRD Focus) | 10+ (Tier 1+2) |
| Traceability | 25% | 30% |
| Fulfillment Cost | ¥87.2M | ¥82M |

**Key Features:**
1. **Side-by-Side Comparison View**
   - Business model comparison
   - SWOT analysis visualization
   - Strengths displayed in green
   - Weaknesses displayed in red

2. **Financial Performance Tracking (Dingdong)**
   - Quarterly profit/loss trend (2021-2024)
   - Break-even line visualization
   - Interactive line chart with color-coded markers
   - Key insight: Dingdong achieved profitability in Q1 2024

3. **Product Portfolio Comparison**
   - Donut charts showing category distribution
   - Dingdong: 40% fresh produce, 25% meat/seafood
   - Freshippo: 35% fresh produce, 30% meat/seafood

4. **Technology Capability Comparison**
   - Grouped bar chart comparing:
     - AI Integration
     - Traceability
     - Membership System
     - Omnichannel presence
     - Supply Chain Digitization

**Implementation Highlight - Financial Chart:**
```python
fig = go.Figure()
colors = ['red' if x < 0 else 'green' for x in df_fin['net_loss_m']]
fig.add_trace(go.Scatter(
    x=df_fin['period'],
    y=df_fin['net_loss_m'],
    mode='lines+markers',
    line=dict(color='#2E7D32', width=3),
    marker=dict(size=8, color=colors)
))
fig.add_hline(y=0, line_dash="dash", annotation_text="Break-even")
```

### 5.4 Module 3: Market Analysis

**Purpose:** Industry trends, market sizing, and pain point analysis.

**Key Visualizations:**

1. **Market Size Growth Chart**
   - Bar chart showing 2023-2025 trajectory
   - 2023: ¥520B → 2024: ¥580B → 2025 (projected): ¥707.6B
   - CAGR: 22%

2. **City Tier Penetration Analysis**
   - Horizontal bar chart by tier
   - Tier 1: 45% | New Tier 1: 38% | Tier 2: 28% | Tier 3: 12%

3. **Consumer Segmentation**
   - Pie chart showing segment distribution
   - Quality-sensitive: 35%
   - Price-sensitive: 40%
   - Balanced/pragmatic: 25%

4. **Industry Pain Points Severity Analysis**
   - Horizontal bar chart with severity scoring
   - Color-coded by severity level
   - Top pain points:
     - Food safety concerns: 90%
     - Quality inconsistency: 85%
     - Lack of transparency: 82%

5. **Industry Health Index (Radar Chart)**
   - Multi-dimensional assessment including:
     - Market Growth: 85%
     - Profitability: 45%
     - Technology Adoption: 65%
     - Supply Chain Maturity: 58%
     - Customer Satisfaction: 62%
     - Competitive Intensity: 75%

### 5.5 Module 4: Customer Insights

**Purpose:** Deep-dive into customer segmentation using Jobs-to-Be-Done (JTBD) framework.

**Primary Segment Focus: Pragmatic Middle-Class Families (45%)**

**Segment Profile:**
| Attribute | Value |
|-----------|-------|
| Income Range | ¥150,000-300,000 |
| Age Range | 28-45 years |
| Household Size | 3-4 members |
| Cities | Tier 1, New Tier 1 |

**JTBD Analysis:**
```
Core Job: "Obtain safe, healthy, quality-stable fresh food at reasonable 
prices with minimal shopping time and decision effort, enabling the family 
to maintain a dignified, healthy, and cost-effective lifestyle"
```

**Functional Jobs:**
- Obtain safe, healthy, quality-stable fresh food at reasonable prices
- Simplify decision-making process and reduce selection time
- Meet continuous healthy dietary needs

**Emotional Jobs:**
- Reduce anxiety about food safety and quality fluctuations
- Gain easy, fast, and worry-free shopping experience
- Enhance sense of control over diet and life

**Social Jobs:**
- Fulfill family role by ensuring reliable food quality
- Maintain dignity and quality of family life
- Express rational consumption values socially

**Pain Points Analysis (Tabbed Interface):**

| Category | Pain Point | Severity | Frequency |
|----------|-----------|----------|-----------|
| Functional | Quality instability & lack of transparency | 90% | Very High |
| Functional | Difficulty balancing price and quality | 85% | Very High |
| Emotional | Long-term concerns about food safety | 95% | Constant |
| Emotional | Cognitive pressure from too many choices | 65% | Frequent |
| Social | Wrong purchases affect family image | 60% | Occasional |

**Customer Priorities Visualization:**
```
Food Safety:        ████████████████████ 98%
Quality Consistency: ███████████████████ 95%
Price Stability:    ██████████████████ 90%
Transparency:       █████████████████ 88%
Delivery Reliability: ████████████████ 85%
Time Saving:        ████████████████ 80%
```

**Shopping Behavior Profile:**
- Frequency: 2-3 times per week
- Average Basket Size: ¥150-250
- Preferred Time: Evening after work
- Device Preference: Mobile app
- Decision Time: 10-15 minutes

### 5.6 Module 5: Opportunity Engine

**Purpose:** Strategic opportunity identification and market entry simulation.

**Opportunity Scoring Methodology:**
```
Score = (Market Need × 0.30) + (Competitor Gap × 0.25) + 
        (CP Capability × 0.25) + (Market Size × 0.20)
```

**Top Ranked Opportunities:**

| Rank | Opportunity | Score | Market Need | Competitor Gap |
|------|-------------|-------|-------------|----------------|
| 1 | Full Supply Chain Traceability | 84/100 | 95% | 75% |
| 2 | Price-Quality Optimization Platform | 83/100 | 90% | 85% |
| 3 | Organic & Low-Pesticide Products | 80/100 | 85% | 90% |
| 4 | AI-Powered Personalization | 74/100 | 75% | 60% |
| 5 | Community-Based Distribution | 71/100 | 70% | 50% |

**City Entry Priority Ranking:**

Priority Score Calculation:
```
Priority = (Market Size × 0.30) + (1-Competition × 0.20) + 
           (Infrastructure × 0.25) + (Target Segment × 0.25)
```

**Market Entry Strategy Simulator:**

Interactive inputs:
- Business Model: Front Warehouse / Store-Warehouse / Hybrid
- Initial City Coverage: 1-5 cities
- Traceability Coverage: 0-100%
- Organic Product Focus: 0-100%
- AI/Tech Investment: 0-100%
- Price Positioning: Premium / Mid-range / Value

Output Metrics:
- Success Probability
- Estimated Market Share (Year 3)
- Estimated Revenue (Year 3)

---

## 6. Part B: Consumer Application (B2C)

### 6.1 Application Overview

The Consumer Application demonstrates a user-centered shopping experience with AI-powered features targeting quality-conscious middle-class families.

### 6.2 User Preference System

**Shopping Profile Types:**
1. **Auto-detect**: System learns from browsing behavior
2. **Quality Priority**: Focus on food safety, quality stability, traceability
3. **Value Priority**: Focus on price stability, value for money, budget control

**Session State Management:**
```python
if 'user_type' not in st.session_state:
    st.session_state.user_type = 'Quality Priority'
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
```

### 6.3 Tab 1: Personalized Recommendations

**Features:**
- Dynamic product sorting based on user preferences
- Quality Priority: Sorted by quality score
- Value Priority: Sorted by discount percentage

**Sample Product Data Structure:**
```python
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
}
```

**Product Categories:**
- Vegetables: Organic Baby Spinach, Low-Pesticide Cherry Tomatoes
- Meat: Grass-Fed Australian Beef
- Seafood: Fresh Norwegian Salmon
- Eggs & Dairy: Free-Range Eggs
- Grains: Organic Brown Rice

**Product Card Display:**
- Product name and origin
- Quality score badge
- Stability score badge
- Certification information
- Price with discount display
- Add to Cart functionality

**Quick Replenishment Section:**
- Based on purchase history
- One-click reorder buttons
- Display of frequently purchased items

### 6.4 Tab 2: Traceability System

**Purpose:** Full supply chain transparency from farm to table.

**Traceability Completeness Score:**
- Displayed as large percentage (85-95%)
- Visual emphasis with colored background

**Supply Chain Journey Visualization:**

| Stage | Location | Status | Details |
|-------|----------|--------|---------|
| 1. Origin | Farm/Producer | Verified | Certified and inspected |
| 2. Processing | Central Facility | Verified | Quality control completed |
| 3. Cold Chain | Distribution Center | Verified | Temperature: 2-4°C |
| 4. Final Mile | Local Warehouse | Ready | Available for delivery |

**Certifications & Test Reports Section:**
- Origin Certificate: Verified
- Quality Test Report: Passed
- Product-specific certification display

**Risk Assessment Alerts:**
- Category-specific warnings (Meat, Seafood)
- Cold chain monitoring information
- Temperature safety assurance

### 6.5 Tab 3: Price-Quality Balance Tool

**Purpose:** Help consumers make informed decisions by visualizing price-quality relationships.

**Interactive Filters:**
- Maximum Price slider (¥0-100)
- Minimum Quality Score slider (0-100%)

**Price-Quality Scatter Plot:**
- X-axis: Price (CNY)
- Y-axis: Quality Score (%)
- Color coding: Green for organic/low-pesticide, Blue for others
- Hover information showing value score calculation

**Value Score Calculation:**
```
Value Score = (Quality Score × 100 / Price) × 10
```

**Best Value Products Ranking:**
- Top 3 products by value score
- Displays price, quality, and computed value score

**Price Stability Guarantee:**
- No sudden price increases without 48-hour notice
- Price matching for equivalent quality products
- Transparent pricing with breakdown available

### 6.6 Tab 4: AI Shopping Assistant

**Purpose:** Conversational AI interface for personalized shopping assistance.

**Capabilities:**
- Product recommendations
- Nutrition advice
- Recipe suggestions
- Food safety questions
- Seasonal produce information

**Response Categories:**

1. **Recommendation Queries:**
   - Personalized based on user type (Quality/Value priority)
   - Suggests products with traceability information

2. **Seasonal/Winter Queries:**
   - Lists in-season vegetables
   - Provides nutritional information
   - Offers recipe suggestions

3. **Safety Queries:**
   - Explains traceability coverage (85-95%)
   - Details testing procedures
   - Describes cold chain monitoring
   - References certification system

4. **Organic Queries:**
   - Highlights organic product line
   - Explains certification standards
   - Mentions customer adoption rates

**Chat History Management:**
- Stores last 5 conversations
- Timestamps for each interaction
- User and assistant message display

**Daily Nutrition Tips:**
- Rotating tips based on day of month
- Topics include:
  - Nutritional comparisons (organic vs. conventional)
  - Seasonal advice
  - Food safety tips
  - Storage recommendations

### 6.7 Shopping Cart Functionality

**Implementation:**
```python
with st.sidebar:
    st.markdown("### Shopping Cart")
    if st.session_state.cart:
        total = sum(item['price'] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.markdown(f"- {item['name']}: ¥{item['price']}")
        st.markdown(f"**Total: ¥{total:.2f}**")
        if st.button("Proceed to Checkout", type="primary"):
            st.success("Order placed successfully!")
            st.session_state.cart = []
```

### 6.8 Tab 5: Auto-Detect User Preference Demo

**Purpose:** Interactive demonstration of the AI-powered user preference detection system that analyzes browsing behavior to automatically classify shoppers.

**Behavior Tracking Session State:**
```python
if 'behavior_data' not in st.session_state:
    st.session_state.behavior_data = {
        'quality_clicks': 0,      # Clicks on quality scores
        'price_clicks': 0,        # Clicks on price tags
        'trace_views': 0,         # Traceability info views
        'discount_views': 0,      # Discount/sale views
        'organic_views': 0,       # Organic product views
        'detected_type': None,    # Detected user type
        'confidence': 0           # Detection confidence
    }
```

**Interactive Behavior Simulation:**

Users can simulate two types of shopping behaviors through clickable buttons:

| Quality-Related Actions | Value-Related Actions |
|------------------------|----------------------|
| Click on Quality Score | Click on Price Tag |
| View Traceability Info | View Discount Offers |
| Browse Organic Products | Sort by Price (Low to High) |
| Check Certifications | Add Sale Item to Cart |

**Detection Algorithm:**

The system uses a weighted scoring approach to classify users:

```python
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
        return {'type': 'Undetermined', 'confidence': 0}
    
    # Calculate confidence
    confidence = abs(quality_score - value_score) / total_score * 100
    
    if quality_score > value_score:
        preference_type = 'Quality Priority'
    else:
        preference_type = 'Value Priority'
    
    return {
        'type': preference_type,
        'confidence': min(confidence, 95),
        'quality_score': quality_score,
        'value_score': value_score
    }
```

**Weight Assignment Rationale:**

| Behavior | Weight | Rationale |
|----------|--------|-----------|
| Quality Score Clicks | 2.0x | Direct interest in quality metrics |
| Traceability Views | 3.0x | Strong indicator of safety concerns |
| Organic Product Views | 2.5x | Premium quality preference |
| Price Clicks | 2.0x | Direct interest in pricing |
| Discount Views | 3.0x | Strong indicator of value seeking |

**Real-time Detection Visualization:**

1. **Score Metrics Display:**
   - Quality Score (with action count)
   - Value Score (with action count)
   - Confidence percentage

2. **Bar Chart Comparison:**
   - Visual comparison of Quality vs Value scores
   - Color-coded (Green: Quality, Orange: Value)

3. **Detection Result Display:**
   - Status messages based on data sufficiency
   - Personalized experience recommendations

**Detection Status Levels:**

| Status | Condition | Message |
|--------|-----------|---------|
| Collecting Data | Total score = 0 | "Not enough data. Keep browsing!" |
| Still Learning | Confidence < 30% | Current tendency shown, need more data |
| Detected | Confidence ≥ 30% | Full preference profile with recommendations |

**Personalized Experience Activation:**

For Quality Priority shoppers:
- Products sorted by quality score
- Quality badges and certifications highlighted
- Traceability information prominently displayed
- Organic products recommended first

For Value Priority shoppers:
- Products sorted by discount percentage
- Price tags and savings highlighted
- Best value recommendations shown first
- Price alerts for favorite products

**Behavior Data Log:**

Interactive DataFrame showing:
| Column | Description |
|--------|-------------|
| Behavior Type | Type of user action |
| Count | Number of occurrences |
| Weight | Score multiplier |
| Category | Quality or Value |
| Weighted Score | Count × Weight |

**Technical Implementation Details (Expandable Section):**

The demo includes documentation for production implementation:

1. **Data Collection Points:**
   - Click events on product cards
   - Time spent viewing traceability information
   - Filter and sort preferences
   - Cart additions and purchase history
   - Search queries analysis

2. **Machine Learning Model (Production):**
```python
from sklearn.ensemble import RandomForestClassifier

class UserPreferenceDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
    
    def extract_features(self, user_session):
        return {
            'quality_click_ratio': user_session.quality_clicks / max(total_clicks, 1),
            'trace_view_time_pct': user_session.trace_view_time / max(total_time, 1),
            'organic_browse_ratio': user_session.organic_views / max(total_views, 1),
            'price_sort_count': user_session.price_sort_events,
            'discount_click_ratio': user_session.discount_clicks / max(total_clicks, 1)
        }
    
    def predict(self, features):
        prediction = self.model.predict(features)
        confidence = max(self.model.predict_proba(features)[0])
        return prediction, confidence
```

3. **Real-time Updates:**
   - Behavior tracked via event stream (Kafka/Redis)
   - Model inference at edge for low latency
   - A/B testing for recommendation strategies
   - Continuous model retraining with new data

4. **Privacy Considerations:**
   - All behavior data anonymized
   - User consent for personalization
   - Option to reset preferences
   - Transparent algorithm explanation

---

## 7. Data Architecture

### 7.1 Data Loading Utility

**File:** `utils/data_loader.py`

**Functions:**
1. `get_data_path(filename)`: Returns absolute path to data files
2. `load_json(filename)`: Loads and parses JSON data with error handling
3. `load_all_data()`: Loads all required data files and returns tuple

**Error Handling:**
- FileNotFoundError: Returns empty dict with warning
- JSONDecodeError: Returns empty dict with warning

### 7.2 Data Files Specification

#### 7.2.1 competitors.json

**Structure:**
```json
{
  "dingdong": {
    "name": "string",
    "model": "string",
    "description": "string",
    "cities": ["string"],
    "city_strategy": "string",
    "sku_count": "number",
    "fulfillment_cost_2024": "number",
    "strengths": ["string"],
    "weaknesses": ["string"],
    "opportunities": ["string"],
    "threats": ["string"],
    "traceability_coverage": "number (0-1)",
    "ai_features": ["string"],
    "membership_benefits": ["string"],
    "product_categories": {
      "category_name": "number (0-1)"
    }
  },
  "freshippo": { /* similar structure */ }
}
```

#### 7.2.2 market_data.json

**Key Fields:**
- Market size data (2023-2025)
- CAGR growth rate
- City tier penetration rates
- Consumer behavior shifts
- Age distribution
- Key pain points with severity scores
- Industry trends (AI, Supply Chain, Sustainability)
- Competitive landscape metrics

#### 7.2.3 customer_segments.json

**Primary Segment (pragmatic_middle_class):**
- Demographics (income, age, household size)
- Jobs to Be Done (functional, emotional, social)
- Pain points with severity and frequency
- Expected gains
- Priorities ranking
- Shopping behavior profile
- Product preferences

#### 7.2.4 dingdong_financials.json

**Structure:**
- Quarterly financial data (2021 Q1 - 2024 Q2)
- Net loss/profit values
- Key metrics including turnaround information

---

## 8. User Interface Design

### 8.1 Design Principles

1. **Consistency**: Unified color scheme (primary: #2E7D32 green)
2. **Clarity**: Clear hierarchy with headers and sections
3. **Interactivity**: Responsive charts and interactive controls
4. **Accessibility**: High contrast text and visual indicators

### 8.2 Custom CSS Styling

**Dashboard Styles:**
```css
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
.swot-positive { color: #2E7D32; font-weight: 500; }
.swot-negative { color: #C62828; font-weight: 500; }
```

**Consumer App Styles:**
```css
.product-card {
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 1rem;
    background-color: white;
}
.quality-badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 5px;
    font-weight: 600;
}
.price-tag {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2E7D32;
}
.ai-response {
    background-color: #F5F5F5;
    padding: 1rem;
    border-radius: 10px;
    border-left: 4px solid #2E7D32;
}
```

### 8.3 Color Scheme

| Element | Color Code | Usage |
|---------|------------|-------|
| Primary | #2E7D32 | Headers, buttons, positive indicators |
| Secondary | #1565C0 | Competitor comparison (Freshippo) |
| Warning | #F57C00 | Medium severity items |
| Error | #C62828 | High severity, negative indicators |
| Background | #f8f9fa | Cards and containers |
| Accent | #e8f5e9 | Insight boxes, highlights |

### 8.4 Layout Structure

**Dashboard Layout:**
- Wide layout for data-intensive displays
- Sidebar navigation for module switching
- 4-column metric cards for overview
- 2-column layouts for comparisons
- Full-width charts for detailed analysis

**Consumer App Layout:**
- Wide layout for product display
- Tabbed navigation for features
- 2-column product cards
- Sidebar shopping cart
- Full-width traceability visualization

---

## 9. Key Features Implementation

### 9.1 Interactive Data Visualization

**Financial Trend Chart (Dingdong):**
```python
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_fin['period'],
    y=df_fin['net_loss_m'],
    mode='lines+markers',
    line=dict(color='#2E7D32', width=3),
    marker=dict(size=8, color=colors)
))
fig.add_hline(y=0, line_dash="dash", annotation_text="Break-even")
```

**Radar Chart for Opportunity Analysis:**
```python
fig.add_trace(go.Scatterpolar(
    r=[opp['Market Need'], opp['Competitor Gap'], 
       opp['CP Capability'], opp['Market Size']],
    theta=['Market Need', 'Competitor Gap', 
           'CP Capability', 'Market Size'],
    fill='toself',
    fillcolor='rgba(46, 125, 50, 0.3)',
    line=dict(color='#2E7D32', width=2)
))
```

### 9.2 Session State Management

**Shopping Cart Persistence:**
```python
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Adding items
if st.button(f"Add to Cart", key=f"cart_{product['name']}"):
    st.session_state.cart.append(product)
    st.success(f"Added {product['name']} to cart!")
```

**Chat History Management:**
```python
st.session_state.chat_history.append({
    'user': user_input,
    'timestamp': datetime.now().strftime("%H:%M"),
    'assistant': response
})
```

### 9.3 Dynamic Filtering

**Product Filtering by Price and Quality:**
```python
max_price = st.slider("Maximum Price (CNY)", 0, 100, 50)
min_quality = st.slider("Minimum Quality Score", 0, 100, 80)

filtered = [p for p in products 
            if p['price'] <= max_price 
            and p['quality_score']*100 >= min_quality]
```

### 9.4 Opportunity Scoring Algorithm

```python
for opp in opportunities:
    opp['Score'] = (
        opp['Market Need'] * 0.3 +
        opp['Competitor Gap'] * 0.25 +
        opp['CP Capability'] * 0.25 +
        opp['Market Size'] * 0.2
    )
```

### 9.5 Market Entry Simulation

**ROI Calculation Logic:**
```python
base_score = 50

if entry_model == "Hybrid Model":
    base_score += 15
elif entry_model == "Store-Warehouse Integration":
    base_score += 10

base_score += initial_cities * 3
base_score += traceability_level * 0.2
base_score += organic_focus * 0.15
base_score += tech_investment * 0.1

if price_positioning == "Mid-range":
    base_score += 10

success_probability = min(base_score, 95)
est_market_share = success_probability * 0.08
est_revenue = est_market_share * market['market_size_2025_projected'] / 100
```

---

## 10. Future Development Recommendations

### 10.1 Technical Enhancements

1. **Database Integration**
   - Migrate from JSON files to PostgreSQL/MongoDB
   - Enable real-time data updates
   - Implement data versioning

2. **API Development**
   - RESTful API for data access
   - Integration with external market data providers
   - Real-time competitor monitoring

3. **Machine Learning Integration**
   - True AI-powered recommendation engine
   - Predictive analytics for demand forecasting
   - Natural Language Processing for chatbot

4. **User Authentication**
   - User account management
   - Personalized dashboards
   - Role-based access control

### 10.2 Feature Enhancements

1. **Dashboard Improvements**
   - Real-time data refresh
   - Custom report generation
   - Export functionality (PDF, Excel)
   - Alert system for market changes

2. **Consumer App Enhancements**
   - Actual payment integration
   - Order tracking system
   - Push notifications
   - Social sharing features

3. **Traceability System**
   - Blockchain integration for immutable records
   - QR code scanning
   - IoT sensor data integration
   - Certificate verification API

### 10.3 Scalability Considerations

1. **Performance Optimization**
   - Implement caching (Redis)
   - Lazy loading for large datasets
   - CDN for static assets

2. **Deployment**
   - Containerization with Docker
   - Kubernetes orchestration
   - CI/CD pipeline setup

---

## 11. Conclusion

### 11.1 Key Achievements

This prototype successfully demonstrates:

1. **Comprehensive Market Analysis Platform**
   - In-depth competitor intelligence
   - Data-driven market opportunity identification
   - Customer-centric segmentation analysis

2. **User-Centered Consumer Experience**
   - Personalized product recommendations
   - Full supply chain traceability
   - Intelligent price-quality optimization
   - AI-powered shopping assistance

3. **Strategic Decision Support**
   - Opportunity scoring methodology
   - Market entry simulation
   - City priority ranking

### 11.2 Market Opportunity Summary

The analysis reveals significant opportunities for CP Group:

| Opportunity | Score | Key Advantage |
|-------------|-------|---------------|
| Full Traceability | 84/100 | Leverage integrated supply chain |
| Price-Quality Platform | 83/100 | Address core consumer pain point |
| Organic Products | 80/100 | First-mover in dedicated organic |

### 11.3 Target Market

- **Primary Segment**: Pragmatic Middle-Class Families (45% of market)
- **Market Size**: ¥580B (2024) → ¥707.6B (2025 projected)
- **Growth Rate**: 22% CAGR
- **Key Differentiator**: 95%+ traceability vs. competitors' 25-30%

### 11.4 Technical Summary

The prototype is built on a modern, scalable technology stack:
- **Frontend**: Streamlit for rapid prototyping
- **Visualization**: Plotly for interactive charts
- **Data**: JSON-based for flexibility
- **Architecture**: Modular, maintainable design

This prototype provides a solid foundation for CP Group to evaluate market entry strategies and demonstrate potential differentiated features to stakeholders.

---

## Appendix A: Running the Application

### Prerequisites
```bash
Python 3.10+
pip install -r requirements.txt
```

### Starting the Application
```bash
streamlit run Home.py
```

### Accessing the Application
```
URL: http://localhost:8501
```

---

## Appendix B: Data Sources

All data is extracted from:
- Dingdong Maicai annual reports (2021-2024)
- Industry analysis documents
- Customer research reports
- Market trend reports

---

**Report Prepared By:** ENT302TC Project Team  
**Last Updated:** December 2024  
**Version:** 1.0
