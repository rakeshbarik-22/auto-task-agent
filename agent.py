from tools import onboarding_agent

def agent(data):
    steps = []

    # Step 1: Receive Input
    steps.append("📥 Received new client onboarding request")

    # Step 2: Analyze Goal
    steps.append("🧠 Analyzing client details and defining onboarding goal")

    # Step 3: Plan Workflow
    steps.append("📝 Planning onboarding workflow:")
    steps.append("   • Generate welcome email")
    steps.append("   • Create Google Drive structure")
    steps.append("   • Setup Notion client hub")
    steps.append("   • Create Airtable record")

    # Step 4: Execute Task
    steps.append("⚙️ Executing onboarding steps using AI tools")

    try:
        result = onboarding_agent(data)
        steps.append("✅ All onboarding steps executed successfully")

    except Exception as e:
        result = f"❌ Error occurred: {str(e)}"
        steps.append("⚠️ Error during execution")

    # Step 5: Final Output
    steps.append("📤 Delivering final onboarding summary")

    return steps, result 