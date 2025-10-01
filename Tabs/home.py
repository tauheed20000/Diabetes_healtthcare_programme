import streamlit as st
import PIL

def app():
    st.title("🩺 Diabetes Prediction & Care System")
    st.image('./images/diabetic.png')

    # Intro / About Section
    st.markdown(
        """
        <div style="text-align: justify; font-size:18px; line-height:1.6;">
            <b>Diabetes</b> is a chronic health condition that affects how the body converts food into energy.  
            Although there is no permanent cure, early detection combined with lifestyle improvements like 
            <b>healthy diet, regular exercise, and weight management</b> can significantly reduce risks.  
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Why This App Section
    st.subheader("💡 Why Use This Application?")
    st.markdown(
        """
        - ✅ **Early Detection:** Get an instant risk assessment for diabetes.  
        - ✅ **Data-Driven:** Uses clinical health parameters for accurate predictions.  
        - ✅ **Accessible:** Simple and easy-to-use interface for everyone.  
        - ✅ **Supportive:** Provides insights to help patients and doctors take preventive action.  
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # What User Gets Section
    st.subheader("📊 What You’ll Get Here")
    st.markdown(
        """
        - 🔍 **Diagnosis Page** – Analyze your health parameters.  
        - 💊 **Medication Recommendations** – AI-powered suggestions (Gemini).  
        - 📂 **Knowledge Center** – Learn about diabetes types, symptoms, and care tips.  
        - 📑 **Downloadable Reports** – Save your test results in PDF or CSV format.  
        """,
        unsafe_allow_html=True
    )

    st.info("✨ This platform combines **Machine Learning** & **AI** to make diabetes care more accessible and proactive.")
