# Pulse — Product Case Study
*AI-powered customer feedback insights for small businesses*

---

## Problem
Small business owners receive a constant stream of customer feedback across receipts, Google reviews, Square receipts, and in‑store conversations. While this feedback is valuable, it is almost always unstructured. Owners rarely have the time or tools to read through dozens of comments, identify patterns, or understand what customers consistently praise or complain about. As a result, important insights get lost, and decisions are often made based on intuition rather than data.

---

## User
The primary user is a small business owner or manager who wants to understand customer sentiment but lacks the time, analytical tools, or technical background to process large amounts of text. Their needs are simple: a fast, clear summary of what customers are saying and what actions they should take.

---

## Solution
Pulse is a lightweight, AI‑powered tool that turns raw customer reviews into structured insights. Users upload a CSV containing customer comments, and the app instantly generates:

- Key themes  
- Top complaints  
- Top compliments  
- Actionable recommendations  
- A weekly “health summary”

The goal was to create a tool that feels simple, fast, and accessible—something a busy owner could use in under a minute.

---

## Approach
The product was intentionally scoped around a single, focused workflow: **upload → analyze → insights**. This helped avoid feature creep and ensured the core experience was polished.

- Groq’s Llama‑3.1 model was selected for its speed and free usage tier.  
- Streamlit provided a clean, deployable interface.  
- A realistic 100‑review dataset was created to simulate real‑world usage and ensure the insights felt meaningful.

---

## Constraints and Tradeoffs
- **Cost:** Using Groq’s free tier kept the tool accessible, influencing model selection and prompt design.  
- **Simplicity:** A minimal UI was prioritized to reduce cognitive load and keep the experience fast.  
- **Data realism:** A balanced dataset was generated to avoid relying on proprietary business data while still producing credible insights.  
- **Scope:** Advanced features like dashboards, trend analysis, and segmentation were intentionally deferred to maintain a tight, shippable MVP.

---

## Impact
Pulse demonstrates how AI can make customer understanding more accessible for small businesses. By reducing hours of manual review into a few seconds of automated insight, the tool helps owners make more informed decisions about service, pricing, staffing, and product quality.

---

## Future Improvements

### Trend analysis over time
Adding sentiment trendlines, recurring complaint detection, and emerging theme alerts would help owners make proactive decisions.

### Visual dashboards
Charts for sentiment distribution, theme frequency, and complaint‑versus‑compliment ratios would make insights easier to digest at a glance.

### Segmentation
Different customer groups often have different needs. Segmenting by visit type, customer segment, or rating level would help owners understand which groups are happiest or struggling.

### Multi‑file batch analysis
Businesses with multiple locations or long review histories could upload several files at once and compare store performance, time periods, or product categories.

### Exportable reports
A one‑click PDF or email summary would let owners share insights with staff or use them in weekly meetings.

### Real‑time integrations
Long term, Pulse could connect directly to Square receipts, Google Reviews, Yelp, or social media mentions, turning it into a continuous feedback engine.

### Improved prompt engineering
Refining prompts to produce more structured, consistent outputs would improve reliability as models evolve.
