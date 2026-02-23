Pulse — Product Case Study
Problem
Small business owners receive a constant stream of customer feedback across receipts, Google reviews, social media, and in‑store conversations. While this feedback is valuable, it’s almost always unstructured. Owners rarely have the time or tools to read through dozens of comments, identify patterns, or understand what customers consistently praise or complain about. As a result, important insights get lost, and decisions are often made based on intuition rather than data.

User
The primary user is a small business owner or manager who wants to understand customer sentiment but lacks the time, analytical tools, or technical background to process large amounts of text. Their needs are simple: a fast, clear summary of what customers are saying and what actions they should take.

Solution
Pulse is a lightweight, AI‑powered tool that turns raw customer reviews into structured insights. Users upload a CSV containing customer comments, and the app instantly generates:

Key themes

Top complaints

Top compliments

Actionable recommendations

A weekly “health summary”

The goal was to create a tool that feels simple, fast, and accessible—something a busy owner could use in under a minute.
Approach
I scoped the product around a single, focused workflow: upload → analyze → insights. This helped avoid feature creep and ensured the core experience was polished. I used Groq’s Llama‑3.1 model for fast, free inference and Streamlit for a clean, deployable interface. I also created a realistic 100‑review dataset to simulate real‑world usage and ensure the insights felt meaningful.

Constraints and Tradeoffs
Cost: I used Groq’s free tier to keep the tool accessible, which influenced prompt design and model selection.

Simplicity: I prioritized a minimal UI to reduce cognitive load and keep the experience fast.

Data realism: I generated a balanced dataset to avoid relying on proprietary business data while still producing credible insights.

Scope: I intentionally deferred advanced features like dashboards, trend analysis, and segmentation to maintain a tight, shippable MVP.

Impact
Pulse demonstrates how AI can make customer understanding more accessible for small businesses. By reducing hours of manual review into a few seconds of automated insight, the tool helps owners make more informed decisions about service, pricing, staffing, and product quality.