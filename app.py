import streamlit as st
from agent import agent

st.set_page_config(page_title="TaskPilot AI", page_icon="🚀", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 20px;
    border-radius: 15px;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
h2 {
    text-align: center;
    color: #e2e8f0;
}
.stTextInput input {
    background-color: #1e293b;
    color: white;
    border-radius: 8px;
}
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #0ea5e9, #4f46e5);
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 TaskPilot AI")
st.markdown("### 🤖 Smart Client Onboarding Agent")

st.markdown("💡 *Automate onboarding process using Agentic AI*")

with st.container():
    st.markdown("## 📝 Enter Client Details")

    col1, col2 = st.columns(2)

    with col1:
        brand = st.text_input("🏢 Brand Name")
        manager = st.text_input("👨‍💼 Account Manager")
        email = st.text_input("📧 Client Email")

    with col2:
        start_date = st.text_input("📅 Start Date")
        deliverables = st.text_input("📦 Monthly Deliverables")

if st.button("🚀 Start Onboarding"):

    if brand and manager and email and start_date and deliverables:

        data = {
            "brand": brand,
            "manager": manager,
            "email": email,
            "date": start_date,
            "deliverables": deliverables
        }

        with st.spinner("🤖 AI Agent is working..."):
            steps, result = agent(data)

        st.success("🎉 Onboarding Completed Successfully!")

        with st.expander("🧠 View Agent Steps"):
            for step in steps:
                st.write("✔", step)

        with st.expander("📌 Final Result"):
            st.write(result)

    else:
        st.error("⚠️ Please fill all fields!")

st.markdown("---")
st.caption("💻 Built by Team AVON | Agentic AI Hackathon 🚀")