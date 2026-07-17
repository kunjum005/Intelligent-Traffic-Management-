import os
import shutil
import streamlit as st

from modules.detector import load_model
from modules.video_processor import open_video
from modules.report_generator import generate_report
from modules.database import save_report

from modules.prompt_builder import build_traffic_prompt
from modules.llm_service import generate_ai_report

from modules.dashboard_utils import (
    load_css,
    page_header,
    section,
    show_statistics,
    show_charts,
    show_report_history
)

# -------------------------------------
# Streamlit Page
# -------------------------------------

st.set_page_config(
    page_title="Traffic Management",
    page_icon="🚦",
    layout="wide"
)

load_css()
page_header()

# -------------------------------------
# Session State
# -------------------------------------

if "report" not in st.session_state:
    st.session_state.report = None

if "ai_report" not in st.session_state:
    st.session_state.ai_report = None

if "output_video" not in st.session_state:
    st.session_state.output_video = None

if "original_video" not in st.session_state:
    st.session_state.original_video = None

# -------------------------------------
# Load YOLO
# -------------------------------------

@st.cache_resource
def get_model():
    return load_model()

model = get_model()





section("📤 Upload Traffic Video")

uploaded_file = st.file_uploader(
    "Choose a Traffic Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_file:

    temp_path = os.path.join(
        "temp",
        uploaded_file.name
    )

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    st.success("Video Uploaded Successfully!")

    if st.button("🚀 Analyze Video"):

        with st.spinner("Analyzing Traffic..."):

            cap = open_video(temp_path)

            output_path = os.path.join(
                "output",
                "processed_" + uploaded_file.name
            )

            report = generate_report(
                model=model,
                cap=cap,
                output_path=output_path,
                frame_skip=10
            )

            st.session_state.report = report
            st.session_state.output_video = output_path
            st.session_state.original_video = temp_path

            try:

                save_report(
                    location="Uploaded Video",
                    video_name=uploaded_file.name,
                    counts=report["counts"],
                    total=report["total"],
                    density=report["density"],
                    signal_time=report["signal_time"]
                )

            except Exception as e:

                st.warning(f"MySQL Error : {e}")

            # -----------------------------
            # Generate AI automatically
            # -----------------------------

            prompt = build_traffic_prompt(
                report,
                location="Uploaded Video"
            )

            print("Calling Gemini...")

            st.session_state.ai_report = generate_ai_report(prompt)
            print("SESSION AI REPORT:")
            print(st.session_state.ai_report)

            print("Gemini Finished")

        st.success("Analysis Completed!")
    
    


# ==========================================================
# Show Results (After Analysis)
# ==========================================================

if st.session_state.report is not None:

    report = st.session_state.report

    # -------------------------------------
    # Video Comparison
    # -------------------------------------

    section("🎥 Video Comparison")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Video")
        st.video(st.session_state.original_video)

    with col2:

        st.subheader("Processed Video")

        if (
            st.session_state.output_video is not None
            and os.path.exists(st.session_state.output_video)
        ):
            st.video(st.session_state.output_video)
        else:
            st.warning("Processed video not available.")

    st.divider()

    # -------------------------------------
    # Statistics
    # -------------------------------------

    show_statistics(report)

    st.divider()

    # -------------------------------------
    # Charts
    # -------------------------------------

    show_charts(report)

    st.divider()

    # -------------------------------------
    # AI Analysis
    # -------------------------------------

    section("🤖 AI Traffic Analysis")

    if st.session_state.ai_report is not None:
        st.success("✅ AI Report Generated")
        st.markdown(st.session_state.ai_report)
    else:
        st.warning("AI report could not be generated.")
    st.divider()

    # -------------------------------------
    # Database History
    # -------------------------------------

    show_report_history()