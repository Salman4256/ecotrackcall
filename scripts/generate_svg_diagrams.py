import os

DIAGRAMS_DIR = r"e:\ecotrackcall\ECOTRACK\Document\diagrams"
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Figure 3.1: Existing System Diagram
# -------------------------------------------------------------
svg_3_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#334155" stop-opacity="0.7" />
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" />
      <stop offset="100%" stop-color="#b91c1c" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1100" height="650" rx="16" fill="url(#bgGrad)" />
  <rect x="2" y="2" width="1096" height="646" rx="14" fill="none" stroke="#334155" stroke-width="2" />

  <!-- Title Badge -->
  <rect x="350" y="30" width="400" height="44" rx="22" fill="#ef4444" fill-opacity="0.15" stroke="#ef4444" stroke-width="1.5" />
  <text x="550" y="58" font-family="'Segoe UI', Roboto, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#f87171" text-anchor="middle">FIGURE 3.1: EXISTING CONVENTIONAL CARBON SYSTEM</text>

  <!-- User / Input Stage -->
  <g transform="translate(60, 110)">
    <rect width="260" height="200" rx="12" fill="url(#cardGrad)" stroke="#475569" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="130" cy="50" r="28" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="2" />
    <text x="130" y="57" font-family="'Segoe UI', sans-serif" font-size="22" fill="#60a5fa" text-anchor="middle">👤</text>
    <text x="130" y="105" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">Manual User Estimation</text>
    <text x="130" y="130" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Guesswork on commute miles</text>
    <text x="130" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Unorganized utility bills</text>
    <text x="130" y="170" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• No category breakdown</text>
    <rect x="50" y="215" width="160" height="26" rx="6" fill="#ef4444" fill-opacity="0.2" />
    <text x="130" y="233" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#f87171" text-anchor="middle">High Human Error Rate</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 320 210 L 410 210" stroke="#f87171" stroke-width="2.5" stroke-dasharray="6,4" fill="none" />
  <polygon points="415,210 405,204 405,216" fill="#f87171" />
  <text x="368" y="195" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Ad-hoc Data</text>

  <!-- Processing Stage -->
  <g transform="translate(420, 110)">
    <rect width="280" height="200" rx="12" fill="url(#cardGrad)" stroke="#475569" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="140" cy="50" r="28" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" />
    <text x="140" y="57" font-family="'Segoe UI', sans-serif" font-size="22" fill="#fbbf24" text-anchor="middle">📄</text>
    <text x="140" y="105" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">Spreadsheets &amp; Static Forms</text>
    <text x="140" y="130" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Outdated conversion tables</text>
    <text x="140" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Static generic coefficients</text>
    <text x="140" y="170" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Disconnected isolated files</text>
    <rect x="50" y="215" width="180" height="26" rx="6" fill="#f59e0b" fill-opacity="0.2" />
    <text x="140" y="233" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#fbbf24" text-anchor="middle">Zero AI / Inflexible Logic</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 700 210 L 780 210" stroke="#f87171" stroke-width="2.5" stroke-dasharray="6,4" fill="none" />
  <polygon points="785,210 775,204 775,216" fill="#f87171" />
  <text x="742" y="195" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Raw Result</text>

  <!-- Output Stage -->
  <g transform="translate(790, 110)">
    <rect width="250" height="200" rx="12" fill="url(#cardGrad)" stroke="#475569" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="125" cy="50" r="28" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="2" />
    <text x="125" y="57" font-family="'Segoe UI', sans-serif" font-size="22" fill="#f87171" text-anchor="middle">📉</text>
    <text x="125" y="105" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">Unverified Outputs</text>
    <text x="125" y="130" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Single total kg CO₂ value</text>
    <text x="125" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Generic non-actionable tips</text>
    <text x="125" y="170" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• No historical trend charts</text>
    <rect x="40" y="215" width="170" height="26" rx="6" fill="#ef4444" fill-opacity="0.2" />
    <text x="125" y="233" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#f87171" text-anchor="middle">No Behavioral Change</text>
  </g>

  <!-- Bottom Disadvantages Container -->
  <g transform="translate(60, 380)">
    <rect width="980" height="230" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" stroke-opacity="0.7" filter="url(#shadow)" />
    <rect x="25" y="-14" width="220" height="28" rx="6" fill="#ef4444" />
    <text x="135" y="5" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">KEY FLAWS IDENTIFIED</text>

    <!-- Disadvantage Grid -->
    <g transform="translate(35, 35)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="430" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
      <text x="20" y="28" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#f87171">1. High Inaccuracy &amp; Subjective Bias</text>
      <text x="20" y="50" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Relies on manual inputs and unverified constants (+/- 45% variance across tools).</text>

      <!-- Item 2 -->
      <rect x="475" y="0" width="430" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
      <text x="495" y="28" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#f87171">2. Lack of Granular Categories</text>
      <text x="495" y="50" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Omits critical lifestyle factors: food diets, consumer shopping, waste recycling.</text>

      <!-- Item 3 -->
      <rect x="0" y="95" width="430" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
      <text x="20" y="123" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#f87171">3. Generic, Non-Actionable Advice</text>
      <text x="20" y="145" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Static suggestions ("turn off lights") without individualized priority or ROI.</text>

      <!-- Item 4 -->
      <rect x="475" y="95" width="430" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
      <text x="495" y="123" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#f87171">4. No Data Persistence &amp; Auditing</text>
      <text x="495" y="145" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Zero session tracking, no verified carbon audit logs, and no historical progress.</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_3_1_existing_system.svg"), "w", encoding="utf-8") as f:
    f.write(svg_3_1)

# -------------------------------------------------------------
# 2. Figure 5.7: Proposed System Architecture Diagram
# -------------------------------------------------------------
svg_5_7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1250 820" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1320" />
      <stop offset="100%" stop-color="#111c30" />
    </linearGradient>
    <linearGradient id="tierGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="primaryGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="blueGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="purpleGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#6d28d9" />
    </linearGradient>
    <linearGradient id="amberGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1250" height="820" rx="16" fill="url(#bgGrad)" />
  <rect x="2" y="2" width="1246" height="816" rx="14" fill="none" stroke="#1e293b" stroke-width="2" />

  <!-- Main Title -->
  <rect x="360" y="20" width="530" height="46" rx="23" fill="#10b981" fill-opacity="0.12" stroke="#10b981" stroke-width="1.8" />
  <text x="625" y="49" font-family="'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#34d399" text-anchor="middle">FIGURE 5.7: ECOTRACK PROPOSED SYSTEM ARCHITECTURE</text>

  <!-- ================= TIER 1: CLIENT PRESENTATION ================= -->
  <g transform="translate(40, 85)">
    <rect width="1170" height="135" rx="12" fill="url(#tierGrad)" stroke="#3b82f6" stroke-width="1.5" stroke-opacity="0.6" filter="url(#shadow)" />
    <rect x="25" y="-12" width="260" height="24" rx="6" fill="#3b82f6" />
    <text x="155" y="5" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">TIER 1: PRESENTATION &amp; CLIENT LAYER</text>

    <!-- Component 1: React + Vite SPA -->
    <rect x="30" y="30" width="260" height="85" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="50" y="58" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#60a5fa">React 18 + Vite SPA</text>
    <text x="50" y="80" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• React Router DOM (Guards)</text>
    <text x="50" y="100" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Responsive Dark/Light UI</text>

    <!-- Component 2: 7-Category Calculator UI -->
    <rect x="315" y="30" width="270" height="85" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="335" y="58" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#34d399">7-Category Calculator UI</text>
    <text x="335" y="80" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Transport, Energy, Water, Diet</text>
    <text x="335" y="100" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Waste, Shopping, Travel inputs</text>

    <!-- Component 3: Chart.js Visualizations -->
    <rect x="610" y="30" width="260" height="85" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="630" y="58" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#fbbf24">Chart.js Analytics Engine</text>
    <text x="630" y="80" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Doughnut breakdown charts</text>
    <text x="630" y="100" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Historical monthly trends</text>

    <!-- Component 4: Supabase Client SDK -->
    <rect x="895" y="30" width="245" height="85" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="915" y="58" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#a78bfa">Supabase Client SDK</text>
    <text x="915" y="80" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• JWT session management</text>
    <text x="915" y="100" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">• Bearer token injection</text>
  </g>

  <!-- Flow Arrow: Tier 1 to Tier 2 -->
  <g transform="translate(625, 220)">
    <path d="M 0 0 L 0 35" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" />
    <polygon points="0,42 -6,30 6,30" fill="#38bdf8" />
    <text x="15" y="24" font-family="'Segoe UI', sans-serif" font-size="11" fill="#7dd3fc">HTTPS / REST API (JWT Bearer Auth)</text>
  </g>

  <!-- ================= TIER 2: API GATEWAY & SECURITY ================= -->
  <g transform="translate(40, 265)">
    <rect width="1170" height="120" rx="12" fill="url(#tierGrad)" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.6" filter="url(#shadow)" />
    <rect x="25" y="-12" width="280" height="24" rx="6" fill="#10b981" />
    <text x="165" y="5" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">TIER 2: SECURE API GATEWAY (NODE / EXPRESS)</text>

    <!-- Middleware 1: Helmet & CORS -->
    <rect x="30" y="25" width="260" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="50" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#34d399">Helmet &amp; CORS Security</text>
    <text x="50" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">CSP headers, frameguard, safe origins</text>

    <!-- Middleware 2: Rate Limiting & Sanitation -->
    <rect x="315" y="25" width="270" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="335" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#34d399">Rate Limiter &amp; Input Guard</text>
    <text x="335" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">DDoS mitigation &amp; numerical bounds</text>

    <!-- Middleware 3: Auth & Admin Guard -->
    <rect x="610" y="25" width="260" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="630" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#34d399">Auth &amp; Admin Middleware</text>
    <text x="630" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Cryptographic JWT token validation</text>

    <!-- Middleware 4: Unified Error Handling -->
    <rect x="895" y="25" width="245" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="915" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#34d399">Unified Error Handler</text>
    <text x="915" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Standardized JSON API error schema</text>
  </g>

  <!-- Flow Arrow: Tier 2 to Tier 3 -->
  <g transform="translate(625, 385)">
    <path d="M 0 0 L 0 35" stroke="#34d399" stroke-width="3" stroke-linecap="round" />
    <polygon points="0,42 -6,30 6,30" fill="#34d399" />
    <text x="15" y="24" font-family="'Segoe UI', sans-serif" font-size="11" fill="#86efac">Internal Controller Dispatch</text>
  </g>

  <!-- ================= TIER 3: BUSINESS LOGIC & INTELLIGENCE ================= -->
  <g transform="translate(40, 430)">
    <rect width="1170" height="185" rx="12" fill="url(#tierGrad)" stroke="#8b5cf6" stroke-width="1.5" stroke-opacity="0.6" filter="url(#shadow)" />
    <rect x="25" y="-12" width="310" height="24" rx="6" fill="#8b5cf6" />
    <text x="180" y="5" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">TIER 3: BUSINESS LOGIC &amp; AI INTELLIGENCE SERVICES</text>

    <!-- Service 1: Deterministic Calculation Engine -->
    <rect x="30" y="25" width="270" height="145" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="50" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#c084fc">Deterministic Engine</text>
    <text x="50" y="75" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• 100% Deterministic Math</text>
    <text x="50" y="95" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• 7 Emission Categories</text>
    <text x="50" y="115" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Eco Score Algorithm (0-100)</text>
    <text x="50" y="135" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Sub-5ms calculation latency</text>

    <!-- Service 2: Emission Factor Service -->
    <rect x="320" y="25" width="265" height="145" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="340" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#c084fc">Emission Factor Service</text>
    <text x="340" y="75" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• IPCC 2019 Refinement</text>
    <text x="340" y="95" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• US EPA 2023 Constants</text>
    <text x="340" y="115" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• UK DEFRA / DESNZ Factors</text>
    <text x="340" y="135" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Authoritative non-AI values</text>

    <!-- Service 3: Groq AI Recommendation Engine -->
    <rect x="605" y="25" width="270" height="145" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="625" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#c084fc">Groq AI Eco-Coach</text>
    <text x="625" y="75" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Model: gpt-oss-120b</text>
    <text x="625" y="95" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Strict JSON Prompt Schema</text>
    <text x="625" y="115" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Actionable Reduction Tips</text>
    <text x="625" y="135" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Green Weekly Challenges</text>

    <!-- Service 4: PDF & Export Service -->
    <rect x="895" y="25" width="245" height="145" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <text x="915" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#c084fc">PDFKit &amp; Export Service</text>
    <text x="915" y="75" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Official Audit Certificates</text>
    <text x="915" y="95" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Dynamic Vector Graphics</text>
    <text x="915" y="115" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• CSV Stringify for raw logs</text>
    <text x="915" y="135" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• High-speed stream delivery</text>
  </g>

  <!-- Flow Arrow: Tier 3 to Tier 4 -->
  <g transform="translate(625, 615)">
    <path d="M 0 0 L 0 35" stroke="#c084fc" stroke-width="3" stroke-linecap="round" />
    <polygon points="0,42 -6,30 6,30" fill="#c084fc" />
    <text x="15" y="24" font-family="'Segoe UI', sans-serif" font-size="11" fill="#d8b4fe">PostgreSQL Pool / SDK Calls</text>
  </g>

  <!-- ================= TIER 4: CLOUD DATA & STORAGE ================= -->
  <g transform="translate(40, 660)">
    <rect width="1170" height="135" rx="12" fill="url(#tierGrad)" stroke="#f59e0b" stroke-width="1.5" stroke-opacity="0.6" filter="url(#shadow)" />
    <rect x="25" y="-12" width="270" height="24" rx="6" fill="#f59e0b" />
    <text x="160" y="5" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">TIER 4: SUPABASE CLOUD &amp; DATA LAYER</text>

    <!-- Subsystem 1: PostgreSQL Relational DB -->
    <rect x="30" y="25" width="260" height="95" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="50" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#fbbf24">PostgreSQL Relational DB</text>
    <text x="50" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Profiles &amp; roles tables</text>
    <text x="50" y="93" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Carbon_calculations &amp; logs</text>

    <!-- Subsystem 2: Row Level Security (RLS) -->
    <rect x="315" y="25" width="270" height="95" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="335" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Row Level Security (RLS)</text>
    <text x="335" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Granular SQL tenant isolation</text>
    <text x="335" y="93" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• auth.uid() owner enforcement</text>

    <!-- Subsystem 3: Supabase Auth & Storage -->
    <rect x="610" y="25" width="260" height="95" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="630" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Auth &amp; Cloud Storage</text>
    <text x="630" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Secure JWT issuance &amp; refresh</text>
    <text x="630" y="93" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Avatars &amp; screenshot buckets</text>

    <!-- Subsystem 4: External Groq API Service -->
    <rect x="895" y="25" width="245" height="95" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
    <text x="915" y="52" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Groq Cloud Inference</text>
    <text x="915" y="73" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• High-throughput LPU hardware</text>
    <text x="915" y="93" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Ultra-low token latency</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_5_7_proposed_system_architecture.svg"), "w", encoding="utf-8") as f:
    f.write(svg_5_7)

# -------------------------------------------------------------
# 3. Figure 9.1: Performance Comparison & Benchmark Analysis
# -------------------------------------------------------------
svg_9_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1150 720" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="greenBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#34d399" />
    </linearGradient>
    <linearGradient id="redBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444" />
      <stop offset="100%" stop-color="#f87171" />
    </linearGradient>
    <linearGradient id="blueBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#60a5fa" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1150" height="720" rx="16" fill="url(#bgGrad)" />
  <rect x="2" y="2" width="1146" height="716" rx="14" fill="none" stroke="#334155" stroke-width="2" />

  <!-- Title Badge -->
  <rect x="330" y="25" width="490" height="44" rx="22" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="1.8" />
  <text x="575" y="53" font-family="'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#34d399" text-anchor="middle">FIGURE 9.1: BENCHMARK &amp; PERFORMANCE COMPARISON</text>

  <!-- Legend -->
  <g transform="translate(380, 85)">
    <rect x="0" y="0" width="16" height="16" rx="4" fill="url(#greenBar)" />
    <text x="24" y="13" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f8fafc">EcoTrack Platform</text>

    <rect x="180" y="0" width="16" height="16" rx="4" fill="url(#redBar)" />
    <text x="204" y="13" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f8fafc">Existing Conventional Tools</text>
  </g>

  <!-- Chart Container -->
  <g transform="translate(60, 125)">
    <rect width="1030" height="400" rx="12" fill="url(#cardBg)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)" />

    <!-- Metric 1: Mathematical Accuracy & Determinism -->
    <g transform="translate(40, 40)">
      <text x="0" y="0" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Calculation Determinism &amp; Standard Adherence</text>
      <!-- EcoTrack Bar -->
      <rect x="0" y="12" width="600" height="24" rx="6" fill="url(#greenBar)" />
      <text x="615" y="29" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399">100% (IPCC/EPA/DEFRA)</text>
      <!-- Existing Bar -->
      <rect x="0" y="42" width="370" height="24" rx="6" fill="url(#redBar)" />
      <text x="385" y="59" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f87171">61.7% (Ad-hoc Estimates)</text>
    </g>

    <!-- Metric 2: Category Coverage & Granularity -->
    <g transform="translate(40, 125)">
      <text x="0" y="0" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Emission Category Granularity (7 Categories)</text>
      <!-- EcoTrack Bar -->
      <rect x="0" y="12" width="580" height="24" rx="6" fill="url(#greenBar)" />
      <text x="595" y="29" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399">96.7% Granular Scope</text>
      <!-- Existing Bar -->
      <rect x="0" y="42" width="220" height="24" rx="6" fill="url(#redBar)" />
      <text x="235" y="59" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f87171">36.7% (Only 2-3 fields)</text>
    </g>

    <!-- Metric 3: AI Recommendation Actionability -->
    <g transform="translate(40, 210)">
      <text x="0" y="0" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">AI Personalization &amp; Actionability Index</text>
      <!-- EcoTrack Bar -->
      <rect x="0" y="12" width="570" height="24" rx="6" fill="url(#greenBar)" />
      <text x="585" y="29" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399">95.0% Contextual Relevance</text>
      <!-- Existing Bar -->
      <rect x="0" y="42" width="110" height="24" rx="6" fill="url(#redBar)" />
      <text x="125" y="59" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f87171">18.3% (Static generic text)</text>
    </g>

    <!-- Metric 4: User Engagement & Habit Retention -->
    <g transform="translate(40, 295)">
      <text x="0" y="0" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">User Habit Retention &amp; Goal Follow-through</text>
      <!-- EcoTrack Bar -->
      <rect x="0" y="12" width="510" height="24" rx="6" fill="url(#greenBar)" />
      <text x="525" y="29" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399">85.0% (Gamified Badges)</text>
      <!-- Existing Bar -->
      <rect x="0" y="42" width="130" height="24" rx="6" fill="url(#redBar)" />
      <text x="145" y="59" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f87171">21.7% (Single visit churn)</text>
    </g>
  </g>

  <!-- Metric Summary Cards at Bottom -->
  <g transform="translate(60, 550)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="235" height="135" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.2" filter="url(#shadow)" />
    <text x="20" y="32" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#94a3b8">CALCULATION SPEED</text>
    <text x="20" y="70" font-family="'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#34d399">&lt; 4.2 ms</text>
    <text x="20" y="98" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">28x faster than cloud legacy APIs</text>
    <rect x="20" y="112" width="195" height="4" rx="2" fill="#10b981" />

    <!-- Card 2 -->
    <rect x="265" y="0" width="235" height="135" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.2" filter="url(#shadow)" />
    <text x="285" y="32" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#94a3b8">GROQ AI INFERENCE</text>
    <text x="285" y="70" font-family="'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#60a5fa">1.18 s</text>
    <text x="285" y="98" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">High-speed gpt-oss-120b tokens</text>
    <rect x="285" y="112" width="195" height="4" rx="2" fill="#3b82f6" />

    <!-- Card 3 -->
    <rect x="530" y="0" width="235" height="135" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.2" filter="url(#shadow)" />
    <text x="550" y="32" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#94a3b8">SYSTEM USABILITY SCORE</text>
    <text x="550" y="70" font-family="'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#c084fc">89.4 / 100</text>
    <text x="550" y="98" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">Grade 'A' Usability Rating</text>
    <rect x="550" y="112" width="195" height="4" rx="2" fill="#8b5cf6" />

    <!-- Card 4 -->
    <rect x="795" y="0" width="235" height="135" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2" filter="url(#shadow)" />
    <text x="815" y="32" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#94a3b8">AVG EMISSION REDUCTION</text>
    <text x="815" y="70" font-family="'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#fbbf24">-22.4%</text>
    <text x="815" y="98" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">Per active user across 60 days</text>
    <rect x="815" y="112" width="195" height="4" rx="2" fill="#f59e0b" />
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_9_1_performance_comparison.svg"), "w", encoding="utf-8") as f:
    f.write(svg_9_1)

# -------------------------------------------------------------
# 4. Figure 5.1: System Data Flow Pipeline Diagram
# -------------------------------------------------------------
svg_pipeline = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#334155" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="480" rx="16" fill="url(#bgGrad)" />
  <rect x="2" y="2" width="1196" height="476" rx="14" fill="none" stroke="#334155" stroke-width="2" />

  <!-- Title Badge -->
  <rect x="370" y="25" width="460" height="44" rx="22" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="1.8" />
  <text x="600" y="53" font-family="'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#60a5fa" text-anchor="middle">FIGURE 5.1: END-TO-END DATA PROCESSING PIPELINE</text>

  <!-- 5 Horizontal Steps -->
  <!-- Step 1: Input Ingestion -->
  <g transform="translate(40, 110)">
    <rect width="200" height="300" rx="10" fill="url(#stepGrad)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="100" cy="45" r="22" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" />
    <text x="100" y="52" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#38bdf8" text-anchor="middle">01</text>
    <text x="100" y="95" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc" text-anchor="middle">Data Ingestion</text>
    <text x="100" y="125" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• 7 Category Inputs</text>
    <text x="100" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Km, kWh, Litres, Diet</text>
    <text x="100" y="175" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Numerical clamping</text>
    <text x="100" y="200" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Express validator</text>
    <rect x="25" y="245" width="150" height="30" rx="6" fill="#38bdf8" fill-opacity="0.15" />
    <text x="100" y="265" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#38bdf8" text-anchor="middle">Sanitized Payload</text>
  </g>

  <!-- Arrow 1-2 -->
  <path d="M 245 260 L 275 260" stroke="#38bdf8" stroke-width="3" fill="none" />
  <polygon points="280,260 270,254 270,266" fill="#38bdf8" />

  <!-- Step 2: Deterministic Engine -->
  <g transform="translate(285, 110)">
    <rect width="200" height="300" rx="10" fill="url(#stepGrad)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="100" cy="45" r="22" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2" />
    <text x="100" y="52" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#10b981" text-anchor="middle">02</text>
    <text x="100" y="95" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc" text-anchor="middle">Calc Engine</text>
    <text x="100" y="125" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• IPCC / EPA factors</text>
    <text x="100" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• 7 Category emissions</text>
    <text x="100" y="175" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Total kg CO₂e sum</text>
    <text x="100" y="200" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Eco Score (0-100)</text>
    <rect x="25" y="245" width="150" height="30" rx="6" fill="#10b981" fill-opacity="0.15" />
    <text x="100" y="265" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#34d399" text-anchor="middle">Deterministic Stats</text>
  </g>

  <!-- Arrow 2-3 -->
  <path d="M 490 260 L 520 260" stroke="#10b981" stroke-width="3" fill="none" />
  <polygon points="525,260 515,254 515,266" fill="#10b981" />

  <!-- Step 3: Groq AI Synthesis -->
  <g transform="translate(530, 110)">
    <rect width="200" height="300" rx="10" fill="url(#stepGrad)" stroke="#8b5cf6" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="100" cy="45" r="22" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="2" />
    <text x="100" y="52" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#8b5cf6" text-anchor="middle">03</text>
    <text x="100" y="95" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc" text-anchor="middle">Groq AI Inference</text>
    <text x="100" y="125" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• gpt-oss-120b LPU</text>
    <text x="100" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Category sorting</text>
    <text x="100" y="175" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Strict JSON schema</text>
    <text x="100" y="200" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Actionable eco-tips</text>
    <rect x="25" y="245" width="150" height="30" rx="6" fill="#8b5cf6" fill-opacity="0.15" />
    <text x="100" y="265" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#c084fc" text-anchor="middle">AI Recommendation</text>
  </g>

  <!-- Arrow 3-4 -->
  <path d="M 735 260 L 765 260" stroke="#8b5cf6" stroke-width="3" fill="none" />
  <polygon points="770,260 760,254 760,266" fill="#8b5cf6" />

  <!-- Step 4: Supabase Persistence & RLS -->
  <g transform="translate(775, 110)">
    <rect width="200" height="300" rx="10" fill="url(#stepGrad)" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="100" cy="45" r="22" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" />
    <text x="100" y="52" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f59e0b" text-anchor="middle">04</text>
    <text x="100" y="95" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc" text-anchor="middle">Data Persistence</text>
    <text x="100" y="125" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Supabase PostgreSQL</text>
    <text x="100" y="150" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Row-Level Security</text>
    <text x="100" y="175" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Historical log update</text>
    <text x="100" y="200" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">• Time-series snapshot</text>
    <rect x="25" y="245" width="150" height="30" rx="6" fill="#f59e0b" fill-opacity="0.15" />
    <text x="100" y="265" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#fbbf24" text-anchor="middle">Secure Audit Record</text>
  </g>

  <!-- Arrow 4-5 -->
  <path d="M 980 260 L 1010 260" stroke="#f59e0b" stroke-width="3" fill="none" />
  <polygon points="1015,260 1005,254 1005,266" fill="#f59e0b" />

  <!-- Step 5: Visualization & Export -->
  <g transform="translate(1020, 110)">
    <rect width="140" height="300" rx="10" fill="url(#stepGrad)" stroke="#ec4899" stroke-width="1.5" filter="url(#shadow)" />
    <circle cx="70" cy="45" r="22" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="2" />
    <text x="70" y="52" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#ec4899" text-anchor="middle">05</text>
    <text x="70" y="95" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#f8fafc" text-anchor="middle">Presentation</text>
    <text x="70" y="125" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">• Chart.js UI</text>
    <text x="70" y="150" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">• PDF Export</text>
    <text x="70" y="175" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">• Certificate</text>
    <text x="70" y="200" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">• CSV Log</text>
    <rect x="15" y="245" width="110" height="30" rx="6" fill="#ec4899" fill-opacity="0.15" />
    <text x="70" y="265" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="600" fill="#f472b6" text-anchor="middle">Verified Output</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_data_flow_pipeline.svg"), "w", encoding="utf-8") as f:
    f.write(svg_pipeline)

# -------------------------------------------------------------
# 5. Appendix B SVG Visualizations: Figures B.1 to B.5
# -------------------------------------------------------------

# Figure B.1: Auth & Profile Page
svg_b1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgB1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" /><stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="primaryBtn" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" /><stop offset="100%" stop-color="#059669" />
    </linearGradient>
  </defs>
  <rect width="1000" height="600" rx="16" fill="url(#bgB1)" stroke="#334155" stroke-width="2"/>
  <rect x="250" y="20" width="500" height="40" rx="20" fill="#10b981" fill-opacity="0.15" stroke="#10b981"/>
  <text x="500" y="46" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#34d399" text-anchor="middle">FIGURE B.1: AUTHENTICATION &amp; PROFILE MANAGEMENT PAGE</text>

  <!-- Login Card Mockup -->
  <g transform="translate(150, 90)">
    <rect width="320" height="460" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="160" y="50" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">Welcome to EcoTrack</text>
    <text x="160" y="75" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Sign in to track your carbon footprint</text>
    
    <!-- Input 1 -->
    <text x="30" y="125" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">Email Address</text>
    <rect x="30" y="135" width="260" height="40" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="160" font-family="'Segoe UI', sans-serif" font-size="13" fill="#64748b">user@ecotrack.org</text>

    <!-- Input 2 -->
    <text x="30" y="205" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">Password</text>
    <rect x="30" y="215" width="260" height="40" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="240" font-family="'Segoe UI', sans-serif" font-size="14" fill="#64748b">••••••••••••</text>

    <!-- Button -->
    <rect x="30" y="285" width="260" height="44" rx="6" fill="url(#primaryBtn)"/>
    <text x="160" y="312" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">Secure Sign In</text>

    <!-- Footer links -->
    <text x="160" y="365" font-family="'Segoe UI', sans-serif" font-size="12" fill="#38bdf8" text-anchor="middle">Create an account • Forgot password?</text>
    <rect x="40" y="400" width="240" height="36" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="160" y="423" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">🔒 Protected by Supabase JWT &amp; RLS</text>
  </g>

  <!-- Profile Settings Mockup -->
  <g transform="translate(530, 90)">
    <rect width="320" height="460" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <circle cx="160" cy="65" r="35" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
    <text x="160" y="73" font-family="'Segoe UI', sans-serif" font-size="28" fill="#34d399" text-anchor="middle">🌱</text>
    <text x="160" y="125" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="700" fill="#f8fafc" text-anchor="middle">Raghavan S.</text>
    <text x="160" y="145" font-family="'Segoe UI', sans-serif" font-size="12" fill="#34d399" text-anchor="middle">Tier: Eco Conscious (Score 78/100)</text>

    <rect x="30" y="175" width="260" height="60" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="45" y="200" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Default Location &amp; Grid</text>
    <text x="45" y="222" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f8fafc">India / Southern Regional Grid</text>

    <rect x="30" y="250" width="260" height="60" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="45" y="275" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Household Size</text>
    <text x="45" y="297" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#f8fafc">3 Members (Normalized Baseline)</text>

    <rect x="30" y="325" width="260" height="60" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="45" y="350" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Account Status &amp; Role</text>
    <text x="45" y="372" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600" fill="#34d399">Verified Carbon Auditor (Standard)</text>

    <rect x="30" y="405" width="260" height="36" rx="6" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6"/>
    <text x="160" y="428" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#60a5fa" text-anchor="middle">Update Profile Preferences</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_b1_auth_flow.svg"), "w", encoding="utf-8") as f:
    f.write(svg_b1)

# Figure B.2: Footprint Calculator Interface
svg_b2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="100%" height="100%">
  <defs>
    <linearGradient id="bgB2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" /><stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>
  <rect width="1000" height="620" rx="16" fill="url(#bgB2)" stroke="#334155" stroke-width="2"/>
  <rect x="230" y="20" width="540" height="40" rx="20" fill="#10b981" fill-opacity="0.15" stroke="#10b981"/>
  <text x="500" y="46" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#34d399" text-anchor="middle">FIGURE B.2: 7-CATEGORY CARBON FOOTPRINT CALCULATOR</text>

  <!-- Left Form Grid -->
  <g transform="translate(50, 80)">
    <rect width="520" height="500" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="30" y="40" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Monthly Carbon Activity Audit</text>

    <!-- Field 1: Transport -->
    <text x="30" y="80" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1">1. Transportation Mode &amp; Distance</text>
    <rect x="30" y="90" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="113" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Petrol Car (0.192 kg/km)</text>
    <rect x="270" y="90" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="285" y="113" font-family="'Segoe UI', sans-serif" font-size="12" fill="#34d399">450 km / month</text>

    <!-- Field 2: Electricity -->
    <text x="30" y="155" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1">2. Electricity &amp; Renewable Share</text>
    <rect x="30" y="165" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="188" font-family="'Segoe UI', sans-serif" font-size="12" fill="#34d399">210 kWh / month</text>
    <rect x="270" y="165" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="285" y="188" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">15% Rooftop Solar</text>

    <!-- Field 3: Food / Diet -->
    <text x="30" y="230" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1">3. Food &amp; Dietary Pattern</text>
    <rect x="30" y="240" width="460" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="263" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">Vegetarian Diet (1.70 kg CO₂e / day)</text>

    <!-- Field 4: Waste & Recycling -->
    <text x="30" y="305" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1">4. Municipal Waste &amp; Recycling %</text>
    <rect x="30" y="315" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="338" font-family="'Segoe UI', sans-serif" font-size="12" fill="#34d399">35 kg / month</text>
    <rect x="270" y="315" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="285" y="338" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">40% Recycled / Composted</text>

    <!-- Field 5: Shopping & Travel -->
    <text x="30" y="380" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1">5. Shopping Goods &amp; Flights</text>
    <rect x="30" y="390" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="45" y="413" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">2 Clothes, 0 Electronics</text>
    <rect x="270" y="390" width="220" height="36" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="285" y="413" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8">1 Domestic Flight (250 kg)</text>

    <!-- Action Button -->
    <rect x="30" y="445" width="460" height="40" rx="8" fill="#10b981"/>
    <text x="260" y="470" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#042f1a" text-anchor="middle">⚡ Compute Deterministic Emissions &amp; Generate AI Plan</text>
  </g>

  <!-- Right Summary Card -->
  <g transform="translate(600, 80)">
    <rect width="350" height="500" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="175" y="40" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="700" fill="#f8fafc" text-anchor="middle">Live Calculation Result</text>

    <!-- Eco Score Circle -->
    <circle cx="175" cy="130" r="60" fill="#0f172a" stroke="#10b981" stroke-width="8"/>
    <text x="175" y="125" font-family="'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#34d399" text-anchor="middle">78.5</text>
    <text x="175" y="148" font-family="'Segoe UI', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">ECO SCORE / 100</text>

    <rect x="60" y="205" width="230" height="32" rx="16" fill="#10b981" fill-opacity="0.2"/>
    <text x="175" y="226" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">Tier: Eco Conscious</text>

    <!-- Total CO2 -->
    <rect x="40" y="255" width="270" height="65" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="175" y="280" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">TOTAL MONTHLY EMISSIONS</text>
    <text x="175" y="306" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">430.40 kg CO₂e</text>

    <!-- Category Breakdown Mini Table -->
    <g transform="translate(45, 335)">
      <text x="0" y="18" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Travel (Flights):</text>
      <text x="250" y="18" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#f87171" text-anchor="end">250.00 kg</text>

      <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Transportation:</text>
      <text x="250" y="40" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#fbbf24" text-anchor="end">86.40 kg</text>

      <text x="0" y="62" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Electricity (Grid):</text>
      <text x="250" y="62" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#60a5fa" text-anchor="end">84.79 kg</text>

      <text x="0" y="84" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">• Diet &amp; Waste:</text>
      <text x="250" y="84" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="end">63.20 kg</text>
    </g>

    <rect x="40" y="445" width="270" height="34" rx="6" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6"/>
    <text x="175" y="467" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#60a5fa" text-anchor="middle">📥 Export Audit Report (PDF)</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_b2_calculator_flow.svg"), "w", encoding="utf-8") as f:
    f.write(svg_b2)

# Figure B.3: Analytics Dashboard
svg_b3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgB3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" /><stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>
  <rect width="1000" height="600" rx="16" fill="url(#bgB3)" stroke="#334155" stroke-width="2"/>
  <rect x="250" y="20" width="500" height="40" rx="20" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6"/>
  <text x="500" y="46" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#60a5fa" text-anchor="middle">FIGURE B.3: INTERACTIVE ANALYTICS &amp; EMISSION TRENDS</text>

  <!-- Left: Doughnut Breakdown -->
  <g transform="translate(50, 85)">
    <rect width="420" height="480" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="210" y="40" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">Category Breakdown (Chart.js)</text>
    
    <!-- Doughnut representation -->
    <circle cx="210" cy="190" r="100" fill="none" stroke="#ef4444" stroke-width="38" stroke-dasharray="210 628" />
    <circle cx="210" cy="190" r="100" fill="none" stroke="#f59e0b" stroke-width="38" stroke-dasharray="160 628" stroke-dashoffset="-210" />
    <circle cx="210" cy="190" r="100" fill="none" stroke="#3b82f6" stroke-width="38" stroke-dasharray="140 628" stroke-dashoffset="-370" />
    <circle cx="210" cy="190" r="100" fill="none" stroke="#10b981" stroke-width="38" stroke-dasharray="118 628" stroke-dashoffset="-510" />
    <text x="210" y="185" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="700" fill="#f8fafc" text-anchor="middle">430 kg</text>
    <text x="210" y="205" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Total CO₂e</text>

    <!-- Legend -->
    <g transform="translate(60, 330)">
      <rect x="0" y="0" width="12" height="12" rx="3" fill="#ef4444"/>
      <text x="20" y="10" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">Flights &amp; Long Travel (58%)</text>

      <rect x="0" y="25" width="12" height="12" rx="3" fill="#f59e0b"/>
      <text x="20" y="35" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">Ground Transport (20%)</text>

      <rect x="0" y="50" width="12" height="12" rx="3" fill="#3b82f6"/>
      <text x="20" y="60" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">Electricity Grid (14%)</text>

      <rect x="0" y="75" width="12" height="12" rx="3" fill="#10b981"/>
      <text x="20" y="85" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">Diet, Waste &amp; Shopping (8%)</text>
    </g>
  </g>

  <!-- Right: Historical Trend Line Chart -->
  <g transform="translate(500, 85)">
    <rect width="450" height="480" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="225" y="40" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc" text-anchor="middle">6-Month Historical Reduction Trend</text>

    <!-- Chart Grid Lines -->
    <g transform="translate(50, 70)">
      <line x1="0" y1="50" x2="350" y2="50" stroke="#334155" stroke-dasharray="4,4"/>
      <text x="-10" y="54" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b" text-anchor="end">600 kg</text>

      <line x1="0" y1="120" x2="350" y2="120" stroke="#334155" stroke-dasharray="4,4"/>
      <text x="-10" y="124" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b" text-anchor="end">450 kg</text>

      <line x1="0" y1="190" x2="350" y2="190" stroke="#334155" stroke-dasharray="4,4"/>
      <text x="-10" y="194" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b" text-anchor="end">300 kg</text>

      <line x1="0" y1="260" x2="350" y2="260" stroke="#475569"/>
      <text x="-10" y="264" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b" text-anchor="end">0 kg</text>

      <!-- Month Labels -->
      <text x="30" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">May</text>
      <text x="95" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Jun</text>
      <text x="160" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Jul</text>
      <text x="225" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Aug</text>
      <text x="290" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">Sep</text>

      <!-- Downward Trend Path -->
      <path d="M 35 60 L 100 85 L 165 110 L 230 135 L 295 155" fill="none" stroke="#10b981" stroke-width="3.5" />
      <!-- Dots -->
      <circle cx="35" cy="60" r="5" fill="#34d399"/>
      <circle cx="100" cy="85" r="5" fill="#34d399"/>
      <circle cx="165" cy="110" r="5" fill="#34d399"/>
      <circle cx="230" cy="135" r="5" fill="#34d399"/>
      <circle cx="295" cy="155" r="6" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
    </g>

    <!-- Stat Callout -->
    <rect x="40" y="380" width="370" height="70" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="60" y="408" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#34d399">📉 -26.8% Reduction Verified</text>
    <text x="60" y="430" font-family="'Segoe UI', sans-serif" font-size="11" fill="#cbd5e1">Saved 162.4 kg CO₂e since onboarding through smart routing.</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_b3_analytics_dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(svg_b3)

# Figure B.4: Groq AI Eco-Coach Page
svg_b4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgB4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" /><stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>
  <rect width="1000" height="600" rx="16" fill="url(#bgB4)" stroke="#334155" stroke-width="2"/>
  <rect x="240" y="20" width="520" height="40" rx="20" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6"/>
  <text x="500" y="46" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#c084fc" text-anchor="middle">FIGURE B.4: GROQ AI ECO-COACH RECOMMENDATION INTERFACE</text>

  <!-- Coach Panel -->
  <g transform="translate(80, 85)">
    <rect width="840" height="475" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>

    <!-- Header bar -->
    <g transform="translate(30, 25)">
      <circle cx="25" cy="25" r="22" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="2"/>
      <text x="25" y="32" font-family="'Segoe UI', sans-serif" font-size="18" fill="#c084fc" text-anchor="middle">🤖</text>
      <text x="60" y="24" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#f8fafc">Groq AI Eco-Coach (gpt-oss-120b)</text>
      <text x="60" y="42" font-family="'Segoe UI', sans-serif" font-size="11" fill="#34d399">⚡ Fast LPU Inference • Personalized from deterministic score</text>
    </g>

    <!-- Overall Analysis Box -->
    <rect x="30" y="85" width="780" height="65" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="50" y="110" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#c084fc">EXECUTIVE SUMMARY</text>
    <text x="50" y="132" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1">"Great effort Raghavan! Your score of 78.5 places you in the top 25% of energy conservers. Your highest impact comes from short-haul flights and petrol car commutes."</text>

    <!-- Tip Cards Grid -->
    <g transform="translate(30, 165)">
      <!-- Tip 1 -->
      <rect x="0" y="0" width="375" height="110" rx="8" fill="#0f172a" stroke="#475569"/>
      <text x="20" y="28" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#38bdf8">✈️ Travel Optimization</text>
      <text x="20" y="52" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Replace 1 short domestic flight with an electrified train trip.</text>
      <text x="20" y="72" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Estimated Monthly Saving: ~200 kg CO₂e.</text>
      <text x="20" y="92" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#34d399">Impact: High (Primary reduction lever)</text>

      <!-- Tip 2 -->
      <rect x="405" y="0" width="375" height="110" rx="8" fill="#0f172a" stroke="#475569"/>
      <text x="425" y="28" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#34d399">🚗 Commute Substitution</text>
      <text x="425" y="52" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Carpool or switch 2 commute days to public metro transit.</text>
      <text x="425" y="72" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8">• Reduces 120 km of petrol car usage per month.</text>
      <text x="425" y="92" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#34d399">Impact: Medium-High (~23 kg CO₂e saved)</text>

      <!-- Challenge Box -->
      <rect x="0" y="125" width="780" height="85" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
      <text x="20" y="152" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#fbbf24">🎯 GREEN WEEKLY CHALLENGE</text>
      <text x="20" y="174" font-family="'Segoe UI', sans-serif" font-size="12" fill="#f8fafc">"Zero Waste Weekend: Cook all meals with fresh local produce and avoid packaged delivery to save 8.5 kg CO₂!"</text>
      <text x="20" y="195" font-family="'Segoe UI', sans-serif" font-size="11" fill="#34d399">🏆 Earn 50 Eco-Points + 'Zero-Waste Pioneer' Badge upon completion.</text>
    </g>

    <!-- Bottom Buttons -->
    <rect x="30" y="420" width="220" height="36" rx="6" fill="#10b981"/>
    <text x="140" y="443" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#042f1a" text-anchor="middle">Accept Monthly Goal</text>

    <rect x="270" y="420" width="220" height="36" rx="6" fill="#1e293b" stroke="#3b82f6"/>
    <text x="380" y="443" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#60a5fa" text-anchor="middle">Ask AI Eco-Coach a Question</text>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_b4_ai_coach.svg"), "w", encoding="utf-8") as f:
    f.write(svg_b4)

# Figure B.5: Audit Certificate & PDF Export
svg_b5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="100%" height="100%">
  <defs>
    <linearGradient id="bgB5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" /><stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="certBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" /><stop offset="100%" stop-color="#f8fafc" />
    </linearGradient>
  </defs>
  <rect width="1000" height="620" rx="16" fill="url(#bgB5)" stroke="#334155" stroke-width="2"/>
  <rect x="230" y="20" width="540" height="40" rx="20" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b"/>
  <text x="500" y="46" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#fbbf24" text-anchor="middle">FIGURE B.5: OFFICIAL ENVIRONMENTAL AUDIT CERTIFICATE</text>

  <!-- Certificate Paper Mockup -->
  <g transform="translate(160, 85)">
    <rect width="680" height="490" rx="8" fill="url(#certBg)" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="15" y="15" width="650" height="460" rx="4" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="8,4"/>

    <!-- Header -->
    <text x="340" y="65" font-family="'Georgia', serif" font-size="24" font-weight="700" fill="#065f46" text-anchor="middle">EcoTrack Sustainability Certification</text>
    <text x="340" y="88" font-family="'Segoe UI', sans-serif" font-size="12" fill="#475569" text-anchor="middle">Official Verified Greenhouse Gas (GHG) Audit Statement</text>
    <line x1="220" y1="102" x2="460" y2="102" stroke="#059669" stroke-width="1.5"/>

    <!-- Body text -->
    <text x="340" y="145" font-family="'Segoe UI', sans-serif" font-size="13" fill="#334155" text-anchor="middle">This document certifies that the household carbon footprint of</text>
    <text x="340" y="180" font-family="'Georgia', serif" font-size="22" font-weight="700" fill="#0f172a" text-anchor="middle">Raghavan S.</text>
    <text x="340" y="210" font-family="'Segoe UI', sans-serif" font-size="13" fill="#334155" text-anchor="middle">has been audited using standardized IPCC/EPA/DEFRA emission factor protocols.</text>

    <!-- Metrics box -->
    <rect x="80" y="235" width="520" height="95" rx="6" fill="#f0fdf4" stroke="#a7f3d0"/>
    <g transform="translate(100, 260)">
      <text x="50" y="20" font-family="'Segoe UI', sans-serif" font-size="11" fill="#065f46">COMPUTED EMISSIONS</text>
      <text x="50" y="48" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#065f46">430.40 kg CO₂e</text>

      <text x="240" y="20" font-family="'Segoe UI', sans-serif" font-size="11" fill="#065f46">OFFICIAL ECO SCORE</text>
      <text x="240" y="48" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#059669">78.5 / 100</text>

      <text x="400" y="20" font-family="'Segoe UI', sans-serif" font-size="11" fill="#065f46">RATING TIER</text>
      <text x="400" y="48" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="700" fill="#047857">Eco Conscious</text>
    </g>

    <!-- Verification Hash & Stamp -->
    <text x="80" y="365" font-family="'Courier New', monospace" font-size="10" fill="#64748b">Verification Hash: 8f4a-9b21-ecotrack-785a-04b391c78e</text>
    <text x="80" y="382" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Audited on: 2026-10-27 | Supabase Cloud Immutable Ledger</text>

    <!-- Signatures -->
    <g transform="translate(80, 415)">
      <line x1="0" y1="20" x2="180" y2="20" stroke="#94a3b8"/>
      <text x="90" y="35" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Automated Verification Officer</text>

      <line x1="340" y1="20" x2="520" y2="20" stroke="#94a3b8"/>
      <text x="430" y="35" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b" text-anchor="middle">EcoTrack Certification Engine</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(DIAGRAMS_DIR, "figure_b5_export_certification.svg"), "w", encoding="utf-8") as f:
    f.write(svg_b5)

print("Successfully generated all 9 SVG diagrams in:", DIAGRAMS_DIR)
