import streamlit as st
from agent import agent

# Page config
st.set_page_config(page_title="TaskPilot AI", page_icon="🚀", layout="centered")

# Custom UI styling
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #38bdf8;
    text-align: center;
}
.stTextInput input {
    background-color: #1e293b;
    color: white;
}
.stButton>button {
    background-color: #38bdf8;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 TaskPilot AI")
st.subheader("🤖 Client Onboarding Agent")

st.write("💡 Enter client details and let the AI agent automate onboarding")

# Input fields
brand = st.text_input("🏢 Brand Name")
manager = st.text_input("👨‍💼 Account Manager")
email = st.text_input("📧 Client Email")
start_date = st.text_input("📅 Start Date")
deliverables = st.text_input("📦 Monthly Deliverables")

# Button click
if st.button("🚀 Start Onboarding"):

    if brand and manager and email and start_date and deliverables:

        data = {
            "brand": brand,
            "manager": manager,
            "email": email,
            "date": start_date,
            "deliverables": deliverables
        }

        with st.spinner("🤖 Agent is processing onboarding..."):
            steps, result = agent(data)

        # Success message
        st.success("✅ Onboarding Completed Successfully!")

        # Agent thinking
        st.subheader("🧠 Agent Thinking")
        for step in steps:
            st.info(step)

        # Result output
        st.subheader("📌 Final Output")
        st.write(result)

    else:
        st.warning("⚠️ Please fill all fields before proceeding")

# Footer
st.markdown("---")
