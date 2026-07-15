import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from parallel.engine import run_parallel

# ==============================================================================
# PAGE CONFIG
# ==============================================================================
st.set_page_config(
    page_title="AutoPrepX | Smart Data Preprocessing",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# THEME / CUSTOM CSS
# ==============================================================================
PRIMARY = "#6C5CE7"
PRIMARY_DARK = "#4834D4"
ACCENT = "#00CEC9"
BG_SOFT = "#F7F7FD"
TEXT_DARK = "#1E1E2E"
MUTED = "#6B7280"

sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#FFFFFF", "figure.facecolor": "#FFFFFF"})

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"]  {{
            font-family: 'Inter', sans-serif;
        }}

        .stApp {{
            background: {BG_SOFT};
        }}

        #MainMenu, footer {{visibility: hidden;}}

        .hero-wrap {{
            background: linear-gradient(120deg, {PRIMARY} 0%, {PRIMARY_DARK} 55%, #2D1F8F 100%);
            border-radius: 22px;
            padding: 2.6rem 2.8rem;
            margin-bottom: 1.6rem;
            box-shadow: 0 12px 30px rgba(76, 52, 212, 0.25);
            position: relative;
            overflow: hidden;
        }}
        .hero-wrap::after {{
            content: "";
            position: absolute;
            right: -60px; top: -60px;
            width: 220px; height: 220px;
            background: radial-gradient(circle, rgba(0,206,201,0.35) 0%, rgba(0,206,201,0) 70%);
        }}
        .hero-badge {{
            display: inline-block;
            background: rgba(255,255,255,0.15);
            color: #fff;
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 0.9rem;
            border: 1px solid rgba(255,255,255,0.25);
        }}
        .hero-title {{
            font-family: 'Poppins', sans-serif;
            font-weight: 800;
            font-size: 2.6rem;
            color: #ffffff;
            margin: 0 0 0.4rem 0;
            line-height: 1.15;
        }}
        .hero-sub {{
            font-size: 1.05rem;
            color: rgba(255,255,255,0.85);
            max-width: 640px;
            margin-bottom: 0;
        }}

        .section-title {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 1.35rem;
            color: {TEXT_DARK};
            margin: 1.6rem 0 0.2rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .section-sub {{
            color: {MUTED};
            font-size: 0.92rem;
            margin-bottom: 1rem;
        }}

        .card {{
            background: #ffffff;
            border-radius: 16px;
            padding: 1.3rem 1.4rem;
            border: 1px solid #EDEBFB;
            box-shadow: 0 4px 14px rgba(30, 30, 46, 0.04);
            height: 100%;
        }}

        .step-track {{
            display: flex;
            justify-content: space-between;
            gap: 0.6rem;
            margin-bottom: 1.8rem;
        }}
        .step-item {{
            flex: 1;
            background: #ffffff;
            border: 1px solid #EDEBFB;
            border-radius: 14px;
            padding: 0.9rem 1rem;
            text-align: left;
            box-shadow: 0 3px 10px rgba(30,30,46,0.03);
        }}
        .step-num {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 26px; height: 26px;
            border-radius: 50%;
            background: {PRIMARY};
            color: #fff;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }}
        .step-item.done .step-num {{ background: {ACCENT}; }}
        .step-label {{
            font-weight: 600;
            font-size: 0.9rem;
            color: {TEXT_DARK};
        }}
        .step-desc {{
            font-size: 0.78rem;
            color: {MUTED};
        }}

        .pill {{
            display: inline-block;
            background: #EDEBFB;
            color: {PRIMARY_DARK};
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.2rem 0.7rem;
            border-radius: 999px;
            margin-right: 0.4rem;
        }}

        .stButton>button {{
            background: linear-gradient(120deg, {PRIMARY}, {PRIMARY_DARK});
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.4rem;
            font-weight: 600;
            font-size: 0.95rem;
            box-shadow: 0 6px 16px rgba(108,92,231,0.35);
            transition: transform 0.15s ease;
        }}
        .stButton>button:hover {{
            transform: translateY(-1px);
            color: #fff;
        }}

        [data-testid="stMetricValue"] {{
            color: {PRIMARY_DARK};
            font-family: 'Poppins', sans-serif;
        }}

        [data-testid="stFileUploaderDropzone"] {{
            background: #ffffff;
            border-radius: 14px;
        }}

        section[data-testid="stSidebar"] {{
            background: #ffffff;
            border-right: 1px solid #EDEBFB;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.4rem;">
            <div style="font-size:1.6rem;">🚀</div>
            <div style="font-family:'Poppins',sans-serif;font-weight:800;font-size:1.15rem;color:{TEXT_DARK};">
                AutoPrepX
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Smart Parallel Data Preprocessing Platform")
    st.divider()

    st.markdown("**📁 Upload Dataset**")
    uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"], label_visibility="collapsed")

    st.divider()
    st.markdown("**⚙️ Pipeline Steps**")
    st.markdown(
        """
        <span class="pill">Missing Values</span><br><br>
        <span class="pill">Outlier Removal</span><br><br>
        <span class="pill">Encoding</span><br><br>
        <span class="pill">Scaling</span>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    st.caption("Built with Streamlit · Pandas · Seaborn")

# ==============================================================================
# HERO
# ==============================================================================
st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-badge">⚡ Parallel Preprocessing Engine</div>
        <div class="hero-title">AutoPrepX</div>
        <p class="hero-sub">
            Upload any CSV, instantly explore data quality, and run a smart
            parallel preprocessing pipeline — missing value imputation, outlier
            removal, encoding, and scaling — in a single click.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# STEP TRACKER
# ==============================================================================
step2_done = uploaded_file is not None
step3_done = step2_done and st.session_state.get("processed", False)

st.markdown(
    f"""
    <div class="step-track">
        <div class="step-item done">
            <div class="step-num">1</div>
            <div class="step-label">Upload CSV</div>
            <div class="step-desc">Bring your raw dataset</div>
        </div>
        <div class="step-item {'done' if step2_done else ''}">
            <div class="step-num">2</div>
            <div class="step-label">Explore Quality</div>
            <div class="step-desc">Missing values & correlations</div>
        </div>
        <div class="step-item {'done' if step3_done else ''}">
            <div class="step-num">3</div>
            <div class="step-label">Run Pipeline</div>
            <div class="step-desc">Clean, encode & scale in parallel</div>
        </div>
        <div class="step-item {'done' if step3_done else ''}">
            <div class="step-num">4</div>
            <div class="step-label">Download</div>
            <div class="step-desc">Export the processed CSV</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# MAIN APP
# ==============================================================================
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # ---------------- ORIGINAL DATASET ----------------
    st.markdown('<div class="section-title">📂 Original Dataset</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">A quick look at the raw data you uploaded.</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Rows", f"{df.shape[0]:,}")
    m2.metric("Columns", df.shape[1])
    m3.metric("Missing Cells", f"{int(df.isnull().sum().sum()):,}")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.dataframe(df.head(10), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- DASHBOARD ----------------
    st.markdown('<div class="section-title">📊 Dataset Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Understand data quality before preprocessing.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Missing Values by Column**")
        missing = df.isnull().sum()
        missing = missing[missing > 0]
        if len(missing) > 0:
            fig, ax = plt.subplots(figsize=(5, 3.2))
            missing.sort_values(ascending=False).plot(kind="bar", ax=ax, color=PRIMARY)
            ax.set_ylabel("Missing count")
            ax.spines[["top", "right"]].set_visible(False)
            st.pyplot(fig, use_container_width=True)
        else:
            st.success("No Missing Values Found ✅")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Correlation Heatmap**")
        numeric_df = df.select_dtypes(include=["number"])
        if numeric_df.shape[1] > 1:
            fig2, ax2 = plt.subplots(figsize=(5, 3.2))
            sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax2, cbar_kws={"shrink": 0.8})
            st.pyplot(fig2, use_container_width=True)
        else:
            st.info("Not Enough Numeric Columns")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- PREPROCESS BUTTON ----------------
    st.markdown('<div class="section-title">⚙️ Data Preprocessing</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Run the parallel pipeline: missing values → outliers → encoding → scaling.</div>', unsafe_allow_html=True)

    run_clicked = st.button("▶  Run Preprocessing")

    if run_clicked:
        st.session_state["processed"] = True

    if st.session_state.get("processed", False):
        with st.spinner("Running parallel preprocessing pipeline..."):
            result = run_parallel(df)

        st.success("✅ Preprocessing Completed Successfully!")

        # ---------------- ORIGINAL VS PROCESSED ----------------
        st.markdown('<div class="section-title">🔍 Original vs Processed</div>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Original Data", "Processed Data"])
        with tab1:
            st.dataframe(df.head(20), use_container_width=True)
        with tab2:
            st.dataframe(result.head(20), use_container_width=True)

        # ---------------- BEFORE VS AFTER METRICS ----------------
        st.markdown('<div class="section-title">📈 Before vs After</div>', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Original Rows", df.shape[0])
        c2.metric("Processed Rows", result.shape[0], delta=int(result.shape[0] - df.shape[0]))
        c3.metric("Original Columns", df.shape[1])
        c4.metric("Processed Columns", result.shape[1], delta=int(result.shape[1] - df.shape[1]))

        # ---------------- FINAL DATASET ----------------
        st.markdown('<div class="section-title">✅ Final Dataset Preview</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.dataframe(result, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- STATISTICS & TYPES ----------------
        st.markdown('<div class="section-title">📋 Statistics & Data Types</div>', unsafe_allow_html=True)
        s1, s2 = st.columns(2)
        with s1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("**Summary Statistics**")
            st.write(result.describe())
            st.markdown('</div>', unsafe_allow_html=True)
        with s2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("**Data Types**")
            st.write(result.dtypes)
            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- DOWNLOAD BUTTON ----------------
        st.markdown('<div class="section-title">⬇ Export</div>', unsafe_allow_html=True)
        csv = result.to_csv(index=False)
        st.download_button(
            label="⬇ Download Processed Dataset",
            data=csv,
            file_name="processed_dataset.csv",
            mime="text/csv",
        )

else:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("👋 Upload a CSV file from the sidebar to begin.")
    st.markdown(
        """
        **What AutoPrepX does for you:**
        - Fills missing values (median / mode strategies)
        - Removes statistical outliers using the IQR method
        - Prepares text/categorical columns for downstream use
        - Normalizes numeric columns
        - Gives you a clean, ready-to-use CSV in one click
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)
