import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to visualize health metrics
def app():
    st.title("📊 Diabetes Patient Health Insights Dashboard")

    st.markdown(
        """
        This dashboard provides a visual overview of simulated patient health data.  
        It compares glucose and insulin levels, and shows how diabetes cases may be distributed across different categories.  
        These visual insights help understand the impact of treatment and overall patient health trends.
        """
    )

    # Use dark theme with neon highlights
    plt.style.use("dark_background")

    # --- Glucose Trends Section ---
    st.subheader("🔍 Glucose Level Trends (With & Without Medication)")
    days = np.arange(1, 31)
    glucose_no_med = np.random.normal(loc=180, scale=20, size=len(days))
    glucose_with_med = glucose_no_med - np.random.normal(loc=40, scale=10, size=len(days))

    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    ax.plot(days, glucose_no_med, marker='o', linestyle='-', label='Without Medication', color='#FF00FF')
    ax.plot(days, glucose_with_med, marker='s', linestyle='--', label='With Medication', color='#00FFFF')
    ax.set_title("Glucose Level Trend", color='white', fontsize=14)
    ax.set_xlabel("Days", color='white')
    ax.set_ylabel("Glucose Level (mg/dL)", color='white')
    ax.legend()
    st.pyplot(fig)

    st.info("📌 Insight: Medication helps maintain glucose levels closer to normal range, reducing fluctuations.")

    # --- Insulin Levels Section ---
    st.subheader("💉 Insulin Level Comparison")
    patient_insulin = np.random.normal(loc=12, scale=2, size=1)[0]
    healthy_insulin = 15

    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    ax.bar(["Patient"], [patient_insulin], color='#00FF00', label='Patient')
    ax.bar(["Healthy"], [healthy_insulin], color='#FF4500', label='Healthy')
    ax.set_title("Insulin Levels: Patient vs Healthy", color='white', fontsize=14)
    ax.set_ylabel("Insulin Level (μU/mL)", color='white')
    ax.legend()
    st.pyplot(fig)

    st.info(f"📌 Insight: The patient’s insulin level is around {patient_insulin:.2f} μU/mL compared to the healthy benchmark of {healthy_insulin} μU/mL.")

    # --- Diabetes Type Distribution Section ---
    st.subheader("📊 Distribution of Diabetes Types (Simulated Data)")
    diabetes_classes = ["Type 1", "Type 2", "Gestational", "Prediabetes", "Other"]
    diabetes_distribution = np.random.randint(10, 50, size=len(diabetes_classes))

    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    colors = ['#FF00FF', '#00FFFF', '#00FF00', '#FFFF00', '#FF4500']
    ax.pie(
        diabetes_distribution,
        labels=diabetes_classes,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'color': "white"}
    )
    ax.set_title("Diabetes Classification Distribution", color='white', fontsize=14)
    st.pyplot(fig)

    st.info("📌 Insight: Type 2 diabetes is generally the most prevalent form, while gestational and rare types have smaller shares.")

# Run the dashboard
if __name__ == "__main__":
    app()
