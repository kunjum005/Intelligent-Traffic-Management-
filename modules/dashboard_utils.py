"""
dashboard_utils.py

Utility functions for Streamlit Dashboard.
"""

import streamlit as st
import plotly.express as px
import pandas as pd

from modules.database import get_all_reports


def load_css():

    st.markdown("""
    <style>

    .block-container{
        padding-top:1rem;
        padding-bottom:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    .title{
        font-size:54px;
        font-weight:800;
        text-align:center;
        background:linear-gradient(90deg,#00c6ff,#00ff95);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-bottom:5px;
    }

    .subtitle{
        text-align:center;
        color:#c7c7c7;
        font-size:20px;
        margin-bottom:35px;
    }

    .section{
        font-size:30px;
        font-weight:700;
        color:white;
        margin-top:25px;
        margin-bottom:15px;
    }

    div[data-testid="stMetric"]{
        background:#1d2128;
        border-radius:18px;
        padding:15px;
        border:1px solid #2d323b;
        box-shadow:0px 6px 18px rgba(0,0,0,.35);
        transition:all .3s ease;
    }

    div[data-testid="stMetric"]:hover{
        transform:translateY(-4px);
        border:1px solid #00d4ff;
    }

    div[data-testid="stMetricLabel"]{
        justify-content:center;
        color:#dddddd;
    }

    div[data-testid="stMetricValue"]{
        justify-content:center;
        color:white;
        font-size:34px;
        font-weight:bold;
    }

    div[data-testid="stDataFrame"]{
        border-radius:15px;
        overflow:hidden;
    }

    </style>
    """, unsafe_allow_html=True)

def page_header():

    st.markdown(
        """
        <div class="title">
            🚦 Intelligent Traffic Management System
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            AI Powered Vehicle Detection • Traffic Analysis • Signal Recommendation
        </div>
        """,
        unsafe_allow_html=True
    )


def section(title):

    st.markdown(
        f'<div class="section">{title}</div>',
        unsafe_allow_html=True
    )


def show_statistics(report):

    section("📊 Traffic Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🚗 Cars",
            report["counts"]["Car"]
        )

    with c2:
        st.metric(
            "🏍 Motorcycles",
            report["counts"]["Motorcycle"]
        )

    with c3:
        st.metric(
            "🚌 Buses",
            report["counts"]["Bus"]
        )

    with c4:
        st.metric(
            "🚛 Trucks",
            report["counts"]["Truck"]
        )

    st.write("")

    c5, c6, c7 = st.columns(3)

    with c5:
        st.metric(
            "📈 Average Vehicles",
            report["total"]
        )

    with c6:
        density = report["density"]

        if density == "LOW":
            density = "🟢 LOW"
        elif density == "MEDIUM":
            density = "🟡 MEDIUM"
        else:
            density = "🔴 HIGH"

        st.metric(
            "🚦 Traffic Density",
            density
        )

    with c7:
        st.metric(
            "⏱ Green Signal",
            f'{report["signal_time"]} sec'
        )
        
def show_charts(report):
    """
    Display interactive charts.
    """

    section("📈 Traffic Analytics")

    vehicle_names = [
        "Car",
        "Motorcycle",
        "Bus",
        "Truck"
    ]

    vehicle_counts = [
        report["counts"]["Car"],
        report["counts"]["Motorcycle"],
        report["counts"]["Bus"],
        report["counts"]["Truck"]
    ]

    col1, col2 = st.columns(2)

    # -----------------------
    # Bar Chart
    # -----------------------

    with col1:

        bar_chart = px.bar(
            x=vehicle_names,
            y=vehicle_counts,
            text=vehicle_counts,
            labels={
                "x": "Vehicle Type",
                "y": "Average Count"
            },
            title="Vehicle Count"
        )

        bar_chart.update_layout(
    template="plotly_dark",
    height=450,
    title_x=0.5,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    # -----------------------
    # Pie Chart
    # -----------------------

    with col2:

        pie_chart = px.pie(
            names=vehicle_names,
            values=vehicle_counts,
            title="Vehicle Distribution"
        )

        pie_chart.update_layout(
    template="plotly_dark",
    height=450,
    title_x=0.5,
    paper_bgcolor="rgba(0,0,0,0)"
)

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )
        
def show_report_history():

    section("📋 Previous Traffic Reports")

    reports = get_all_reports()

    if len(reports) == 0:

        st.info("No reports available.")

        return

    columns = [

        "ID",
        "Location",
        "Video",
        "Cars",
        "Motorcycles",
        "Buses",
        "Trucks",
        "Total",
        "Density",
        "Signal Time (sec)"

    ]

    df = pd.DataFrame(
        reports,
        columns=columns
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )