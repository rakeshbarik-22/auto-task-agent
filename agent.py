from tools import onboarding_agent

def agent(data):
    steps = []

    steps.append("📥 Received new client onboarding request")

    steps.append("🧠 Analyzing client details and defining onboarding goal")

    steps.append("📝 Planning onboarding workflow:")
    steps.append("   • Generate welcome email")
    steps.append("   • Create Google Drive structure")
    steps.append("   • Setup Notion client hub")
    steps.append("   • Create Airtable record")

    steps.append("⚙️ Executing onboarding steps using AI tools")

    try:
        result = onboarding_agent(data)
        steps.append("✅ All onboarding steps executed successfully")

    except Exception as e:
        result = f"❌ Error occurred: {str(e)}"
        steps.append("⚠️ Error during execution")

    steps.append("📤 Delivering final onboarding summary")

    return steps, result 