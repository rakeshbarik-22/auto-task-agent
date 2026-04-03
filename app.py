import streamlit as st
from agent import agent

st.set_page_config(page_title="TaskPilot AI", page_icon="🚀")

st.title("🚀 TaskPilot AI")
st.subheader("🤖 Client Onboarding Agent")

st.write("Automate full client onboarding process using Agentic AI")

# Input Form
brand = st.text_input("🏢 Brand Name")
manager = st.text_input("👨‍💼 Account Manager")
email = st.text_input("📧 Client Email")
start_date = st.text_input("📅 Start Date")
deliverables = st.text_input("📦 Monthly Deliverables")

if st.button("🚀 Start Onboarding"):
    if brand and manager and email:

        data = {
            "brand": brand,
            "manager": manager,
            "email": email,
            "date": start_date,
            "deliverables": deliverables
        }

        with st.spinner("🤖 Agent is working..."):
            steps, result = agent(data)

        st.success("✅ Onboarding Completed!")

        st.subheader("🧠 Agent Steps")
        for step in steps:
            st.info(step)

        st.subheader("📌 Result")
        st.write(result)

    else:
        st.warning("⚠️ Please fill all required fields")

st.markdown("---")
st.caption("Built by Rakesh | Agentic AI Hackathon 🚀")