<style>
  .case-study-container {
    max-width: 800px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    line-height: 1.6;
  }
  .case-study-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 600;
    margin-bottom: 0.25rem;
  }
  .case-study-subtitle {
    text-align: center;
    color: #555;
    font-size: 0.98rem;
    margin-bottom: 2rem;
  }
  .case-study-section-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-top: 1.8rem;
    margin-bottom: 0.4rem;
    border-bottom: 1px solid #e5e5e5;
    padding-bottom: 0.25rem;
  }
  .case-study-section p {
    margin: 0.4rem 0 0.6rem 0;
  }
  .case-study-list {
    margin: 0.2rem 0 0.8rem 1.2rem;
  }
</style>

<div class="case-study-container">

  <div class="case-study-title">Pulse — Product Case Study</div>
  <div class="case-study-subtitle">AI-powered customer feedback insights for small businesses</div>

  <div class="case-study-section">
    <div class="case-study-section-title">Problem</div>
    <p>
      Small business owners receive a constant stream of customer feedback across receipts, Google reviews,
      Square receipts, and in-store conversations. While this feedback is valuable, it is almost always
      unstructured. Owners rarely have the time or tools to read through dozens of comments, identify patterns,
      or understand what customers consistently praise or complain about. As a result, important insights get
      lost, and decisions are often made based on intuition rather than data.
    </p>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">User</div>
    <p>
      The primary user is a small business owner or manager who wants to understand customer sentiment but lacks
      the time, analytical tools, or technical background to process large amounts of text. Their needs are
      simple: a fast, clear summary of what customers are saying and what actions they should take.
    </p>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">Solution</div>
    <p>
      Pulse is a lightweight, AI-powered tool that turns raw customer reviews into structured insights. Users
      upload a CSV containing customer comments, and the app instantly generates:
    </p>
    <ul class="case-study-list">
      <li>Key themes</li>
      <li>Top complaints</li>
      <li>Top compliments</li>
      <li>Actionable recommendations</li>
      <li>A weekly "health summary"</li>
    </ul>
    <p>
      The goal was to create a tool that feels simple, fast, and accessible—something a busy owner could use in
      under a minute.
    </p>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">Approach</div>
    <p>
      The product was intentionally scoped around a single, focused workflow: <b>upload → analyze → insights</b>.
      This helped avoid feature creep and ensured the core experience was polished.
    </p>
    <ul class="case-study-list">
      <li>Groq's Llama-3.1 model was selected for its speed and free usage tier.</li>
      <li>Streamlit provided a clean, deployable interface.</li>
      <li>A realistic 100-review dataset was created to simulate real-world usage and ensure the insights felt meaningful.</li>
    </ul>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">Constraints and Tradeoffs</div>
    <ul class="case-study-list">
      <li><b>Cost:</b> Using Groq's free tier kept the tool accessible, influencing model selection and prompt design.</li>
      <li><b>Simplicity:</b> A minimal UI was prioritized to reduce cognitive load and keep the experience fast.</li>
      <li><b>Data realism:</b> A balanced dataset was generated to avoid relying on proprietary business data while still producing credible insights.</li>
      <li><b>Scope:</b> Advanced features like dashboards, trend analysis, and segmentation were intentionally deferred to maintain a tight, shippable MVP.</li>
    </ul>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">Impact</div>
    <p>
      Pulse demonstrates how AI can make customer understanding more accessible for small businesses. By reducing
      hours of manual review into a few seconds of automated insight, the tool helps owners make more informed
      decisions about service, pricing, staffing, and product quality.
    </p>
  </div>

  <div class="case-study-section">
    <div class="case-study-section-title">Future Improvements</div>
    <p>
      The current version of Pulse focuses on delivering fast, high-quality insights from unstructured text.
      The next steps would deepen the product's value and move it toward a more comprehensive insights platform.
    </p>

    <p><b>Trend analysis over time</b></p>
    <p>
      Adding sentiment trendlines, recurring complaint detection, and emerging theme alerts would help owners
      make proactive decisions.
    </p>

    <p><b>Visual dashboards</b></p>
    <p>
      Charts for sentiment distribution, theme frequency, and complaint versus compliment ratios would make
      insights easier to digest at a glance.
    </p>

    <p><b>Segmentation</b></p>
    <p>
      Different customer groups often have different needs. Segmenting by visit type, customer segment, or
      rating level would help owners understand which groups are happiest or struggling.
    </p>

    <p><b>Multi-file batch analysis</b></p>
    <p>
      Businesses with multiple locations or long review histories could upload several files at once and compare
      store performance, time periods, or product categories.
    </p>

    <p><b>Exportable reports</b></p>
    <p>
      A one-click PDF or email summary would let owners share insights with staff or use them in weekly meetings.
    </p>

    <p><b>Real-time integrations</b></p>
    <p>
      Long term, Pulse could connect directly to Square receipts, Google Reviews, Yelp, or social media mentions,
      turning it into a continuous feedback engine rather than a one-off tool.
    </p>

    <p><b>Improved prompt engineering</b></p>
    <p>
      Refining prompts to produce more structured, consistent outputs would improve reliability as models evolve.
    </p>
  </div>

  <p class="case-study-subtitle">
    This case study reflects the product thinking, scoping discipline, and user empathy behind Pulse.
  </p>

</div>
