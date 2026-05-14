import streamlit as st

st.set_page_config(page_title="Interview Readiness Analyzer")

st.title("🎯 Interview Readiness Analyzer")

st.write("Evaluate your interview preparation level.")

name = st.text_input("Enter Your Name")

tech = st.slider("Technical Skills", 0, 100, 50)
resume = st.slider("Resume Quality", 0, 100, 50)
communication = st.slider("Communication Skills", 0, 100, 50)
portfolio = st.slider("Portfolio Strength", 0, 100, 50)

score = (
    tech * 0.35
    + resume * 0.25
    + communication * 0.20
    + portfolio * 0.20
)

if st.button("Analyze"):
    
    st.subheader("📊 Result")

    st.metric("Interview Readiness Score", f"{score:.2f}/100")

    if score >= 85:
        st.success("Excellent Interview Readiness")
    elif score >= 70:
        st.info("Good Interview Readiness")
    elif score >= 50:
        st.warning("Average Readiness")
    else:
        st.error("Needs Improvement")

    st.subheader("📌 Suggestions")

    if tech < 70:
        st.write("✔ Improve coding and DSA skills")

    if resume < 70:
        st.write("✔ Improve resume formatting and projects")

    if communication < 70:
        st.write("✔ Practice communication and mock interviews")

    if portfolio < 70:
        st.write("✔ Build projects and upload to GitHub")
